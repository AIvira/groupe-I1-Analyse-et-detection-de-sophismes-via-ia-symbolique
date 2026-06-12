# Groupe I1 — Detection neuro-symbolique de sophismes

Ce sous-projet implemente `I1 — Analyse et detection de sophismes par apprentissage symbolique` :
le pipeline **neuro-symbolique** decrit par le sujet, de bout en bout :

1. un **LLM** (Claude) extrait la structure argumentative d'un texte — premisses,
   conclusions, relations d'attaque/support, types de sophismes ;
2. **TweetyProject** projette cette structure dans un **framework d'argumentation de
   Dung** et calcule l'acceptabilite des arguments (extensions grounded / preferred /
   stable) — verification formelle de la coherence et filtrage des faux positifs ;
3. l'evaluation se fait a la fois sur un corpus de classification de sophismes
   (`causalNLP/logical-fallacy`) et sur un **corpus annote d'argument mining
   (US2016, AIFdb)** dont les conflits annotes alimentent directement les AF de Dung.

### Conformite au sujet

| Objectif du sujet | Etat | Realisation |
|---|---|---|
| Extraction d'arguments (premisses, conclusions, attaque/support) | ✅ | `src/extraction.py` — LLM Claude (sortie structuree) + repli heuristique hors-ligne |
| Classification des sophismes | ✅ | baseline TF-IDF / transformer / NLI + regles |
| Validation formelle via AF de Dung (TweetyProject) | ✅ | `src/symbolic.py` + `src/argmodel.py` (`to_dung`, `coherence`) |
| Evaluation sur corpus annote (US2016, ArgMine) F1/P/R | ✅ | `src/corpus_aif.py` — US2016 (AIFdb) -> AF de Dung |
| Analyse des corrections symbolique ↔ neuronal | ✅ | `scripts/evaluate_symbolic.py` |

## Objectif

Construire un pipeline explicable qui :
- charge un corpus tabulaire `csv` (dataset `causalNLP/logical-fallacy`)
- entraine des classifieurs (baseline TF-IDF rapide, transformer, NLI) en respectant les splits officiels
- applique des regles lexicales/structurelles de haute precision sur les sophismes bien marques
- **valide et arbitre** les predictions via l'argumentation abstraite de Dung (TweetyProject) :
  - chaque sophisme est associe a son *scheme argumentatif* (Walton) et sa *question critique* ;
  - la conclusion est projetee dans un AF de Dung et son acceptabilite calculee (extension fondee) ;
  - un desaccord regle/ML est resolu par la semantique fondee de Dung.

## Demarrage rapide

```bash
# 1. Dependances Python (uv) + JAR TweetyProject (necessite un JDK 11+)
uv sync
bash scripts/setup_tweety.sh

# 2. Entrainer une baseline rapide (sans torch)
python3 -m src.main train --dataset data/processed/fallacies_full.csv

# 3. Analyse neuro-symbolique complete d'un texte
python3 -m src.main analyze --text "Either you support this law or you hate freedom."
```

Le MVP cible d'abord les labels suivants :
- `ad_hominem`
- `fallacy_of_credibility`
- `false_dilemma`
- `straw_man`
- `not_fallacy`
- `other_fallacy`

## Structure

- `src/domain.py` : structures de donnees
- `src/rules.py` : moteur de regles lexicales/structurelles (haute precision)
- `src/training.py` : baseline supervisee TF-IDF (rapide, sans torch)
- `src/transformer_training.py` / `src/nli_training.py` : pipelines transformer & NLI (torch, charges a la demande)
- `src/metrics.py` : metriques unifiees (accuracy, balanced acc, macro/micro/weighted F1, par-classe) + dashboard console et JSON
- `src/extraction.py` : **extraction d'arguments** — LLM Claude (`messages.parse` + schema) + repli heuristique hors-ligne
- `src/llm_classifier.py` : **classifieur LLM** (version 2) — Claude classe les sophismes, pour comparaison avec le ML
- `src/argmodel.py` : modele de carte argumentative (`ArgUnit`/`ArgRelation`/`ArgumentMap`) + projection `to_dung()`
- `src/corpus_aif.py` : chargement de corpus AIF (US2016) -> `ArgumentMap` -> AF de Dung
- `src/symbolic.py` : **couche symbolique** — AF de Dung via TweetyProject (JPype), schemes argumentatifs, arbitrage
- `src/pipeline.py` : orchestration neuro-symbolique (`analyze` = extraction + classification + Dung)
- `src/main.py` : point d'entree CLI (imports paresseux : `train`/`predict`/`analyze` demarrent en < 0.5 s)
- `lib/` : JAR TweetyProject (telecharge via `scripts/setup_tweety.sh`, non versionne)
- `scripts/setup_tweety.sh` : telechargement du JAR Tweety
- `scripts/evaluate_symbolic.py` : mesure l'apport de la couche symbolique sur un CSV de predictions
- `scripts/import_causalnlp_logic.py` : import normalise du dataset `causalNLP/logical-fallacy`
- `tests/test_rules.py`, `tests/test_symbolic.py` : tests (regles + couche symbolique)

