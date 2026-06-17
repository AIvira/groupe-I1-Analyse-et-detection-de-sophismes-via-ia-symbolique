"""Mesure l'apport de la couche symbolique (arbitrage Dung) par-dessus un modele.

Prend un CSV de predictions (colonnes: text, label, predicted_label,
predicted_confidence), applique le moteur de regles puis l'arbitrage par
semantique fondee de Dung (TweetyProject), et compare l'accuracy avant/apres.
Liste aussi les cas concrets ou le symbolique corrige le modele neuronal.

Usage:
    python3 scripts/evaluate_symbolic.py --predictions results/full_pred.csv
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.rules.detector import RuleBasedFallacyDetector  # noqa: E402
from src.symbolic.dung import arbitrate  # noqa: E402

NONE_LABELS = ("not_fallacy", "other_fallacy")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--predictions", required=True, help="CSV de predictions du modele.")
    parser.add_argument("--rule-override-threshold", type=float, default=0.9)
    parser.add_argument("--show", type=int, default=15, help="Nb de corrections a afficher.")
    args = parser.parse_args()

    df = pd.read_csv(args.predictions)
    for col in ("text", "label", "predicted_label"):
        if col not in df.columns:
            raise SystemExit(f"Colonne manquante dans le CSV: {col}")
    if "predicted_confidence" not in df.columns:
        df["predicted_confidence"] = 0.5

    detector = RuleBasedFallacyDetector()

    ml_correct = 0
    sym_correct = 0
    fixed_rows = []     # le symbolique corrige une erreur du modele
    broke_rows = []     # le symbolique casse une bonne prediction

    for _, row in df.iterrows():
        text = str(row["text"])
        true = str(row["label"])
        ml_label = str(row["predicted_label"])
        ml_conf = float(row["predicted_confidence"]) if pd.notna(row["predicted_confidence"]) else 0.5

        rule_pred = detector.predict(text)
        rule_label = rule_pred.label if rule_pred.label != "not_fallacy" else None
        rule_conf = rule_pred.confidence if rule_label else 0.0

        result = arbitrate(
            ml_label=ml_label, ml_confidence=ml_conf,
            rule_label=rule_label, rule_confidence=rule_conf,
            rule_override_threshold=args.rule_override_threshold,
        )
        sym_label = result["final_label"]

        ml_ok = ml_label == true
        sym_ok = sym_label == true
        ml_correct += int(ml_ok)
        sym_correct += int(sym_ok)

        if sym_label != ml_label:
            entry = {
                "text": text[:90],
                "true": true,
                "ml": ml_label,
                "symbolic": sym_label,
            }
            if sym_ok and not ml_ok:
                fixed_rows.append(entry)
            elif ml_ok and not sym_ok:
                broke_rows.append(entry)

    n = len(df)
    print("=" * 60)
    print("  APPORT DE LA COUCHE SYMBOLIQUE (arbitrage de Dung)")
    print("=" * 60)
    print(f"  examples              : {n}")
    print(f"  accuracy modele seul  : {ml_correct / n:.4f}")
    print(f"  accuracy + symbolique : {sym_correct / n:.4f}")
    print(f"  delta                 : {(sym_correct - ml_correct) / n:+.4f}")
    print(f"  cas corriges (gain)   : {len(fixed_rows)}")
    print(f"  cas degrades (perte)  : {len(broke_rows)}")
    print("=" * 60)

    if fixed_rows:
        print("\nCorrections symboliques (le symbolique rattrape le neuronal):")
        print(pd.DataFrame(fixed_rows).head(args.show).to_string(index=False))
    if broke_rows:
        print("\nRegressions (le symbolique degrade le neuronal):")
        print(pd.DataFrame(broke_rows).head(args.show).to_string(index=False))


if __name__ == "__main__":
    main()
