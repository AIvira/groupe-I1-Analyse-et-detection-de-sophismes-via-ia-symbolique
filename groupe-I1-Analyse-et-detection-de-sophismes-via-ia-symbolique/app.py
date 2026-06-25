"""Demo interactive du pipeline neuro-symbolique de detection de sophismes (I1).

Lancer depuis le dossier `groupe-I1-Analyse-et-detection-de-sophismes-via-ia-symbolique/` :

    streamlit run app.py

L'utilisateur saisit un texte argumentatif ; l'app affiche :
  1. la structure argumentative extraite (premisses/conclusions + relations),
  2. le graphe d'argumentation de Dung (unites acceptees / rejetees),
  3. le label de sophisme + le verdict symbolique formel,
  4. la question critique du scheme de Walton associe.

Tout reutilise `HybridFallacyPipeline.analyze()` : extraction LLM (Ollama local
par defaut) -> classification ML/regles -> arbitrage et verdict via TweetyProject.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# Demo locale : on cible Ollama (llama3.2) par defaut, meme si une cle OpenAI
# (potentiellement sans quota) traine dans l'environnement. Surchargeable en
# exportant LLM_BACKEND=openai avant de lancer l'app.
os.environ.setdefault("LLM_BACKEND", "ollama")

import streamlit as st

# Rendre le package `src` importable quand on lance `streamlit run app.py`.
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

MODEL_PATH = PROJECT_ROOT / "models" / "baseline.pkl"
TRANSFORMER_DIR = PROJECT_ROOT / "models" / "transformer"

EXAMPLES = [
    "Either you support this law or you hate freedom.",
    "We must ban this app because everyone knows it spies, but the firm denies it.",
    "You can't trust his economic plan, he's been divorced twice.",
    "Studies are funded by the industry, so their conclusions must be false.",
    "Every time I wash my car it rains, so washing my car causes rain.",
]

ROLE_COLORS = {
    "premise": "#dbeafe",      # bleu clair
    "conclusion": "#fde68a",   # jaune
    "claim": "#e9d5ff",        # violet clair
}


@st.cache_resource(show_spinner="Chargement du modele + demarrage de la JVM Tweety...")
def load_pipeline():
    """Charge le modele et construit le pipeline (JVM demarree paresseusement).

    Si un dossier RoBERTa est present, on charge l'ensemble TF-IDF+RoBERTa
    (meilleur macro F1 mesure ~0.47) ; sinon on retombe sur le baseline TF-IDF.
    """
    from src.classifiers.ensemble import load_ml_model
    from src.pipeline.hybrid import HybridFallacyPipeline

    model = None
    ensemble = False
    if MODEL_PATH.exists():
        transformer_dir = str(TRANSFORMER_DIR) if TRANSFORMER_DIR.exists() else None
        model = load_ml_model(str(MODEL_PATH), transformer_dir=transformer_dir)
        ensemble = transformer_dir is not None
    return HybridFallacyPipeline(model=model, extract_structure=True), model is not None, ensemble


def backend_status() -> str:
    from src.llm_backend import default_model, llm_available, using_local

    if not llm_available():
        return "Extraction : repli heuristique (aucun backend LLM joignable)"
    where = "Ollama local" if using_local() else "OpenAI distant"
    return f"Extraction LLM : {where} (modele `{default_model()}`)"


def structure_graph_dot(structure: dict) -> str:
    """Construit un graphe Graphviz (DOT) de la structure argumentative.

    Noeuds = unites (colorees par role, bord rouge si rejetees / non acceptees
    dans l'extension fondee). Aretes = relations support (gris) / attaque (rouge).
    """
    coherence = structure.get("coherence", {})
    accepted = set(coherence.get("accepted", []))
    fallacy_units = set(structure.get("fallacies", {}).keys())

    lines = [
        "digraph G {",
        "  rankdir=BT;",
        '  node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=10];',
        '  edge [fontname="Helvetica", fontsize=9];',
    ]
    for unit in structure.get("units", []):
        uid = unit["id"]
        role = unit.get("role", "claim")
        fill = ROLE_COLORS.get(role, "#e5e7eb")
        text = unit["text"].replace('"', "'")
        if len(text) > 60:
            text = text[:57] + "..."
        accepted_mark = "✓" if uid in accepted else "✗"
        flag = "  ⚠ sophisme" if uid in fallacy_units else ""
        label = f"{uid} [{role}] {accepted_mark}{flag}\\n{text}"
        border = "#dc2626" if uid not in accepted else "#16a34a"
        penwidth = "3" if uid in fallacy_units else "1.5"
        lines.append(
            f'  "{uid}" [label="{label}", fillcolor="{fill}", '
            f'color="{border}", penwidth={penwidth}];'
        )
    for rel in structure.get("relations", []):
        src, tgt, kind = rel["source"], rel["target"], rel["kind"]
        if kind == "attack":
            lines.append(f'  "{src}" -> "{tgt}" [label="attaque", color="#dc2626", penwidth=2];')
        else:
            lines.append(f'  "{src}" -> "{tgt}" [label="support", color="#9ca3af", style=dashed];')
    lines.append("}")
    return "\n".join(lines)


def verdict_graph_dot(verdict: dict) -> str:
    """Mini-AF du scheme de Walton : CRITICAL_QUESTION attaque CLAIM."""
    accepted = verdict.get("claim_accepted", False)
    claim_color = "#16a34a" if accepted else "#dc2626"
    lines = [
        "digraph V {",
        "  rankdir=LR;",
        '  node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=10];',
        f'  "CLAIM" [label="CLAIM\\n(conclusion)", fillcolor="#fef3c7", color="{claim_color}", penwidth=3];',
        '  "CRITICAL_QUESTION" [label="QUESTION\\nCRITIQUE", fillcolor="#fee2e2", color="#dc2626"];',
        '  "CRITICAL_QUESTION" -> "CLAIM" [label="attaque", color="#dc2626", penwidth=2];',
    ]
    if accepted:
        lines.append('  "ANSWER" [label="REPONSE", fillcolor="#dcfce7", color="#16a34a"];')
        lines.append('  "ANSWER" -> "CRITICAL_QUESTION" [label="defait", color="#16a34a", penwidth=2];')
    lines.append("}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Interface
# ---------------------------------------------------------------------------

st.set_page_config(page_title="I1 — Detection de sophismes (neuro-symbolique)", layout="wide")

st.title("🧠⚖️ Detection de sophismes — pipeline neuro-symbolique")
st.caption(
    "Sujet EPITA I1 : un LLM extrait la structure argumentative, "
    "puis TweetyProject (frameworks de Dung) valide formellement et arbitre."
)

with st.sidebar:
    st.header("Pipeline")
    st.markdown(
        "1. **Extraction** (LLM) : premisses, conclusions, relations\n"
        "2. **Classification** : regles lexicales + ML (TF-IDF)\n"
        "3. **Symbolique** (Dung/Tweety) : arbitrage + verdict formel\n"
        "4. **Scheme de Walton** : question critique du sophisme"
    )
    st.divider()
    extractor_choice = st.radio(
        "Extracteur d'arguments",
        ["Auto (LLM si dispo)", "LLM (Ollama/OpenAI)", "Heuristique (hors-ligne, deterministe)"],
        index=0,
        help="L'heuristique est deterministe : elle reconnait le motif « objection, "
             "but refutation » (retracted/debunked/exposed as false...) et reinstaure "
             "alors la conclusion — utile pour demontrer le filtrage de faux positif "
             "de facon reproductible, sans dependre d'un LLM.",
    )
    st.caption(backend_status())
    if not MODEL_PATH.exists():
        st.warning("Modele ML absent (`models/baseline.pkl`). Lancer `train` d'abord — "
                   "le pipeline tourne en mode regles seules en attendant.")

pipeline, has_model, ensemble_active = load_pipeline()
if ensemble_active:
    st.caption("Classifieur : ensemble TF-IDF + RoBERTa (macro F1 ~0.47)")
elif has_model:
    st.caption("Classifieur : TF-IDF seul (RoBERTa absent)")

st.subheader("Texte a analyser")
example = st.selectbox("Exemples", ["(saisie libre)"] + EXAMPLES, index=1)
default_text = "" if example == "(saisie libre)" else example
text = st.text_area("Texte argumentatif", value=default_text, height=100)

if st.button("Analyser", type="primary") and text.strip():
    # Choix de l'extracteur (cf. barre laterale) : on l'injecte dans le pipeline
    # mis en cache. `analyze()` utilise `self._extractor` s'il est defini, sinon
    # il retombe sur `get_extractor()` (LLM si dispo).
    from src.extraction.extractor import HeuristicArgumentExtractor, get_extractor

    if extractor_choice.startswith("Heuristique"):
        pipeline._extractor = HeuristicArgumentExtractor()
    elif extractor_choice.startswith("LLM"):
        pipeline._extractor = get_extractor(prefer_llm=True)
    else:
        pipeline._extractor = None  # auto
    with st.spinner("Analyse (extraction + Dung/Tweety)..."):
        result = pipeline.analyze(text)

    # --- Verdict principal -------------------------------------------------
    verdict = result["symbolic_verdict"]
    structure = result["argument_structure"]
    col1, col2, col3 = st.columns(3)
    col1.metric("Sophisme detecte", result["final_label"])
    col2.metric("Decide par", result["decided_by"])
    status = verdict["status"]
    col3.metric("Verdict symbolique", "🔴 fallacieux" if status == "fallacieux" else "🟢 valide")
    if verdict.get("false_positive_filtered"):
        st.success(
            "✅ **Faux positif filtre par le symbolique** : le neuronal a detecte un "
            "sophisme, mais la conclusion est reinstauree dans l'AF de Dung "
            "(la question critique du scheme est repondue)."
        )

    # --- Structure argumentative + graphe de Dung --------------------------
    st.divider()
    left, right = st.columns([3, 2])
    with left:
        st.subheader("Structure argumentative & graphe de Dung")
        if structure and structure.get("units"):
            st.graphviz_chart(structure_graph_dot(structure))
            st.caption(
                f"Extracteur : `{structure.get('extractor')}` · "
                f"✓ = accepte dans l'extension fondee, ✗ = rejete · "
                f"⚠ = unite taguee sophisme"
            )
            coh = structure.get("coherence", {})
            st.caption(
                f"Coherence (grounded) : {len(coh.get('accepted', []))} acceptes / "
                f"{len(coh.get('rejected', []))} rejetes — "
                f"{'coherent' if coh.get('coherent') else 'incoherent'}"
            )
        else:
            st.info("Pas de structure multi-unites extraite pour ce texte.")
    with right:
        st.subheader("Scheme de Walton")
        st.markdown(f"**Scheme** : {verdict['scheme']}")
        st.markdown(f"**Question critique** : _{verdict['critical_question']}_")
        st.graphviz_chart(verdict_graph_dot(verdict))
        st.caption(verdict["explanation"])

    # --- Detecteurs et arbitrage ------------------------------------------
    st.divider()
    st.subheader("Detecteurs & arbitrage symbolique")
    d1, d2, d3 = st.columns(3)
    neural = result.get("neural")
    if neural:
        d1.markdown(f"**Neuronal/ML**\n\n`{neural['label']}`\n\nconfiance {neural['confidence']:.2f}")
    else:
        d1.markdown("**Neuronal/ML**\n\n_(aucun modele charge)_")
    rules = result["rules"]
    d2.markdown(f"**Regles**\n\n`{rules['label']}`\n\nconfiance {rules['confidence']:.2f}")
    arb = result["symbolic_arbitration"]
    d3.markdown(
        f"**Arbitrage (Dung)**\n\n"
        f"desaccord : {'oui' if arb['disagreement'] else 'non'}\n\n"
        f"extension fondee : {arb['grounded_extension']}"
    )
    if rules.get("evidence"):
        with st.expander("Indices des regles"):
            for ev in rules["evidence"]:
                st.write(f"- {ev}")

    with st.expander("Resultat brut (JSON)"):
        st.json(result)
