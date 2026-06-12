# Corpus recommandes

## Priorite pour le MVP

### 1. Logic / LogicClimate
- Source papier : ACL Anthology, `Logical Fallacy Detection` (EMNLP Findings 2022)
- URL papier : `https://aclanthology.org/2022.findings-emnlp.532/`
- URL code/dataset : `https://github.com/causalNLP/logical-fallacy`
- Interet : dataset directement centre sur les sophismes logiques, avec labels exploitables pour une baseline de classification.
- Usage recommande : point de depart principal pour la V1.
- Statut ici : retenu comme corpus principal.

### 2. Argotario
- Source papier : ACL Anthology, `Argotario: Computational Argumentation Meets Serious Games` (2017)
- URL papier : `https://aclanthology.org/D17-2002/`
- Interet : corpus centre sur des sophismes du quotidien et utile pour completer des exemples plus simples et plus pedagogiques.
- Usage recommande : ajout en second temps pour enrichir quelques classes.

### 3. CoCoLoFa
- Source papier : `CoCoLoFa: A Dataset of News Comments with Common Logical Fallacies` (2024)
- URL papier : `https://arxiv.org/abs/2410.03457`
- Interet : corpus recent, plus grand, axe commentaires d'actualite.
- Usage recommande : extension apres MVP, une fois la normalisation des labels stabilisee.

## Corpus utiles pour la structure argumentative

### 4. US2016
- Source papier : Springer, `Argumentation in the 2016 US presidential elections` (publie le 9 fevrier 2019)
- URL papier : `https://link.springer.com/article/10.1007/s10579-019-09446-8`
- Interet : tres utile pour la structure argumentative, les relations et les debats, mais moins direct pour la classification de sophismes.
- Usage recommande : plutot pour la V2/V3 si vous ajoutez extraction de relations d'attaque/support.

### 5. SemEval 2020 Task 11 — Propaganda Techniques Corpus
- Source papier : ACL Anthology, `SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles`
- URL papier : `https://aclanthology.org/2020.semeval-1.186/`
- Interet : bon corpus voisin pour le detection de techniques rhetoriques fines.
- Usage recommande : extension si vous voulez comparer sophismes et propagande.

## Recommandation concrete

Pour une premiere version, je recommande :
- `Logic` comme dataset principal
- `Argotario` comme jeu complementaire
- `US2016` seulement si vous ajoutez l'etape de graphe argumentatif

## Schema normalise cible

Convertissez chaque corpus vers un CSV unique avec :
- `text`
- `label`
- `source`
- `split`
- `context`
- `topic`
- `masked_text`

## Mapping de labels conseille

Comme les corpus n'utilisent pas exactement les memes taxonomies, commencez par une taxonomie reduite :
- `ad_hominem`
- `fallacy_of_credibility`
- `false_dilemma`
- `straw_man`
- `not_fallacy`
- `other_fallacy`

Cela evite de casser la V1 avec une taxonomie trop fine et desequilibree.

## Notes specifiques a causalNLP/logical-fallacy

- Le sous-corpus `edu` contient un champ `masked_articles` utile pour une representation plus abstraite du texte.
- Le sous-corpus `climate` ne contient pas ce champ, mais il apporte des exemples en contexte reel.
- Le fichier `mappings.csv` fournit :
  - un nom plus lisible du sophisme
  - une description textuelle
  - une forme logique
  - une forme logique masquee

Pour le MVP, il faut exploiter `mappings.csv` uniquement pour l'explication et l'analyse. L'utiliser comme feature d'entree pour l'apprentissage fuiterait le label.
