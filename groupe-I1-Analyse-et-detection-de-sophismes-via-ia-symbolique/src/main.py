from __future__ import annotations

import argparse
import dataclasses
import json
import pickle
import sys
from pathlib import Path

# Lazy package bootstrap: when run as `python src/main.py`, expose `src` on path.
if __package__ in {None, ""}:
    project_root = Path(__file__).resolve().parents[1]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

# IMPORTANT: keep top-level imports cheap.
# `torch`/`transformers` are heavy (several seconds to import) and are only
# needed by the `train-transformer` / `train-nli` commands. We import them
# lazily inside those command handlers so that `train`, `predict` and
# `evaluate` start instantly.

DEFAULT_MODEL_PATH = Path("models/baseline.pkl")
DEFAULT_MAPPINGS_PATH = Path("data/raw/causalNLP/mappings.csv")
DEFAULT_REPORT_PATH = Path("results/training_report.txt")
DEFAULT_PREDICTIONS_PATH = Path("results/test_predictions.csv")
DEFAULT_ERRORS_PATH = Path("results/test_errors.csv")
DEFAULT_METRICS_PATH = Path("results/metrics.json")
DEFAULT_TRANSFORMER_DIR = Path("models/transformer")
DEFAULT_NLI_DIR = Path("models/nli")


def _print_artifacts(artifacts) -> None:
    """Shared, compact console summary for any training artifacts."""
    from src.evaluation.metrics import format_metrics_console

    print(format_metrics_console(artifacts))


def cmd_train(args: argparse.Namespace) -> None:
    from src.domain.models import TrainingConfig
    from src.classifiers.baseline import (
        train_baseline,
        write_error_examples_csv,
        write_predictions_csv,
        write_training_summary,
    )
    from src.evaluation.metrics import write_metrics_json

    config = TrainingConfig()
    artifacts = train_baseline(args.dataset, config)

    model_path = Path(args.model_path)
    model_path.parent.mkdir(parents=True, exist_ok=True)
    with model_path.open("wb") as handle:
        pickle.dump(artifacts.pipeline, handle)

    write_training_summary(artifacts, args.report_path)
    write_predictions_csv(artifacts, args.predictions_path)
    write_error_examples_csv(artifacts, args.errors_path)
    write_metrics_json(artifacts, args.metrics_path)

    _print_artifacts(artifacts)
    print(f"Model saved to:    {model_path}")
    print(f"Report:            {args.report_path}")
    print(f"Predictions:       {args.predictions_path}")
    print(f"Metrics (JSON):    {args.metrics_path}")


def _load_ml_model(args: argparse.Namespace):
    """Charge le classifieur ML : baseline TF-IDF seul, ou ensemble TF-IDF+RoBERTa.

    L'ensemble est active par defaut des qu'un dossier transformer existe ; on peut
    le forcer au baseline seul via `--no-ensemble`.
    """
    from src.classifiers.ensemble import load_ml_model

    model_path = Path(args.model_path)
    if not model_path.exists():
        return None
    transformer_dir = None
    if not getattr(args, "no_ensemble", False):
        candidate = Path(getattr(args, "transformer_dir", DEFAULT_TRANSFORMER_DIR))
        if candidate.exists():
            transformer_dir = str(candidate)
    return load_ml_model(str(model_path), transformer_dir=transformer_dir)


def cmd_predict(args: argparse.Namespace) -> None:
    from src.pipeline.hybrid import HybridFallacyPipeline

    model = _load_ml_model(args)
    mode = args.mode
    if model is None and mode in {"ml", "hybrid"}:
        print(
            f"[warn] no trained model at {args.model_path}; falling back to --mode rules. "
            "Run `train` first.",
            file=sys.stderr,
        )
        mode = "rules"

    pipeline = HybridFallacyPipeline(model=model, mappings_path=args.mappings_path)

    if mode == "rules":
        prediction = pipeline.predict_rules(args.text)
    elif mode == "ml":
        prediction = pipeline.predict_ml(args.text)
    else:
        prediction = pipeline.predict_hybrid(args.text)

    print(json.dumps(dataclasses.asdict(prediction), ensure_ascii=False, indent=2))


