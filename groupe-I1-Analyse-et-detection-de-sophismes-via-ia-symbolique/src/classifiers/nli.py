from __future__ import annotations

import csv
import inspect
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, f1_score

from src.classifiers.baseline import build_split_datasets, load_dataset, summarize_top_confusions

LABEL_ALIASES = {
    "ad_hominem": "ad hominem",
    "ad_populum": "ad populum",
    "appeal_to_emotion": "appeal to emotion",
    "circular_reasoning": "circular reasoning",
    "equivocation": "equivocation",
    "fallacy_of_credibility": "fallacy of credibility",
    "straw_man": "fallacy of extension",
    "fallacy_of_logic": "fallacy of logic",
    "fallacy_of_relevance": "fallacy of relevance",
    "false_causality": "false causality",
    "false_dilemma": "false dilemma",
    "faulty_generalization": "faulty generalization",
    "intentional": "intentional",
    "miscellaneous": "miscellaneous",
}


@dataclass(slots=True)
class NLITrainingArtifacts:
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

    if "evaluation_strategy" not in accepted and "eval_strategy" in accepted and "evaluation_strategy" in kwargs:
        filtered["eval_strategy"] = kwargs["evaluation_strategy"]

    if "logging_strategy" not in accepted and "logging_steps" in accepted:
        filtered.pop("logging_strategy", None)

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
        return trainer_cls(**kwargs)
    filtered = {key: value for key, value in kwargs.items() if key in accepted}
    return trainer_cls(**filtered)


