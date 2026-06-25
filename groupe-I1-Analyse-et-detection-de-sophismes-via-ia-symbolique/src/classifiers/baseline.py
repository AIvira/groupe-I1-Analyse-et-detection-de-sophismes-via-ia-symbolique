from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Tuple

import pandas as pd
from sklearn.calibration import CalibratedClassifierCV
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, f1_score
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

from src.domain.models import TrainingConfig


@dataclass(slots=True)
class TrainingArtifacts:
    pipeline: Pipeline
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


def load_dataset(csv_path: str, config: TrainingConfig) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    missing = {config.text_column, config.label_column} - set(df.columns)
    if missing:
        raise ValueError(f"Colonnes manquantes: {sorted(missing)}")

    df = df.dropna(subset=[config.text_column, config.label_column]).copy()
    df[config.text_column] = df[config.text_column].astype(str).str.strip()
    df[config.label_column] = df[config.label_column].astype(str).str.strip()

    if "masked_text" not in df.columns:
        df["masked_text"] = ""
    else:
        df["masked_text"] = df["masked_text"].fillna("").astype(str).str.strip()

    if "context" not in df.columns:
        df["context"] = ""
    else:
        df["context"] = df["context"].fillna("").astype(str).str.strip()

    if "split" in df.columns:
        df["split"] = df["split"].fillna("").astype(str).str.strip().str.lower()

    return df[df[config.text_column] != ""]


def build_split_datasets(df: pd.DataFrame, config: TrainingConfig) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    if "split" not in df.columns:
        raise ValueError("Le dataset doit contenir une colonne `split` avec `train`, `dev`, `test`.")

    train_df = df[df["split"] == "train"].copy()
    dev_df = df[df["split"] == "dev"].copy()
    test_df = df[df["split"] == "test"].copy()

    if train_df.empty or dev_df.empty or test_df.empty:
        raise ValueError("Les splits `train`, `dev` et `test` doivent tous etre presents.")

    required_labels = set(train_df[config.label_column].unique())
    for split_name, split_df in [("dev", dev_df), ("test", test_df)]:
        split_labels = set(split_df[config.label_column].unique())
        missing_labels = required_labels - split_labels
        if missing_labels:
            print(f"[warn] labels absents de {split_name}: {sorted(missing_labels)}")

    audit_split_overlap(train_df, dev_df, test_df, config)
    if config.drop_text_overlap_between_splits:
        train_df, dev_df, test_df = drop_text_overlap_between_splits(train_df, dev_df, test_df, config)

    return train_df, dev_df, test_df


def audit_split_overlap(
    train_df: pd.DataFrame,
    dev_df: pd.DataFrame,
    test_df: pd.DataFrame,
    config: TrainingConfig,
) -> None:
    train_texts = set(train_df[config.text_column].astype(str))
    dev_texts = set(dev_df[config.text_column].astype(str))
    test_texts = set(test_df[config.text_column].astype(str))

    train_dev = len(train_texts & dev_texts)
    train_test = len(train_texts & test_texts)
    dev_test = len(dev_texts & test_texts)
    print(
        "[audit] overlapping texts across splits:"
        f" train/dev={train_dev}, train/test={train_test}, dev/test={dev_test}"
    )


def drop_text_overlap_between_splits(
    train_df: pd.DataFrame,
    dev_df: pd.DataFrame,
    test_df: pd.DataFrame,
    config: TrainingConfig,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    dev_texts = set(dev_df[config.text_column].astype(str))
    test_texts = set(test_df[config.text_column].astype(str))
    protected_texts = dev_texts | test_texts

    original_train_size = len(train_df)
    filtered_train_df = train_df[~train_df[config.text_column].astype(str).isin(protected_texts)].copy()
    dropped = original_train_size - len(filtered_train_df)
    if dropped:
        print(f"[audit] dropped {dropped} overlapping train rows also present in dev/test")

    overlapping_dev_test = dev_texts & test_texts
    if overlapping_dev_test:
        original_dev_size = len(dev_df)
        filtered_dev_df = dev_df[~dev_df[config.text_column].astype(str).isin(overlapping_dev_test)].copy()
        print(f"[audit] dropped {original_dev_size - len(filtered_dev_df)} overlapping dev rows also present in test")
        dev_df = filtered_dev_df

    return filtered_train_df, dev_df, test_df


def build_feature_frame(df: pd.DataFrame, config: TrainingConfig) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "text": df[config.text_column].fillna("").astype(str),
            "masked_text": df["masked_text"].fillna("").astype(str),
            "context": df["context"].fillna("").astype(str),
        }
    )


