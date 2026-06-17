from __future__ import annotations

import inspect
from dataclasses import dataclass
from pathlib import Path
from typing import Dict

import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, f1_score
from sklearn.utils.class_weight import compute_class_weight

from src.classifiers.baseline import build_split_datasets, load_dataset, summarize_top_confusions


@dataclass(slots=True)
class TransformerTrainingArtifacts:
    model_name: str
    dev_macro_f1: float
    report: str
    labels: list[str]
    train_size: int
    dev_size: int
    test_size: int
    candidate_scores: Dict[str, float]
    confusion: pd.DataFrame
    top_confusions: pd.DataFrame
    error_examples: pd.DataFrame
    predictions: pd.DataFrame
    output_dir: str


class _ImportGuard:
    @staticmethod
    def load():
        import torch
        from datasets import Dataset
        from transformers import (
            AutoModelForSequenceClassification,
            AutoTokenizer,
            Trainer,
            TrainingArguments,
        )
        return torch, Dataset, AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments


def _make_training_arguments(training_arguments_cls, **kwargs):
    accepted = inspect.signature(training_arguments_cls.__init__).parameters
    filtered = {key: value for key, value in kwargs.items() if key in accepted}

    # Compatibility across transformers versions:
    # some versions expose `eval_strategy` instead of `evaluation_strategy`.
    if "evaluation_strategy" not in accepted and "eval_strategy" in accepted and "evaluation_strategy" in kwargs:
        filtered["eval_strategy"] = kwargs["evaluation_strategy"]

    if "logging_strategy" not in accepted and "logging_steps" in accepted:
        filtered.pop("logging_strategy", None)

    # If the installed transformers version cannot configure evaluation properly,
    # disable best-checkpoint reloading rather than crash at init time.
    has_eval_strategy = (
        ("evaluation_strategy" in filtered and filtered["evaluation_strategy"] is not None)
        or ("eval_strategy" in filtered and filtered["eval_strategy"] is not None)
    )
    if "load_best_model_at_end" in filtered and not has_eval_strategy:
        filtered["load_best_model_at_end"] = False

    return training_arguments_cls(**filtered)


def _make_trainer(trainer_cls, **kwargs):
    accepted = inspect.signature(trainer_cls.__init__).parameters
    if any(param.kind == inspect.Parameter.VAR_KEYWORD for param in accepted.values()):
        explicit_params = {
            name
            for name, param in accepted.items()
            if name != "self" and param.kind not in {inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD}
        }
        base_init = trainer_cls.__mro__[1].__init__
        base_params = set(inspect.signature(base_init).parameters)
        base_params.discard("self")
        allowed = explicit_params | base_params
        filtered = {key: value for key, value in kwargs.items() if key in allowed}
        return trainer_cls(**filtered)
    filtered = {key: value for key, value in kwargs.items() if key in accepted}
    return trainer_cls(**filtered)


def _build_feature_text(df: pd.DataFrame, use_masked_text: bool) -> list[str]:
    texts = df["text"].fillna("").astype(str).str.strip()
    if use_masked_text and "masked_text" in df.columns:
        masked = df["masked_text"].fillna("").astype(str).str.strip()
        return [f"{text} [MASKED] {masked_text}".strip() for text, masked_text in zip(texts, masked)]
    return texts.tolist()


def _make_dataset(df: pd.DataFrame, label_to_id: Dict[str, int], use_masked_text: bool, dataset_cls):
    features = {
        "text": _build_feature_text(df, use_masked_text),
        "labels": [label_to_id[label] for label in df["label"].tolist()],
    }
    return dataset_cls.from_dict(features)


def _make_weighted_trainer_class(base_trainer, torch_module):
    class WeightedTrainer(base_trainer):
        def __init__(self, *args, class_weights=None, **kwargs):
            super().__init__(*args, **kwargs)
            self.class_weights = class_weights

        def compute_loss(self, model, inputs, return_outputs=False, num_items_in_batch=None):
            labels = inputs.pop("labels")
            outputs = model(**inputs)
            logits = outputs.get("logits")
            loss_fct = torch_module.nn.CrossEntropyLoss(
                weight=self.class_weights.to(logits.device) if self.class_weights is not None else None
            )
            loss = loss_fct(logits.view(-1, model.config.num_labels), labels.view(-1))
            return (loss, outputs) if return_outputs else loss

    return WeightedTrainer


def _softmax(logits: np.ndarray) -> np.ndarray:
    stabilized = logits - logits.max(axis=1, keepdims=True)
    exp = np.exp(stabilized)
    return exp / exp.sum(axis=1, keepdims=True)


def _build_predictions_frame(
    df: pd.DataFrame,
    predicted_labels: list[str],
    confidence_scores: list[float],
    true_label_scores: list[float],
) -> pd.DataFrame:
    result = df.copy().reset_index(drop=True)
    result["predicted_label"] = predicted_labels
    result["is_correct"] = result["label"] == result["predicted_label"]
    result["predicted_confidence"] = confidence_scores
    result["true_label_score"] = true_label_scores
    columns = [
        "text",
        "label",
        "predicted_label",
        "is_correct",
        "predicted_confidence",
        "true_label_score",
        "source",
        "split",
        "topic",
        "original_label",
    ]
    existing_columns = [column for column in columns if column in result.columns]
    return result[existing_columns]