def _read_mappings(mappings_path: str) -> Dict[str, Dict[str, str]]:
    path = Path(mappings_path)
    metadata: Dict[str, Dict[str, str]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            key = row["Original Name"].strip().lower()
            metadata[key] = {
                "original_name": row["Original Name"].strip(),
                "understandable_name": row.get("Understandable Name", "").strip(),
                "description": row.get("Description", "").strip(),
                "logical_form": row.get("Logical Form", "").strip(),
                "masked_logical_form": row.get("Masked Logical Form", "").strip(),
            }
    return metadata


def _label_to_mapping_key(label: str) -> str:
    return LABEL_ALIASES.get(label, label.replace("_", " ")).lower()


def _build_hypothesis(label: str, metadata: Dict[str, Dict[str, str]]) -> str:
    entry = metadata.get(_label_to_mapping_key(label), {})
    name = entry.get("understandable_name") or label.replace("_", " ")
    description = entry.get("description", "")
    logical_form = entry.get("logical_form", "")
    parts = [f"This text contains the logical fallacy: {name}."]
    if description:
        parts.append(f"Description: {description}")
    if logical_form:
        parts.append(f"Logical form: {logical_form}")
    return " ".join(parts)


def _make_pair_rows(
    df: pd.DataFrame,
    labels: List[str],
    metadata: Dict[str, Dict[str, str]],
    negatives_per_example: int,
    seed: int,
    use_masked_text: bool,
) -> List[dict]:
    rng = random.Random(seed)
    rows: List[dict] = []
    for _, row in df.iterrows():
        text = row["text"].strip()
        if use_masked_text and str(row.get("masked_text", "")).strip():
            text = f"{text} [MASKED] {str(row['masked_text']).strip()}"
        true_label = row["label"]
        rows.append({"premise": text, "hypothesis": _build_hypothesis(true_label, metadata), "labels": 1})
        negative_labels = [label for label in labels if label != true_label]
        sampled_negatives = rng.sample(negative_labels, k=min(negatives_per_example, len(negative_labels)))
        for negative_label in sampled_negatives:
            rows.append({
                "premise": text,
                "hypothesis": _build_hypothesis(negative_label, metadata),
                "labels": 0,
            })
    return rows


def _softmax(logits: np.ndarray) -> np.ndarray:
    stabilized = logits - logits.max(axis=1, keepdims=True)
    exp = np.exp(stabilized)
    return exp / exp.sum(axis=1, keepdims=True)


def _predict_label_scores(
    texts: List[str],
    labels: List[str],
    metadata: Dict[str, Dict[str, str]],
    tokenizer,
    model,
    torch_module,
    max_length: int,
    batch_size: int,
) -> Tuple[List[str], List[float], List[List[float]]]:
    hypotheses = [_build_hypothesis(label, metadata) for label in labels]
    predicted_labels: List[str] = []
    confidences: List[float] = []
    all_scores: List[List[float]] = []

    model.eval()
    device = model.device
    for text in texts:
        premises = [text] * len(labels)
        encoded = tokenizer(
            premises,
            hypotheses,
            truncation=True,
            padding=True,
            max_length=max_length,
            return_tensors="pt",
        )
        encoded = {key: value.to(device) for key, value in encoded.items()}
        with torch_module.no_grad():
            outputs = model(**encoded)
            probabilities = _softmax(outputs.logits.detach().cpu().numpy())[:, 1]
        best_index = int(np.argmax(probabilities))
        predicted_labels.append(labels[best_index])
        confidences.append(float(probabilities[best_index]))
        all_scores.append(probabilities.tolist())
    return predicted_labels, confidences, all_scores


def _build_predictions_frame(
    df: pd.DataFrame,
    predicted_labels: list[str],
    confidences: list[float],
    all_scores: list[list[float]],
    labels: list[str],
) -> pd.DataFrame:
    result = df.copy().reset_index(drop=True)
    result["predicted_label"] = predicted_labels
    result["is_correct"] = result["label"] == result["predicted_label"]
    result["predicted_confidence"] = confidences
    true_label_scores = []
    label_to_index = {label: idx for idx, label in enumerate(labels)}
    for row_idx, row in result.iterrows():
        true_label_scores.append(float(all_scores[row_idx][label_to_index[row["label"]]]))
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


def train_nli_label_matching(
    dataset_path: str,
    mappings_path: str,
    output_dir: str,
    pretrained_model_name: str = "roberta-base",
    use_masked_text: bool = True,
    max_length: int = 256,
    num_train_epochs: int = 4,
    learning_rate: float = 2e-5,
    weight_decay: float = 0.01,
    train_batch_size: int = 8,
    eval_batch_size: int = 16,
    negatives_per_example: int = 3,
    seed: int = 42,
) -> NLITrainingArtifacts:
    torch, Dataset, AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments = _ImportGuard.load()
    from src.domain.models import TrainingConfig

    config = TrainingConfig()
    config.use_masked_text_features = use_masked_text
    df = load_dataset(dataset_path, config)
    train_df, dev_df, test_df = build_split_datasets(df, config)

    labels = sorted(train_df["label"].unique().tolist())
    metadata = _read_mappings(mappings_path)
    tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name)

    train_pairs = _make_pair_rows(train_df, labels, metadata, negatives_per_example, seed, use_masked_text)
    dev_pairs = _make_pair_rows(dev_df, labels, metadata, negatives_per_example, seed + 1, use_masked_text)

    train_dataset = Dataset.from_list(train_pairs)
    dev_dataset = Dataset.from_list(dev_pairs)

    def tokenize_batch(batch):
        return tokenizer(batch["premise"], batch["hypothesis"], truncation=True, padding="max_length", max_length=max_length)

    train_dataset = train_dataset.map(tokenize_batch, batched=True)
    dev_dataset = dev_dataset.map(tokenize_batch, batched=True)
    train_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])
    dev_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])

    model = AutoModelForSequenceClassification.from_pretrained(pretrained_model_name, num_labels=2)

    def compute_metrics(eval_pred):
        logits, label_ids = eval_pred
        predictions = np.argmax(logits, axis=-1)
        accuracy = float((predictions == label_ids).mean())
        return {"pair_accuracy": accuracy}

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
        load_best_model_at_end=False,
        seed=seed,
        logging_strategy="epoch",
        report_to="none",
    )

    trainer = _make_trainer(
        Trainer,
        model=model,
        args=args,
        train_dataset=train_dataset,
        eval_dataset=dev_dataset,
        tokenizer=tokenizer,
        processing_class=tokenizer,
        compute_metrics=compute_metrics,
    )
    trainer.train()
    trainer.save_model(str(run_output_dir))
    tokenizer.save_pretrained(str(run_output_dir))

    def prepare_texts(df_split: pd.DataFrame) -> List[str]:
        texts = []
        for _, row in df_split.iterrows():
            text = row["text"].strip()
            if use_masked_text and str(row.get("masked_text", "")).strip():
                text = f"{text} [MASKED] {str(row['masked_text']).strip()}"
            texts.append(text)
        return texts

    dev_texts = prepare_texts(dev_df)
    dev_predicted_labels, _, _ = _predict_label_scores(
        dev_texts,
        labels,
        metadata,
        tokenizer,
        trainer.model,
        torch,
        max_length,
        eval_batch_size,
    )
    dev_macro_f1 = f1_score(dev_df["label"].tolist(), dev_predicted_labels, average="macro")

    test_texts = prepare_texts(test_df)
    test_predicted_labels, test_confidences, test_all_scores = _predict_label_scores(
        test_texts,
        labels,
        metadata,
        tokenizer,
        trainer.model,
        torch,
        max_length,
        eval_batch_size,
    )

    report = classification_report(test_df["label"].tolist(), test_predicted_labels, digits=3)
    confusion = confusion_matrix(test_df["label"].tolist(), test_predicted_labels, labels=labels)
    confusion_df = pd.DataFrame(confusion, index=labels, columns=labels)
    predictions_df = _build_predictions_frame(test_df, test_predicted_labels, test_confidences, test_all_scores, labels)
    top_confusions_df = summarize_top_confusions(confusion_df)
    error_examples_df = predictions_df[predictions_df["is_correct"] == False].copy()

    return NLITrainingArtifacts(
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
