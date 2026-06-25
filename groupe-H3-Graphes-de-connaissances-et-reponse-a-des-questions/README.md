#### H3 — Graphes de connaissances et reponse a des questions

La reponse a des questions sur graphes de connaissances (KGQA) consiste a traduire une question en langage naturel en une requete structuree (SPARQL, lambda-DCS ou chemin de raisonnement) executable sur un graphe RDF. Ce sujet aborde le pipeline complet : reconnaissance d'entites nommees (NER) pour identifier les noeuds du graphe, liaison entite-texte (entity linking) pour desambiguiser les mentions, et generation de requetes SPARQL ou de chemins de raisonnement. L'integration d'un LLM pour l'analyse syntaxique et semantique des questions permettra de comparer les approches basees sur des modeles de langage avec les approches symboliques traditionnelles (parsing SPARQL, templates). L'evaluation se fera sur un benchmark KGQA standard (LC-QuAD, WebQuestionsSP) en mesurant la precision de traduction et la correction des reponses.

### Notebook de demonstration

- [H3_KGQA_Demo.ipynb](H3_KGQA_Demo.ipynb) — mini-projet KGQA autonome avec graphe RDF, traduction de questions en SPARQL, exemples de requetes et mini-evaluation.

### Objectifs

- Implementer un pipeline complet de traduction question naturelle vers requete SPARQL ou chemin de raisonnement
- Maitriser les techniques d'entity linking et de desambiguation pour connecter les mentions textuelles aux entites du graphe
- Comparer les approches template-based, neural semantic parsing et LLM-based pour la generation de requetes
- Evaluer sur un benchmark KGQA standard (LC-QuAD, WebQuestionsSP) avec des metriques de precision et de rappel
- Analyser les erreurs recurrentes et les limites de chaque approche sur des questions complexes (multi-hop, aggregees)

### Notebooks CoursIA pertinents

| Notebook               | Chemin                                                                                                                                                                                | Pertinence      |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| SW-11 Knowledge Graphs | [SymbolicAI/SemanticWeb/SW-11-Python-KnowledgeGraphs.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-11-Python-KnowledgeGraphs.ipynb) | KG, requetage   |
| SW-12 GraphRAG         | [SymbolicAI/SemanticWeb/SW-12-Python-GraphRAG.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-12-Python-GraphRAG.ipynb)               | KG + LLM        |
| Argument Analysis      | [SymbolicAI/Argument_Analysis/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis)                                                          | NLP, extraction |
| SW-3 SPARQL Basics     | [SymbolicAI/SemanticWeb/SW-4b-Python-SPARQL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-4b-Python-SPARQL.ipynb)                   | SPARQL          |

### References externes

- Lan, Y., et al. (2023). "A Survey on Complex Question Answering over Knowledge Graphs." _ACM Computing Surveys_. [ACM](https://doi.org/10.1145/3556578)
- Unger, C., et al. (2012). "Template-Based Question Answering over RDF Data." _WWW_. [ACM](https://doi.org/10.1145/2187836.2187923)
- Dubey, M., et al. (2019). "LC-QuAD 2.0: A Large Dataset for Complex Question Answering over Wikidata and DBpedia." _ISWC_. [Springer](https://doi.org/10.1007/978-3-030-30793-6_5)
- Yih, W., et al. (2015). "Semantic Parsing via Staged Query Graph Generation." _EMNLP_. [ACL](https://aclanthology.org/D15-1198/)
