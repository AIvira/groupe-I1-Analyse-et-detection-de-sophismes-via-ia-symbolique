"""Template minimal pour convertir un corpus brut vers le schema CSV du projet.

Usage attendu:
- adapter `load_raw_examples()` pour un corpus specifique
- produire `data/processed/fallacies.csv`
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable


OUTPUT_COLUMNS = ["text", "label", "source", "split", "context", "topic"]


def load_raw_examples() -> Iterable[dict]:
    raise NotImplementedError("Adapter ce script au corpus choisi.")


def normalize_label(raw_label: str) -> str:
    mapping = {
        "ad hominem": "ad_hominem",
        "appeal to authority": "appeal_to_authority",
        "false dilemma": "false_dilemma",
        "straw man": "straw_man",
    }
    return mapping.get(raw_label.strip().lower(), "other_fallacy")


def write_csv(rows: Iterable[dict], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> None:
    destination = Path("data/processed/fallacies.csv")
    normalized = []
    for item in load_raw_examples():
        normalized.append(
            {
                "text": item["text"],
                "label": normalize_label(item["label"]),
                "source": item.get("source", "unknown"),
                "split": item.get("split", "train"),
                "context": item.get("context", ""),
                "topic": item.get("topic", ""),
            }
        )
    write_csv(normalized, destination)


if __name__ == "__main__":
    main()