def build_preprocessor(config: TrainingConfig) -> ColumnTransformer:
    transformers = [
        (
            "word_text",
            TfidfVectorizer(
                lowercase=True,
                ngram_range=(1, 2),
                max_features=config.word_max_features,
                sublinear_tf=True,
                min_df=config.min_df,
            ),
            "text",
        ),
        (
            "char_text",
            TfidfVectorizer(
                analyzer="char_wb",
                ngram_range=(3, 5),
                max_features=config.char_max_features,
                sublinear_tf=True,
                min_df=config.min_df,
            ),
            "text",
        ),
    ]

    if config.use_masked_text_features:
        transformers.append(
            (
                "word_masked",
                TfidfVectorizer(
                    lowercase=True,
                    ngram_range=(1, 2),
                    max_features=config.masked_max_features,
                    sublinear_tf=True,
                    min_df=1,
                ),
                "masked_text",
            )
        )

    if config.use_context_features:
        transformers.append(
            (
                "word_context",
                TfidfVectorizer(
                    lowercase=True,
                    ngram_range=(1, 2),
                    max_features=config.context_max_features,
                    sublinear_tf=True,
                    min_df=1,
                ),
                "context",
            )
        )

    return ColumnTransformer(transformers=transformers, remainder="drop")


def build_candidate_pipelines(config: TrainingConfig) -> Dict[str, Pipeline]:
    preprocessor = build_preprocessor(config)

    logistic_kwargs = {
        "max_iter": 3000,
        "class_weight": "balanced",
        "C": 1.5,
        "solver": "lbfgs",
    }

    logistic = Pipeline(
        steps=[
            ("features", preprocessor),
            (
                "clf",
                LogisticRegression(**logistic_kwargs),
            ),
        ]
    )

    linear_svc = LinearSVC(
        class_weight="balanced",
        C=0.75,
    )

    try:
        calibrated_svc = CalibratedClassifierCV(
            estimator=linear_svc,
            cv=3,
        )
    except TypeError:
        calibrated_svc = CalibratedClassifierCV(
            base_estimator=linear_svc,
            cv=3,
        )

    linear_svc = Pipeline(
        steps=[
            ("features", preprocessor),
            ("clf", calibrated_svc),
        ]
    )

    return {
        "logreg_tfidf_rich": logistic,
        "linear_svc_calibrated": linear_svc,
    }


def evaluate_candidates(
    candidates: Dict[str, Pipeline],
    train_df: pd.DataFrame,
    dev_df: pd.DataFrame,
    config: TrainingConfig,
) -> Tuple[str, Pipeline, Dict[str, float]]:
    train_features = build_feature_frame(train_df, config)
    dev_features = build_feature_frame(dev_df, config)
    y_train = train_df[config.label_column]
    y_dev = dev_df[config.label_column]

    scores: Dict[str, float] = {}
    best_name = ""
    best_pipeline = None
    best_score = -1.0

    for name, pipeline in candidates.items():
        pipeline.fit(train_features, y_train)
        predictions = pipeline.predict(dev_features)
        score = f1_score(y_dev, predictions, average="macro")
        scores[name] = float(score)
        if score > best_score:
            best_name = name
            best_pipeline = pipeline
            best_score = score

    if best_pipeline is None:
        raise RuntimeError("Aucun modele n'a pu etre entraine.")

    return best_name, best_pipeline, scores


