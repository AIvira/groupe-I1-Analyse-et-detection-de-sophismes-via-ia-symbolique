from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Dict, Iterable, List


OUTPUT_COLUMNS = [
    "text",
    "label",
    "source",
    "split",
    "context",
    "topic",
    "masked_text",
    "original_label",
]


REDUCED_LABEL_MAP = {
    "ad hominem": "ad_hominem",
    "fallacy of credibility": "fallacy_of_credibility",
    "false dilemma": "false_dilemma",
    "fallacy of extension": "straw_man",
    "faulty generalization": "other_fallacy",
    "ad populum": "other_fallacy",
    "false causality": "other_fallacy",
    "circular reasoning": "other_fallacy",
    "appeal to emotion": "other_fallacy",
    "fallacy of relevance": "other_fallacy",
    "fallacy of logic": "other_fallacy",
    "intentional": "other_fallacy",
    "equivocation": "other_fallacy",
    "miscellaneous": "other_fallacy",
}


FULL_LABEL_NORMALIZATION = {
    "ad hominem": "ad_hominem",
    "ad populum": "ad_populum",
    "appeal to emotion": "appeal_to_emotion",
    "circular reasoning": "circular_reasoning",
    "equivocation": "equivocation",
    "fallacy of credibility": "fallacy_of_credibility",
    "fallacy of extension": "straw_man",
    "fallacy of logic": "fallacy_of_logic",
    "fallacy of relevance": "fallacy_of_relevance",
    "false causality": "false_causality",
    "false dilemma": "false_dilemma",
    "faulty generalization": "faulty_generalization",
    "intentional": "intentional",
    "miscellaneous": "miscellaneous",
}


def normalize_label(raw_label: str, taxonomy: str) -> str:
    key = raw_label.strip().lower()
    if taxonomy == "reduced":
        return REDUCED_LABEL_MAP.get(key, "other_fallacy")
    return FULL_LABEL_NORMALIZATION.get(key, key.replace(" ", "_"))


def read_mapping_descriptions(mappings_path: Path) -> Dict[str, str]:
    descriptions: Dict[str, str] = {}
    if not mappings_path.exists():
        return descriptions
    with mappings_path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            descriptions[row["Original Name"].strip().lower()] = row.get("Description", "").strip()
    return descriptions


def iter_edu_rows(repo_path: Path, taxonomy: str) -> Iterable[dict]:
    descriptions = read_mapping_descriptions(repo_path / "data" / "mappings.csv")
    for split in ["train", "dev", "test"]:
        csv_path = repo_path / "data" / f"edu_{split}.csv"
        with csv_path.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                raw_label = row["updated_label"].strip()
                yield {
                    "text": row["source_article"].strip(),
                    "label": normalize_label(raw_label, taxonomy),
                    "source": "causalNLP_logic_edu",
                    "split": split,
                    "context": descriptions.get(raw_label.lower(), ""),
                    "topic": "education_examples",
                    "masked_text": row.get("masked_articles", "").strip(),
                    "original_label": raw_label,
                }


def iter_climate_rows(repo_path: Path, taxonomy: str) -> Iterable[dict]:
    descriptions = read_mapping_descriptions(repo_path / "data" / "mappings.csv")
    for split in ["train", "dev", "test"]:
        csv_path = repo_path / "data" / f"climate_{split}.csv"
        with csv_path.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                raw_label = row["logical_fallacies"].strip()
                yield {
                    "text": row["source_article"].strip(),
                    "label": normalize_label(raw_label, taxonomy),
                    "source": "causalNLP_logic_climate",
                    "split": split,
                    "context": descriptions.get(raw_label.lower(), ""),
                    "topic": row.get("original_url", "").strip(),
                    "masked_text": "",
                    "original_label": raw_label,
                }


def write_rows(rows: List[dict], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def build_rows(repo_path: Path, dataset: str, taxonomy: str) -> List[dict]:
    rows: List[dict] = []
    if dataset in {"edu", "both"}:
        rows.extend(iter_edu_rows(repo_path, taxonomy))
    if dataset in {"climate", "both"}:
        rows.extend(iter_climate_rows(repo_path, taxonomy))
    return rows


def output_for_taxonomy(output: Path, taxonomy: str) -> Path:
    if output.suffix.lower() == ".csv":
        return output.with_name(f"{output.stem}_{taxonomy}{output.suffix}")
    return output / f"fallacies_{taxonomy}.csv"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Importe le dataset causalNLP/logical-fallacy")
    parser.add_argument("--repo-path", required=True, help="Chemin du clone du repo causalNLP/logical-fallacy")
    parser.add_argument(
        "--dataset",
        choices=["edu", "climate", "both"],
        default="both",
        help="Sous-corpus a importer",
    )
    parser.add_argument(
        "--taxonomy",
        choices=["reduced", "full", "both"],
        default="full",
        help="Taxonomie reduite pour le MVP ou taxonomie complete du dataset",
    )
    parser.add_argument(
        "--output",
        default="data/processed/fallacies.csv",
        help="CSV normalise de sortie",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repo_path = Path(args.repo_path)
    output = Path(args.output)

    if args.taxonomy == "both":
        for taxonomy in ["full", "reduced"]:
            rows = build_rows(repo_path, args.dataset, taxonomy)
            taxonomy_output = output_for_taxonomy(output, taxonomy)
            write_rows(rows, taxonomy_output)
            print(f"Imported {len(rows)} rows to {taxonomy_output}")
        return

    rows = build_rows(repo_path, args.dataset, args.taxonomy)
    write_rows(rows, output)
    print(f"Imported {len(rows)} rows to {output}")


if __name__ == "__main__":
    main()