def cmd_train_transformer(args: argparse.Namespace) -> None:
    # Heavy deps imported only here.
    from src.classifiers.transformer import train_transformer_classifier
    from src.classifiers.baseline import (
        write_error_examples_csv,
        write_predictions_csv,
        write_training_summary,
    )
    from src.evaluation.metrics import write_metrics_json

    artifacts = train_transformer_classifier(
        dataset_path=args.dataset,
        output_dir=args.output_dir,
        pretrained_model_name=args.pretrained_model_name,
        num_train_epochs=args.epochs,
    )
    write_training_summary(artifacts, args.report_path)
    write_predictions_csv(artifacts, args.predictions_path)
    write_error_examples_csv(artifacts, args.errors_path)
    write_metrics_json(artifacts, args.metrics_path)

    _print_artifacts(artifacts)
    print(f"Model directory:   {artifacts.output_dir}")
    print(f"Metrics (JSON):    {args.metrics_path}")


def cmd_train_nli(args: argparse.Namespace) -> None:
    from src.classifiers.nli import train_nli_label_matching
    from src.classifiers.baseline import (
        write_error_examples_csv,
        write_predictions_csv,
        write_training_summary,
    )
    from src.evaluation.metrics import write_metrics_json

    artifacts = train_nli_label_matching(
        dataset_path=args.dataset,
        mappings_path=args.mappings_path,
        output_dir=args.output_dir,
        pretrained_model_name=args.pretrained_model_name,
        num_train_epochs=args.epochs,
    )
    write_training_summary(artifacts, args.report_path)
    write_predictions_csv(artifacts, args.predictions_path)
    write_error_examples_csv(artifacts, args.errors_path)
    write_metrics_json(artifacts, args.metrics_path)

    _print_artifacts(artifacts)
    print(f"Model directory:   {artifacts.output_dir}")
    print(f"Metrics (JSON):    {args.metrics_path}")


