"""Classification des propositions d'un corpus AIF (US2016/ArgMine) par l'ensemble
TF-IDF+RoBERTa, croisee avec le statut Dung (acceptee/rejetee dans l'extension fondee).

Objectif : analyse neuro-symbolique combinee. Le moteur de Dung (Tweety) dit quels
arguments survivent au debat (acceptes) ou tombent (rejetes) ; le classifieur dit de
quel TYPE de sophisme chaque proposition releve. On croise les deux pour voir si le
profil de sophismes des arguments REJETES differe de celui des arguments ACCEPTES.

Attention : ces corpus n'ont pas de label gold de sophisme. Le classifieur est
multi-classe force (13 classes, pas de "non-sophisme") : chaque proposition recoit
donc un type, qu'elle soit fallacieuse ou non. On rapporte la confiance moyenne et
un sous-ensemble haute-confiance pour temperer cette limite.

Usage :
    PYTHONPATH=. uv run python scripts/classify_aif_corpus.py US2016
    PYTHONPATH=. uv run python scripts/classify_aif_corpus.py ArgMine --conf 0.5
"""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd

from src.classifiers.ensemble import load_ml_model
from src.extraction.corpus_aif import attack_subgraph, load_aif

BASELINE = "models/baseline.pkl"
TRANSFORMER = "models/transformer"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("corpus", help="Nom du corpus (US2016, ArgMine).")
    ap.add_argument("--corpus-path", default=None)
    ap.add_argument("--conf", type=float, default=0.5, help="Seuil de confiance haute-conf.")
    ap.add_argument("--out-dir", default="results")
    args = ap.parse_args()

    corpus_path = args.corpus_path or f"data/raw/{args.corpus.lower()}.json"
    if not Path(corpus_path).exists():
        raise SystemExit(f"Corpus introuvable: {corpus_path}")

    # 1. Charger le corpus, restreindre au sous-graphe d'attaques + statut Dung.
    amap = load_aif(corpus_path)
    sub = attack_subgraph(amap)
    coh = sub.coherence("grounded")
    accepted = set(coh["accepted"])
    units = list(sub.units.values())
    print(f"[{args.corpus}] sous-graphe d'attaques : {len(units)} propositions "
          f"({len(accepted)} acceptees / {len(units) - len(accepted)} rejetees)")

    # 2. Classifier chaque proposition avec l'ensemble TF-IDF + RoBERTa.
    model = load_ml_model(BASELINE, transformer_dir=TRANSFORMER)
    classes = list(model.classes_)
    frame = pd.DataFrame({"text": [u.text for u in units], "masked_text": "", "context": ""})
    proba = np.asarray(model.predict_proba(frame))
    pred_idx = proba.argmax(axis=1)
    rows = []
    for unit, idx, dist in zip(units, pred_idx, proba):
        rows.append({
            "id": unit.id,
            "text": unit.text,
            "dung_status": "accepted" if unit.id in accepted else "rejected",
            "fallacy": classes[idx],
            "confidence": float(dist[idx]),
        })
    df = pd.DataFrame(rows)

    # 3. Distributions croisees.
    def profile(sub_df: pd.DataFrame, title: str) -> None:
        print(f"\n=== {title} (n={len(sub_df)}, conf moy={sub_df['confidence'].mean():.3f}) ===")
        counts = Counter(sub_df["fallacy"])
        for label, n in counts.most_common():
            print(f"  {label:24} {n:4d}  ({100*n/len(sub_df):4.1f}%)")

    profile(df, "TOUTES propositions (sophisme predit)")
    profile(df[df["dung_status"] == "accepted"], "ACCEPTEES par Dung")
    profile(df[df["dung_status"] == "rejected"], "REJETEES par Dung")

    hi = df[df["confidence"] >= args.conf]
    if len(hi):
        profile(hi, f"HAUTE CONFIANCE (>= {args.conf})")

    # 4. Tableau accepted vs rejected en pourcentage (ecart de profil).
    ct = pd.crosstab(df["fallacy"], df["dung_status"], normalize="columns") * 100
    ct = ct.reindex(columns=["accepted", "rejected"]).fillna(0.0)
    ct["delta(rej-acc)"] = ct.get("rejected", 0) - ct.get("accepted", 0)
    ct = ct.sort_values("delta(rej-acc)", ascending=False)
    print("\n=== PROFIL accepte vs rejete (% par colonne), trie par sur-representation chez les REJETES ===")
    print(ct.round(1).to_string())

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    csv_path = out / f"{args.corpus.lower()}_fallacy_classification.csv"
    df.to_csv(csv_path, index=False)
    print(f"\n[ecrit] {csv_path}")


if __name__ == "__main__":
    main()