def finalize_best_pipeline(
    pipeline: Pipeline,
    train_df: pd.DataFrame,
    dev_df: pd.DataFrame,
    test_df: pd.DataFrame,
    config: TrainingConfig,
) -> Tuple[Pipeline, str, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    final_train_df = pd.concat([train_df, dev_df], ignore_index=True)
    final_train_features = build_feature_frame(final_train_df, config)
    test_features = build_feature_frame(test_df, config)

    y_train = final_train_df[config.label_column]
    y_test = test_df[config.label_column]

    pipeline.fit(final_train_features, y_train)
    predictions = pipeline.predict(test_features)

    labels = sorted(final_train_df[config.label_column].unique().tolist())
    report = classification_report(y_test, predictions, digits=3)
    confusion = confusion_matrix(y_test, predictions, labels=labels)
    confusion_df = pd.DataFrame(confusion, index=labels, columns=labels)
    predictions_df = build_predictions_frame(test_df, predictions, pipeline, labels, config)
    top_confusions_df = summarize_top_confusions(confusion_df)
    error_examples_df = predictions_df[predictions_df["is_correct"] == False].copy()
    return pipeline, report, confusion_df, top_confusions_df, error_examples_df, predictions_df


def build_predictions_frame(
    test_df: pd.DataFrame,
    predictions,
    pipeline: Pipeline,
    labels: list[str],
    config: TrainingConfig,
) -> pd.DataFrame:
    result = test_df.copy().reset_index(drop=True)
    result["predicted_label"] = list(predictions)
    result["is_correct"] = result[config.label_column] == result["predicted_label"]

    try:
        probabilities = pipeline.predict_proba(build_feature_frame(test_df, config))
    except Exception:
        probabilities = None

    if probabilities is not None:
        label_to_index = {label: idx for idx, label in enumerate(labels)}
        confidences = []
        true_label_scores = []
        for row_idx, predicted_label in enumerate(result["predicted_label"]):
            predicted_index = label_to_index[predicted_label]
            confidences.append(float(probabilities[row_idx][predicted_index]))
            true_label = result.iloc[row_idx][config.label_column]
            true_label_scores.append(float(probabilities[row_idx][label_to_index[true_label]]))
        result["predicted_confidence"] = confidences
        result["true_label_score"] = true_label_scores
    else:
        result["predicted_confidence"] = None
        result["true_label_score"] = None

    columns = [
        config.text_column,
        config.label_column,
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


def summarize_top_confusions(confusion_df: pd.DataFrame, top_k: int = 15) -> pd.DataFrame:
    rows = []
    for true_label in confusion_df.index:
        for predicted_label in confusion_df.columns:
            if true_label == predicted_label:
                continue
            count = int(confusion_df.loc[true_label, predicted_label])
            if count > 0:
                rows.append(
                    {
                        "true_label": true_label,
                        "predicted_label": predicted_label,
                        "count": count,
                    }
                )
    if not rows:
        return pd.DataFrame(columns=["true_label", "predicted_label", "count"])
    return pd.DataFrame(rows).sort_values(["count", "true_label", "predicted_label"], ascending=[False, True, True]).head(top_k)


def train_baseline(csv_path: str, config: TrainingConfig) -> TrainingArtifacts:
    df = load_dataset(csv_path, config)
    train_df, dev_df, test_df = build_split_datasets(df, config)

    candidates = build_candidate_pipelines(config)
    best_name, best_pipeline, candidate_scores = evaluate_candidates(candidates, train_df, dev_df, config)
    best_dev_macro_f1 = candidate_scores[best_name]

    final_pipeline, report, confusion_df, top_confusions_df, error_examples_df, predictions_df = finalize_best_pipeline(
        best_pipeline,
        train_df,
        dev_df,
        test_df,
        config,
    )

    return TrainingArtifacts(
        pipeline=final_pipeline,
        model_name=best_name,
        dev_macro_f1=best_dev_macro_f1,
        report=report,
        labels=sorted(df[config.label_column].unique().tolist()),
        train_size=len(train_df),
        dev_size=len(dev_df),
        test_size=len(test_df),
        candidate_scores=candidate_scores,
        confusion=confusion_df,
        top_confusions=top_confusions_df,
        error_examples=error_examples_df,
        predictions=predictions_df,
    )


def write_training_summary(artifacts: TrainingArtifacts, output_path: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        f"Best model: {artifacts.model_name}",
        f"Best dev macro F1: {artifacts.dev_macro_f1:.4f}",
        "Candidate dev macro F1:",
    ]
    for name, score in sorted(artifacts.candidate_scores.items()):
        lines.append(f"- {name}: {score:.4f}")

    lines.extend(
        [
            "",
            "Test classification report:",
            artifacts.report,
            "",
            "Top confusions:",
            artifacts.top_confusions.to_string(index=False) if not artifacts.top_confusions.empty else "No confusions.",
            "",
            "Confusion matrix:",
            artifacts.confusion.to_string(),
            "",
            "Sample errors:",
            artifacts.error_examples.head(20).to_string(index=False) if not artifacts.error_examples.empty else "No errors.",
            "",
            f"Train size: {artifacts.train_size}",
            f"Dev size: {artifacts.dev_size}",
            f"Test size: {artifacts.test_size}",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_predictions_csv(artifacts: TrainingArtifacts, output_path: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    artifacts.predictions.to_csv(path, index=False)


def write_error_examples_csv(artifacts: TrainingArtifacts, output_path: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    artifacts.error_examples.to_csv(path, index=False)