def cmd_analyze(args: argparse.Namespace) -> None:
    """Analyse neuro-symbolique complete (neuronal + regles + Dung/Tweety)."""
    from src.pipeline.hybrid import HybridFallacyPipeline

    model = _load_ml_model(args)

    pipeline = HybridFallacyPipeline(
        model=model,
        mappings_path=args.mappings_path,
        extract_structure=not args.no_structure,
    )
    result = pipeline.analyze(args.text)
    print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_analyze_corrections(args: argparse.Namespace) -> None:
    """Quantifier l'effet de la couche symbolique sur le classifieur statistique.

    Objectif I1 : « analyser les cas ou l'approche symbolique corrige les erreurs
    du modele (et inversement) ». On rejoue le pipeline sur le jeu de test et on
    compare, ligne a ligne, l'etiquette du **ML seul** a l'etiquette **hybride**
    (apres arbitrage regle/ML par la semantique fondee de Dung), face au gold.
    """
    import json as _json

    import pandas as pd

    from src.domain.models import TrainingConfig
    from src.classifiers.baseline import build_split_datasets, load_dataset
    from src.pipeline.hybrid import HybridFallacyPipeline
    from src.symbolic.dung import arbitrate

    model_path = Path(args.model_path)
    if not model_path.exists():
        raise SystemExit(
            f"Modele introuvable: {model_path}. Lancer `train` d'abord."
        )
    model = _load_ml_model(args)

    config = TrainingConfig()
    df = load_dataset(args.dataset, config)
    _, _, test_df = build_split_datasets(df, config)
    if args.limit:
        test_df = test_df.head(args.limit)

    pipeline = HybridFallacyPipeline(model=model, config=config, extract_structure=False)
    texts = test_df[config.text_column].astype(str).tolist()
    gold = test_df[config.label_column].astype(str).tolist()

    rows = []
    n_disagree = 0
    for i, (text, y) in enumerate(zip(texts, gold)):
        ml = pipeline.predict_ml(text)
        rule = pipeline.predict_rules(text)
        rule_label = rule.label if rule.label != "not_fallacy" else None
        rule_conf = rule.confidence if rule_label else 0.0
        arb = arbitrate(
            ml_label=ml.label,
            ml_confidence=ml.confidence,
            rule_label=rule_label,
            rule_confidence=rule_conf,
        )
        n_disagree += int(bool(arb["disagreement"]))
        rule_only = rule_label or "not_fallacy"
        rows.append(
            {
                "text": text,
                "gold": y,
                "ml_label": ml.label,
                "rule_label": rule_label or "",
                "rule_only_label": rule_only,
                "final_label": arb["final_label"],
                "winner": arb["winner"],
                "changed": arb["final_label"] != ml.label,
                "ml_correct": ml.label == y,
                "rule_correct": rule_only == y,
                "hybrid_correct": arb["final_label"] == y,
            }
        )
        if args.progress:
            print(f"\r  corrections: {i + 1}/{len(texts)}", end="", file=sys.stderr, flush=True)
    if args.progress:
        print("", file=sys.stderr)

    n = len(rows)
    changed = [r for r in rows if r["changed"]]
    # Sens 1 : le symbolique (arbitrage regle/Dung) corrige le neuronal/ML.
    corrected = [r for r in changed if not r["ml_correct"] and r["hybrid_correct"]]
    regressed = [r for r in changed if r["ml_correct"] and not r["hybrid_correct"]]
    neutral = [r for r in changed if r not in corrected and r not in regressed]
    # Sens 2 (inversement) : le neuronal corrige la couche symbolique/regles,
    # i.e. la regle proposait une etiquette fausse mais l'hybride retient le ML correct.
    neural_fixes_rule = [
        r for r in rows
        if r["rule_label"] and not r["rule_correct"] and r["hybrid_correct"]
        and r["final_label"] != r["rule_only_label"]
    ]
    ml_acc = sum(r["ml_correct"] for r in rows) / n if n else 0.0
    rule_acc = sum(r["rule_correct"] for r in rows) / n if n else 0.0
    hyb_acc = sum(r["hybrid_correct"] for r in rows) / n if n else 0.0

    summary = {
        "n_test": n,
        "ml_only_accuracy": round(ml_acc, 4),
        "rule_only_accuracy": round(rule_acc, 4),
        "hybrid_accuracy": round(hyb_acc, 4),
        "accuracy_delta_vs_ml": round(hyb_acc - ml_acc, 4),
        "disagreements_rule_vs_ml": n_disagree,
        "labels_changed_by_symbolic": len(changed),
        "symbolic_corrects_neural": len(corrected),
        "symbolic_regressed": len(regressed),
        "symbolic_changed_but_neutral": len(neutral),
        "neural_corrects_symbolic": len(neural_fixes_rule),
    }

    out_csv = Path(args.output_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(out_csv, index=False)
    Path(args.output_json).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output_json).write_text(
        _json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print("=" * 64)
    print("  INTERACTIONS SYMBOLIQUE <-> NEURONAL (jeu de test)")
    print("=" * 64)
    print(f"  exemples de test                : {summary['n_test']}")
    print(f"  accuracy ML seul                : {summary['ml_only_accuracy']:.4f}")
    print(f"  accuracy regles seules          : {summary['rule_only_accuracy']:.4f}")
    print(f"  accuracy hybride (apres Dung)   : {summary['hybrid_accuracy']:.4f}")
    print(f"  delta hybride vs ML             : {summary['accuracy_delta_vs_ml']:+.4f}")
    print("-" * 64)
    print(f"  desaccords regle vs ML          : {summary['disagreements_rule_vs_ml']}")
    print(f"  Sens 1 — le symbolique corrige le neuronal : {summary['symbolic_corrects_neural']}")
    print(f"    -> regressions introduites    : {summary['symbolic_regressed']}")
    print(f"    -> changements neutres        : {summary['symbolic_changed_but_neutral']}")
    print(f"  Sens 2 — le neuronal corrige le symbolique : {summary['neural_corrects_symbolic']}")
    print("=" * 64)
    if corrected:
        print("\n  Exemples ou le SYMBOLIQUE corrige le neuronal :")
        for r in corrected[: args.examples]:
            print(f"   - gold={r['gold']} | ml={r['ml_label']} -> final={r['final_label']} "
                  f"(regle={r['rule_label']})")
            print(f"     « {r['text'][:90]} »")
    if neural_fixes_rule:
        print("\n  Exemples ou le NEURONAL corrige le symbolique :")
        for r in neural_fixes_rule[: args.examples]:
            print(f"   - gold={r['gold']} | regle={r['rule_only_label']} -> final={r['final_label']} "
                  f"(ml={r['ml_label']})")
            print(f"     « {r['text'][:90]} »")
    print(f"\nDetail par exemple : {out_csv}")
    print(f"Synthese (JSON)    : {args.output_json}")


def cmd_extract(args: argparse.Namespace) -> None:
    """Extraire la structure argumentative d'un texte (LLM ou heuristique)."""
    from src.extraction.extractor import get_extractor

    extractor = get_extractor(prefer_llm=not args.no_llm)
    argmap = extractor.extract(args.text)
    out = argmap.to_dict()
    out["coherence"] = argmap.coherence("grounded")
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_eval_corpus(args: argparse.Namespace) -> None:
    """Charger un corpus AIF annote (US2016, ArgMine...), projeter en AF de Dung, evaluer."""
    from src.extraction.corpus_aif import aifdb_url, attack_subgraph, download_aif, load_aif

    corpus_path = Path(args.corpus_path) if args.corpus_path else Path(
        f"data/raw/{args.corpus_name.lower()}.json"
    )
    if not corpus_path.exists():
        if args.download:
            url = aifdb_url(args.corpus_name)
            print(f"[eval-corpus] telechargement {url} ...")
            download_aif(url, str(corpus_path))
        else:
            raise SystemExit(
                f"Corpus introuvable: {corpus_path}. Relancer avec --download "
                "ou fournir --corpus-path."
            )

    amap = load_aif(str(corpus_path))
    sub = attack_subgraph(amap)
    print("=" * 56)
    print(f"  CORPUS AIF '{args.corpus_name}' -> AF de Dung (TweetyProject)")
    print("=" * 56)
    print(amap.summary())
    print(f"sous-graphe d'attaques : {len(sub.units)} arguments, {len(sub.attacks())} attaques")
    for sem in ("grounded", "stable", "preferred"):
        if sem != "grounded" and not args.all_semantics:
            continue
        coh = sub.coherence(sem)
        print(
            f"  {sem:<10}: accepte={len(coh['accepted'])}  rejete={len(coh['rejected'])}  "
            f"extensions={coh['n_extensions']}  coherent={coh['coherent']}"
        )


def cmd_demo_af(args: argparse.Namespace) -> None:
    """Demontre les semantiques de Dung sur un AF (TweetyProject)."""
    from src.symbolic.dung import DungAF

    af = DungAF()
    for src_node, tgt_node in args.attacks:
        af.add_attack(src_node, tgt_node)
    print(af.describe())


def cmd_evaluate(args: argparse.Namespace) -> None:
    """Re-print metrics from a saved predictions CSV without retraining."""
    from src.evaluation.metrics import metrics_from_predictions_csv, format_metrics_dict

    metrics = metrics_from_predictions_csv(args.predictions_path)
    print(format_metrics_dict(metrics))


def cmd_compare(args: argparse.Namespace) -> None:
    """Comparer plusieurs approches depuis leurs fichiers metrics.json."""
    import json as _json

    rows = []
    for path in args.metrics_paths:
        p = Path(path)
        if not p.exists():
            print(f"[warn] absent: {path}", file=sys.stderr)
            continue
        data = _json.loads(p.read_text(encoding="utf-8"))
        m = data.get("test_metrics", {})
        rows.append((
            data.get("model_name", p.stem),
            m.get("n_examples", 0),
            m.get("accuracy", 0.0),
            m.get("macro_f1", 0.0),
            m.get("balanced_accuracy", 0.0),
        ))

    if not rows:
        raise SystemExit("Aucun fichier de metriques lisible.")

    print("=" * 72)
    print("  COMPARAISON DES APPROCHES")
    print("=" * 72)
    print(f"  {'modele':<34}{'n':>6}{'accuracy':>10}{'macroF1':>10}{'bal.acc':>10}")
    print("-" * 72)
    for name, n, acc, mf1, bacc in sorted(rows, key=lambda r: -r[3]):
        print(f"  {name:<34}{n:>6}{acc:>10.4f}{mf1:>10.4f}{bacc:>10.4f}")
    print("=" * 72)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="sophismes",
        description="I1 - detection de sophismes (baseline ML, transformer, NLI, symbolique).",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # train (baseline sklearn, instantane)
    p = sub.add_parser("train", help="Baseline TF-IDF (rapide, sans torch).")
    p.add_argument("--dataset", required=True, help="CSV normalise (text,label,split,...).")
    p.add_argument("--model-path", default=str(DEFAULT_MODEL_PATH))
    p.add_argument("--report-path", default=str(DEFAULT_REPORT_PATH))
    p.add_argument("--predictions-path", default=str(DEFAULT_PREDICTIONS_PATH))
    p.add_argument("--errors-path", default=str(DEFAULT_ERRORS_PATH))
    p.add_argument("--metrics-path", default=str(DEFAULT_METRICS_PATH))
    p.set_defaults(func=cmd_train)

    # predict
    p = sub.add_parser("predict", help="Predire le sophisme d'un texte.")
    p.add_argument("--text", required=True)
    p.add_argument("--mode", choices=["rules", "ml", "hybrid"], default="hybrid")
    p.add_argument("--model-path", default=str(DEFAULT_MODEL_PATH))
    p.add_argument("--mappings-path", default=str(DEFAULT_MAPPINGS_PATH))
    p.add_argument("--transformer-dir", default=str(DEFAULT_TRANSFORMER_DIR),
                   help="Dossier RoBERTa pour l'ensemble TF-IDF+RoBERTa (defaut: models/transformer).")
    p.add_argument("--no-ensemble", action="store_true",
                   help="Forcer le baseline TF-IDF seul (desactive l'ensemble).")
    p.set_defaults(func=cmd_predict)

    # train-transformer (charge torch a la demande)
    p = sub.add_parser("train-transformer", help="Fine-tune un transformer (necessite torch).")
    p.add_argument("--dataset", required=True)
    p.add_argument("--output-dir", default=str(DEFAULT_TRANSFORMER_DIR))
    p.add_argument("--pretrained-model-name", default="roberta-base")
    p.add_argument("--epochs", type=int, default=4)
    p.add_argument("--report-path", default=str(DEFAULT_REPORT_PATH))
    p.add_argument("--predictions-path", default=str(DEFAULT_PREDICTIONS_PATH))
    p.add_argument("--errors-path", default=str(DEFAULT_ERRORS_PATH))
    p.add_argument("--metrics-path", default=str(DEFAULT_METRICS_PATH))
    p.set_defaults(func=cmd_train_transformer)

    # train-nli (charge torch a la demande)
    p = sub.add_parser("train-nli", help="Label-matching par entailment (necessite torch).")
    p.add_argument("--dataset", required=True)
    p.add_argument("--mappings-path", default=str(DEFAULT_MAPPINGS_PATH))
    p.add_argument("--output-dir", default=str(DEFAULT_NLI_DIR))
    p.add_argument("--pretrained-model-name", default="roberta-base")
    p.add_argument("--epochs", type=int, default=4)
    p.add_argument("--report-path", default=str(DEFAULT_REPORT_PATH))
    p.add_argument("--predictions-path", default=str(DEFAULT_PREDICTIONS_PATH))
    p.add_argument("--errors-path", default=str(DEFAULT_ERRORS_PATH))
    p.add_argument("--metrics-path", default=str(DEFAULT_METRICS_PATH))
    p.set_defaults(func=cmd_train_nli)

    # analyze (pipeline neuro-symbolique complet)
    p = sub.add_parser("analyze", help="Analyse neuro-symbolique d'un texte (extraction + Dung/Tweety).")
    p.add_argument("--text", required=True)
    p.add_argument("--model-path", default=str(DEFAULT_MODEL_PATH))
    p.add_argument("--mappings-path", default=str(DEFAULT_MAPPINGS_PATH))
    p.add_argument("--no-structure", action="store_true", help="Ne pas extraire la structure argumentative.")
    p.add_argument("--transformer-dir", default=str(DEFAULT_TRANSFORMER_DIR),
                   help="Dossier RoBERTa pour l'ensemble TF-IDF+RoBERTa (defaut: models/transformer).")
    p.add_argument("--no-ensemble", action="store_true",
                   help="Forcer le baseline TF-IDF seul (desactive l'ensemble).")
    p.set_defaults(func=cmd_analyze)

    # extract (structure argumentative : LLM ou heuristique)
    p = sub.add_parser("extract", help="Extraire la structure argumentative (premisses/conclusions/relations).")
    p.add_argument("--text", required=True)
    p.add_argument("--no-llm", action="store_true", help="Forcer l'extracteur heuristique (pas d'appel LLM).")
    p.set_defaults(func=cmd_extract)

    # analyze-corrections (objectif I1 : ou le symbolique corrige le classifieur)
    p = sub.add_parser(
        "analyze-corrections",
        help="Quantifier sur le test ou la couche symbolique corrige le classifieur.",
    )
    p.add_argument("--dataset", required=True)
    p.add_argument("--model-path", default=str(DEFAULT_MODEL_PATH))
    p.add_argument("--limit", type=int, default=None, help="Limiter le nombre d'exemples.")
    p.add_argument("--output-csv", default="results/corrections_detail.csv")
    p.add_argument("--output-json", default="results/corrections_summary.json")
    p.add_argument("--examples", type=int, default=5, help="Nb d'exemples corriges a afficher.")
    p.add_argument("--progress", action="store_true", help="Afficher la progression.")
    p.add_argument("--transformer-dir", default=str(DEFAULT_TRANSFORMER_DIR),
                   help="Dossier RoBERTa pour l'ensemble TF-IDF+RoBERTa (defaut: models/transformer).")
    p.add_argument("--no-ensemble", action="store_true",
                   help="Forcer le baseline TF-IDF seul (desactive l'ensemble).")
    p.set_defaults(func=cmd_analyze_corrections)

    # eval-corpus (corpus AIF annote -> AF de Dung)
    p = sub.add_parser("eval-corpus", help="Charger un corpus AIF annote (US2016, ArgMine...) et l'evaluer via Dung.")
    p.add_argument("--corpus-name", default="US2016", help="Nom du corpus AIFdb (ex. US2016, ArgMine).")
    p.add_argument("--corpus-path", default=None, help="Chemin local (sinon data/raw/<nom>.json).")
    p.add_argument("--download", action="store_true", help="Telecharger le corpus s'il est absent.")
    p.add_argument("--all-semantics", action="store_true", help="Calculer aussi stable et preferred (plus lent).")
    p.set_defaults(func=cmd_eval_corpus)

    # demo-af (semantiques de Dung sur un AF arbitraire)
    p = sub.add_parser("demo-af", help="Calculer les extensions de Dung d'un AF.")
    p.add_argument(
        "--attack",
        dest="attacks",
        action="append",
        type=lambda s: tuple(s.split("->", 1)),
        default=[],
        metavar="A->B",
        help="Arete d'attaque, ex: --attack a->b --attack b->c (repetable).",
    )
    p.set_defaults(func=cmd_demo_af)

    # evaluate (re-affiche les metriques depuis un CSV de predictions)
    p = sub.add_parser("evaluate", help="Recalculer les metriques depuis un CSV de predictions.")
    p.add_argument("--predictions-path", default=str(DEFAULT_PREDICTIONS_PATH))
    p.set_defaults(func=cmd_evaluate)

    # compare (tableau cote a cote des approches)
    p = sub.add_parser("compare", help="Comparer plusieurs metrics.json cote a cote.")
    p.add_argument("metrics_paths", nargs="+", help="Chemins de fichiers metrics.json.")
    p.set_defaults(func=cmd_compare)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()