def train_transformer_classifier(
    dataset_path: str,
    output_dir: str,
    pretrained_model_name: str = "roberta-base",
    use_masked_text: bool = True,
    max_length: int = 256,
    num_train_epochs: int = 4,
    learning_rate: float = 2e-5,
    weight_decay: float = 0.01,
    train_batch_size: int = 8,
    eval_batch_size: int = 16,
    gradient_accumulation_steps: int = 1,
    seed: int = 42,
) -> TransformerTrainingArtifacts:
    torch, Dataset, AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments = _ImportGuard.load()
    from src.domain.models import TrainingConfig

    config = TrainingConfig()
    config.use_masked_text_features = use_masked_text
    df = load_dataset(dataset_path, config)
    train_df, dev_df, test_df = build_split_datasets(df, config)

    labels = sorted(train_df["label"].unique().tolist())
    label_to_id = {label: idx for idx, label in enumerate(labels)}
    id_to_label = {idx: label for label, idx in label_to_id.items()}

    tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name)
    train_dataset = _make_dataset(train_df, label_to_id, use_masked_text, Dataset)
    dev_dataset = _make_dataset(dev_df, label_to_id, use_masked_text, Dataset)
    test_dataset = _make_dataset(test_df, label_to_id, use_masked_text, Dataset)

    def tokenize_batch(batch):
        return tokenizer(batch["text"], truncation=True, padding="max_length", max_length=max_length)

    train_dataset = train_dataset.map(tokenize_batch, batched=True)
    dev_dataset = dev_dataset.map(tokenize_batch, batched=True)
    test_dataset = test_dataset.map(tokenize_batch, batched=True)
    train_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])
    dev_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])
    test_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])

    class_weights = compute_class_weight(
        class_weight="balanced",
        classes=np.array(labels),
        y=train_df["label"].to_numpy(),
    )
    class_weights_tensor = torch.tensor(class_weights, dtype=torch.float)

    model = AutoModelForSequenceClassification.from_pretrained(
        pretrained_model_name,
        num_labels=len(labels),
        id2label=id_to_label,
        label2id=label_to_id,
    )

    def compute_metrics(eval_pred):
        logits, label_ids = eval_pred
        predictions = np.argmax(logits, axis=-1)
        macro_f1 = f1_score(label_ids, predictions, average="macro")
        accuracy = float((predictions == label_ids).mean())
        return {"macro_f1": macro_f1, "accuracy": accuracy}

    run_output_dir = Path(output_dir)
    run_output_dir.mkdir(parents=True, exist_ok=True)
    args = _make_training_arguments(
        TrainingArguments,
        output_dir=str(run_output_dir),
        overwrite_output_dir=True,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        learning_rate=learning_rate,
        per_device_train_batch_size=train_batch_size,
        per_device_eval_batch_size=eval_batch_size,
        num_train_epochs=num_train_epochs,
        weight_decay=weight_decay,
        gradient_accumulation_steps=gradient_accumulation_steps,
        load_best_model_at_end=True,
        metric_for_best_model="macro_f1",
        greater_is_better=True,
        seed=seed,
        logging_strategy="epoch",
        report_to="none",
    )

    WeightedTrainer = _make_weighted_trainer_class(Trainer, torch)
    trainer = _make_trainer(
        WeightedTrainer,
        model=model,
        args=args,
        train_dataset=train_dataset,
        eval_dataset=dev_dataset,
        tokenizer=tokenizer,
        processing_class=tokenizer,
        compute_metrics=compute_metrics,
        class_weights=class_weights_tensor,
    )
    trainer.train()
    trainer.save_model(str(run_output_dir))
    tokenizer.save_pretrained(str(run_output_dir))

    dev_predictions = trainer.predict(dev_dataset)
    dev_macro_f1 = f1_score(dev_predictions.label_ids, np.argmax(dev_predictions.predictions, axis=-1), average="macro")

    test_predictions = trainer.predict(test_dataset)
    test_logits = test_predictions.predictions
    test_probabilities = _softmax(test_logits)
    predicted_ids = np.argmax(test_logits, axis=-1)
    predicted_labels = [id_to_label[int(idx)] for idx in predicted_ids]
    true_ids = test_predictions.label_ids
    true_labels = [id_to_label[int(idx)] for idx in true_ids]

    confidences = [float(test_probabilities[i, predicted_ids[i]]) for i in range(len(predicted_ids))]
    true_label_scores = [float(test_probabilities[i, true_ids[i]]) for i in range(len(true_ids))]

    report = classification_report(true_labels, predicted_labels, digits=3)
    confusion = confusion_matrix(true_labels, predicted_labels, labels=labels)
    confusion_df = pd.DataFrame(confusion, index=labels, columns=labels)
    predictions_df = _build_predictions_frame(test_df, predicted_labels, confidences, true_label_scores)
    top_confusions_df = summarize_top_confusions(confusion_df)
    error_examples_df = predictions_df[predictions_df["is_correct"] == False].copy()

    return TransformerTrainingArtifacts(
        model_name=pretrained_model_name,
        dev_macro_f1=float(dev_macro_f1),
        report=report,
        labels=labels,
        train_size=len(train_df),
        dev_size=len(dev_df),
        test_size=len(test_df),
        candidate_scores={pretrained_model_name: float(dev_macro_f1)},
        confusion=confusion_df,
        top_confusions=top_confusions_df,
        error_examples=error_examples_df,
        predictions=predictions_df,
        output_dir=str(run_output_dir),
    )