## Schema de donnees attendu

Le pipeline attend un fichier `csv` avec au minimum :
- `text` : texte de l'argument
- `label` : etiquette du sophisme

Colonnes optionnelles :
- `source`
- `split`
- `context`
- `topic`
- `masked_text`

Pour `causalNLP/logical-fallacy`, la colonne `split` doit etre preservee :
- `train`
- `dev`
- `test`

## Commandes (CLI)

La CLI a des imports paresseux : `train`, `predict`, `analyze`, `extract`,
`eval-corpus`, `evaluate` et `demo-af` demarrent vite ; seules
`train-transformer` / `train-nli` chargent `torch`/`transformers`.

```bash
# Baseline TF-IDF (rapide, sans torch)
python3 -m src.main train --dataset data/processed/fallacies_full.csv

# Prediction simple (rules | ml | hybrid)
python3 -m src.main predict --text "Either you support this law or you hate freedom." --mode hybrid

# Analyse neuro-symbolique complete (extraction + neuronal + regles + Dung/Tweety)
python3 -m src.main analyze --text "Either you support this law or you hate freedom."

# Extraire la structure argumentative (LLM si ANTHROPIC_API_KEY, sinon heuristique)
python3 -m src.main extract --text "We must ban it because everyone knows it is bad, but they deny it."

# Evaluer un corpus annote d'argument mining (US2016) via les AF de Dung
python3 -m src.main eval-corpus --download --all-semantics

# Version 2 : Claude comme classifieur, puis comparaison cote a cote
python3 -m src.main classify-llm --dataset data/processed/fallacies_full.csv --limit 100
python3 -m src.main compare results/full_metrics.json results/llm_metrics.json

# Re-afficher les metriques depuis un CSV de predictions
python3 -m src.main evaluate --predictions-path results/test_predictions.csv

# Pipelines plus forts (chargent torch a la demande, defaults senses)
python3 -m src.main train-transformer --dataset data/processed/fallacies_full.csv --epochs 4
python3 -m src.main train-nli --dataset data/processed/fallacies_full.csv
```

L'entrainement :
- selectionne le meilleur modele selon le `macro F1` sur `dev`, re-entraine sur `train + dev`, evalue sur `test`
- affiche un dashboard de metriques (accuracy, balanced acc, macro/micro/weighted F1, par-classe, top confusions)
- sauvegarde : rapport texte (`results/training_report.txt`), metriques (`results/metrics.json`),
  predictions (`results/test_predictions.csv`), erreurs (`results/test_errors.csv`)

Le pipeline `train-transformer` :
- fine-tune un transformer multiclasses sur les `13` labels du corpus
- utilise des `class weights`
- selectionne le meilleur checkpoint sur `dev macro F1`

Le pipeline `train-nli` :
- transforme la classification en `label matching`
- compare le texte a chaque label via :
  - le nom du sophisme
  - sa description
  - sa forme logique issue de `mappings.csv`
- choisit le label avec le meilleur score d'entailment

## Import du dataset causalNLP

Cloner le repo source :

```bash
git clone https://github.com/causalNLP/logical-fallacy data/raw/causalNLP-repo
```

Produire le CSV normalise pour le MVP :

```bash
python3 scripts/import_causalnlp_logic.py \
  --repo-path data/raw/causalNLP-repo \
  --dataset both \
  --taxonomy full \
  --output data/processed/fallacies.csv
```

Si vous voulez une taxonomie reduite pour un premier benchmark plus stable :

```bash
python3 scripts/import_causalnlp_logic.py \
  --repo-path data/raw/causalNLP-repo \
  --dataset both \
  --taxonomy reduced \
  --output data/processed/fallacies_reduced.csv
```

Si vous voulez generer les deux variantes d'un coup :

```bash
python3 scripts/import_causalnlp_logic.py \
  --repo-path data/raw/causalNLP-repo \
  --dataset both \
  --taxonomy both \
  --output data/processed/fallacies.csv
```

Cela produit :
- `data/processed/fallacies_full.csv`
- `data/processed/fallacies_reduced.csv`

Comparaison recommandee :

```bash
python3 -m src.main train --dataset data/processed/fallacies_full.csv --report-path results/full_report.txt
python3 -m src.main train --dataset data/processed/fallacies_reduced.csv --report-path results/reduced_report.txt
```

## Couche symbolique (TweetyProject / Dung)

Le module `src/symbolic.py` demarre un JVM (JPype) et expose l'argumentation
abstraite de Dung de TweetyProject.

**Schemes & questions critiques.** Chaque type de sophisme est associe a un
*scheme argumentatif* (Walton) et a la *question critique* qui le met en defaut.
On encode cela par un petit AF `CLAIM <- CRITICAL_QUESTION` : sans reponse a la
question critique (cas par defaut d'un sophisme), `CLAIM` n'est pas dans
l'extension fondee => verdict formel « fallacieux ». Si une reponse est fournie,
`ANSWER -> CRITICAL_QUESTION` reinstaure `CLAIM` => le sophisme detecte etait un
faux positif.

**Arbitrage.** En cas de desaccord regle/ML, on construit un AF ou chaque
detecteur attaque l'hypothese nulle `DEFAULT_NONE` ; une regle explicite tres
confiante (poids >= 0.9) attaque la prediction ML (la regle prime), sinon le ML
prime. Le label retenu est le detecteur acceptable (extension fondee) le plus
confiant.

```bash
# Analyse complete (neuronal + regles + verdict symbolique de Dung)
python3 -m src.main analyze --text "“against the man;” attacking the individual rather than their position."

# Demonstration des semantiques de Dung sur un AF arbitraire
python3 -m src.main demo-af --attack "a->b" --attack "b->c" --attack "c->a"

# Mesurer l'apport du symbolique sur un CSV de predictions
python3 scripts/evaluate_symbolic.py --predictions results/full_pred.csv
```

## Extraction d'arguments (LLM) & corpus US2016

**Extraction.** `src/extraction.py` transforme un texte en carte argumentative
(`ArgumentMap`). Avec une cle API Anthropic, l'extraction est faite par Claude
(`messages.parse` + schema Pydantic, modele `claude-opus-4-8` par defaut,
surchargeable via `ANTHROPIC_MODEL`). Sans cle, un **repli heuristique
deterministe** (marqueurs de discours « because / therefore / but » + regles de
sophismes) prend le relais, ce qui rend tout le pipeline executable et testable
hors-ligne.

```bash
# Avec LLM : export ANTHROPIC_API_KEY=...  (sinon repli heuristique automatique)
python3 -m src.main extract --text "We must ban this app because everyone knows it spies, but the firm denies it."
```

La carte est projetee en AF de Dung (`ArgumentMap.to_dung()`), puis on calcule
l'acceptabilite des unites (`coherence()`) : une conclusion attaquee et non
reinstauree n'appartient pas a l'extension fondee => incoherence / sophisme.

**Corpus US2016 (argument mining annote).** `src/corpus_aif.py` charge un
nodeset AIF (AIFdb) : les propositions (I-nodes) deviennent des arguments, les
conflits annotes (CA-nodes) des **attaques de Dung**, les inferences (RA-nodes)
des supports. On obtient un **vrai** framework d'argumentation extrait d'un
corpus annote, evalue par TweetyProject.

```bash
python3 -m src.main eval-corpus --download --all-semantics
# ex. US2016 : 5293 propositions, 889 attaques -> AF de Dung
#   grounded/stable/preferred : 802 arguments acceptes, 542 rejetes
```

## Version 2 — Claude comme classifieur (comparaison pedagogique)

`src/llm_classifier.py` ajoute un **classifieur LLM** (`LLMFallacyClassifier`) :
Claude classe directement chaque texte dans l'un des 13 sophismes (sortie
structuree contrainte a un `enum`, prompt systeme des definitions mis en cache).
But : comparer, pour la soutenance, une approche **LLM zero-shot** a nos
classifieurs **statistiques** (TF-IDF, transformer) sur le meme split de test —
notamment sur les classes semantiquement diffuses (ex. `intentional`) ou un
sac-de-mots plafonne.

```bash
export ANTHROPIC_API_KEY=...
# Classer le test avec Claude (--limit pour borner le cout)
python3 -m src.main classify-llm --dataset data/processed/fallacies_full.csv --limit 100

# Comparer toutes les approches cote a cote
python3 -m src.main compare results/full_metrics.json results/llm_metrics.json
```

Exemple de sortie `compare` :

```
  modele                                 n  accuracy   macroF1   bal.acc
  llm:claude-opus-4-8                  100    ......    ......    ......
  logreg_tfidf_rich                    511    0.4129    0.3990    0.4042
```

> Sans cle API, `classify-llm` s'arrete avec un message clair ; le reste du
> pipeline reste utilisable.

## Resultats & metriques

Commande `train` / `analyze` -> dashboard console + `results/metrics.json`.

| Approche | Taxonomie | Classes | Accuracy | Macro F1 |
|----------|-----------|---------|----------|----------|
| TF-IDF baseline | full | 13 | 0.413 | 0.399 |
| Transformer (roberta-base) | full | 13 | 0.474 | 0.442 |
| TF-IDF baseline | reduced | 5 | 0.767 | 0.578 |

Sur 13 classes, ~0.47 est proche du plafond rapporte par le papier `causalNLP`
(les classes sont fortement confusables ; hasard ~0.08, classe majoritaire ~0.13).

**Apport symbolique.** Sur la taxonomie `full`, le moteur de regles se declenche
sur ~4.5 % du test (precision ~74 %). L'arbitrage de Dung corrige des cas a
marqueur lexical net (ex. « attacking the individual » mal classe `faulty_generalization`
par le ML -> corrige en `ad_hominem`) sans regression au seuil 0.9. L'effet net
sur l'accuracy est faible (+0.2 pt) : ce corpus est constitue d'exemples courts
de manuel ou le signal lexical est deja capte par le neuronal. La valeur
principale du symbolique ici est **l'explicabilite formelle** (verdict + question
critique par prediction) et le **mecanisme d'arbitrage** verifiable.

## Notes de conception

- Les regles servent d'explicabilite et de garde-fou.
- Le classifieur leger sert de premiere couche d'apprentissage.
- Le mode hybride permet de comparer facilement : `rules` vs `ml` vs `hybrid`.
- La normalisation du corpus est separee du pipeline pour pouvoir brancher plusieurs datasets sans reecrire le coeur du code.
- Le dataset `causalNLP/logical-fallacy` expose un champ `masked_articles` sur la partie `edu`; il est conserve dans `masked_text` pour experimenter une representation plus structuree.
- Le fichier `groupe-I1/data/raw/causalNLP/mappings.csv` sert a enrichir les predictions avec la description et la forme logique associees au label predit.
- Avec ce dataset, la taxonomie `full` doit etre consideree comme la reference. La taxonomie `reduced` est volontairement lossy et sert seulement a un premier benchmark plus simple.
- La baseline supervisee exploite maintenant :
  - `word n-grams` sur `text`
  - `char n-grams` sur `text`
  - `word n-grams` sur `masked_text`
- Par defaut, `context` n'est plus utilise pour l'entrainement.
  `context` provient de `mappings.csv` et encode directement la classe; l'utiliser comme feature provoquerait une fuite de label.
- Un audit verifie aussi les recouvrements exacts de `text` entre `train`, `dev` et `test`, puis retire par defaut les doublons de `train` qui reapparaissent dans `dev/test`.
- Les modeles compares sont :
  - `LogisticRegression`
  - `LinearSVC` calibre pour obtenir des probabilites
- Le rapport d'entrainement inclut maintenant :
  - la matrice de confusion
  - les principales paires de confusion
  - un echantillon d'erreurs reelles
- Pour la taxonomie `full`, la strategie recommandee est maintenant :
  - baseline `train`
  - transformer multiclasses `train-transformer`
  - pipeline NLI `train-nli`
