# EPITA 2026 — Intelligence Symbolique

## Liste des sujets de projet

Ce document presente les sujets de projet pour le cours d'Intelligence Symbolique (SCIA). Chaque sujet inclut une description detaillee, des references academiques et pratiques, des liens vers les notebooks CoursIA pertinents, et les technologies a utiliser.

> **Consignes de choix** : Chaque groupe doit forker ce depot et creer un dossier pour son projet contenant le code source, un notebook explicatif OU une UI/demo fonctionnelle (au choix), et les slides de soutenance. Les livraisons se font via des pull requests regulieres.
>
> **Inscription** : Inscrivez-vous et choisissez votre sujet dans la [feuille d'inscription des projets de groupe](https://docs.google.com/spreadsheets/d/1xmxEJcOyTegIhjW8LEqYewkCJ7m8_vK4/edit?usp=sharing). Chaque etudiant renseigne sa ligne (onglet `eleves`, colonne *Sujet Projet IA Symbolique*, menu deroulant) ; le catalogue complet des sujets est sur l'onglet `Sujets`.

### Du cours de Programmation par Contraintes a l'Intelligence Symbolique

Ce cours d'Intelligence Symbolique **ne prolonge pas** le cours de Programmation par Contraintes. Il ouvre un espace conceptuel different :

| Aspect | Programmation par Contraintes | Intelligence Symbolique |
|--------|-------------------------------|------------------------|
| **Questions** | Comment resoudre un probleme combinatoire ? | Comment representer et raisonner sur des connaissances ? |
| **Paradigme** | Espaces de recherche, propagation, optimisation | Logiques, argumentation, ontologies, preuves formelles |
| **Solveur** | CP-SAT, SAT, SMT comme boites noires | Z3/Lean comme assistants de raisonnement |
| **Sortie** | Une solution optimale ou faisable | Une preuve, un argument, une ontologie, un plan |
| **Evaluation** | Performance (temps, optimalite) | Correction (validite logique, coherence) |

Les solveurs SAT/SMT (Z3, PySAT) apparaissent dans les deux cours, mais avec des usages differents : en PC, ce sont des moteurs d'optimisation ; en IS, ce sont des verificateurs de proprietes logiques, des outils de preuve, ou des backend pour le raisonnement formel. Les sujets de ce depot exploitent SAT/SMT comme couches de verification au service de taches symboliques de plus haut niveau (demonstration automatique, model checking, verification de smart contracts, encodage de theoremes d'impossibilite).

---

## Modalites du projet

### Taille des groupes

| Taille | Bonus/Malus |
|--------|-------------|
| 3 personnes | Standard |
| 2 personnes | +1 point |
| 1 personne (solo) | +3 points |
| 4 personnes | -1 point |

### Soutenance — Evaluation par le professeur

La soutenance finale est evaluee par **le professeur** (pas d'evaluation collégiale par les pairs). Chaque groupe est note sur **4 criteres** (0-10 chacun) :

| Critere | Description |
|---------|-------------|
| **Qualite de la presentation** | Communication, clarte, pedagogie, qualite des slides, demonstrations |
| **Qualite theorique** | Principes utilises, classes d'algorithmes, contexte historique, explication des performances et limitations |
| **Qualite technique** | Livrables (code, notebook, UI), qualite du code, commits Git, demonstrations, resultats, perspectives |
| **Organisation** | Planning, repartition des taches, collaboration, activite Git, documentation |

**Note finale = somme des 4 criteres / 2 (echelle /20), ajustee du bonus/malus taille de groupe.**

### Livrables attendus

- **Code source** documente dans un sous-dossier dedie (`groupe-XX-nom-sujet/`)
- **Notebook Jupyter** explicatif avec analyse et visualisations **OU** **UI/demo fonctionnelle** (au choix — un notebook tres complet peut tenir lieu de demo, et inversement)
- **Slides de soutenance** (PDF ou lien)
- **Pull Request** soumise **avant la soutenance** (voir echeances ci-dessous)

### Echeances

- **Soutenances** : reparties en deux temps suite a une modification d'emploi du temps — une partie le **vendredi 26 juin 2026**, le reste en **juillet 2026** (dates exactes en cours de confirmation avec la scolarite).
- **Deadline PR** : les PRs doivent etre soumises dans les jours precedant votre creneau de soutenance ; receptionnez-les sur ce depot **avant votre passage**.

---

## Ressources communes a tous les sujets

### Solveurs et outils
- **Z3 SMT Solver** : solveur SMT de reference pour verification formelle et raisonnement symbolique. [Documentation](https://z3prover.github.io/api/html/namespacez3py.html), [Tutoriel Python](https://ericpony.github.io/z3py-tutorial/guide-examples.htm)
- **Google OR-Tools CP-SAT** : solveur CP pour problemes combinatoires. [Documentation](https://developers.google.com/optimization/cp/cp_solver)
- **CVC5 SMT Solver** : solveur SMT alternatif. [Documentation](https://cvc5.github.io/)
- **TweetyProject** : librairie Java pour logique formelle, argumentation et raisonnement probabiliste. [Documentation](https://tweetyproject.org/)

### Frameworks et plateformes
- **Semantic Kernel** : orchestration d'agents IA avec plugins. [GitHub](https://github.com/microsoft/semantic-kernel)
- **Fast Downward** : planificateur PDDL de reference. [Site](https://www.fast-downward.org/)
- **Solidity / Foundry** : developpement et test de smart contracts. [Documentation](https://docs.soliditylang.org/)
- **PySAT** : interface Python pour solveurs SAT. [Documentation](https://pysathq.github.io/)
- **QuantConnect Lean** : plateforme de backtest et trading algorithmique (partenariat educatif sponsorise par Jared Broad, CEO QC). [Site](https://www.quantconnect.com/), [Documentation](https://www.quantconnect.com/docs/)

### Notebooks du cours CoursIA
Les notebooks suivants sont disponibles dans le depot CoursIA ([jsboige/CoursIA](https://github.com/jsboige/CoursIA)) et constituent des prerequis ou des points de depart pour les projets :

#### Demonstration automatique et typage dependant (Lean 4)
- **SymbolicAI/Lean/** : 12 notebooks — Lean-1 (Setup), Lean-2 (Dependent Types), Lean-3 (Propositions & Proofs), Lean-4 (Quantifiers), Lean-5 (Tactics), Lean-6 (Mathlib), Lean-7 (LLM Integration), Lean-8 (Agentic Proving), Lean-9 (Semantic Kernel Multi-Agents), Lean-10 (LeanDojo), Lean-11 (Neural Theorem Proving)

#### Logique formelle, SAT/SMT et solveurs
- **SymbolicAI/Linq2Z3.ipynb** : Z3 SMT Solver en C#
- **SymbolicAI/OR-tools-Stiegler.ipynb** : OR-Tools CP en C#
- **Sudoku/** : 18 notebooks couvrant Sudoku avec multiples solveurs (backtracking, DLX, GA, SA, PSO, Norvig, OR-Tools, Choco, Z3, BDD, neural, LLM)

#### TweetyProject — Logique et Argumentation
- **SymbolicAI/Tweety/** : 11 notebooks — Tweety-1 (Setup), Tweety-2 (Basic Logics), Tweety-3 (Advanced Logics), Tweety-4 (Belief Revision/AGM), Tweety-5 (Abstract Argumentation/Dung), Tweety-6 (Structured Argumentation/ASPIC+), Tweety-7a (Extended Frameworks), Tweety-7b (Ranking & Probabilistic), Tweety-8 (Agent Dialogues), Tweety-9 (Preferences)

#### Web Semantique et Graphes de Connaissances
- **SymbolicAI/SemanticWeb/** : 13 notebooks — SW-1 (Setup C#/Python), SW-2 (RDF), SW-3 (Graph Operations), SW-4 (SPARQL), SW-5 (Linked Data), SW-6 (RDFS), SW-7 (OWL), SW-8 (SHACL), SW-9 (JSON-LD), SW-10 (RDF*), SW-11 (Knowledge Graphs), SW-12 (GraphRAG), SW-13 (Reasoners)

#### Smart Contracts et Blockchain
- **SymbolicAI/SmartContracts/** : 27 notebooks (SC-0 a SC-26) — cypherpunk, Solidity, Foundry, ERC-20/721, DeFi, DAO Governance, Account Abstraction, LLM-assisted contracts, fuzz testing (SC-13), formal verification (SC-14), ZKP (SC-15), homomorphic encryption (SC-16), voting, Vyper, Bitcoin Script, Move/Sui, Solana/Anchor, cross-chain, deployment

#### Analyse d'Argumentation (Agentic)
- **SymbolicAI/Argument_Analysis/** : 7 notebooks — Agentic-0 (Init), Agentic-1 (Informal Argument Agent), Agentic-2 (Planning-Based Agent), Agentic-3 (Orchestration multi-agent)

#### Planification
- **SymbolicAI/Planners/** : 12 notebooks — Planners-1 (Intro), Planners-2 (PDDL), Planners-3 (State Space), Planners-4 (Fast Downward), Planners-5 (Heuristics), Planners-6 (Domains), Planners-7 (OR-Tools), Planners-8 (Temporal), Planners-9 (HTN), Planners-10 (LLM Planning), Planners-11 (Unified Planning), Planners-12 (LOOP)

#### Theorie des Jeux et Choix Social
- **GameTheory/** : 27 notebooks — forme normale, equilibres de Nash, zero-sum/minimax, evolution & trust, forme extensive, jeux combinatoires, induction, jeux bayesiens, reputation, information imparfaite/CFR, jeux cooperatifs/Shapley, mechanism design, choix social (Arrow SAT/Z3), multi-agent RL

#### Recherche et Metaheuristiques
- **Search/Part1-Foundations/** : 11 notebooks — StateSpace, uninformed, A*/heuristiques, local search, GA, adversarial/minimax, MCTS, Dancing Links, PL, automates symboliques, metaheuristiques

#### Programmation par Contraintes
- **Search/Part2-CSP/** : 9 notebooks — CSP-1 (Fondamentaux), CSP-2 (Consistency), CSP-3 (Advanced), CSP-4 (Scheduling), CSP-5 (Optimization), CSP-6 (Hybridation CP+SAT, LLM+CSP), CSP-7 (Soft Constraints), CSP-8 (Temporal CSP), CSP-9 (Distributed CSP)
- **Search/Applications/CSP/** : 11 notebooks — N-Queens, Graph Coloring, Nurse Scheduling, Job-Shop, Timetabling, Minesweeper, Wordle, MiniZinc, Picross, Sports Scheduling, Crossword
- **Search/Applications/Hybrid/** : 7 notebooks — Edge Detection, Portfolio Optimization, Connect Four, TSP Metaheuristics, VRP Logistics

#### Raisonnement Probabiliste et Decision

- **Research/** : 20 notebooks — Infer.NET (programmation probabiliste), melanges gaussiens, graphes de facteurs, reseaux bayesiens, modeles de Markov caches, LDA, crowdsourcing, recommandation, reseaux de decision, MDP/bandits/POMDP, TrueSkill, IRT

#### Reinforcement Learning

- **RL/** : 6 notebooks — MDP, Q-learning, DQN, policy gradient, multi-agent RL (NFSP, PSRO), Stable Baselines3, Gym wrappers, HER

#### Trading Algorithmique (QuantConnect)

- **QuantConnect/Python/** : 40+ notebooks — QC-Py-01 a QC-Py-34 couvrant la plateforme, backtesting, indicateurs techniques, modeles alpha, ML (classification, regression, LSTM, Transformer, RL DQN/PPO/SAC), detection de regimes, LLM trading signals, et paper trading Binance/IBKR

---

## Index des Sujets

### Categorie A : Demonstration Automatique et Typage Dependant (Lean 4)

| # | Sujet | Difficulte |
|---|-------|------------|
| [A1](#a1--preuve-formelle-dalgorithme-par-lean-4) | Preuve formelle d'algorithme par Lean 4 | 3/5 |
| [A2](#a2--agent-llm-assiste-pour-la-preuve-formelle) | Agent LLM-assiste pour la preuve formelle | 4/5 |
| [A3](#a3--theoreme-darrow-par-preuve-automatisee-satz3lean) | Theoreme d'Arrow par preuve automatisee (SAT/Z3/Lean) | 5/5 |
| [A4](#a4--bibliotheque-de-preuves-mathlib--extensions) | Bibliotheque de preuves Mathlib — extensions | 3/5 |
| [A5](#a5--mariages-stables-gale-shapley--preuve-formelle-et-extensions-en-lean-4) | Mariages stables Gale-Shapley : preuve formelle et extensions en Lean 4 | 3/5 |
| [A6](#a6--preuve-de-lexistence-de-nash-par-point-fixe-en-lean-4) | Preuve de l'existence de Nash par point fixe en Lean 4 | 5/5 |

### Categorie B : Logique Formelle, SAT et Demonstration Automatique

| # | Sujet | Difficulte |
|---|-------|------------|
| [B1](#b1--resolution-automatique-de-theoremes-par-sat) | Resolution automatique de theoremes par SAT | 3/5 |
| [B2](#b2--synthese-de-programmes-par-programming-by-sketching) | Synthese de programmes par Programming-by-Sketching | 4/5 |
| [B3](#b3--model-checking-de-protocoles-de-communication) | Model checking de protocoles de communication | 3/5 |
| [B4](#b4--resolution-de-puzzles-logiques-par-smt) | Resolution de puzzles logiques par SMT | 2/5 |
| [B5](#b5--demonstration-automatique-en-geometrie) | Demonstration automatique en geometrie | 4/5 |
| [B6](#b6--programmation-par-ensembles-de-reponses-asp-avec-clingo) | Programmation par ensembles de reponses (ASP) avec Clingo | 3/5 |
| [B7](#b7--resolution-de-problemes-pspace-par-qbf-quantified-booleans) | Resolution de problemes PSPACE par QBF (Quantified Booleans) | 3/5 |
| [B8](#b8--solveur-satsmt-certifiant--certificats-unsat-verifies-dratlrat-et-checker-prouve-en-lean-4) | Solveur SAT/SMT certifiant : certificats UNSAT verifies (DRAT/LRAT) et checker prouve en Lean 4 | 5/5 |

### Categorie C : Verification Formelle et Surete des Logiciels

| # | Sujet | Difficulte |
|---|-------|------------|
| [C1](#c1--verification-formelle-de-smart-contracts-solidity-par-smt) | Verification formelle de smart contracts Solidity par SMT | 3/5 |
| [C2](#c2--fuzzing-guide-par-contraintes-constraint-based-fuzzing) | Fuzzing guide par contraintes (constraint-based fuzzing) | 4/5 |
| [C3](#c3--analyse-statique-et-detection-de-vulnerabilites-par-abstraction) | Analyse statique et detection de vulnerabilites par abstraction | 3/5 |
| [C4](#c4--preuves-de-correcteur-zero-knowledge-zk-snarks) | Preuves de correcteur Zero-Knowledge (zk-SNARKs) | 4/5 |
| [C5](#c5--synthese-de-programmes-corrects-par-construction-par-cegis-et-verification-deductive) | Synthese de programmes corrects-par-construction par CEGIS et verification deductive | 5/5 |

### Categorie D : Planification et Ordonnancement

| # | Sujet | Difficulte |
|---|-------|------------|
| [D1](#d1--planification-robotique-avec-pddl-et-integration-capteurs) | Planification robotique avec PDDL et integration capteurs | 3/5 |
| [D2](#d2--planification-htn-pour-jeux-video) | Planification HTN pour jeux video | 3/5 |
| [D3](#d3--ordonnancement-multi-agent-par-csp-distribue) | Ordonnancement multi-agent par CSP distribue | 4/5 |
| [D4](#d4--planification-temporelle-pour-systemes-cyber-physiques) | Planification temporelle pour systemes cyber-physiques | 4/5 |
| [D5](#d5--planification-neuro-symbolique-certifiee--llm-heuristiques-unified-planning-et-validation-formelle-de-plans) | Planification neuro-symbolique certifiee : LLM-heuristiques, Unified Planning et validation formelle de plans | 5/5 |

### Categorie E : Theorie des Jeux et Mechanism Design

| # | Sujet | Difficulte |
|---|-------|------------|
| [E1](#e1--comptabilite-maximin-et-equilibres-de-nash-par-programmation-lineaire) | Comptabilite maximin et equilibres de Nash par programmation lineaire | 3/5 |
| [E2](#e2--encheres-combinatoires-et-allocation-de-biens-publics) | Encheres combinatoires et allocation de biens publics | 4/5 |
| [E3](#e3--jeux-cooperatifs-et-valeur-de-shapley) | Jeux cooperatifs et valeur de Shapley | 3/5 |
| [E4](#e4--conception-de-mecanismes-resistants-a-la-manipulation) | Conception de mecanismes resistants a la manipulation | 4/5 |
| [E5](#e5--counterfactual-regret-minimization-cfr-et-poker-ia) | Counterfactual Regret Minimization (CFR) et poker IA | 3/5 |
| [E6](#e6--conception-automatisee-de-mecanismes--optimisation-sous-incentive-compatibility-et-verification-formelle-smtlean) | Conception automatisee de mecanismes : optimisation sous incentive-compatibility et verification formelle (SMT/Lean) | 5/5 |

### Categorie F : Smart Contracts et Blockchain Symbolique

| # | Sujet | Difficulte |
|---|-------|------------|
| [F1](#f1--super-optimisation-de-gas-solidity-par-max-smt) | Super-optimisation de gas Solidity par Max-SMT | 4/5 |
| [F2](#f2--ordonnancement-mev-resistant-de-transactions-on-chain) | Ordonnancement MEV-resistant de transactions on-chain | 3/5 |
| [F3](#f3--circuits-zero-knowledge-sous-contraintes-arithmetiques) | Circuits Zero-Knowledge sous contraintes arithmetiques | 4/5 |
| [F4](#f4--governance-decentralisee-et-vote-quadratique) | Governance decentralisee et vote quadratique | 3/5 |
| [F5](#f5--coffre-defi-verifie-de-bout-en-bout--synthese-dinvariants-preuve-certoracvl-et-execution-symbolique) | Coffre DeFi verifie de bout en bout : synthese d'invariants, preuve Certora/CVL et execution symbolique | 5/5 |

### Categorie G : Web Semantique et Graphes de Connaissances

| # | Sujet | Difficulte |
|---|-------|------------|
| [G1](#g1--construction-et-interrogation-dun-graphe-de-connaissances-par-sparql) | Construction et interrogation d'un graphe de connaissances par SPARQL | 3/5 |
| [G2](#g2--raisonnement-owl-et-verification-de-coherence-dontologie) | Raisonnement OWL et verification de coherence d'ontologie | 3/5 |
| [G3](#g3--graphrag--combine-knowledge-graphs-et-llm-pour-le-rag) | GraphRAG — combine Knowledge Graphs et LLM pour le RAG | 4/5 |
| [G4](#g4--validation-de-donnees-par-shacl-shapes-constraint-language) | Validation de donnees par SHACL (Shapes Constraint Language) | 3/5 |
| [G5](#g5--architecture-agentique-semantique-pour-le-traitement-de-documents-rdf) | Architecture agentique semantique pour le traitement de documents RDF | 3/5 |
| [G6](#g6--graphrag-verifie--reponses-tracees-ancrees-dans-le-graphe-et-garanties-par-raisonnement-owlshacl) | GraphRAG verifie : reponses tracees, ancrees dans le graphe et garanties par raisonnement OWL/SHACL | 5/5 |

### Categorie H : Representation des Connaissances et Raisonnement

| # | Sujet | Difficulte |
|---|-------|------------|
| [H1](#h1--systeme-de-maintenance-de-verite-jtms) | Systeme de maintenance de verite (JTMS) | 3/5 |
| [H2](#h2--ontologies-et-raisonnement-semantique-owl-reasoning) | Ontologies et raisonnement semantique (OWL Reasoning) | 3/5 |
| [H3](#h3--graphes-de-connaissances-et-reponse-a-des-questions) | Graphes de connaissances et reponse a des questions | 3/5 |
| [H4](#h4--logique-de-description-et-raisonnement-sur-des-domaines-medicaux) | Logique de description et raisonnement sur des domaines medicaux | 4/5 |
| [H5](#h5--apprentissage-dontologies-par-programmation-logique-inductive--induction-daxiomes-sroiq-verifies-par-raisonneur-dl) | Apprentissage d'ontologies par programmation logique inductive : induction d'axiomes SROIQ verifies par raisonneur DL | 5/5 |

### Categorie I : Argumentation et Raisonnement Debateur

| # | Sujet | Difficulte |
|---|-------|------------|
| [I1](#i1--analyse-et-detection-de-sophismes-par-apprentissage-symbolique) | Analyse et detection de sophismes par apprentissage symbolique | 3/5 |
| [I2](#i2--generation-de-contre-arguments-par-raisonnement-formel) | Generation de contre-arguments par raisonnement formel | 3/5 |
| [I3](#i3--argumentation-dialogique-multi-agents) | Argumentation dialogique multi-agents | 4/5 |
| [I4](#i4--evaluation-automatique-de-la-qualite-argumentative) | Evaluation automatique de la qualite argumentative | 3/5 |
| [I5](#i5--benchmarks-iccma--solveurs-dargumentation-de-dung) | Benchmarks ICCMA — solveurs d'argumentation de Dung | 2/5 |
| [I6](#i6--argumentation-structuree-aspic-et-logique-defaisable-delpaba) | Argumentation structuree ASPIC+ et logique defaisable (DeLP/ABA) | 3/5 |
| [I7](#i7--du-texte-au-verdict-argumentatif-certifie--extraction-llm--solveur-de-dung-avec-certificat-dextension-verifiable) | Du texte au verdict argumentatif certifie : extraction LLM + solveur de Dung avec certificat d'extension verifiable | 5/5 |

### Categorie J : Agents Symboliques et Architecture Cognitive

| # | Sujet | Difficulte |
|---|-------|------------|
| [J1](#j1--systeme-multi-agents-de-resolution-de-problemes-par-planification) | Systeme multi-agents de resolution de problemes par planification | 3/5 |
| [J2](#j2--agent-cognitif-hybride-symbolique--subsymbolique) | Agent cognitif hybride (symbolique + subsymbolique) | 4/5 |
| [J3](#j3--serveur-mcp-doutils-danalyse-symbolique) | Serveur MCP d'outils d'analyse symbolique | 3/5 |
| [J4](#j4--integration-llm--solveurs-symboliques-llm-as-a-reasoner) | Integration LLM + solveurs symboliques (LLM-as-a-reasoner) | 4/5 |
| [J5](#j5--apprentissage-par-renforcement-multi-agents-marl-et-emergence-de-cooperation) | Apprentissage par renforcement multi-agents (MARL) et emergence de cooperation | 4/5 |
| [J6](#j6--diagnostic-medical-multi-paradigme-par-agents-symboliques) | Diagnostic medical multi-paradigme par agents symboliques | 4/5 |
| [J7](#j7--architecture-cognitive-a-noyau-symbolique-verifie--agent-llm-pilote-par-planificateur-pddl-et-garde-fou-shield-formel) | Architecture cognitive a noyau symbolique verifie : agent LLM pilote par planificateur PDDL et garde-fou (shield) formel | 5/5 |

### Categorie K : Cryptographie Symbolique et Securite

| # | Sujet | Difficulte |
|---|-------|------------|
| [K1](#k1--cryptanalyse-par-contraintes-de-chiffrements-classiques) | Cryptanalyse par contraintes de chiffrements classiques | 3/5 |
| [K2](#k2--verification-de-protocoles-cryptographiques-par-model-checking) | Verification de protocoles cryptographiques par model checking | 4/5 |
| [K3](#k3--chiffrement-homomorphe-et-calcul-sur-donnees-chiffrees) | Chiffrement homomorphe et calcul sur donnees chiffrees | 4/5 |
| [K4](#k4--vote-electronique-verifiable-de-bout-en-bout--chiffrement-homomorphe-preuves-zero-knowledge-et-verification-symbolique-du-protocole) | Vote electronique verifiable de bout en bout : chiffrement homomorphe, preuves zero-knowledge et verification symbolique du protocole | 5/5 |

### Categorie L : Puzzles, Jeux et Problemes Combinatoires

| # | Sujet | Difficulte |
|---|-------|------------|
| [L1](#l1--resolution-de-sudoku-par-multiples-solveurs-sat-cp-lll) | Resolution de Sudoku par multiples solveurs (SAT, CP, LLL) | 2/5 |
| [L2](#l2--generation-procedurale-par-contraintes-de-niveaux-de-jeu) | Generation procedurale par contraintes de niveaux de jeu | 3/5 |
| [L3](#l3--resolution-de-jeux-combinatoires-par-minimax-et-alpha-beta-symbolique) | Resolution de jeux combinatoires par minimax et alpha-beta symbolique | 3/5 |
| [L4](#l4--benchmark-cross-paradigme-de-solveurs-de-jeux-sudoku-connect-four-wordle) | Benchmark cross-paradigme de solveurs de jeux (Sudoku, Connect Four, Wordle) | 3/5 |
| [L5](#l5--generateur-de-puzzles-a-unicite-certifiee--synthese-sous-contraintes-preuve-dunicite-de-solution-et-calibration-de-difficulte) | Generateur de puzzles a unicite certifiee : synthese sous contraintes, preuve d'unicite de solution et calibration de difficulte | 5/5 |

---

### Categorie M : IA Neuro-Symbolique

> L'IA neuro-symbolique combine le raisonnement formel (logique, contraintes) avec l'apprentissage profond (LLM, reseaux de neurones). Domaine en pleine expansion avec des applications en raisonnement verifiable, generation guidee par contraintes, et interpretabilite.

| # | Sujet | Difficulte |
|---|-------|------------|
| [M1](#m1--pipeline-llm--verificateur-symbolique-pour-la-generation-fiable) | Pipeline LLM + verificateur symbolique pour la generation fiable | 3/5 |
| [M2](#m2--reseau-de-neurones-logique-logical-neural-networks) | Reseau de neurones logique (Logical Neural Networks) | 4/5 |
| [M3](#m3--regression-symbolique--decouvrir-des-equations-a-partir-de-donnees) | Regression symbolique -- decouvrir des equations a partir de donnees | 3/5 |
| [M4](#m4--decouverte-scientifique-automatisee-par-regression-symbolique-et-llm) | Decouverte scientifique automatisee par regression symbolique et LLM | 4/5 |
| [M5](#m5--evaluation-comparee-llm-vs-approches-symboliques-sur-un-benchmark) | Evaluation comparee LLM vs. approches symboliques sur un benchmark | 2/5 |
| [M6](#m6--theorie-de-linformation-integree-iit-et-conscience-artificielle-par-pyphi) | Theorie de l'Information Integree (IIT) et conscience artificielle par PyPhi | 3/5 |
| [M7](#m7--generation-de-contenu-neuro-symbolique-par-semantic-kernel--validation-csp) | Generation de contenu neuro-symbolique par Semantic Kernel + validation CSP | 4/5 |
| [M8](#m8--demonstration-automatique-neuro-symbolique--agent-llm-pour-lean-4) | Demonstration automatique neuro-symbolique : agent LLM pour Lean 4 | 5/5 |
| [M9](#m9--compresseur-sans-perte-neuro-symbolique--llm-decouvreur-decodeur-certifie-et-registre-de-recettes-signees) | Compresseur sans perte neuro-symbolique : LLM-decouvreur, decodeur certifie et registre de recettes signees | 5/5 |

### Categorie N : Raisonnement Causal et Decision

> Le raisonnement causal (Pearl, 2009) depasse la correlation pour raisonner sur les interventions et les contrefactuels. Fondamental pour la prise de decision dans les systemes IA, la medecine, et l'analyse de politiques.

| # | Sujet | Difficulte |
|---|-------|------------|
| [N1](#n1--decouverte-causale-a-partir-de-donnees-observationnelles) | Decouverte causale a partir de donnees observationnelles | 3/5 |
| [N2](#n2--raisonnement-causal-par-le-do-calculus-avec-dowhy) | Raisonnement causal par le do-calculus avec DoWhy | 3/5 |
| [N3](#n3--diagnostic-abductif--raisonnement-par-abduction) | Diagnostic abductif — raisonnement par abduction | 3/5 |
| [N4](#n4--evaluation-du-raisonnement-causal-des-llm) | Evaluation du raisonnement causal des LLM | 4/5 |
| [N5](#n5--planification-oncologique-symbolique-ontologies-z3-et-modeles-probabilistes) | Planification oncologique symbolique (ontologies, Z3 et modeles probabilistes) | 5/5 |

### Categorie O : Raisonnement Qualitatif et Bon Sens

> Le raisonnement qualitatif manipule des representations symboliques de l'espace, du temps, et du bon sens sans recourir a des modeles numeriques. Inclut les calculs relationnels spatiaux (RCC8), temporels (Allen), et le raisonnement de sens commun.

| # | Sujet | Difficulte |
|---|-------|------------|
| [O1](#o1--raisonnement-spatial-qualitatif-par-les-calculs-rcc8) | Raisonnement spatial qualitatif par les calculs RCC8 | 3/5 |
| [O2](#o2--raisonnement-temporel-qualitatif--algebres-dallen-et-stp) | Raisonnement temporel qualitatif — Algebres d'Allen et STP | 3/5 |
| [O3](#o3--raisonnement-de-bon-sens-par-graphe-de-connaissances-commonsense) | Raisonnement de bon sens par graphe de connaissances (Commonsense) | 3/5 |
| [O4](#o4--raisonnement-par-analogie--theorie-du-mapping-structurel) | Raisonnement par analogie — theorie du mapping structurel | 3/5 |
| [O5](#o5--raisonneur-spatio-temporel-qualitatif-integre--composition-rcc8-x-allen-coherence-par-csp-et-extraction-depuis-le-langage-naturel) | Raisonneur spatio-temporel qualitatif integre : composition RCC8 x Allen, coherence par CSP et extraction depuis le langage naturel | 5/5 |

### Categorie P : Verification Formelle des Systemes IA

> La verification formelle des systemes d'IA est un domaine emergent critique pour la surete. Il s'agit de prouver formellement qu'un systeme d'IA (reseau de neurones, agent LLM, politique RL) satisfait des proprietes de surete, equite, ou robustesse.

| # | Sujet | Difficulte |
|---|-------|------------|
| [P1](#p1--verification-de-robustesse-de-reseaux-de-neurones-par-abstraction) | Verification de robustesse de reseaux de neurones par abstraction | 4/5 |
| [P2](#p2--verification-de-politiques-rl-par-contraintes-formelles) | Verification de politiques RL par contraintes formelles | 4/5 |
| [P3](#p3--specification-et-verification-de-securite-dagents-llm-par-logique-temporelle) | Specification et verification de securite d'agents LLM par logique temporelle | 4/5 |
| [P4](#p4--robustesse-formelle-des-reseaux-de-neurones-binaires-par-le-sensitivity-theorem) | Robustesse formelle des reseaux de neurones binaires par le Sensitivity Theorem | 5/5 |

### Categorie Q : Raisonnement Ethique et Normatif

> Le raisonnement ethique et normatif utilise la logique deontique (obligations, permissions, interdictions) et les cadres d'argumentation pour raisonner formellement sur les normes, les valeurs, et l'alignement des systemes d'IA.

| # | Sujet | Difficulte |
|---|-------|------------|
| [Q1](#q1--raisonneur-deontique--logique-des-normes-et-obligations) | Raisonneur deontique — logique des normes et obligations | 3/5 |
| [Q2](#q2--verification-dalignement-de-valeurs-par-methodes-formelles) | Verification d'alignement de valeurs par methodes formelles | 4/5 |
| [Q3](#q3--raisonnement-juridique-formel-par-argumentation-et-logique) | Raisonnement juridique formel par argumentation et logique | 3/5 |
| [Q4](#q4--agent-conforme-par-construction--raisonneur-deontique-garde-fou-normatif-shield-et-tracabilite-reglementaire-ai-act--rgpd) | Agent conforme par construction : raisonneur deontique, garde-fou normatif (shield) et tracabilite reglementaire (AI Act / RGPD) | 5/5 |

### Categorie R : Raisonnement sous Incertitude et Revision des Croyances

> La revision des croyances et le raisonnement sous incertitude sont au coeur des systemes symboliques devant mettre a jour leurs connaissances face a de nouvelles informations contradictoires. Inclut les postulats AGM, les croyances probabilistes, et la programmation probabiliste.

| # | Sujet | Difficulte |
|---|-------|------------|
| [R1](#r1--revision-des-croyances-par-les-postulats-agm) | Revision des croyances par les postulats AGM | 3/5 |
| [R2](#r2--programmation-probabiliste-avec-infernet) | Programmation probabiliste avec Infer.NET | 3/5 |
| [R3](#r3--raisonnement-epistemique-et-logique-multi-agents) | Raisonnement epistemique et logique multi-agents | 4/5 |
| [R4](#r4--agent-de-decision-sequentielle-a-croyances-revisees--fusion-agm-symbolique-et-inference-bayesienne-sous-information-contradictoire) | Agent de decision sequentielle a croyances revisees : fusion AGM symbolique et inference bayesienne sous information contradictoire | 5/5 |

### Categorie S : Trading Algorithmique Symbolique

> Les sujets de la categorie S combinent un **noyau IA Symbolique** (logique epistemique, web semantique, verification formelle SMT, programmation probabiliste) avec une validation pratique via la plateforme [QuantConnect Lean](https://www.quantconnect.com/). Chaque projet est fondamentalement symbolique et utilise le backtest QuantConnect uniquement comme couche de validation sur donnees reelles de marche. Les etudiants ayant rejoint l'organisation QuantConnect sponsorisee par Jared Broad (CEO QC) sont encourages a choisir en priorite ces sujets.
>
> **Attention** : Si votre objectif est d'optimiser un portefeuille par programmation par contraintes (CP-SAT, MiniZinc, CPMpy, MIP), consultez la [Categorie M du cours Programmation par Contraintes](https://github.com/jsboigeEpita/2026-Epita-Programmation-par-Contraintes#categorie-m--finance-quantitative-et-trading-algorithmique). La categorie S vise le **raisonnement symbolique formel** sur acteurs, contrats et regimes de marche — pas l'optimisation numerique.

| # | Sujet | Difficulte |
|---|-------|------------|
| [S1](#s1--raisonnement-epistemique-pour-le-trading-multi-agents) | Raisonnement epistemique pour le trading multi-agents | 4/5 |
| [S2](#s2--ontologies-financieres-et-web-semantique-pour-le-screening-dactifs) | Ontologies financieres et Web Semantique pour le screening d'actifs | 3/5 |
| [S3](#s3--verification-formelle-de-protocoles-defi-par-smt) | Verification formelle de protocoles DeFi par SMT | 4/5 |
| [S4](#s4--programmation-probabiliste-symbolique-pour-la-detection-de-regimes-de-marche) | Programmation probabiliste symbolique pour la detection de regimes de marche | 3/5 |
| [S5](#s5--enumeration-asp-des-strategies-doptions-multi-jambes-et-backtest-quantconnect) | Enumeration ASP des strategies d'options multi-jambes et backtest QuantConnect | 4/5 |
| [S6](#s6--safe-rl-shielding-smt-des-politiques-de-trading-rl-et-deployment-quantconnect-live) | Safe RL : shielding SMT des politiques de trading RL et deployment QuantConnect Live | 5/5 |
| [S7](#s7--fusion-de-signaux-multi-strategie-par-argumentation-dung-sur-le-research-executor-quantconnect) | Fusion de signaux multi-strategie par argumentation Dung sur le Research-Executor QuantConnect | 5/5 |
| [S8](#s8--model-checking-ctl-dun-trading-bot-avant-deployment-live-quantconnect) | Model checking CTL d'un trading bot avant deployment live QuantConnect | 4/5 |

### Categorie T : Sciences Sociales Computationnelles et Choix Collectif

> Les sujets de la categorie T appliquent les outils de l'IA symbolique (verification formelle SAT/SMT, preuve Lean, argumentation structuree, revision des croyances AGM, logique epistemique) a des problemes de sciences sociales et de choix collectif. Chaque sujet repose sur un **noyau symbolique implementable** (solveur, raisonneur, module de preuve) et utilise la theorie des jeux, les modeles probabilistes ou les donnees reelles comme contexte d'application. Les sources de donnees sont publiques et verifiables (data.gouv.fr, assemblee-nationale.fr, election resources).

| # | Sujet | Difficulte |
|---|-------|------------|
| [T1](#t1--pouvoir-de-coalition-par-verification-formelle-shapley-banzhaf-et-donnees-electorales-reelles) | Pouvoir de coalition par verification formelle (Shapley, Banzhaf et donnees electorales reelles) | 3/5 |
| [T2](#t2--choix-social-et-procedures-de-vote-analyse-formelle-par-satsmt) | Choix social et procedures de vote : analyse formelle par SAT/SMT | 4/5 |
| [T3](#t3--information-asymetrique-et-capture-modelisation-par-argumentation-et-logique-epistemique) | Information asymetrique et capture : modelisation par argumentation et logique epistemique | 4/5 |
| [T4](#t4--decision-publique-sous-incertitude-revision-des-croyances-et-argumentation) | Decision publique sous incertitude : revision des croyances et argumentation | 3/5 |
| [T5](#t5--decouverte-automatique-de-theoremes-dimpossibilite-en-choix-social--recherche-sat-de-contre-exemples-et-certification-lean) | Decouverte automatique de theoremes d'impossibilite en choix social : recherche SAT de contre-exemples et certification Lean | 5/5 |

---

> **Note** : Les descriptions detaillees de chaque sujet, les references academiques et les notebooks CoursIA associes seront enrichis progressivement. Cette premiere version est un draft soumis pour revue et enrichissement par l'equipe pedagogique.

---

## Descriptions detaillees des sujets

### Categorie A : Demonstration Automatique et Typage Dependant (Lean 4)

#### A1 — Preuve formelle d'algorithme par Lean 4

La preuve formelle d'algorithmes en Lean 4 consiste a specifier la correction fonctionnelle d'un algorithme classique (tri insertion, recherche dichotomique, plus court chemin de Dijkstra) en utilisant le systeme de types dependants de Lean et la bibliotheque Mathlib4. L'etudiant definit les types inductifs (listes, arbres, graphes), exprime les proprietes sous forme de theoremes (tri : la sortie est triee et est une permutation de l'entree ; recherche : le resultat est un element de la collection s'il existe), et mene la preuve en mode tactique. Ce sujet permet de maitriser le moteur de preuves, les tactiques (intro, apply, exact, simp, omega, linarith), et la specification formelle de programmes. L'approche est fondamentalement differente de la verification par tests : elle garantit la correction pour toutes les entrees possibles.

### Objectifs
- Installer l'environnement Lean 4 (elan, lake, VS Code extension) et se familiariser avec le mode tactique sur des preuves simples d'egalite et de logique propositionnelle
- Prouver la correction d'un algorithme de tri (insertion sort ou merge sort) : definir `Sorted` et `Perm` comme predicates inductifs, puis prouver `sorted (sort l)` et `Perm l (sort l)`
- Etendre a un algorithme de recherche (dichotomique sur tableau trie) ou de plus court chemin (Dijkstra sur graphe pondere), en specifiant la precondition et la postcondition
- Comparer la difficulte de preuve entre un algorithme impératif (tableaux, boucles while) et un algorithme fonctionnel (recursif, pattern matching)
- Documenter les tactiques les plus utiles et les patterns de preuve recurents dans un notebook explicatif

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Lean-1 Setup | [SymbolicAI/Lean/Lean-1-Setup.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-1-Setup.ipynb) | Installation, premieres preuves |
| Lean-2 Dependent Types | [SymbolicAI/Lean/Lean-2-Dependent-Types.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-2-Dependent-Types.ipynb) | Types dependants, specifications |
| Lean-3 Propositions | [SymbolicAI/Lean/Lean-3-Propositions-Proofs.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-3-Propositions-Proofs.ipynb) | Theoremes, tactiques de base |
| Lean-5 Tactics | [SymbolicAI/Lean/Lean-5-Tactics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-5-Tactics.ipynb) | Tactiques avancees (simp, omega) |
| Conway Lean (Surreals) | [GameTheory/conway_lean/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/GameTheory/conway_lean/) | Nombres surreels en Lean 4 |

### References externes
- Avigad, J. et al. (2024). *Theorem Proving in Lean 4*. [lean-lang.org](https://lean-lang.org/theorem_proving_in_lean4/)
- Mathlib Community. *The Mathematical Library of Lean 4*. [GitHub](https://github.com/leanprover-community/mathlib4)
- Ullrich, S. & de Moura, L. (2023). "Beyond Notations: Hygienic Macro Expansion for Theorem Proving Languages." *JAR*. [Springer](https://link.springer.com/article/10.1007/s10817-022-09634-1)
- Lean 4 Reference Manual. [lean-lang.org/lean4/doc/](https://lean-lang.org/lean4/doc/)
- Lammich, P. (2023). "Verified Efficient Implementation of Graph Algorithms." *ITP*. [Springer](https://link.springer.com/chapter/10.1007/978-3-031-40355-9_12)

### Difficulte : 3/5

---

#### A2 — Agent LLM-assiste pour la preuve formelle

L'integration des LLM dans les assistants de preuve est l'une des avances les plus prometteuses de l'IA symbolique recente. Ce sujet consiste a construire un agent qui analyse l'etat courant d'une preuve Lean 4 (buts, hypotheses, contexte), utilise un LLM (via Semantic Kernel ou API directe) pour suggerer des candidats tactiques, et les valide en les soumettant au moteur de preuve. L'agent s'appuie sur LeanCopilot (inference de tactiques par modele de langage) et LeanDojo (extraction de donnees d'entrainement et interaction programmatique avec Lean). Le defi est de gerer l'arbre de recherche (backtracking quand une tactique echoue), le contexte mathematique (formater l'etat de preuve pour le LLM), et la selection des meilleurs candidats. L'evaluation se fait sur un benchmark de theoremes Mathlib.

### Objectifs
- Installer et configurer LeanCopilot comme plugin Lean 4, comprendre l'API de suggestion de tactiques et le format d'entree/sortie
- Implementer un agent de recherche qui interroge le LLM pour chaque but, collecte les suggestions tactiques, les essaie, et effectue un backtracking en cas d'echec (strategie BFS ou DFS avec timeout)
- Intégrer LeanDojo pour l'extraction du contexte de preuve (hypotheses, buts, declarations importees) et le formatage en prompt pour le LLM
- Evaluer l'agent sur un sous-ensemble de theoremes Mathlib4 (ex: top 100 theoremes du tutorial) et mesurer le taux de succes, le nombre de tactiques essayees, et le temps moyen par preuve
- Comparer les performances de l'agent avec la recherche exhaustive (tactiques enumerees) et avec AlphaProof/DeepSeek-Prover sur les memes theoremes

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Lean-7 LLM Integration | [SymbolicAI/Lean/Lean-7-LLM-Integration.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-7-LLM-Integration.ipynb) | LLM + Lean, suggestions tactiques |
| Lean-8 Agentic Proving | [SymbolicAI/Lean/Lean-8-Agentic-Proving.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-8-Agentic-Proving.ipynb) | Agent autonome de preuve |
| Lean-9 SK Multi-Agents | [SymbolicAI/Lean/Lean-9-SK-Multi-Agents.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-9-SK-Multi-Agents.ipynb) | Orchestration multi-agents |
| Lean-10 LeanDojo | [SymbolicAI/Lean/Lean-10-LeanDojo.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-10-LeanDojo.ipynb) | Interaction programmatique |

### References externes
- Song, D. et al. (2025). "Lean Copilot: LLMs as Copilots for Theorem Proving in Lean." *NeuS 2025*, PMLR v288. [proceedings.mlr.press](https://proceedings.mlr.press/v288/song25a.html)
- Yang, K. & Deng, J. (2023). "LeanDojo: Theorem Proving with Retrieval-Augmented Language Models." *NeurIPS 2023*. [openreview.net](https://openreview.net/forum?id=HWPJFOb2Sm)
- First, E. et al. (2023). "Baldur: Whole-Proof Generation and Repair with Large Language Models." *ESEC/FSE 2023*. [ACM](https://dl.acm.org/doi/10.1145/3611643.3616243)
- DeepSeek-AI (2024). "DeepSeek-Prover: Advancing Theorem Proving in Lean 4." *arXiv*. [arxiv.org/abs/2406.14320](https://arxiv.org/abs/2406.14320)
- Polu, S. et al. (2023). "Formal Mathematics Statement Curriculum Learning." *ICLR*. [openreview.net](https://openreview.net/forum?id=lmRwOP2AcF)

### Difficulte : 4/5

---

#### A3 — Theoreme d'Arrow par preuve automatisee (SAT/Z3/Lean)

Le theoreme d'impossibilite d'Arrow (1951) affirme qu'aucune regle d'agregation de preferences ne peut satisfaire simultanement quatre conditions (universalite, unanimité, independance des alternatives non pertinentes, absence de dictateur). Ce sujet aborde ce resultat fondamental de la theorie du choix social par trois approches complementaires : (1) encodage du theoreme comme probleme SAT (si N electeurs et M alternatives, les contraintes d'Arrow deviennent des clauses CNF), resolu avec PySAT pour trouver un contrexemple a la negation du theoreme ; (2) raisonnement SMT avec Z3 en utilisant des theories d'ordre et de fonctions ; (3) preuve formelle en Lean 4 avec Mathlib. La comparaison des trois approches revele les compromis entre expressivite, automatisation, confiance et comprehensibilite.

### Objectifs
- Encoder le theoreme d'Arrow comme un probleme SAT : modeliser les preferences comme permutations, les conditions d'Arrow comme contraintes boolennes, et la negation comme clause CNF a satisfaire
- Implementer le meme encodage en SMT avec Z3 (theorie des relations d'ordre, quantificateurs) et comparer le temps de resolution avec l'approche SAT
- Prouver le theoreme en Lean 4 en suivant l'encodage de Peters (SocialChoiceLean) et comparer l'effort de preuve avec les approches automatiques
- Etendre l'encodage SAT au theoreme de Sen (impossibilite du Pareto liberal) ou au theoreme de Gibbard-Satterthwaite (manipulation strategique)
- Rediger une analyse comparative des trois approches : expressivite du langage, temps de calcul, garantie de correction, effort humain, passage a l'echelle

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Arrow SAT | [GameTheory/SocialChoice/01-Arrow-Impossibility-Theorem.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/01-Arrow-Impossibility-Theorem.ipynb) | Theoreme d'Arrow par encodage SAT |
| Arrow SMT (Z3) | [GameTheory/SocialChoice/04-Computational-Aggregation-SAT-Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/04-Computational-Aggregation-SAT-Z3.ipynb) | Theoreme d'Arrow par SMT (Z3) |
| Arrow Lean | [GameTheory/SocialChoice/02-Lean-SocialChoice-Formal.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/02-Lean-SocialChoice-Formal.ipynb) | Theoreme d'Arrow en Lean 4 |
| Arrow Voting Methods | [GameTheory/SocialChoice/03-Voting-Methods.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/03-Voting-Methods.ipynb) | Methodes de vote, Arrow et au-dela |
| Lean-2 Types Dependants | [SymbolicAI/Lean/Lean-2-Dependent-Types.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-2-Dependent-Types.ipynb) | Types dependants, preuves formelles |

### References externes
- Arrow, K.J. (1951). *Social Choice and Individual Values*. 2nd ed. 1963, Wiley. [cowles.yale.edu](https://cowles.yale.edu/sites/default/files/files/pub/mon/m12-2-all.pdf)
- Geist, C. & Endriss, U. (2011). "Automated Search for Impossibility Theorems in Social Choice." *JAIR*, 40, 211-243. [AAAI](https://ojs.aaai.org/index.php/jair/article/view/10704)
- Peters, D. *SocialChoiceLean*. [GitHub](https://github.com/dominikpeters/SocialChoiceLean)
- Tang, P. & Lin, F. (2009). "Computer-Aided Proofs of Arrow's and Other Impossibility Theorems." *Artificial Intelligence*, 173(11), 1041-1053. [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0004370209000827)
- Brandt, F. et al. (2016). *Handbook of Computational Social Choice*. Cambridge. [cambridge.org](https://www.cambridge.org/core/books/handbook-of-computational-social-choice/)

### Difficulte : 5/5

---

#### A4 — Bibliotheque de preuves Mathlib — extensions

Mathlib4 est la bibliotheque mathematique de Lean 4, contenant plus de 1.5 million de lignes de preuves couvrant l'algebre, l'analyse, la topologie, la combinatoire et l'informatique theorique. Ce sujet invite l'etudiant a contribuer directement a Mathlib en ajoutant des resultats absents : identites trigonometriques, lemmes combinatoires (generatrices, relations de recurrence), proprietes de graphes (connexite, eulerience), ou extensions de l'interface data/Equiv. Le processus de contribution suit un workflow strict : fork, implementation, test avec Lake, passage du linter (leanwarningfree), soumission par PR, et review par la communaute. Ce sujet fait decouvrir l'ecosysteme Mathlib, les conventions de code, et la collaboration sur un projet open source majeur de mathematiques formelles.

### Objectifs
- Installer Mathlib4 en local (lake + cache), comprendre la structure du depot (Mathlib/Mathlib/, Mathlib/Test/, Mathlib/Archive/) et les conventions de nommage
- Identifier 3-5 resultats absents de Mathlib (en parcourant les issues GitHub, les TODO dans le code, ou en proposant des extensions naturelles de fichiers existants)
- Implementer les preuves en suivant le style Mathlib (tactics, lemma/theorem ordering, docstrings), passer le linter et les tests CI
- Soumettre au moins une contribution par PR sur le depot Mathlib4, interagir avec les reviewers et adresser les commentaires
- Rediger un notebook recapitulant les contributions, les difficultes rencontrees et les lecons apprises sur lecosysteme Mathlib

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Lean-4 Mathlib | [SymbolicAI/Lean/Lean-6-Mathlib-Essentials.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-6-Mathlib-Essentials.ipynb) | Decouverte de Mathlib, structure |
| Lean-5 Tactics | [SymbolicAI/Lean/Lean-5-Tactics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-5-Tactics.ipynb) | Tactiques avancees, automatisation |
| Lean-6 Mathlib Avance | [SymbolicAI/Lean/Lean-6-Mathlib-Essentials.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-6-Mathlib-Essentials.ipynb) | Contributions, workflow PR |
| Lean-3 Propositions | [SymbolicAI/Lean/Lean-3-Propositions-Proofs.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-3-Propositions-Proofs.ipynb) | Preuves de proprietes |

### References externes
- Mathlib Community. *Contributing to Mathlib*. [leanprover-community.github.io/contribute/](https://leanprover-community.github.io/contribute/index.html)
- Mathlib4 Repository. [github.com/leanprover-community/mathlib4](https://github.com/leanprover-community/mathlib4)
- The Mathlib Community (2020). "The Lean Mathematical Library." *CPP 2020*. [dl.acm.org](https://dl.acm.org/doi/10.1145/3372885.3373824)
- van Doorn, F. et al. (2023). "Maintaining a Library of Formal Mathematics." *ITP*. [Springer](https://link.springer.com/chapter/10.1007/978-3-031-40355-9_12)
- Lean 4 Documentation. [lean-lang.org](https://lean-lang.org/)

### Difficulte : 3/5


#### A5 — Mariages stables Gale-Shapley : preuve formelle et extensions en Lean 4

Le theoreme de Gale-Shapley (1962) garantit l'existence d'un mariage stable pour tout profil de preferences des hommes et des femmes, et l'algorithme correspondant trouve un tel mariage en temps O(n^2). Un mariage est stable si aucun couple (homme, femme) prefere mutuellement se quitter pour s'apparier. Ce sujet propose de formaliser ce resultat classique en Lean 4 en suivant le port existant dans CoursIA (GameTheory/stable_marriage_lean/), de prouver la correction et la terminaison de l'algorithme, et d'explorer les extensions : mariages stables avec preferences incompletes, problemes d'allocation ecole-eleve (college admissions), et la structure des treillis des mariages stables. L'etude des proprietes strategiques (le cote proposant est favorise) relie ce sujet a la theorie des mecanismes.

### Objectifs
- Comprendre et implementer l'algorithme de Gale-Shapley en Python, verifier la stabilite sur des instances aleatoires
- Formaliser le theoreme d'existence du mariage stable en Lean 4 en suivant le port CoursIA (StableMarriage.lean)
- Prouver la correction (le resultat est un mariage stable) et la terminaison (O(n^2)) de l'algorithme
- Explorer les extensions : preferences incompletes, couples impossibles, et la structure de treillis des mariages stables
- Analyser les proprietes strategiques (truthfulness du cote proposant) et les relier a la theorie des mecanismes

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Stable Marriage Lean | [GameTheory/stable_marriage_lean/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/GameTheory/stable_marriage_lean/) | Port Lean 4 de Gale-Shapley |
| Lean-4 Mathlib | [SymbolicAI/Lean/Lean-6-Mathlib-Essentials.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-6-Mathlib-Essentials.ipynb) | Structures Mathlib (finset, list) |
| Lean-5 Tactics | [SymbolicAI/Lean/Lean-5-Tactics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-5-Tactics.ipynb) | Tactiques de preuve |
| SocialChoice Arrow | [GameTheory/SocialChoice/01-Arrow-Impossibility-Theorem.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/01-Arrow-Impossibility-Theorem.ipynb) | Choix social, connexions mechanism design |

### References externes
- Gale, D. & Shapley, L.S. (1962). "College Admissions and the Stability of Marriage." *American Mathematical Monthly*, 69(1), 9-15. [JSTOR](https://www.jstor.org/stable/2312726)
- Gusfield, D. & Irving, R.W. (1989). *The Stable Marriage Problem: Structure and Algorithms*. MIT Press.
- Roth, A.E. (2008). "Deferred Acceptance Algorithms: History, Theory, Practice, and Open Questions." *International Journal of Game Theory*, 36, 537-569. [Springer](https://doi.org/10.1007/s00182-008-0117-6)
- Mathlib Stable Marriage. [leanprover-community](https://github.com/leanprover-community/mathlib4/)

### Difficulte : 3/5

---

#### A6 — Preuve de l'existence de Nash par point fixe en Lean 4

Le theoreme d'existence de Nash (1950) affirme que tout jeu fini a N joueurs admet au moins un equilibre en strategies mixtes. Deux routes de preuve sont formalisees en Lean 4 dans la litterature, mais **aucune n'est dans Mathlib** a ce jour : (1) la voie Brouwer via le lemme de Scarf (`math-xmum/Brouwer` — pipeline complet Scarf→Brouwer→produit→Nash, 0 sorry) ; (2) la voie Kakutani via correspondance de meilleure reponse (`harfe/fixed-point-theorems-lean4` — Kakutani complet, 0 sorry, mais non encore connecte a Nash). Ce sujet propose soit de reproduire et comprendre l'une de ces formalisations, soit de combler le gap ouvert : connecter le Kakutani de `harfe` avec les definitions de jeux de `MixedMatched/formalizing-game-theory` pour obtenir Nash par la voie "manuel d'economie" (correspondance de meilleure reponse → convexite/fermeture → point fixe de Kakutani → existence Nash). C'est un sujet de recherche en mathematiques formelles.

### Objectifs
1. Etudier et comprendre la formalisation complete `math-xmum/Brouwer` (Scarf→Brouwer→produit→Nash) et la reproduire pas a pas
2. Etudier le theoreme de Kakutani dans `harfe/fixed-point-theorems-lean4` (Brouwer + partition unite + Caratheodory → Kakutani)
3. Definir les jeux sous forme normale, strategies mixtes et correspondance de meilleure reponse en s'appuyant sur `MixedMatched/formalizing-game-theory`
4. Prouver que la correspondance de meilleure reponse satisfait les hypotheses de Kakutani (convexite, fermeture, graphes fermes)
5. Combiner pour obtenir le theoreme d'existence de Nash via Kakutani (contribution potentiellement originale si complet)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| GT-4 Nash Equilibrium | [GameTheory/GameTheory-4-NashEquilibrium.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-4-NashEquilibrium.ipynb) | Equilibres de Nash, Lemke-Howson |
| GT-4b Lean Nash | [GameTheory/GameTheory-4b-Lean-NashExistence.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-4b-Lean-NashExistence.ipynb) | Preuve d'existence en Lean 4 |
| GT-4c Nash Python | [GameTheory/GameTheory-4c-NashExistence-Python.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-4c-NashExistence-Python.ipynb) | Implementation Python |
| Lean-4 Mathlib | [SymbolicAI/Lean/Lean-6-Mathlib-Essentials.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-6-Mathlib-Essentials.ipynb) | Structures Mathlib (convexite, topologie) |

### References externes
- Nash, J.F. (1950). "Equilibrium Points in N-Person Games." *PNAS*, 36(1), 48-49. [PNAS](https://www.pnas.org/doi/10.1073/pnas.36.1.48)
- Kakutani, S. (1941). "A Generalization of Brouwer's Fixed Point Theorem." *Duke Mathematical Journal*, 8(3), 457-459. [Duke](https://doi.org/10.1215/S0012-7094-41-00838-4)
- `math-xmum/Brouwer` — Nash existence via Scarf→Brouwer en Lean 4 (0 sorry). [GitHub](https://github.com/math-xmum/Brouwer)
- `harfe/fixed-point-theorems-lean4` — Kakutani fixed-point theorem en Lean 4 (0 sorry). [GitHub](https://github.com/harfe/fixed-point-theorems-lean4)
- `MixedMatched/formalizing-game-theory` — Definitions N-joueurs, strategies mixtes en Lean 4. [GitHub](https://github.com/MixedMatched/formalizing-game-theory)
- Geanakoplos, J. (2003). "Nash and Walras Equilibrium via Brouwer." *Economic Theory*, 21, 585-603. [Springer](https://doi.org/10.1007/s001990000076)

### Difficulte : 5/5

---

### Categorie B : Logique Formelle, SAT et Demonstration Automatique

#### B1 — Resolution automatique de theoremes par SAT

La resolution automatique de theoremes par SAT consiste a encoder des problemes mathematiques (coloriage de graphes, principe des tiroirs de Dirichlet, nombres de Ramsey) en formules boolennes sous forme CNF, puis a utiliser un solveur SAT (PySAT/glucose/CaDiCaL) pour determiner la satisfiabilite. La transformation en CNF repose sur la transformation de Tseitin (introduction de variables auxiliaires pour eviter l'explosion exponentielle). L'etudiant etudie les heuristiques de branchement (VSIDS, phase saving), les mecanismes de clause learning (CDCL), et interprete les modeles et les certificats d'insatisfiabilite (proof traces). Ce sujet fait le pont entre la logique propositionnelle et la resolution automatique de problemes combinatoires, en situant SAT comme outil de verification symbolique plutot que d'optimisation.

### Objectifs
- Maitriser la transformation de Tseitin pour convertir des formules arbitraires en CNF sans explosion exponentielle, et implementer un encodeur Python vers le format DIMACS
- Encoder au moins 3 problemes classiques en SAT : coloriage de graphe (chromatique k), pigeonhole principle (injectivite), et un probleme de Ramsey (R(3,3)=6)
- Utiliser PySAT avec differents solveurs (glucose, CaDiCaL, Lingeling) et comparer les temps de resolution sur des instances de taille croissante
- Analyser les certificats de refutation (UNSAT proofs) produits par les solveurs et verifier leur validite avec un proof checker (DRAT-trim)
- Comparer l'approche SAT avec un encodage SMT (Z3, theorie des entiers/non lineaire) sur les memes problemes et discuter les compromis

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| CSP-6 SAT/SMT | [Search/Part2-CSP/CSP-6-Hybridization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-6-Hybridization.ipynb) | Encodage SAT, PySAT, solveurs |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Z3 SMT, comparaison SAT vs SMT |
| CSP-1 Fondamentaux | [Search/Part2-CSP/CSP-1-Fundamentals.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-1-Fundamentals.ipynb) | Modelisation, variables, contraintes |

### References externes
- Biere, A. et al. (2021). *Handbook of Satisfiability*. 2nd ed., IOS Press. [iospress.com](https://www.iospress.com/catalog/books/handbook-of-satisfiability-2)
- Gomes, C.P. et al. (2021). "Model Counting." *Handbook of SAT*, Chapter 22. [iospress.com](https://www.iospress.com/catalog/books/handbook-of-satisfiability-2)
- Silva, J.P.M. & Sakallah, K.A. (1999). "GRASP: A Search Algorithm for Propositional Satisfiability." *IEEE TC*, 48(5). [IEEE](https://ieeexplore.ieee.org/document/764881)
- Moskewicz, M.W. et al. (2001). "Chaff: Engineering an Efficient SAT Solver." *DAC*. [ACM](https://dl.acm.org/doi/10.1145/378239.379017)
- PySAT Documentation. [pysathq.github.io](https://pysathq.github.io/)

### Difficulte : 3/5

---

#### B2 — Synthese de programmes par Programming-by-Sketching

La synthese de programmes par sketching est une approche ou le programmeur fournit une esquisse (sketch) — un squelette de programme avec des trous (holes) a completer — et un solveur SMT determine automatiquement les valeurs des trous pour que le programme satisfasse une specification formelle. Par exemple, un tri peut etre specifie par un sketch avec un comparateur incomplet, et Z3 trouve la condition de comparaison correcte. Ce sujet utilise les theories de Z3 (tableaux, quantificateurs, entiers non lineaires) et CVC5 comme solveur SMT alternatif. Il illustre un usage symbolique de SMT : non pas verifier une propriete d'un programme existant, mais generer un programme correct par construction. Les applications vont des transformations de donnees a l'optimisation de boucles en passant par la generation de sequences d'instructions.

### Objectifs
- Comprendre le formalisme du sketching : definir un langage de sketchs avec trous, une semantique de specification (pre/post-conditions), et formuler le probleme de synthese comme une requete SMT
- Implementer un synthetiseur simplifie qui encode un sketch et sa specification en logique Z3 (quantificateurs, tableaux, fonctions non interpretees) et extrait le programme complet du modele
- Appliquer le synthetiseur a 3 cas : (a) completion d'un algorithme de tri (comparateur a trouver), (b) transformation de donnees (mapping inverse), (c) optimisation d'une boucle (invariant a synthetiser)
- Comparer les performances et l'expressivite de Z3 vs. CVC5 sur les memes problemes de synthese
- Evaluer les limitations : passage a l'echelle, profondeur du programme, theories supportees, et discuter les approches alternatives (enumeration, CEGIS)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Z3 en C#, theories SMT, modeles |
| CSP-6 SAT/SMT | [Search/Part2-CSP/CSP-6-Hybridization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-6-Hybridization.ipynb) | SAT/SMT, resolution |
| CSP-5 Optimization | [Search/Part2-CSP/CSP-5-Optimization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-5-Optimization.ipynb) | Optimisation, objective functions |

### References externes
- Solar-Lezama, A. (2008). *Program Synthesis by Sketching*. PhD Thesis, UC Berkeley. [people.csail.mit.edu](https://people.csail.mit.edu/asolar/)
- Gulwani, S. et al. (2017). "Program Synthesis." *Foundations and Trends in Programming Languages*, 4(1-2), 1-119. [nowpublishers.com](https://nowpublishers.com/article/Details/PGL-013)
- Solar-Lezama, A. et al. (2006). "Combinatorial Sketching for Finite Programs." *ASPLOS*. [ACM](https://dl.acm.org/doi/10.1145/1168857.1168907)
- Jha, S. et al. (2010). "Oracle-Guided Component-Based Program Synthesis." *ICSE*. [ACM](https://dl.acm.org/doi/10.1145/1806799.1806834)
- CVC5 Documentation. [cvc5.github.io](https://cvc5.github.io/)

### Difficulte : 4/5

---

#### B3 — Model checking de protocoles de communication

Le model checking est une technique de verification formelle qui explore exhaustivement l'espace d'etats d'un systeme pour verifier qu'il satisfait une propriete temporelle (surete LTL : "jamais d'etat d'erreur", vivacite CTL : "toujours eventuallement une reponse"). Ce sujet consiste a modeliser un protocole de communication (exclusion mutuelle de Peterson, consensus Paxos ou Raft, poignee de main TCP) comme une machine a etats finis (Kripke structure), specifier les proprietes en LTL/CTL, et utiliser un model checker (NuSMV, SPIN) pour la verification automatique. En complement, l'etudiant peut utiliser Z3 pour une verification symbolique (BDD ou SAT-based model checking) et comparer les approches.

### Objectifs
- Modeliser un protocole d'exclusion mutuelle (Peterson, Lamport's Bakery) en NuSMV comme machine a etats avec variables d'etat et transitions, et specifier les proprietes de surete (exclusion mutuelle) et de vivacite (absence de famine) en LTL/CTL
- Etendre la modelisation a un protocole de consensus (Paxos simplifie ou Raft) avec N processus et verifier la tolerance aux pannes (crash d'un processus)
- Implementer un model checker symbolique simplifie en Python utilisant Z3 (representation BDD ou encodage SAT de l'exploration d'etats) et comparer avec NuSMV
- Etudier le probleme de l'explosion combinatoire de l'espace d'etats et les techniques d'abstraction (predicate abstraction, CEGAR)
- Rediger une analyse comparative : model checking explicite (SPIN) vs. symbolique (NuSMV/BDD) vs. SAT-based, avec mesures de temps et memoire

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Search-10 Automates | [Search/Part1-Foundations/Search-10-SymbolicAutomata.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part1-Foundations/Search-10-SymbolicAutomata.ipynb) | Automates symboliques, etats |
| CSP-1 Fondamentaux | [Search/Part2-CSP/CSP-1-Fundamentals.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-1-Fundamentals.ipynb) | Modelisation par contraintes |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Z3, verification formelle |

### References externes
- Baier, C. & Katoen, J.-P. (2008). *Principles of Model Checking*. MIT Press. [mitpress.mit.edu](https://mitpress.mit.edu/9780262026499/principles-of-model-checking/)
- Clarke, E.M. et al. (2018). *Model Checking*. 2nd ed., MIT Press. [mitpress.mit.edu](https://mitpress.mit.edu/9780262038836/model-checking/)
- Holzmann, G.J. (2004). *The SPIN Model Checker*. Addison-Wesley. [spinroot.com](http://spinroot.com/spin/Doc/Book96.html)
- NuSMV Documentation. [nusmv.fbk.eu](https://nusmv.fbk.eu/)
- McMillan, K.L. (1993). *Symbolic Model Checking*. Kluwer. [springer.com](https://link.springer.com/book/10.1007/978-1-4615-3190-6)

### Difficulte : 3/5

---

#### B4 — Resolution de puzzles logiques par SMT

Les puzzles logiques (Einstein/Zebra, Knights and Knaves, Nonograms/Picross, Sudoku, Kakuro) sont des problemes de satisfaction de contraintes qui se pretent naturellement a un encodage SMT. Ce sujet compare differents encodages : booleen pur (chaque case = variable binaire), entier (chaque case = variable entiere avec contraintes de domaine), et mixte (contraintes globales comme AllDifferent). L'objectif est de comprendre les compromis entre compacite de l'encodage, temps de resolution, et expressivite. L'etudiant utilise Z3 comme solveur SMT et OR-Tools CP-SAT comme solveur CP, et compare les performances sur des instances de difficulte croissante.

### Objectifs
- Encoder le puzzle d'Einstein (Zebra puzzle) en SMT : 5 maisons, 5 attributs, 15 indices — variables entieres, contraintes d'egalite, de voisinage et d'ordre
- Encoder les puzzles Knights and Knaves en logique propositionnelle pure et en SMT, et analyser les differences de representation
- Implementer un solveur de Nonograms/Picross avec Z3 (contraintes sur les sequences de cases) et comparer avec un solveur CP-SAT (OR-Tools)
- Benchmarker les 3 encodages (booleen, entier, mixte) sur des instances de taille croissante et analyser l'impact sur le temps de resolution
- Etendre a un puzzle non traite (Kakuro, Fill-a-Pix, Slitherlink) et discuter la generalite de l'approche SMT pour les puzzles

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Sudoku multi-solveurs | [Sudoku/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Sudoku) | 18 solveurs compares, Z3, SAT, CP |
| App-11 Picross | [Search/Applications/CSP/App-11-Picross.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Applications/CSP/App-11-Picross.ipynb) | Nonograms/Picross par contraintes |
| CSP-3 Global Constraints | [Search/Part2-CSP/CSP-3-Advanced.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-3-Advanced.ipynb) | AllDifferent, contraintes globales |

### References externes
- de Moura, L. & Bjorner, N. (2008). "Z3: An Efficient SMT Solver." *TACAS*. [Springer](https://link.springer.com/chapter/10.1007/978-3-540-78800-3_24)
- Regin, J.-C. (1994). "A Filtering Algorithm for Constraints of Difference in CSPs." *AAAI*. [aaai.org](https://ojs.aaai.org/index.php/AAAI/article/view/9084)
- Bessi, C. et al. (2014). "Verifying Integer and Floating-Point Constraints in SMT." *TACAS*. [Springer](https://link.springer.com/chapter/10.1007/978-3-642-54862-8_20)
- Eiter, T. et al. (2023). "Answer Set Programming and SMT for Combinatorial Problem Solving." *Kuenstliche Intelligenz*. [springer.com](https://link.springer.com/article/10.1007/s13218-023-00816-5)

### Difficulte : 2/5

---

#### B5 — Demonstration automatique en geometrie

La demonstration automatique en geometrie elementaire consiste a prouver des theoremes geometriques (Thales, Pythagore, points cocycliques, theoreme de Ceva, theoreme de Menelaus) par des methodes algebriques. L'approche principale est le calcul de Wu (elimination de pseudo-restes dans un anneau de polynomes) qui reduit un theoreme geometrique a la verification que le pseudo-reste du polynome conclusion par les polynomes hypotheses est nul. L'alternative est l'encodage SMT : exprimer les hypotheses et la conclusion comme equations sur les coordonnees des points, puis laisser Z3 verifier l'implication. Ce sujet combine geometrie, algebre computationnelle (SymPy) et logique, et produit des visualisations matplotlib des theoremes prouves.

### Objectifs
- Implementer le calcul de Wu en Python (SymPy) : conversion d'un enonce geometrique en polynomes, calcul du pseudo-reste, verification de la nullite
- Encoder 5 theoremes classiques (Pythagore, Thales, points cocycliques, Ceva, Menelaus) en coordonnees et verifier avec Z3 (theorie QF_NRA)
- Comparer les deux approches : Wu (base analytique, resultat exact) vs. SMT (approche verification, passages a l'echelle differents)
- Generer des visualisations matplotlib des constructions geometriques avec les points, droites et cercles impliques dans chaque theoreme
- Explorer les limitations : theoremes necessitant des degres eleves, cas singuliers (points alignes), et la difference entre preuve generique et preuve exhaustive

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Z3, theorie NRA, verification |
| CSP-6 SAT/SMT | [Search/Part2-CSP/CSP-6-Hybridization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-6-Hybridization.ipynb) | SMT, theories non-lineaires |

### References externes
- Wu, W.-T. (1994). *Mechanical Theorem Proving in Geometries*. Springer. [springer.com](https://link.springer.com/book/10.1007/978-3-7091-6636-9)
- Chou, S.-C. et al. (1994). *Machine Proofs in Geometry*. World Scientific. [worldscientific.com](https://www.worldscientific.com/worldscibooks/10.1142/2038)
- Kapur, D. (1986). "Geometry Theorem Proving Using Hilbert's Nullstellensatz." *SYMSAC*. [ACM](https://dl.acm.org/doi/10.1145/32439.32419)
- J9anicke, M. et al. (2021). "Automated Reasoning in Geometry." *Journal of Automated Reasoning*. [Springer](https://link.springer.com/article/10.1007/s10817-020-09573-0)

### Difficulte : 4/5

---

#### B6 — Programmation par ensembles de reponses (ASP) avec Clingo

La programmation par ensembles de reponses (Answer Set Programming, ASP) est un paradigme declaratif de programmation logique, distinct de SAT et de la programmation par contraintes. Un programme ASP est un ensemble de regles logiques de la forme "tete :- corps" (la tete est vraie si le corps est vrai), et la semantique est donnee par les modeles stables de Gelfond-Lifschitz (points fixes de la reduct du programme). Clingo (Potassco) est le solveur ASP de reference. L'ASP est particulierement adapte aux problemes avec raisonnement par defaut, exceptions, preferences, et connaissances incompletes. Ce sujet couvre la modelisation de problemes combinatoires en ASP (scheduling, planning, coloriage, claquage de ponts), l'API Python de Clingo pour le scripting, et la comparaison avec les approches SAT et CP sur les memes instances.

### Objectifs
- Apprendre la syntaxe ASP (regles, faits, contraintes d'integrite, choice rules, aggregate) et la semantique des modeles stables sur des exemples simples (coloriage de graphe, N-queens)
- Modeliser un probleme de scheduling ou de planning en ASP avec Clingo, incluant des contraintes d'integrite, des preferences faibles (#minimize), et des regles par defaut
- Utiliser l'API Python de Clingo (module clingo) pour controler le solving depuis Python (parametrage, extraction de solutions, post-traitement)
- Comparer ASP avec un encodage SAT (PySAT) et CP-SAT (OR-Tools) sur les memes instances de problemes (coloriage, scheduling), en mesurant temps et qualite des solutions
- Explorer l'hybridation LLM+ASP : utiliser un LLM pour generer automatiquement des programmes ASP a partir d'une description en langage naturel (approche LLASP)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-6 ASP/Clingo | [SymbolicAI/Tweety/Tweety-6-Structured-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-6-Structured-Argumentation.ipynb) | ASP avec Clingo, argumentation |
| CSP-1 Fondamentaux | [Search/Part2-CSP/CSP-1-Fundamentals.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-1-Fundamentals.ipynb) | Comparaison CSP, modelisation |
| Tweety-2 Basic Logics | [SymbolicAI/Tweety/Tweety-2-Basic-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-2-Basic-Logics.ipynb) | Logiques classiques, raisonnement |

### References externes
- Gelfond, M. & Lifschitz, V. (1988). "The Stable Model Semantics for Logic Programming." *ICLP/SLP*. [cs.utexas.edu](https://www.cs.utexas.edu/~vl/papers/stable.pdf)
- Gebser, M. et al. (2012). *Answer Set Solving in Practice*. Springer. [potassco.org](https://potassco.org/book/)
- Brewka, G. et al. (2011). "Answer Set Programming at a Glance." *CACM*, 54(12). [ACM](https://dl.acm.org/doi/10.1145/2043174.2043195)
- Lifschitz, V. (2019). *Answer Set Programming*. Springer. [springer.com](https://link.springer.com/book/10.1007/978-3-030-24658-7)
- Potassco, Clingo Documentation. [potassco.org/clingo/](https://potassco.org/clingo/)

### Difficulte : 3/5

---

#### B7 — Resolution de problemes PSPACE par QBF (Quantified Booleans)

Les formules booleennes quantifiees (QBF) etendent SAT en ajoutant des quantificateurs existentiels et universels sur les variables. Un probleme QBF de la forme Ex1 Ax2 Ex3 ... phi(x1,x2,x3,...) est PSPACE-complet, capturant une classe de complexite strictement plus grande que SAT (NP-complet). Les QBF permettent d'encoder naturellement des jeux a deux joueurs (E joue les coups existentiels, A joue les coups universels), de la verification de circuits sequentiels (deraisonnement temporel), et du planning conformant (plan qui fonctionne quelles que soient les observations). Ce sujet utilise PyQBF comme interface Python pour les solveurs QBF (DepQBF, CAQE, Qute) et evalue les performances sur les benchmarks QBFLib.

### Objectifs
- Comprendre la semantique des QBF (jeu semantique : E et A jouent alternativement les valeurs des variables) et la hierarchie des prenex forms (Sigma_k, Pi_k)
- Encoder 3 problemes en QBF : (a) un jeu a deux joueurs (Tic-tac-toe, Hex, ou Geographie), (b) un probleme de verification de circuit sequentiel, (c) un probleme de planning conformant
- Utiliser PyQBF avec au moins 2 solveurs (DepQBF, CAQE) et comparer les temps de resolution sur les encodages produits
- Evaluer sur les benchmarks QBFLib (instances de reference de la competition QBF Eval) et analyser les facteurs de difficulte (profondeur de quantification, nombre de variables)
- Comparer les solveurs QBF avec une approche iterative (re-resolution SAT dans une boucle) et discuter l'avantage du solving QBF natif

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-3 Advanced Logics | [SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb) | QBF, logiques modales, model checking |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Z3, quantificateurs, theories |
| CSP-6 SAT/SMT | [Search/Part2-CSP/CSP-6-Hybridization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-6-Hybridization.ipynb) | SAT, comparaison avec QBF |

### References externes
- Peyrer, M. et al. (2025). "PyQBF: A Python Framework for Solving QBF." *ACM TOCL*. [dl.acm.org](https://dl.acm.org/doi/10.1145/3701776)
- Shukla, A. et al. (2026). "The QBF Gallery 2023." *arXiv*. [arxiv.org](https://arxiv.org/abs/2305.01699)
- Biere, A. et al. (2021). "QBF." *Handbook of Satisfiability*, Chapter 23. [iospress.com](https://www.iospress.com/catalog/books/handbook-of-satisfiability-2)
- Lonsing, F. & Biere, A. (2010). "DepQBF: A Dependency-Preserving QBF Solver." *SAT*. [Springer](https://link.springer.com/chapter/10.1007/978-3-642-14186-7_10)
- QBFLib Benchmark Collection. [qbflib.org](https://qbflib.org/)

### Difficulte : 3/5

---

#### B8 — Solveur SAT/SMT certifiant : certificats UNSAT verifies (DRAT/LRAT) et checker prouve en Lean 4

Les solveurs SAT et SMT modernes sont au coeur de la verification formelle, mais ils constituent eux-memes des logiciels complexes et faillibles : un bug dans un solveur peut produire un verdict UNSAT errone, invalidant silencieusement toute preuve qui en depend. La reponse de la communaute est le solveur **certifiant** : plutot que de faire confiance au solveur, on lui demande de produire un **certificat** verifiable de son resultat. Pour l'insatisfiabilite, le standard est le format de preuve par resolution etendue **DRAT** (et son successeur indexe **LRAT**), un journal de clauses apprises et supprimees permettant de rejouer et valider la refutation. Ce sujet de recherche consiste a (1) instrumenter un solveur CDCL pour emettre des preuves DRAT/LRAT, (2) construire un **verificateur de certificats formellement prouve correct** -- a la maniere de cake_lpr (CakeML) ou GRAT -- de sorte que la confiance repose sur un noyau verifie minuscule plutot que sur le solveur entier, et (3) etendre l'approche aux preuves SMT (reconstruction de preuve facon Z3/cvc5 dans un assistant). L'enjeu pratique : des preuves industrielles atteignent des centaines de teraoctets (probleme des triplets pythagoriciens booleens), ce qui exige des verificateurs a la fois surs et efficaces.

### Objectifs
1. Instrumenter un solveur SAT de type CDCL pour emettre des preuves DRAT puis LRAT (clauses apprises, suppressions), et valider la chaine de bout en bout avec DRAT-trim / lrat-check
2. Implementer un verificateur de certificats UNSAT et le **certifier** : soit en l'extrayant d'un developpement Lean 4 prouve correct, soit en reconstruisant la refutation pas-a-pas dans l'assistant (noyau de confiance minimal)
3. Etendre au cadre SMT : capturer et rejouer les preuves d'un solveur (Z3, cvc5) sur des theories decidables (egalite + fonctions non interpretees, arithmetique lineaire), avec reconstruction de preuve verifiee
4. Construire un banc d'essai a partir d'instances reelles (SAT Competition, encodages combinatoires type Sudoku-Z3, agregation sociale SAT/Z3) et mesurer le surcout d'emission et de verification
5. Analyser le compromis confiance/performance : taille des preuves, temps de verification, taille du noyau de confiance (TCB), et qualifier rigoureusement ce qui est *prouve* par rapport a ce qui reste *suppose*

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Sudoku-12 Z3 (C#) | [Sudoku/Sudoku-12-Z3-Csharp.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Sudoku/Sudoku-12-Z3-Csharp.ipynb) | Encodage SAT/SMT d'un probleme combinatoire : source d'instances et de verdicts a certifier |
| Sudoku-14 BDD | [Sudoku/Sudoku-14-BDD-Csharp.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Sudoku/Sudoku-14-BDD-Csharp.ipynb) | Representation symbolique alternative (BDD) : verification croisee independante des verdicts |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Pilotage de Z3 depuis .NET : extraction de preuves et d'unsat-cores |
| SocialChoice-04 Aggregation SAT/Z3 | [GameTheory/SocialChoice/04-Computational-Aggregation-SAT-Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/04-Computational-Aggregation-SAT-Z3.ipynb) | Encodage SAT d'enonces a refuter : instances UNSAT realistes a certifier |
| Lean-5 Tactics | [SymbolicAI/Lean/Lean-5-Tactics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-5-Tactics.ipynb) | Tactiques Lean 4 : socle pour un verificateur de certificats prouve correct |
| Lean-6 Mathlib Essentials | [SymbolicAI/Lean/Lean-6-Mathlib-Essentials.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-6-Mathlib-Essentials.ipynb) | Structures et lemmes reutilisables pour formaliser la correction du checker |

### References externes

**Certificats de preuve UNSAT (DRAT/LRAT)**
- Wetzler, N., Heule, M. & Hunt, W. (2014). "DRAT-trim: Efficient Checking and Trimming Using Expressive Clausal Proofs." *SAT 2014*. [Springer](https://link.springer.com/)
- Heule, M., Hunt, W. & Wetzler, N. (2013). "Verifying Refutations with Extended Resolution." *CADE 2013*. [Springer](https://link.springer.com/)
- Heule, M., Kullmann, O. & Marek, V. (2016). "Solving and Verifying the Boolean Pythagorean Triples Problem via Cube-and-Conquer." *SAT 2016*. (preuve de ~200 To : motive des verificateurs surs ET efficaces) [arXiv:1605.00723](https://arxiv.org/abs/1605.00723)

**Verificateurs de certificats formellement prouves**
- Tan, Y.K., Heule, M. & Myreen, M. (2021). "cake_lpr: Verified Propagation Redundancy Checking in CakeML." *TACAS 2021*. [Springer](https://link.springer.com/)
- Lammich, P. (2017). "Efficient Verified (UN)SAT Certificate Checking." *CADE 2017*. (GRAT) [Springer](https://link.springer.com/)
- Cruz-Filipe, L., Marques-Silva, J. & Schneider-Kamp, P. (2017). "Efficient Certified Resolution Proof Checking." *TACAS 2017*. [Springer](https://link.springer.com/)

**SMT et reconstruction de preuve**
- de Moura, L. & Bjorner, N. (2008). "Z3: An Efficient SMT Solver." *TACAS 2008*. [Springer](https://link.springer.com/)
- Bohme, S. & Weber, T. (2010). "Fast LCF-Style Proof Reconstruction for Z3." *ITP 2010*. [Springer](https://link.springer.com/)
- Barbosa, H. et al. (2022). "cvc5: A Versatile and Industrial-Strength SMT Solver." *TACAS 2022*. [Springer](https://link.springer.com/)
- Barrett, C. & Tinelli, C. (2018). "Satisfiability Modulo Theories." *Handbook of Model Checking*, Springer. [Springer](https://link.springer.com/)

### Difficulte : 5/5

---

### Categorie C : Verification Formelle et Surete des Logiciels

#### C1 — Verification formelle de smart contracts Solidity par SMT

La verification formelle de smart contracts Solidity exploite le SMTChecker integre au compilateur solc ainsi que des outils externes comme Mythril et Slither pour prouver automatiquement des proprietes de surete sur des contrats deploies sur Ethereum. Le SMTChecker traduit les invariants Solidity (`assert`, `require`, conditions de boucle) en formules SMT resolues par Z3 ou CVC5, permettant de detecter des vulnerabilites critiques comme la reentrancy, les overflow arithmetiques et les defauts de controle d'acces sans execution concrete. Ce sujet amene a comprendre le modele memoire de Solidity (storage, memory, calldata), les limitations de la verification SMT (explosion combinatoire, boucles non bornees), et la complementarite entre model checking et analyse statique. L'etudiant ecrit des specifications formelles pour des patterns de contrats courants (ERC-20, multisig, timelock) et interprete les contre-exemples produits par le solveur.

### Objectifs
- Configurer le pipeline de verification : activer le SMTChecker dans solc, ecrire des invariants Solidity, et analyser les contre-exemples produits par Z3/CVC5 sur des contrats vulnérables
- Verifier formellement un contrat ERC-20 complet : prouver l'absence de reentrancy sur transfer, la conservation du total supply, et la coherence des balances
- Comparer les resultats du SMTChecker avec des outils d'analyse statique (Slither taint analysis, Mythril symbolic execution) sur un benchmark de contrats avec vulnerabilites connues (SWC Registry)
- Etudier les limitations pratiques : gestion des boucles non bornees, approximation des mappings dynamiques, timeout du solveur, et proposer des strategies de modelisation pour les contourner
- Rediger un rapport comparatif des techniques de verification (model checking SMT vs. analyse statique vs. fuzzing) avec leurs forces, faiblesses et domaines d'application preferentiels

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SC-13 Fuzz Testing | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-13-Fuzz-Invariants.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-13-Fuzz-Invariants.ipynb) | Fuzzing Foundry, complementaire au model checking |
| SC-14 Formal Verification | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb) | SMTChecker, invariants, contre-exemples |
| SC-0 Solidity Basics | [SymbolicAI/SmartContracts/01-Solidity-Foundation/SC-3-Solidity-Basics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/01-Solidity-Foundation/SC-3-Solidity-Basics.ipynb) | Fondamentaux Solidity, prerequis |
| CSP-1 Fondamentaux | [Search/Part2-CSP/CSP-1-Fundamentals.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-1-Fundamentals.ipynb) | Contraintes et propagation, bases conceptuelles |

### References externes
- Hajdu, A. & Jovanovic, D. (2020). "SMT-Friendly Formalization of the Solidity Memory Model." *ESOP 2020*, LNCS 12075. [Springer](https://link.springer.com/chapter/10.1007/978-3-030-44914-8_9)
- Feist, J., Grieco, G. & Groce, A. (2019). "Slither: A Static Analysis Framework for Smart Contracts." *IEEE S&B Workshop*. [arXiv](https://arxiv.org/abs/1906.06505)
- Mueller, B. (2017). "Smashing Ethereum Smart Contracts for Fun and Real Profit." *HITB*. [github.com/crytic](https://github.com/crytic/publications/blob/master/Smashing%20Ethereum%20Smart%20Contracts%20for%20Fun%20and%20Real%20Profit.pdf)
- SWC Registry. *Smart Contract Weakness Classification and Test Cases*. [swcregistry.io](https://swcregistry.io/)
- Alt, L. & Reitwiessner, C. (2018). "SMT-Based Verification of Solidity Smart Contracts." *SSS*. [Springer](https://link.springer.com/chapter/10.1007/978-3-030-03080-2_11)

### Difficulte : 3/5

---

#### C2 — Fuzzing guide par contraintes (constraint-based fuzzing)

Le fuzzing guide par contraintes (concolic fuzzing) combine l'execution symbolique et le fuzzing aleatoire pour explorer systematiquement les chemins d'execution d'un programme. A chaque etape, le fuzzer collecte les contraintes de branche rencontrees le long d'un chemin d'execution, les negate une par une avec Z3 pour generer de nouvelles entrees atteignant des branches non couvertes, puis injecte ces entrees dans le programme concret. Cette approche hybride, illustree par des outils comme Driller et Echidna, surcome les limitations du fuzzing pur (difficulte a traverser les comparaisons magiques) et de l'execution symbolique pure (explosion du nombre de chemins). Le sujet couvre la theorie de l'execution symbolique (formules path conditions), la resolution de contraintes SMT, les strategies de selection de chemins, et l'application aux smart contracts Solidity via Foundry/Echidna.

### Objectifs
- Implementer un moteur d'execution symbolique simplifie sur un sous-ensemble de bytecode EVM ou d'instructions Solidity, collectant les path conditions comme conjonction de contraintes de branche
- Integrer Z3 comme solveur de contraintes pour generer de nouvelles entrees a partir des path conditions negatees, en gerant les contraintes non lineaires et les timeout
- Comparer le coverage de code obtenu par le fuzzer symbolique vs. le fuzzing aleatoire (AFL/libFuzzer) sur des benchmarks Solidity (contrats avec branches conditionnelles complexes)
- Evaluer l'apport du seed scheduling intelligent (priorisation des chemins non explores, energy-based scheduling) sur l'efficacite de l'exploration
- Documenter les cas ou l'execution symbolique echoue (operations non supportees, appels externes, gas limits) et les strategies de fallback vers le fuzzing aleatoire

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SC-13 Fuzz Testing | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-13-Fuzz-Invariants.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-13-Fuzz-Invariants.ipynb) | Fuzzing Foundry/Echidna, point de depart |
| SC-14 Formal Verification | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb) | Verification formelle, complementaire |
| CSP-6 Hybridation | [Search/Part2-CSP/CSP-6-Hybridization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-6-Hybridization.ipynb) | Hybridation CP+SAT, strategies de recherche |
| Planners-3 State Space | [SymbolicAI/Planners/01-Foundation/Planners-3-State-Space.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/01-Foundation/Planners-3-State-Space.ipynb) | Exploration d'espaces d'etats, concepts transversaux |

### References externes
- Stephens, N. et al. (2016). "Driller: Augmenting Fuzzing Through Selective Symbolic Execution." *NDSS 2016*. [NDSS Symposium](https://www.ndss-symposium.org/ndss2016/ndss-2016-programme/augmenting-fuzzing-through-selective-symbolic-execution/)
- Bosman, E. et al. (2015). "Firmalice - Automatic Detection of Authentication Bypass Vulnerabilities." *USENIX Security*. [usenix.org](https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/bosman)
- Cadar, C. & Sen, K. (2013). "Symbolic Execution for Software Testing: Three Decades Later." *Communications of the ACM*, 56(2). [CACM](https://cacm.acm.org/research/symbolic-execution-for-software-testing/)
- Coppola, G. (2023). "Echidna: A Smart Fuzzer for Ethereum Smart Contracts." *Trail of Bits*. [github.com/crytic/echidna](https://github.com/crytic/echidna)
- Li, Y. et al. (2023). "Large Language Models for Fuzzing and Testing." *arXiv*. [arxiv.org/abs/2312.03614](https://arxiv.org/abs/2312.03614)

### Difficulte : 4/5

---

#### C3 — Analyse statique et detection de vulnerabilites par abstraction

L'analyse statique par interpretation abstraite est une technique formelle qui approxime le comportement d'un programme sans l'executer, en remplaçant les valeurs concretes par des representations abstraites issues de domaines lattice (intervalles, signes, congruences, octogones). Inventee par Cousot & Cousot en 1977, cette approche calcule un point fixe du systeme de transitions du programme dans le domaine abstrait, garantissant une sure-approximation (soundness) de tous les comportements possibles. Les vulnerabilites sont detectees quand l'etat abstrait est incompatible avec les assertions de surete. Ce sujet couvre la theorie des treillis complets, les operateurs de widening/narrowing pour assurer la convergence, la construction de domaines abstraits composes (produit reduit), et l'application a la detection de buffer overflows, use-after-free, et fuites d'information dans du code source.

### Objectifs
- Implementer un domaine abstrait des intervalles (lattice des intervalles entiers avec bornes infinies) et l'operateur de transfer pour les operations arithmetiques, comparaisons et affectations
- Construire un analyseur de flot de donnees qui itere sur le CFG du programme jusqu'a atteindre un point fixe, en utilisant un operateur de widening pour garantir la convergence sur les boucles
- Etendre le domaine des intervalles par produit reduit avec le domaine des signes et des congruences, et mesurer la precision gagnee sur des programmes de test
- Evaluer l'analyseur sur un benchmark de vulnerabilities connues (buffer overflow, division par zero, debordement d'entier) et calculer le taux de faux positifs
- Utiliser Z3 comme oracle de contrexemple : quand l'analyse abstraite rapporte une potentielle erreur, invoquer Z3 sur la negation de la contrainte pour determiner si l'erreur est reelle ou un faux positif

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SC-13 Fuzz Testing | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-13-Fuzz-Invariants.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-13-Fuzz-Invariants.ipynb) | Techniques dynamiques complementaires |
| SC-14 Formal Verification | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb) | Model checking, complementaire a l'interpretation abstraite |
| Lean-2 Dependent Types | [SymbolicAI/Lean/Lean-2-Dependent-Types.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-2-Dependent-Types.ipynb) | Raisonnement formel sur les types, bases conceptuelles |
| CSP-1 Fondamentaux | [Search/Part2-CSP/CSP-1-Fundamentals.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-1-Fundamentals.ipynb) | Domaines, propagation de contraintes, points fixes |

### References externes
- Cousot, P. & Cousot, R. (1977). "Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs." *POPL 1977*. [ACM](https://dl.acm.org/doi/10.1145/512950.512973)
- Mine, A. (2004). *Weakly Relational Numerical Abstract Domains*. PhD Thesis, ENS. [cel.archives-ouvertes.fr](https://cel.archives-ouvertes.fr/tel-00136648)
- Blanchet, B. et al. (2003). "A Static Analyzer for Large Safety-Critical Software." *PLDI 2003*. [ACM](https://dl.acm.org/doi/10.1145/781131.781153)
- Schmidt, D.A. (1998). "Data Flow Analysis is Model Checking of Abstract Interpretations." *POPL 1998*. [ACM](https://dl.acm.org/doi/10.1145/268946.268956)
- Cousot, P. (2021). "Principles of Abstract Interpretation." *MIT Press*. [mitpress.mit.edu](https://mitpress.mit.edu/9780262045214/principles-of-abstract-interpretation/)

### Difficulte : 3/5

---

#### C4 — Preuves de correcteur Zero-Knowledge (zk-SNARKs)

Les preuves Zero-Knowledge (zk-SNARKs) permettent a un prover de convaincre un verifier qu'un calcul est correct sans reveler aucune information sur les entrees, en utilisant des systemes de preuve succints bases sur des courbes elliptiques (bn254, bls12-381) et des polynomes d'engagement. Ce sujet etudie la construction complete d'un circuit arithmetique (R1CS ou Plonkish) encodant une relation computationnelle (range proof, preuve d'appartenance a un arbre de Merkle, preuve de solvabilite), la generation de la proving key et verifying key via un trusted setup ou un setup universel (PLONK), et la verification on-chain dans un smart contract Solidity. La correction du circuit est cruciale : un circuit mal contraint peut accepter des preuves invalides (under-constrained), ce qui motive l'utilisation d'outils de verification formelle sur les circuits eux-memes.

### Objectifs
- Implementer un circuit arithmetique simple en Circom (range proof sur 64 bits, preuve d'appartenance dans un Merkle tree) et comprendre le passage du code Circom au systeme R1CS
- Maitriser le pipeline Circom -> SnarkJS : compilation, trusted setup (Powers of Tau), generation de preuve, et verification dans un contrat Solidity deploye sur testnet
- Analyser la correction du circuit : identifier les contraintes sous-determinees (under-constrained signals), verifier l'equivalence entre la specification et le circuit, et tester avec des entrees maliceses
- Comparer les systemes de preuve zk-SNARK (Groth16 vs. PLONK) sur les criteres de taille de preuve, temps de verification, necessity du trusted setup, et expressivite du circuit
- Explorer les applications avancees : preuves de solvabilite pour exchanges decentralises, votes anonymes, ou credentials verifiables (ZK-DAO)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SC-15 Zero-Knowledge Proofs | [SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-15-Zero-Knowledge-Proofs.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-15-Zero-Knowledge-Proofs.ipynb) | ZKP, Circom, SnarkJS, circuits arithmetiques |
| SC-16 Homomorphic Encryption | [SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-16-Homomorphic-Encryption.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-16-Homomorphic-Encryption.ipynb) | Chiffrement homomorphe, calcul sur donnees chiffrees |
| SC-14 Formal Verification | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb) | Verification de circuits, complementaire |
| SC-0 Solidity Basics | [SymbolicAI/SmartContracts/01-Solidity-Foundation/SC-3-Solidity-Basics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/01-Solidity-Foundation/SC-3-Solidity-Basics.ipynb) | Prerequis Solidity pour la verification on-chain |

### References externes
- Ben-Sasson, E. et al. (2019). "Scalable Zero Knowledge with No Trusted Setup." *CRYPTO 2019*. [ePrint](https://eprint.iacr.org/2019/099)
- Gabizon, A., Williamson, Z. & Ciobotaru, O. (2019). "PLONK: Permutations over Lagrange-Bases for Oecumenical Noninteractive Arguments of Knowledge." *ePrint 2019/953*. [ePrint](https://eprint.iacr.org/2019/953)
- Groth, J. (2016). "On the Size of Pairing-Based Non-Interactive Arguments." *EUROCRYPT 2016*. [Springer](https://link.springer.com/chapter/10.1007/978-3-662-49896-5_2)
- Thaler, J. (2022). *Proofs, Arguments, and Zero-Knowledge*. Now Publishers. [people.cs.georgetown.edu](https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.html)
- Nitulescu, A. (2020). "zk-SNARKs: A Gentle Introduction." *Electric Coin Co.* [electriccoin.co](https://electriccoin.co/blog/snark-explain/)

### Difficulte : 4/5

---


---

#### C5 — Synthese de programmes corrects-par-construction par CEGIS et verification deductive

La verification formelle prouve qu'un programme *existant* respecte sa specification ; la **synthese de programmes** va plus loin en *fabriquant* un programme garanti correct a partir de la specification. La technique pivot est **CEGIS** (Counterexample-Guided Inductive Synthesis) : un synthetiseur propose un candidat, un verificateur (solveur SMT) cherche un contre-exemple, et chaque contre-exemple raffine l'espace de recherche jusqu'a un programme prouve correct sur tout le domaine. Ce sujet de recherche combine trois piliers : (1) la **synthese guidee par syntaxe** (SyGuS) ou l'espace des programmes est decrit par une grammaire et la specification par une formule logique ; (2) la **synthese d'invariants inductifs** -- verrou central de la verification de boucles -- ou il faut decouvrir automatiquement l'assertion qui se propage d'une iteration a l'autre ; et (3) la **verification deductive** de bout en bout (logique de Hoare, plus faible precondition) certifiant que le code synthetise satisfait sa specification. L'ambition est de produire des composants *corrects-par-construction* (fragment d'interpreteur, parseur, structure de donnees) accompagnes d'une preuve verifiable, et de mesurer le passage a l'echelle de CEGIS face a la complexite des invariants.

### Objectifs
1. Formaliser une tache de synthese en SyGuS (grammaire de l'espace des programmes + specification logique) et implementer une boucle CEGIS complete (proposer / verifier / raffiner) au-dessus d'un solveur SMT (Z3, cvc5)
2. Attaquer la **synthese d'invariants inductifs** pour la verification de boucles : implementer au moins deux strategies (template-based facon Houdini, et apprentissage data-driven facon ICE) et comparer leur portee
3. Mettre en place une verification deductive (logique de Hoare / plus faible precondition) du programme synthetise, via un verificateur de type Dafny ou un encodage SMT direct des obligations de preuve
4. Appliquer la chaine a un composant non trivial correct-par-construction (interpreteur d'un DSL borne, parseur, structure de donnees avec invariant) et livrer l'artefact + sa specification + sa preuve
5. Evaluer : classes de programmes synthetisables, explosion combinatoire de CEGIS, qualite des invariants decouverts, et limites (ce qui echappe a la synthese automatique)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SL-4 Inductive Logic Programming | [SymbolicAI/SymbolicLearning/SL-4-InductiveLogicProgramming.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SymbolicLearning/SL-4-InductiveLogicProgramming.ipynb) | Synthese inductive de programmes a partir d'exemples : coeur de la generalisation CEGIS |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Pilotage de Z3 : le verificateur de la boucle CEGIS et le generateur de contre-exemples |
| SC-13 Fuzz-Invariants | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-13-Fuzz-Invariants.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-13-Fuzz-Invariants.ipynb) | Decouverte et test d'invariants : analogue data-driven de la synthese d'invariants |
| SC-14 Formal Verification | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb) | Specifications, pre/post-conditions et invariants : la cible deductive |
| Lean-5 Tactics | [SymbolicAI/Lean/Lean-5-Tactics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-5-Tactics.ipynb) | Preuve des obligations de correction (logique de Hoare formalisee) |
| SL-7 LLM Symbolic Learning | [SymbolicAI/SymbolicLearning/SL-7-LLM-SymbolicLearning.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SymbolicLearning/SL-7-LLM-SymbolicLearning.ipynb) | LLM comme proposeur de candidats dans la boucle de synthese (variante neuro-symbolique) |

### References externes

**Synthese par contre-exemples (CEGIS, SyGuS)**
- Solar-Lezama, A. et al. (2006). "Combinatorial Sketching for Finite Programs." *ASPLOS 2006*. (origine de CEGIS) [ACM Digital Library](https://dl.acm.org/)
- Alur, R. et al. (2013). "Syntax-Guided Synthesis." *FMCAD 2013*. (SyGuS) [IEEE](https://ieeexplore.ieee.org/)
- Gulwani, S., Polozov, O. & Singh, R. (2017). "Program Synthesis." *Foundations and Trends in Programming Languages*. [nowpublishers](https://www.nowpublishers.com/)

**Synthese d'invariants inductifs**
- Flanagan, C. & Leino, K.R.M. (2001). "Houdini, an Annotation Assistant for ESC/Java." *FME 2001*. [Springer](https://link.springer.com/)
- Garg, P. et al. (2014). "ICE: A Robust Framework for Learning Invariants." *CAV 2014*. [Springer](https://link.springer.com/)
- Si, X. et al. (2018). "Learning Loop Invariants for Program Verification." *NeurIPS 2018*. [proceedings.neurips.cc](https://proceedings.neurips.cc/)

**Verification deductive (fondements)**
- Hoare, C.A.R. (1969). "An Axiomatic Basis for Computer Programming." *CACM*, 12(10). [ACM Digital Library](https://dl.acm.org/)
- Dijkstra, E.W. (1975). "Guarded Commands, Nondeterminacy and Formal Derivation of Programs." *CACM*. [ACM Digital Library](https://dl.acm.org/)
- Leino, K.R.M. (2010). "Dafny: An Automatic Program Verifier for Functional Correctness." *LPAR-16*. [Springer](https://link.springer.com/)
- Srivastava, S., Gulwani, S. & Foster, J. (2010). "From Program Verification to Program Synthesis." *POPL 2010*. [ACM Digital Library](https://dl.acm.org/)

### Difficulte : 5/5

---

### Categorie D : Planification et Ordonnancement

#### D1 — Planification robotique avec PDDL et integration capteurs

La planification robotique avec PDDL consiste a modeliser un domaine de planification autonome pour un robot evoluant dans un environnement structure tel qu'un entrepot logistique, en definissant les predicats, les actions (navigation, saisie, depose) et les contraintes d'occupance dans le formalisme PDDL. Le planificateur Fast Downward genere ensuite un plan d'actions sequencees que le robot doit executer dans un monde reel ou l'incertitude sensorielle rend l'execution naive impraticable. L'integration de capteurs (lidar, vision, proprioception) permet de detecter les ecarts entre l'etat attendu et l'etat observe, declenchant une re-planification en ligne lorsque l'environnement diverge du modele. Ce sujet aborde ainsi la boucle complete "modelisation-planification-execution-monitoring-replanification", au coeur de l'architecture robotique moderne (planification contingente, planification de sensibilite). La simulation Python permet de valider l'approche sur des scenarios d'escalade de complexite avant un eventuel deploiement sur robot reel.

### Objectifs
- Modeliser un domaine robotique d'entrepot en PDDL (predicats, actions, types d'objets) et generer des plans avec Fast Downward
- Implementer un simulateur d'execution qui injecte des perturbations sensorielles (obstacles dynamiques, erreurs de localisation)
- Concevoir un module de monitoring qui compare l'etat reel (capteurs) a l'etat attendu (plan) et detecte les violations de preconditions
- Implementer une strategie de re-planification en ligne (replan from current state, plan repair) et mesurer le cout en temps de calcul
- Evaluer la robustesse de l'approche sur des scenarios de complexite croissante (nombre d'objets, obstacles dynamiques, bruit capteur)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Planners-1 Introduction | [SymbolicAI/Planners/01-Foundation/Planners-1-Introduction.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/01-Foundation/Planners-1-Introduction.ipynb) | Fondamentaux PDDL |
| Planners-3 State-Space Search | [SymbolicAI/Planners/01-Foundation/Planners-3-State-Space.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/01-Foundation/Planners-3-State-Space.ipynb) | Heuristiques, Fast Downward |
| Planners-4 Plan Execution | [SymbolicAI/Planners/02-Classical/Planners-4-Fast-Downward.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/02-Classical/Planners-4-Fast-Downward.ipynb) | Execution et monitoring |
| Planners-5 Replanning | [SymbolicAI/Planners/02-Classical/Planners-5-Heuristics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/02-Classical/Planners-5-Heuristics.ipynb) | Re-planification en ligne |

### References externes
- Helmert, M. (2006). "The Fast Downward Planning System." *Journal of Artificial Intelligence Research*, 26, 191-246. [JAIR](https://jair.org/index.php/jair/article/view/10457)
- Fox, M., & Long, D. (2003). "PDDL2.1: An Extension to PDDL for Expressing Temporal Planning Domains." *Journal of Artificial Intelligence Research*, 20, 61-124. [JAIR](https://jair.org/index.php/jair/article/view/10352)
- Ghallab, M., Nau, D., & Traverso, P. (2016). "Automated Planning and Acting." *Cambridge University Press*. [Cambridge](https://www.cambridge.org/core/books/automated-planning-and-acting/)
- Ingrand, F., & Ghallab, M. (2014). "Robotics and AI: From Deliberation to Action." *IEEE Intelligent Systems*. [IEEE](https://ieeexplore.ieee.org/document/6905390)
- Muise, C., et al. (2012). "Planning Over Disjunctive-Constraint-Based Formulas." *ICAPS*. [AAAI](https://ojs.aaai.org/index.php/ICAPS/article/view/13545)

### Difficulte : 3/5

---

#### D2 — Planification HTN pour jeux video

La planification HTN (Hierarchical Task Network) decompose recursivement une tache de haut niveau (accomplir une quete, fabriquer un objet) en sous-taches de plus en plus fines jusqu'a obtenir des actions primitives executables, suivant une hierarchie de methodes predefinies par le concepteur. Cette approche se distingue de la planification classique (STRIPS/PDDL) par sa nature decompositional plutot que compositionnelle : au lieu de chercher une sequence d'actions depuis un etat initial, on decompose une intention en plan concret. Dans le contexte des jeux video, les HTN controlent naturellement le comportement des PNJ (personnages non joueurs) car les game designers specifient les comportements sous forme de hierarchies de taches intuitives. La comparaison avec GOAP (Goal-Oriented Action Planning), qui utilise une recherche en avant depuis l'etat courant, met en lumiere le compromis entre controlabilite par le concepteur (HTN) et autonomie emergente (GOAP).

### Objectifs
- Implementer un planificateur HTN complet avec decomposition recursive, preconditions sur les methodes, et detection d'impossibilite
- Modeliser le comportement de PNJ dans un jeu (quetes, crafting, exploration) sous forme de hierarchies de taches
- Implementer un planificateur GOAP et comparer les plans generes avec l'approche HTN sur les memes scenarios
- Mesurer les performances (temps de planification, qualite des plans, expressivite) des deux approches
- Prototyper une integration dans un moteur de jeu (Unity ou Godot) ou un simulateur 2D minimal

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Planners-9 HTN | [SymbolicAI/Planners/03-Advanced/Planners-9-HTN.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/03-Advanced/Planners-9-HTN.ipynb) | Planification HTN |
| Planners-1 Introduction | [SymbolicAI/Planners/01-Foundation/Planners-1-Introduction.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/01-Foundation/Planners-1-Introduction.ipynb) | Fondamentaux planification |
| Planners-6 GOAP | [SymbolicAI/Planners/02-Classical/Planners-6-Domains.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/02-Classical/Planners-6-Domains.ipynb) | Goal-Oriented Action Planning |

### References externes
- Erol, K., Hendler, J., & Nau, D. (1994). "Complexity Results for HTN Planning." *Annals of Mathematics and Artificial Intelligence*, 18(1), 69-93. [Springer](https://doi.org/10.1007/BF01531470)
- Orkin, J. (2004). "Applying Goal-Oriented Action Planning to Games." *AI Game Programming Wisdom 2*. [GDC Vault](https://www.gdcvault.com/play/1022092/)
- Nau, D., et al. (2003). "SHOP2: An HTN Planning System." *Journal of Artificial Intelligence Research*, 20, 379-404. [JAIR](https://jair.org/index.php/jair/article/view/10373)
- Champandard, A. (2013). "The Mechanics of Influence Arrows: HTN vs. GOAP in Practice." *AiGameDev.com*. [AiGameDev](https://aigamedev.com/)

### Difficulte : 3/5

---

#### D3 — Ordonnancement multi-agent par CSP distribue

L'ordonnancement multi-agent par CSP distribue (DisCSP) modelise un probleme ou plusieurs agents autonomes (drones, robots collaboratifs, vehicules) doivent coordonner leurs horaires et leurs ressources sans centralisateur, chaque agent ne connaissant que ses propres contraintes et un sous-ensemble des variables du probleme global. Les protocoles de resolution distribues tels que ABT (Asynchronous Backtracking) et AWC (Asynchronous Weak-Commitment) permettent aux agents d'echanger des messages pour resoudre les conflits sans partager l'integralite de leur etat interne. La convergence de ces algorithmes depend de la topologie du reseau de contraintes et de la strategie d'ordonnancement des messages. Ce sujet aborde les compromis entre confidentialite (les agents ne revelent pas toutes leurs contraintes), scalabilite (passage a l'echelle avec le nombre d'agents) et optimalite (qualite de la solution distribuee vs. solution centralisee).

### Objectifs
- Modeliser un probleme d'ordonnancement multi-agent (flotte de drones, robots collaboratifs) comme un CSP distribue avec variables et contraintes locales
- Implementer le protocole ABT (Asynchronous Backtracking) avec gestion des nogoods et detection de cycles
- Implementer le protocole AWC (Asynchronous Weak-Commitment) et comparer la vitesse de convergence avec ABT
- Etudier la scalabilite en faisant varier le nombre d'agents, la densite des contraintes inter-agents et la taille des domaines
- Evaluer le ratio qualite/cout de communication par rapport a une resolution centralisee (OR-Tools CP-SAT)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| CSP-9 Distributed CSP | [Search/Part2-CSP/CSP-9-Distributed.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-9-Distributed.ipynb) | DisCSP, ABT, AWC |
| CSP-4 Scheduling | [Search/Part2-CSP/CSP-4-Scheduling.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-4-Scheduling.ipynb) | Ordonnancement, IntervalVar |
| CSP-1 Fundamentals | [Search/Part2-CSP/CSP-1-Fundamentals.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-1-Fundamentals.ipynb) | Modelisation CSP |

### References externes
- Yokoo, M., et al. (1998). "The Distributed Constraint Satisfaction Problem: Formalization and Algorithms." *IEEE Transactions on Knowledge and Data Engineering*, 10(5), 673-685. [IEEE](https://ieeexplore.ieee.org/document/726791)
- Petcu, A., & Faltings, B. (2005). "DPOP: A Scalable Method for Multiagent Constraint Optimization." *IJCAI*. [IJCAI](https://www.ijcai.org/Proceedings/05/Papers/0646.pdf)
- Yokoo, M. (2001). "Distributed Constraint Satisfaction: Foundations of Cooperation in Multi-Agent Systems." *Springer*. [Springer](https://link.springer.com/book/10.1007/978-3-662-04589-7)
- Modi, P., et al. (2005). "A General Formalization of Distributed Constraint Satisfaction Problem." *AAMAS*. [ACM](https://dl.acm.org/doi/10.1145/1082473.1082712)

### Difficulte : 4/5

---

#### D4 — Planification temporelle pour systemes cyber-physiques

La planification temporelle pour systemes cyber-physiques (CPS) etend la planification classique en ajoutant des durees d'actions, des effets continus (consommation d'energie, temperature) et des contraintes de ressources limitees, formalisees en PDDL 2.1. Les systemes cyber-physiques tels que la gestion d'energie dans un batiment intelligent ou le controle du trafic routier requierent des plans ou les actions se chevauchent temporellement et ou les variables continues evoluent pendant l'execution. Le planificateur temporel (par exemple OPTIC, TEMPO or the temporal mode of Fast Downward) doit produire un schedule qui respecte les fenetres temporelles, les contraintes de capacite des ressources et les invariants continus. L'integration de contraintes de type CSP temporel (STP - Simple Temporal Problem) permet de verifier la consistance du schedule et de calculer les marges temporelles.

### Objectifs
- Modeliser un systeme cyber-physique (gestion d'energie, controle de trafic) en PDDL 2.1 avec actions durees, effets continus et contraintes de ressources
- Utiliser un planificateur temporel pour generer des plans avec actions concurrentes et chevauchement temporel
- Integrer un CSP temporel (STP) pour verifier la consistance du schedule et calculer les marges temporelles
- Implementer la gestion des ressources renouvelables et non-renouvelables avec des profils de consommation variables
- Evaluer sur des scenarios realistes (batiment NZEB, reseau de transport urbain) et comparer avec une approche purement CP-SAT

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Planners-8 Temporal Planning | [SymbolicAI/Planners/03-Advanced/Planners-8-Temporal.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/03-Advanced/Planners-8-Temporal.ipynb) | PDDL 2.1, planification temporelle |
| CSP-8 Temporal CSP | [Search/Part2-CSP/CSP-8-Temporal.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-8-Temporal.ipynb) | STP, consistance temporelle |
| CSP-4 Scheduling | [Search/Part2-CSP/CSP-4-Scheduling.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-4-Scheduling.ipynb) | Ordonnancement, ressources |
| Planners-3 State-Space Search | [SymbolicAI/Planners/01-Foundation/Planners-3-State-Space.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/01-Foundation/Planners-3-State-Space.ipynb) | Heuristiques de planification |

### References externes
- Fox, M., & Long, D. (2003). "PDDL2.1: An Extension to PDDL for Expressing Temporal Planning Domains." *Journal of Artificial Intelligence Research*, 20, 61-124. [JAIR](https://jair.org/index.php/jair/article/view/10352)
- Cesta, A., et al. (2002). "Planning and Scheduling: The State of the Art." *AI Magazine*, 23(2), 59-76. [AAAI](https://ojs.aaai.org/index.php/aimagazine/article/view/1674)
- Dechter, R., Meiri, I., & Pearl, J. (1991). "Temporal Constraint Networks." *Artificial Intelligence*, 49(1-3), 61-95. [Elsevier](https://doi.org/10.1016/0004-3702(91)90006-6)
- Coles, A., et al. (2010). "Forward-Chaining Partial-Order Planning." *ICAPS*. [AAAI](https://ojs.aaai.org/index.php/ICAPS/article/view/13561)
- Benton, J., et al. (2012). "Temporal Planning with Preferences and Time-Dependent Continuous Costs." *ICAPS*. [AAAI](https://ojs.aaai.org/index.php/ICAPS/article/view/13540)

### Difficulte : 4/5

---

---


### Difficulte : 3/5

---

#### D5 — Planification neuro-symbolique certifiee : LLM-heuristiques, Unified Planning et validation formelle de plans

La planification automatique (PDDL) garantit des plans corrects par recherche dans l'espace d'etats, mais peine a passer a l'echelle sur les domaines combinatoires ; les LLM proposent des plans plausibles a faible cout mais sans garantie de correction. Ce sujet de recherche construit un planificateur **neuro-symbolique certifie** : un LLM joue le role d'heuristique (suggestion d'actions, decomposition de buts, generation de macro-operateurs) tandis qu'un planificateur symbolique (Fast Downward, solveurs via Unified Planning) conserve la responsabilite de la correction, et un **validateur formel de plans** (de type VAL) certifie que chaque plan produit atteint reellement le but depuis l'etat initial en respectant preconditions et effets. L'ambition est triple : (1) mesurer le gain effectif des heuristiques LLM sur la vitesse et la qualite des plans ; (2) garantir qu'aucun plan invalide n'est jamais accepte (le neuronal *guide*, le symbolique *decide*, le validateur *certifie*) ; (3) couvrir des extensions difficiles -- planification temporelle, hierarchique (HTN) -- ou la validation formelle est la plus critique.

### Objectifs
1. Mettre en place une chaine PDDL complete (modelisation domaine/probleme, planification via Fast Downward et via Unified Planning) sur au moins deux domaines non triviaux
2. Integrer un LLM comme source d'heuristiques (suggestion d'actions, decomposition de buts, generation de macro-operateurs) et mesurer son impact sur le temps de recherche et la longueur des plans
3. Implementer une **validation formelle systematique** des plans produits (verificateur de type VAL : applicabilite des actions, atteinte du but, respect des contraintes temporelles) -- aucun plan non valide ne doit etre accepte
4. Etendre a la planification temporelle (durees, concurrence) et/ou hierarchique (HTN) et analyser ou la validation formelle devient indispensable
5. Evaluer : taux de plans LLM rejetes par le validateur, gain de performance, robustesse aux hallucinations du LLM, limites de la garantie de correction

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Planners-10 LLM-Planning | [SymbolicAI/Planners/04-NeuroSymbolic/Planners-10-LLM-Planning.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/04-NeuroSymbolic/Planners-10-LLM-Planning.ipynb) | LLM comme heuristique de planification : coeur neuro-symbolique |
| Planners-11 Unified-Planning | [SymbolicAI/Planners/04-NeuroSymbolic/Planners-11-Unified-Planning.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/04-NeuroSymbolic/Planners-11-Unified-Planning.ipynb) | API Unified Planning : abstraction multi-solveurs |
| Planners-12 LOOP | [SymbolicAI/Planners/04-NeuroSymbolic/Planners-12-LOOP.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/04-NeuroSymbolic/Planners-12-LOOP.ipynb) | Boucle d'integration apprentissage / planification |
| Planners-8 Temporal | [SymbolicAI/Planners/03-Advanced/Planners-8-Temporal.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/03-Advanced/Planners-8-Temporal.ipynb) | Planification temporelle (durees, concurrence) : cible de validation |
| Planners-9 HTN | [SymbolicAI/Planners/03-Advanced/Planners-9-HTN.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/03-Advanced/Planners-9-HTN.ipynb) | Planification hierarchique : decomposition de taches |
| Planners-4 Fast-Downward | [SymbolicAI/Planners/02-Classical/Planners-4-Fast-Downward.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/02-Classical/Planners-4-Fast-Downward.ipynb) | Planificateur symbolique de reference : le decideur certifie |

### References externes

**Planification classique et heuristiques**
- Helmert, M. (2006). "The Fast Downward Planning System." *JAIR*, 26. [JAIR](https://www.jair.org/)
- Hoffmann, J. & Nebel, B. (2001). "The FF Planning System." *JAIR*, 14. [JAIR](https://www.jair.org/)
- Ghallab, M., Nau, D. & Traverso, P. (2004). *Automated Planning: Theory and Practice*. Morgan Kaufmann. [Elsevier](https://www.elsevier.com/)

**Validation et extensions (temporel, HTN)**
- Howey, R., Long, D. & Fox, M. (2004). "VAL: Automatic Plan Validation." *ICTAI 2004*. [IEEE](https://ieeexplore.ieee.org/)
- Fox, M. & Long, D. (2003). "PDDL2.1: An Extension to PDDL for Expressing Temporal Planning Domains." *JAIR*, 20. [JAIR](https://www.jair.org/)
- Erol, K., Hendler, J. & Nau, D. (1994). "HTN Planning: Complexity and Expressivity." *AAAI 1994*. [AAAI](https://aaai.org/)
- Micheli, A. et al. (2022). "Unified Planning: A Python Library for AI Planning." [aiplan4eu/unified-planning](https://github.com/aiplan4eu/unified-planning)

**LLM et planification**
- Valmeekam, K. et al. (2023). "On the Planning Abilities of Large Language Models." *NeurIPS 2023*. [proceedings.neurips.cc](https://proceedings.neurips.cc/)
- Liu, B. et al. (2023). "LLM+P: Empowering Large Language Models with Optimal Planning Proficiency." [arXiv:2304.11477](https://arxiv.org/abs/2304.11477)
- Silver, T. et al. (2024). "Generalized Planning in PDDL Domains with Pretrained Large Language Models." *AAAI 2024*. [AAAI](https://aaai.org/)

### Difficulte : 5/5

---

### Categorie E : Theorie des Jeux et Mechanism Design

#### E1 — Comptabilite maximin et equilibres de Nash par programmation lineaire

Le calcul des equilibres de Nash en strategies mixtes pour des jeux bi-matrice repose sur la programmation lineaire et l'algorithme de Lemke-Howson, qui transforme la recherche d'equilibre en un probleme de complementarite lineaire. Le theoreme minimax de von Neumann garantit l'existence d'un equilibre dans tout jeu a somme nulle, et la dualite primal-duale de la programmation lineaire fournit une preuve constructive de ce resultat. L'etudiant implemente le solveur de Lemke-Howson, visualise les polyedres de meilleur reponse dans le simplexe des strategies mixtes, et etudie la complexite du probleme (PPAD-complet pour les jeux bi-matrice generaux). Les applications couvrent la modelisation de conflits economiques, la theorie des encheres et la conception de mecanismes d'incitation. La comparaison avec les solveurs de Nashpy et les methodes de support enumeration permet de valider les resultats et d'apprecier les compromis entre precision et temps de calcul.

### Objectifs
- Implementer l'algorithme de Lemke-Howson en Python et l'appliquer a des jeux bi-matrice 3x3 et 4x4, en visualisant les polyedres de meilleur reponse dans le simplexe
- Prouver le theoreme minimax par la dualite de la programmation lineaire (PuLP/scipy) et comparer avec la formulation directe de Nash
- Etudier la complexite du probleme de l'equilibre de Nash (classe PPAD, reduction a l'equilibre exact vs epsilon-approxime)
- Comparer les performances de Lemke-Howson, du support enumeration (Nashpy) et de l'homotopie sur un benchmark de jeux aleatoires et de jeux classiques (Battle of the Sexes, Chicken, Prisoner's Dilemma)
- Appliquer le calcul d'equilibres a un cas concret : modelisation d'un duel commercial, d'une enchere ou d'un jeu de security (allocation de ressources defensives)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| GT-4 Normal Form | [GameTheory/GameTheory-2-NormalForm.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-2-NormalForm.ipynb) | Jeux en forme normale, matrices de gains |
| GT-5 Nash Equilibria | [GameTheory/GameTheory-4-NashEquilibrium.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-4-NashEquilibrium.ipynb) | Equilibres de Nash, Lemke-Howson |
| GT-4c Zero-Sum/Minimax | [GameTheory/GameTheory-5-ZeroSum-Minimax.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-5-ZeroSum-Minimax.ipynb) | Theoreme minimax, dualite LP |
| GT-4 Nash Equilibrium | [GameTheory/GameTheory-4-NashEquilibrium.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-4-NashEquilibrium.ipynb) | Equilibres de Nash, Lemke-Howson |
| GT-4b Lean Nash Existence | [GameTheory/GameTheory-4b-Lean-NashExistence.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-4b-Lean-NashExistence.ipynb) | Preuve d'existence en Lean 4 |

### References externes
- Nash, J. (1951). "Non-Cooperative Games." *Annals of Mathematics*, 54(2), 286-295. [JSTOR](https://www.jstor.org/stable/1969529)
- Lemke, C.E. & Howson, J.T. (1964). "Equilibrium Points of Bimatrix Games." *SIAM Journal on Applied Mathematics*, 12(2), 413-423. [SIAM](https://epubs.siam.org/doi/10.1137/0112033)
- von Neumann, J. & Morgenstern, O. (1944). *Theory of Games and Economic Behavior*. Princeton University Press.
- Chen, X., Deng, X. & Teng, S.-H. (2009). "Settling the Complexity of Computing Two-Player Nash Equilibria." *Journal of the ACM*, 56(3), 1-57. [ACM](https://dl.acm.org/doi/10.1145/1516512.1516516)
- Nisan, N. et al. (2007). *Algorithmic Game Theory*. Cambridge University Press. [cambridge.org](https://www.cambridge.org/core/books/algorithmic-game-theory/)

### Difficulte : 3/5

---

#### E2 — Encheres combinatoires et allocation de biens publics

Les encheres combinatoires permettent aux participants de soumettre des offres sur des combinaisons d'items plutot que sur des items isoles, capturant ainsi les synergies et les complementarites entre biens. Le mecanisme VCG (Vickrey-Clarke-Groves) constitue le cadre de reference : il est truth-telling (chaque participant a interet a reveler ses vraies valuations), efficient au sens de Pareto (l'allocation maximise la somme des utilites), et individuellement rationnel. Le probleme de la determination du gagnant (winner determination) est NP-difficile dans le cas general, mais se prete bien a une resolution par programmation par contraintes (CP-SAT) ou par programmation lineaire en nombres entiers. L'etudiant implemente le mecanisme VCG complet, etudie les compromis entre expressivite du langage d'offres (OR, XOR, OR-of-XOR) et complexite algorithmique, et analyse les limites du mecanisme (revenus potentiellement faibles, vulnerabilite a la collusion).

### Objectifs
- Implementer le mecanisme d'enchere VCG complet : collecte des offres, resolution du probleme de determination du gagnant par OR-Tools CP-SAT, calcul des paiements Clarke
- Prouver les proprietes du mecanisme (truth-telling, efficacite de Pareto, rationalite individuelle) sur des instances de petite taille en verifiant que declarer ses vraies valuations est toujours une strategie dominante
- Etudier la complexite du winner determination et comparer les performances de CP-SAT, de la PLNE et d'une resolution exacte sur des instances croissantes
- Implementer au moins deux langages d'offres (XOR et OR-of-XOR) et analyser l'impact sur la qualite de l'allocation et le temps de resolution
- Simuler un scenario d'allocation de spectre radio ou de creneaux d'aeroport avec des valuations synthetiques et realistes, et visualiser les resultats d'allocation

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| GT-16 Mechanism Design | [GameTheory/GameTheory-16-MechanismDesign.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-16-MechanismDesign.ipynb) | VCG, encheres, mecanismes d'incitation |
| SocialChoice/04 Aggregation Z3 | [GameTheory/SocialChoice/04-Computational-Aggregation-SAT-Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/04-Computational-Aggregation-SAT-Z3.ipynb) | Verification Z3 des proprietes d'aggregation |
| GT-15b Lean Cooperative | [GameTheory/GameTheory-15b-Lean-CooperativeGames.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-15b-Lean-CooperativeGames.ipynb) | Preuve formelle Lean 4 des proprietes VCG |
| GT-4 Normal Form | [GameTheory/GameTheory-2-NormalForm.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-2-NormalForm.ipynb) | Jeux en forme normale, strategies dominantes |
| CSP-5 Optimization | [Search/Part2-CSP/CSP-5-Optimization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-5-Optimization.ipynb) | Optimisation CP-SAT, probleme du sac a dos |

### References externes
- Vickrey, W. (1961). "Counterspeculation, Auctions, and Competitive Sealed Tenders." *Journal of Finance*, 16(1), 8-37. [JSTOR](https://www.jstor.org/stable/2977633)
- Cramton, P., Shoham, Y. & Steinberg, R. (2006). *Combinatorial Auctions*. MIT Press. [mitpress.mit.edu](https://mitpress.mit.edu/9780262534462/combinatorial-auctions/)
- Clarke, E.H. (1971). "Multipart Pricing of Public Goods." *Public Choice*, 11, 17-33. [Springer](https://link.springer.com/article/10.1007/BF01726210)
- Groves, T. (1973). "Incentives in Teams." *Econometrica*, 41(4), 617-631. [JSTOR](https://www.jstor.org/stable/1914085)
- Nisan, N. (2007). "Introduction to Mechanism Design (for Computer Scientists)." In *Algorithmic Game Theory*, Ch. 9. Cambridge.

### Difficulte : 4/5

---

#### E3 — Jeux cooperatifs et valeur de Shapley

La theorie des jeux cooperatifs s'interesse a la formation de coalitions et a la redistribution equitable des gains collectifs entre les joueurs. La valeur de Shapley (1953) est l'unique concept de partage satisfaisant simultanement quatre axiomes : efficacite (tout le gain est distribue), symetrie (joueurs interchangeables recoivent la meme part), joueur nul (un joueur sans contribution recoit zero) et additivite (linearite sur les jeux). Son calcul exact exige l'enumeration de toutes les permutations des joueurs, soit une complexite O(n!), ce qui motive des approximations par echantillonnage Monte Carlo. Les applications modernes incluent l'explicabilite des modeles de ML (SHAP values), le partage de couts d'infrastructure (aeroports, reseaux), et la valorisation des contributions dans des equipes ou des chaines d'approvisionnement. L'etudiant implemente le calcul exact et approche, verifie les axiomes formellement, et explore les extensions aux jeux convexes ou la valeur est dans le coeur du jeu.

### Objectifs
- Implementer le calcul exact de la valeur de Shapley par enumeration des permutations pour des jeux a petit nombre de joueurs (n <= 12) et la verifier sur des jeux classiques (Gloves, Airport, UN Security Council)
- Implementer l'approximation par echantillonnage Monte Carlo (algorithme de Castro et al.) et analyser la convergence en fonction du nombre d'echantillons
- Verifier formellement les quatre axiomes de Shapley (efficacite, symetrie, joueur nul, additivite) en Python et optionnellement en Lean 4 (PGame/Mathlib)
- Appliquer la valeur de Shapley a un cas concret : partage de couts d'infrastructure, allocation de gains logistiques, ou explicabilite d'un modele de ML (SHAP)
- Etudier les jeux cooperatifs convexes et montrer que dans ce cas la valeur de Shapley appartient au coeur, en visualisant le coeur et les allocations

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| GT-15 Cooperative Games | [GameTheory/GameTheory-15-CooperativeGames.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-15-CooperativeGames.ipynb) | Jeux cooperatifs, valeur de Shapley |
| GT-15b Lean Cooperative | [GameTheory/GameTheory-15b-Lean-CooperativeGames.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-15b-Lean-CooperativeGames.ipynb) | Verification formelle Lean 4 |
| GT-15c Cooperative Python | [GameTheory/GameTheory-15c-CooperativeGames-Python.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-15c-CooperativeGames-Python.ipynb) | Implementation Python, SHAP values |
| GT-4 Normal Form | [GameTheory/GameTheory-2-NormalForm.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-2-NormalForm.ipynb) | Prerequis : jeux en forme normale |

### References externes
- Shapley, L.S. (1953). "A Value for n-Person Games." In *Contributions to the Theory of Games*, vol. 2, 307-317. Princeton. [jstor.org](https://www.jstor.org/stable/1960786)
- Roth, A.E., ed. (1988). *The Shapley Value: Essays in Honor of Lloyd S. Shapley*. Cambridge University Press.
- Castro, J., Gomez, D. & Tejada, J. (2009). "Polynomial Calculation of the Shapley Value Based on Sampling." *Computers & Operations Research*, 36(5), 1726-1730. [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0305054808000814)
- Lundberg, S.M. & Lee, S.-I. (2017). "A Unified Approach to Interpreting Model Predictions." *NeurIPS 2017*. [papers.nips.cc](https://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions)
- Peleg, B. & Sudholter, P. (2007). *Introduction to the Theory of Cooperative Games*. 2nd ed., Springer.

### Difficulte : 3/5

---

#### E4 — Conception de mecanismes resistants a la manipulation

La theorie de la conception de mecanismes (mechanism design) vise a concevoir des regles d'interaction strategique telles que les comportements individuels egoistes conduisent a un resultat collectif desire. Le theoreme de revelation (revelation principle) affirme que tout mecanisme admet un equivalent truth-telling, mais les mecanismes veridiques ne sont pas toujours praticables. Le theoreme de Gibbard-Satterthwaite (1973/1975) montre que toute fonction de choix social non dictatoriale pour au moins 3 alternatives est manipulable. L'etudiant etudie les conditions sous lesquelles on peut contourner ce resultat (domaine de preferences restreint, randomisation, mecanismes approximatifs), implemente des mecanismes classiques (d'Alembert, STV, allocation de biens publics), et prouve formellement leurs proprietes (truth-telling, optimalite de Pareto, rationalite individuelle) par encodage SAT ou SMT avec Z3. Ce sujet fait le pont entre la theorie du choix social et la verification formelle.

### Objectifs
- Implementer et comparer plusieurs mecanismes d'allocation (VCG, mecanisme de d'Alembert, lotteries) et verifier experimentalement leurs proprietes d'incitation sur des instances aleatoires
- Encoder le theoreme de Gibbard-Satterthwaite comme probleme SAT/SMT (nombre fini d'agents et d'alternatives) et utiliser Z3 pour enumerer les fonctions de choix social non manipulables
- Prouver formellement les proprietes d'un mecanisme VCG simplifie en Lean 4 ou Z3 : truth-telling, efficacite de Pareto, rationalite individuelle
- Etudier les mecanismes resistants a la manipulation sur des domaines restreints (preferences single-peaked, single-crossing) et montrer que le theoreme de Gibbard-Satterthwaite ne s'applique plus
- Rediger une analyse comparative des approches de preuve (SAT exhaustive vs. SMT vs. formelle) sur un mecanisme donne, en termes d'expressivite et de passage a l'echelle

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| GT-16 Mechanism Design | [GameTheory/GameTheory-16-MechanismDesign.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-16-MechanismDesign.ipynb) | Conception de mecanismes, VCG |
| GT-16b Social Choice | [GameTheory/SocialChoice/01-Arrow-Impossibility-Theorem.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/01-Arrow-Impossibility-Theorem.ipynb) | Choix social, theoremes d'impossibilite |
| GT-16d Arrow SAT | [GameTheory/SocialChoice/04-Computational-Aggregation-SAT-Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/04-Computational-Aggregation-SAT-Z3.ipynb) | Encodage SAT du theoreme d'Arrow |
| GT-16e Arrow Z3 | [GameTheory/SocialChoice/04-Computational-Aggregation-SAT-Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/04-Computational-Aggregation-SAT-Z3.ipynb) | Encodage SMT (Z3) |
| Arrow SAT (SocialChoice) | [GameTheory/SocialChoice/01-Arrow-Impossibility-Theorem.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/01-Arrow-Impossibility-Theorem.ipynb) | Theoreme d'Arrow par SAT, encoding complet |
| Arrow Lean (SocialChoice) | [GameTheory/SocialChoice/02-Lean-SocialChoice-Formal.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/02-Lean-SocialChoice-Formal.ipynb) | Preuve formelle Lean 4 d'Arrow |
| SocialChoice/04 Aggregation Z3 | [GameTheory/SocialChoice/04-Computational-Aggregation-SAT-Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/04-Computational-Aggregation-SAT-Z3.ipynb) | Verification Z3 des proprietes d'aggregation |

### References externes
- Gibbard, A. (1973). "Manipulation of Voting Schemes: A General Result." *Econometrica*, 41(4), 587-601. [JSTOR](https://www.jstor.org/stable/1914083)
- Satterthwaite, M. (1975). "Strategy-Proofness and Arrow's Conditions." *Journal of Economic Theory*, 10(2), 187-217. [ScienceDirect](https://www.sciencedirect.com/science/article/pii/0022053175900502)
- Nisan, N. et al. (2007). *Algorithmic Game Theory*. Cambridge University Press. Ch. 9-10. [cambridge.org](https://www.cambridge.org/core/books/algorithmic-game-theory/)

#### E5 — Counterfactual Regret Minimization (CFR) et poker IA

CFR is an iterative algorithm that minimizes regret at each information set in extensive-form games with imperfect information. At each iteration, it computes counterfactual values for every action, updates cumulative regrets, and derives a strategy via regret matching. The algorithm converges to a Nash equilibrium in two-player zero-sum games. Applied to poker, CFR (and its variants CFR+) powered the breakthroughs of Libratus (2017, heads-up no-limit Texas Hold'em) and Pluribus (2019, six-player no-limit, Brown & Sandholm, Science/AAAI). The student implements vanilla CFR on Kuhn poker (3-card), scales to Leduc Hold'em, and evaluates against best-response opponents.

### Objectifs
- Implement vanilla CFR on Kuhn poker (3 cards, 2 players) with full game tree enumeration
- Extend to Leduc Hold'em and profile the computational cost (nodes explored, memory, convergence rate)
- Implement CFR+ (alternating updates, linear regret) and compare convergence speed with vanilla CFR
- Build a best-response oracle to measure exploitability of the computed strategies over training iterations
- Analyze the scalability challenges for larger games (abstraction techniques, external sampling MCCFR)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| GT-13 Imperfect Info CFR | [GameTheory/GameTheory-13-ImperfectInfo-CFR.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-13-ImperfectInfo-CFR.ipynb) | Information imparfaite, CFR |
| GT-7 Extensive Form | [GameTheory/GameTheory-7-ExtensiveForm.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-7-ExtensiveForm.ipynb) | Jeux sous forme extensive |
| GT-5 Zero-Sum Minimax | [GameTheory/GameTheory-5-ZeroSum-Minimax.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-5-ZeroSum-Minimax.ipynb) | Zero-sum, minimax |
| GT-4b Lean Nash Existence | [GameTheory/GameTheory-4b-Lean-NashExistence.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-4b-Lean-NashExistence.ipynb) | Preuve formelle Lean 4 de l'existence de Nash |
| Tweety-3 Modal Logic | [SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb) | Logique epistemique, information sets comme mondes de Kripke |

### References externes
- Zinkevich, M. et al. (2008). "Regret Minimization in Games with Incomplete Information." *NeurIPS 2007*. [NeurIPS](https://proceedings.neurips.cc/paper/2007/hash/08d98638c5f4bd8614a3ba2c223ab4a0-Abstract.html)
- Brown, N. & Sandholm, T. (2019). "Superhuman AI for Multiplayer Poker." *Science*, 365(6456). [Science](https://doi.org/10.1126/science.aay2400)
- Bowling, M. et al. (2015). "Heads-Up Limit Hold'em Poker Is Solved." *Science*, 347(6218). [Science](https://doi.org/10.1126/science.1259433)
- Burch, N. et al. (2018). "Solving Imperfect-Information Games via Discounted Regret Minimization." *AAAI*. [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/11740)

### Difficulte : 3/5

---

#### E6 — Conception automatisee de mecanismes : optimisation sous incentive-compatibility et verification formelle (SMT/Lean)

Le *mechanism design* est la "theorie des jeux inverse" : au lieu d'analyser un jeu donne, on *concoit* les regles (allocation, paiements) pour qu'un comportement souhaitable emerge a l'equilibre, alors meme que les agents sont strategiques et rationnels. La **conception automatisee de mecanismes** (Automated Mechanism Design, AMD) formule cette conception comme un probleme d'optimisation sous contraintes : maximiser un objectif (revenu, bien-etre social) sous les contraintes d'**incitation a la verite** (incentive-compatibility, IC) et de **participation volontaire** (individual-rationality, IR). Ce sujet combine optimisation et methodes formelles : (1) encoder un probleme d'AMD comme un programme d'optimisation (LP/MILP ou SMT) ; (2) *prouver formellement* que le mecanisme synthetise respecte IC et IR sur tout le domaine des types (et non seulement sur un echantillon), via SMT ou un assistant de preuve (Lean) ; (3) confronter l'approche symbolique aux approches recentes par apprentissage profond (differentiable economics, RegretNet) qui n'offrent que des garanties approximatives. L'enjeu est la *certification* : un mecanisme prouve strategyproof par opposition a un mecanisme empiriquement bon.

### Objectifs
1. Formaliser au moins deux familles de mecanismes (encheres a un bien, allocation de ressources, agregation de preferences bayesiennes) avec leurs proprietes IC et IR
2. Encoder la conception comme un probleme d'optimisation sous contraintes (LP/MILP et/ou SMT) et synthetiser un mecanisme optimal ou quasi-optimal
3. **Prouver formellement** (SMT exhaustif sur le domaine des types, ou preuve Lean) que le mecanisme synthetise est incentive-compatible et individually-rational -- garantie sur *tout* le domaine
4. Comparer a une approche par apprentissage (differentiable economics facon RegretNet) : qualite de l'objectif vs force des garanties (exactes vs approchees)
5. Etudier les jeux bayesiens (types prives, distributions de croyances) et analyser ou la verification formelle reste tractable

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| GameTheory-16 MechanismDesign | [GameTheory/GameTheory-16-MechanismDesign.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-16-MechanismDesign.ipynb) | Conception de mecanismes : VCG, encheres, IC/IR -- coeur du sujet |
| GameTheory-11 BayesianGames | [GameTheory/GameTheory-11-BayesianGames.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-11-BayesianGames.ipynb) | Jeux a information incomplete : types prives et croyances |
| GameTheory-4b Lean-NashExistence | [GameTheory/GameTheory-4b-Lean-NashExistence.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-4b-Lean-NashExistence.ipynb) | Preuve formelle en Lean de proprietes d'equilibre |
| GameTheory-2b Lean-Definitions | [GameTheory/GameTheory-2b-Lean-Definitions.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-2b-Lean-Definitions.ipynb) | Formalisation Lean des concepts de jeux : base de la certification |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Encodage SMT des contraintes IC/IR et synthese du mecanisme |

### References externes

**Conception automatisee de mecanismes**
- Conitzer, V. & Sandholm, T. (2002). "Complexity of Mechanism Design." *UAI 2002*. [arXiv:cs/0205075](https://arxiv.org/abs/cs/0205075)
- Sandholm, T. (2003). "Automated Mechanism Design: A New Application Area for Search Techniques." *CP 2003*. [Springer](https://link.springer.com/)
- Dutting, P. et al. (2019). "Optimal Auctions through Deep Learning." (RegretNet) *ICML 2019*. [PMLR](https://proceedings.mlr.press/)

**Theorie classique du mechanism design**
- Vickrey, W. (1961). "Counterspeculation, Auctions, and Competitive Sealed Tenders." *Journal of Finance*, 16(1). [JSTOR](https://www.jstor.org/)
- Myerson, R. (1981). "Optimal Auction Design." *Mathematics of Operations Research*, 6(1). [INFORMS](https://pubsonline.informs.org/)
- Nisan, N. & Ronen, A. (2001). "Algorithmic Mechanism Design." *Games and Economic Behavior*, 35. [Elsevier](https://www.sciencedirect.com/)
- Harsanyi, J. (1967). "Games with Incomplete Information Played by 'Bayesian' Players." *Management Science*, 14(3). [INFORMS](https://pubsonline.informs.org/)

### Difficulte : 5/5

---

### Categorie F : Smart Contracts et Blockchain Symbolique

#### F1 — Super-optimisation gas Solidity par Max-SMT

La super-optimisation de smart contracts Ethereum consiste a trouver automatiquement la sequence d'instructions EVM (Ethereum Virtual Machine) equivalente a un programme Solidity donne, mais minimisant le cout en gas. Ce probleme se modelise comme un probleme de synthese de programmes sous contraintes d'equivalence fonctionnelle, ou les contraintes sont exprimees en SMT (Satisfiability Modulo Theories). L'outil Souffle ou Z3 permet de verifier l'equivalence entre le programme original et la version optimisee, tandis que l'objectif de minimisation du gas est un probleme d'optimisation Max-SMT. L'EVM offrant un jeu d'instructions reduit mais avec des subtilites semantiques (storage vs memory, opcodes PUSH/DUP/SWAP), l'espace de recherche est combinatoirement explosif mais structurement contraignable. Les approches par echantillonnage de contre-exemples (CEGIS) combinent la generation de tests concretes et le raffinement SMT pour converger vers une solution optimale.

### Objectifs
- Modeliser la super-optimisation EVM comme un probleme Max-SMT avec contraintes d'equivalence et objectif de gas minimum
- Implementer la verification d'equivalence fonctionnelle entre sequences d'instructions avec Z3
- Explorer l'espace des sequences d'instructions equivalentes via echantillonnage et contraintes SMT
- Evaluer sur des snippets Solidity courants (arithmetic operations, storage access, loops)
- Comparer avec les optimiseurs existants (solc --optimize, EOSii)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SC-14 Formal Verification | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb) | Verification formelle Solidity |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Z3 SMT Solver |
| SC-13 Fuzz Testing | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-13-Fuzz-Invariants.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-13-Fuzz-Invariants.ipynb) | Tests et verification |
| SC-7 Solidity Advanced | [SymbolicAI/SmartContracts/02-Solidity-Advanced/SC-7-Token-Standards.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/02-Solidity-Advanced/SC-7-Token-Standards.ipynb) | EVM, gas, opcodes |

### References externes
- Permenev, A., et al. (2020). "VerX: Safety Verification of Smart Contracts." *IEEE S&P*. [IEEE](https://doi.org/10.1109/SP40000.2020.00024)
- So, S., & Oh, H. (2021). "SmarTest: Effectively Hunting Vulnerable Transaction Sequences in Smart Contracts through Call Sequence and Message Feedback." *USENIX Security*. [USENIX](https://www.usenix.org/conference/usenixsecurity21/presentation/so)
- Z3 SMT Solver. [GitHub](https://github.com/Z3Prover/z3)
- Ethereum Yellow Paper: Gas Schedule. [Ethereum](https://ethereum.github.io/yellowpaper/paper.pdf)
- Gast, D. (2021). "The Syntectic Framework for Smart Contract Super-Optimization." [arXiv](https://arxiv.org/abs/2105.09473)

### Difficulte : 4/5

---

#### F2 — Ordonnancement MEV-resistant de transactions on-chain

L'ordonnancement des transactions dans un bloc blockchain est un probleme d'optimisation combinatoire : parmi les transactions en attente (mempool), selectionner et ordonner un sous-ensemble qui maximise les frais collectes par le validateur, sous les contraintes de taille de bloc, de dependances entre transactions (nonce), et de protection contre le MEV (Maximal Extractable Value). Ce probleme combine le Knapsack (selection) et le TSP (ordonnancement) avec des contraintes de precedences specifiques a la blockchain. Les mecanismes de commit-reveal, d'encryption seuil (threshold encryption) et les encheres de blocs (Flashbots) constituent des approches complementaires pour mitigier l'extraction de valeur. Modeliser ce probleme en CP-SAT permet d'explorer systematiquement l'espace des ordonnancements Pareto-optimaux entre revenu du validateur et equite entre utilisateurs.

### Objectifs
- Modeliser la selection et l'ordonnancement de transactions comme un probleme CP-SAT (Knapsack + precedences)
- Implementer les contraintes de taille de bloc, de nonce (ordre des transactions par adresse), et de gas limit
- Ajouter des mecanismes anti-MEV (randomisation partielle, encryption, commit-reveal)
- Evaluer sur des donnees de mempool Ethereum (MEV-Geth logs, Flashbots auctions)
- Comparer les strategies greediest-fee, CP-SAT optimale, et MEV-Boost

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SC-7 Solidity Advanced | [SymbolicAI/SmartContracts/02-Solidity-Advanced/SC-7-Token-Standards.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/02-Solidity-Advanced/SC-7-Token-Standards.ipynb) | Gas, transactions |
| SC-5 DeFi Fundamentals | [SymbolicAI/SmartContracts/02-Solidity-Advanced/SC-8-DeFi-Primitives.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/02-Solidity-Advanced/SC-8-DeFi-Primitives.ipynb) | DeFi, AMM, arbitrage |
| GameTheory/ | [GameTheory/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/GameTheory) | Encheres, strategies |
| CSP-4 Scheduling | [Search/Part2-CSP/CSP-4-Scheduling.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-4-Scheduling.ipynb) | Ordonnancement |

### References externes
- Daian, P., et al. (2020). "Flash Boys 2.0: Frontrunning in Decentralized Exchanges, Miner Extractable Value, and Consensus Instability." *IEEE S&P*. [IEEE](https://ieeexplore.ieee.org/document/9152675)
- Flashbots Research. [writings.flashbots.net](https://writings.flashbots.net/)
- Ethereum Mempool Architecture. [ethereum.org](https://ethereum.org/en/developers/docs/transactions/)
- Quintus, M., et al. (2022). "Fair Sequencing in Blockchain: MEV Resistance." *AFT'22*. [ACM](https://dl.acm.org/doi/10.1145/3559500)

### Difficulte : 3/5

---

#### F3 — Circuits Zero-Knowledge sous contraintes arithmetiques

La synthese de circuits Zero-Knowledge (ZK circuits) consiste a compiler un programme (ou une assertion mathematique) en un circuit arithmetique (R1CS - Rank-1 Constraint System) qui peut etre prouve en zero-knowledge. Le defi est de minimiser le nombre de contraintes (qui determine le temps de preuve et la taille de la preuve) tout en preservant la correction fonctionnelle. Ce probleme d'optimisation se modelise naturellement en CP/SMT : chaque porte du circuit est une contrainte, et l'objectif est de minimiser le nombre de contraintes. Les systemes comme PLONK introduisent des gates custom qui permettent de comprimer plusieurs contraintes R1CS en une seule gate, offrant un compromis entre expressivite et efficacite. Les applications couvrent les range proofs (preuve qu'une valeur est dans un intervalle sans la reveler), les preuves de solvabilite, et les preuves d'identite selective.

### Objectifs
- Modeliser la synthese de circuits ZK comme un probleme d'optimisation sous contraintes d'equivalence avec CP-SAT
- Implementer la generation de contraintes R1CS a partir d'une representation intermediaire
- Optimiser le nombre de contraintes par elimination de sous-expressions communes et selection d'operations
- Evaluer sur des primitives cryptographiques (hash functions, signatures) et des circuits courants
- Comparer avec les compilateurs existants (Circom, Noir, Halo2)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SC-15 Zero-Knowledge Proofs | [SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-15-Zero-Knowledge-Proofs.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-15-Zero-Knowledge-Proofs.ipynb) | Zero-Knowledge Proofs |
| SC-16 Homomorphic Encryption | [SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-16-Homomorphic-Encryption.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-16-Homomorphic-Encryption.ipynb) | Cryptographie avancee |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | SMT solving |
| CSP-1 Fondamentaux | [Search/Part2-CSP/CSP-1-Fundamentals.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-1-Fundamentals.ipynb) | Modelisation CSP |

### References externes
- Ben-Sasson, E., et al. (2018). "Scalable, Transparent, and Post-Quantum Secure Computational Integrity." *IACR Cryptology ePrint Archive*. [ePrint](https://eprint.iacr.org/2018/046)
- Circom Language Documentation. [iden3.io](https://docs.circom.io/)
- Gabizon, A., et al. (2019). "PLONK: Permutations over Lagrange-Bases for Oecumenical Noninteractive Arguments of Knowledge." *ePrint*. [ePrint](https://eprint.iacr.org/2019/953)
- Thaler, J. (2022). "Proofs, Arguments, and Zero-Knowledge." *Foundations and Trends in Privacy and Security*. [Justin Thaler](https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.html)

### Difficulte : 4/5

---

#### F4 — Governance decentralisee et vote quadratique

La gouvernance decentralisee (DAO) pose des problemes de choix social algorithmique : comment agregger les preferences de participants identites de facon equitable, robuste a la manipulation Sybil (creation de fausses identites) et efficiente en gaz on-chain. Le vote quadratique (Quadratic Voting) attribue un budget de credits de vote que chaque participant repartit entre les propositions, avec un cout quadratique (n votes coutent n^2 credits), ce qui permet de reveiller l'intensite des preferences et non seulement leur direction. La formalisation des proprietes de ce mecanisme (resistance Sybil, efficacite allocative, equilibre de Nash) releve de la theorie des mecanismes et de la verification formelle. L'implementation on-chain necessite de modeliser les contraintes de budget, d'eligibilite et de sybil-resistance comme des invariants verifiables dans le smart contract.

### Objectifs
- Modeliser un systeme de vote quadratique comme un mecanisme d'allocation de credits avec contraintes de budget et de sybil-resistance
- Implementer les smart contracts Solidity pour la creation de propositions, l'allocation de credits et le decompte quadratique
- Formaliser et verifier les proprietes du mecanisme (non-manipulabilite, sybil-resistance, efficacite allocative) avec des outils de verification
- Evaluer sur des scenarios de gouvernance simules (distributions de preferences, attaques Sybil, coalitions)
- Comparer avec les mecanismes existants (vote par token, conviction voting, Futarchy)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SC-9 DAO Governance | [SymbolicAI/SmartContracts/02-Solidity-Advanced/SC-9-DAO-Governance.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/02-Solidity-Advanced/SC-9-DAO-Governance.ipynb) | DAO, gouvernance |
| GameTheory/16c-d Social Choice | [GameTheory/SocialChoice/01-Arrow-Impossibility-Theorem.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/01-Arrow-Impossibility-Theorem.ipynb) | Theorie du choix social |
| SC-7 Solidity Advanced | [SymbolicAI/SmartContracts/02-Solidity-Advanced/SC-7-Token-Standards.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/02-Solidity-Advanced/SC-7-Token-Standards.ipynb) | Token standards, ERC-20 |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Verification formelle |

### References externes
- Lalley, S.P., & Weyl, E.G. (2018). "Quadratic Voting: How Mechanism Design Can Radicalize Democracy." *AEA Papers and Proceedings*, 108, 33-37. [AEA](https://www.aeaweb.org/articles?id=10.1257/pandp.20181017)
- Buterin, V., Hitzig, Z., & Weyl, E.G. (2019). "Liberal Radicalism: A Flexible Design for Philanthropic Matching Funds." *Management Science*. [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3243656)
- Posner, E.A., & Weyl, E.G. (2018). "Radical Markets: Uprooting Capitalism and Democracy for a Just Society." *Princeton University Press*. [Princeton](https://press.princeton.edu/books/hardcover/9780691177502/radical-markets)
- Flashbots: MEV and DAO Governance. [Flashbots](https://writings.flashbots.net/writings/on-ethereum-merge-governance/)

### Difficulte : 3/5

---

---

#### F5 — Coffre DeFi verifie de bout en bout : synthese d'invariants, preuve Certora/CVL et execution symbolique

Les pertes liees aux bugs de smart contracts DeFi se chiffrent en milliards ; un contrat est *immuable une fois deploye*, ce qui fait de la verification *avant* deploiement un enjeu critique. Ce sujet de recherche construit un **coffre (vault) DeFi verifie de bout en bout** : un contrat gerant des depots/retraits avec interets, dont on prouve formellement les proprietes de surete sur *toutes* les executions possibles. La chaine combine plusieurs niveaux de garantie : (1) **fuzzing guide par invariants** (Foundry/Echidna) pour decouvrir empiriquement les proprietes et les contre-exemples ; (2) **verification formelle** via un langage de specification (Certora CVL ou equivalent) prouvant des invariants critiques (conservation des fonds, absence de reentrance, monotonie des parts) ; (3) **execution symbolique** (de type ETHBMC/hevm) explorant exhaustivement les chemins jusqu'a une profondeur bornee. L'ambition est de comparer ces methodes (couverture, faux positifs, passage a l'echelle) et de livrer un contrat accompagne de sa specification formelle et de la preuve associee.

### Objectifs
1. Concevoir et implementer un coffre DeFi non trivial (depots/retraits, parts, interets ou strategie de rendement) en Solidity, teste avec Foundry
2. Specifier formellement les proprietes de surete critiques (conservation des fonds, absence de reentrance, monotonie/equite des parts, absence de depassement)
3. Decouvrir et valider les invariants par **fuzzing guide** (invariant testing Foundry / Echidna) et documenter les contre-exemples trouves
4. **Prouver formellement** un sous-ensemble d'invariants via un langage de specification (Certora CVL) et/ou par **execution symbolique** bornee (hevm/ETHBMC)
5. Evaluer comparativement fuzzing vs preuve vs execution symbolique (proprietes couvertes, faux positifs/negatifs, cout) et discuter les limites de chaque methode

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SC-8 DeFi-Primitives | [SymbolicAI/SmartContracts/02-Solidity-Advanced/SC-8-DeFi-Primitives.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/02-Solidity-Advanced/SC-8-DeFi-Primitives.ipynb) | Primitives DeFi (coffres, AMM, prets) : l'objet a verifier |
| SC-12 Foundry-Testing | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-12-Foundry-Testing.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-12-Foundry-Testing.ipynb) | Tests Foundry : base de la validation |
| SC-13 Fuzz-Invariants | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-13-Fuzz-Invariants.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-13-Fuzz-Invariants.ipynb) | Fuzzing guide par invariants : decouverte des proprietes |
| SC-14 Formal Verification | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb) | Specification et preuve formelle des invariants -- coeur du sujet |
| SC-25 Mainnet-Deploy | [SymbolicAI/SmartContracts/06-Real-World/SC-25-Mainnet-Deploy.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/06-Real-World/SC-25-Mainnet-Deploy.ipynb) | Deploiement reel : l'enjeu de l'immuabilite et du pre-audit |

### References externes

**Verification formelle de smart contracts**
- Luu, L. et al. (2016). "Making Smart Contracts Smarter." (Oyente) *CCS 2016*. [ACM Digital Library](https://dl.acm.org/)
- Permenev, A. et al. (2020). "VerX: Safety Verification of Smart Contracts." *IEEE S&P 2020*. [IEEE](https://ieeexplore.ieee.org/)
- Tsankov, P. et al. (2018). "Securify: Practical Security Analysis of Smart Contracts." *CCS 2018*. [ACM Digital Library](https://dl.acm.org/)

**Fuzzing, execution symbolique et outils**
- Grieco, G. et al. (2020). "Echidna: Effective, Usable, and Fast Fuzzing for Smart Contracts." *ISSTA 2020*. [ACM Digital Library](https://dl.acm.org/)
- Frank, J., Aschermann, C. & Holz, T. (2020). "ETHBMC: A Bounded Model Checker for Smart Contracts." *USENIX Security 2020*. [USENIX](https://www.usenix.org/)
- Certora. "The Certora Prover and the Certora Verification Language (CVL)." [Certora docs](https://docs.certora.com/)

### Difficulte : 5/5

---

### Categorie G : Web Semantique et Graphes de Connaissances

#### G1 — Construction et interrogation d'un graphe de connaissances par SPARQL

La construction de graphes de connaissances (Knowledge Graphs, KG) repose sur le modele RDF (Resource Description Framework) pour representer des faits sous forme de triplets (sujet, predicat, objet). Ce sujet propose de construire un KG complet sur un domaine choisi (films, sciences, jeux video) en utilisant les vocabulaires standards (RDFS, SKOS, FOAF), puis de l'enrichir en connectant des sources Linked Data externes telles que DBpedia et Wikidata via des requetes SPARQL federated. L'interrogation du graphe permettra de repondre a des questions complexes combinant donnees locales et distantes, tout en evaluant les compromis entre performance locale et latence reseau. Les etudiants decouvriront les principes fondamentaux du Web Semantique, les patrons de requetes SPARQL avances (OPTIONAL, UNION, FILTER, PROPERTY PATHS), et les enjeux pratiques de l'integration de donnees heterogenes.

### Objectifs
- Concevoir un schema RDF coherent pour un domaine choisi et le peupler avec des donnees structurees
- Maitriser les requetes SPARQL avancees (jointures, filtres, chemins de proprietes, sous-requetes)
- Connecter le KG a des sources Linked Data (DBpedia, Wikidata) via le protocole SPARQL 1.1 Federated Query
- Comparer les performances et la richesse des resultats entre requetes locales, federated et via un endpoint distant
- Evaluer la qualite du graphe (completude, coherence, liens vers les sources externes)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SW-1 Introduction RDF | [SymbolicAI/SemanticWeb/SW-2b-Python-RDFBasics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-2b-Python-RDFBasics.ipynb) | Fondamentaux RDF |
| SW-3 SPARQL Basics | [SymbolicAI/SemanticWeb/SW-4b-Python-SPARQL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-4b-Python-SPARQL.ipynb) | Requetes SPARQL |
| SW-4 SPARQL Advanced | [SymbolicAI/SemanticWeb/SW-4b-Python-SPARQL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-4b-Python-SPARQL.ipynb) | SPARQL federated |
| SW-6 Linked Data | [SymbolicAI/SemanticWeb/SW-5b-Python-LinkedData.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-5b-Python-LinkedData.ipynb) | DBpedia, Wikidata |

### References externes
- Heath, T. & Bizer, C. (2011). "Linked Data: Evolving the Web into a Global Data Space." *Morgan & Claypool Synthesis Lectures*. [Morgan & Claypool](https://doi.org/10.2200/S00334ED1V01Y201102WBE001)
- Perez, J., et al. (2009). "Semantics and Complexity of SPARQL." *ACM Transactions on Database Systems*, 34(3). [ACM](https://doi.org/10.1145/1567274.1567278)
- DBpedia Project. [DBpedia](https://dbpedia.org/)
- Wikidata Query Service. [Wikidata](https://query.wikidata.org/)
- Schreiber, G. & Raimond, Y. (2014). "RDF 1.1 Primer." *W3C Working Group Note*. [W3C](https://www.w3.org/TR/rdf11-primer/)

### Difficulte : 3/5

---

#### G2 — Raisonnement OWL et verification de coherence d'ontologie

Les ontologies OWL 2 (Web Ontology Language) permettent de definir des connaissances formelles sur un domaine en specifiant des classes, des proprietes et des axiomes logiques dont un reasoner peut tirer des consequences implicites. Ce sujet invite a construire une ontologie OWL 2 sur un domaine riche (bio-informatique, IoT, musique), puis a utiliser un reasoner tel qu'HermiT ou Pellet pour inferrer des hierarchies de classes, detecter des incoherences et verifier la satisfiabilite de l'ontologie. L'etude des profils OWL 2 (EL pour les grandes ontologies taxonomiques, QL pour l'acces aux donnees, RL pour les regles) permettra de comprendre les compromis entre expressivite et complexite algorithmique du raisonnement. Les etudiants apprendront a distinguer les axiomes TBox (terminologiques) des assertions ABox (individus) et a maitriser le cycle de developpement ontologique.

### Objectifs
- Definir une ontologie OWL 2 complete avec classes, hierarchies, proprietes (objet et donnees), et axiomes de restriction
- Utiliser un reasoner OWL (HermiT, Pellet) pour la classification automatique, la detection d'inconsistance et l'inférence de connaissances implicites
- Comparer les profils OWL 2 (EL, QL, RL) en termes d'expressivite et de complexite de raisonnement
- Identifier et corriger les incoherences detectees par le reasoner dans l'ontologie construite
- Documenter les choix de modelisation et les compromis entre expressivite et performance

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SW-7 OWL Ontologies | [SymbolicAI/SemanticWeb/SW-7b-Python-OWL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-7b-Python-OWL.ipynb) | OWL 2, axiomes |
| SW-13 Reasoners | [SymbolicAI/SemanticWeb/SW-13-Python-Reasoners.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-13-Python-Reasoners.ipynb) | HermiT, Pellet |
| SW-2 RDFS | [SymbolicAI/SemanticWeb/SW-6-CSharp-RDFS.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-6-CSharp-RDFS.ipynb) | RDFS, base d'OWL |

### References externes
- Hitzler, P., et al. (2012). "OWL 2 Web Ontology Language Primer." *W3C Recommendation*. [W3C](https://www.w3.org/TR/owl2-primer/)
- Horrocks, I., et al. (2003). "From SHIQ and RDF to OWL: The Making of a Web Ontology Language." *Journal of Web Semantics*, 1(1), 7-26. [Elsevier](https://doi.org/10.1016/j.websem.2003.07.001)
- Baader, F., et al. (2007). *The Description Logic Handbook*. Cambridge University Press, 2nd ed. [Cambridge](https://doi.org/10.1017/CBO9780511711787)
- Glimm, B., et al. (2014). "HermiT: An OWL 2 Reasoner." *Journal of Automated Reasoning*, 53, 245-269. [Springer](https://doi.org/10.1007/s10817-014-9305-1)

### Difficulte : 3/5

---

#### G3 — GraphRAG — combine Knowledge Graphs et LLM pour le RAG

Le GraphRAG (Graph-based Retrieval-Augmented Generation) represente une evolution majeure des systemes RAG en integrant la structure relationnelle des graphes de connaissances avec les capacites de generation des grands modeles de langage. Contrairement au RAG vectoriel classique qui s'appuie uniquement sur la similarite cosinus entre embeddings, le GraphRAG exploite les relations structurelles entre entites pour enrichir le contexte de generation, permettant ainsi de repondre a des questions necessitant du raisonnement multi-sauts. Ce sujet propose d'implementer un pipeline complet : extraction d'entites et de relations a partir de documents, construction du graphe, community detection pour le partitionnement thematique, et requetage combine graphe + LLM. L'evaluation comparative avec un RAG vectoriel classique sur un jeu de donnees de reference (HotpotQA, MuSiQue) mettra en evidence les gains en precision et en coherence des reponses.

### Objectifs
- Implementer un pipeline d'extraction d'entites et de relations depuis des documents textuels vers un graphe RDF ou property graph
- Integrate la structure du graphe dans le processus de retrieval (traversals, community summaries, subgraph extraction)
- Comparer les performances de GraphRAG vs. RAG vectoriel sur un benchmark de QA multi-hop
- Evaluer l'impact du partitionnement en communautes (Leiden, Louvain) sur la qualite des reponses
- Analyser les compromis entre cout de construction du graphe, latence de requetage et qualite des reponses

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SW-11 Knowledge Graphs | [SymbolicAI/SemanticWeb/SW-11-Python-KnowledgeGraphs.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-11-Python-KnowledgeGraphs.ipynb) | Construction de KG |
| SW-12 GraphRAG | [SymbolicAI/SemanticWeb/SW-12-Python-GraphRAG.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-12-Python-GraphRAG.ipynb) | Pipeline GraphRAG |
| SW-3 SPARQL Basics | [SymbolicAI/SemanticWeb/SW-4b-Python-SPARQL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-4b-Python-SPARQL.ipynb) | Requetage du graphe |
| Argument Analysis | [SymbolicAI/Argument_Analysis/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis) | Extraction d'arguments |

### References externes
- Edge, D., et al. (2024). "From Local to Global: A Graph RAG Approach to Query-Focused Summarization." *Microsoft Research*. [arXiv](https://arxiv.org/abs/2404.16130)
- Wu, L., et al. (2025). "Neural-Symbolic Reasoning over Knowledge Graphs." *ACM Computing Surveys*. [ACM](https://doi.org/10.1145/3638529)
- Lewis, P., et al. (2020). "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *NeurIPS*. [NeurIPS](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc2694567247b7f-Abstract.html)
- Hogan, A., et al. (2022). "Knowledge Graphs." *ACM Computing Surveys*, 54(4). [ACM](https://doi.org/10.1145/3447772)

### Difficulte : 4/5

---

#### G4 — Validation de donnees par SHACL (Shapes Constraint Language)

SHACL (Shapes Constraint Language) est le standard W3C pour valider des graphes RDF par rapport a des contraintes structurelles appelees "shapes". Contrairement a OWL, qui raisonne sur la coherence logique, SHACL verifie la conformite operationnelle des donnees : cardinalite des proprietes, types attendus, plages de valeurs, motifs reguliers et contraintes sparql-personnalisees. Ce sujet propose de definir un ensemble de shapes SHACL pour valider des donnees RDF issues de sources ouvertes (data.gouv.fr, OpenData), puis de generer des rapports de validation detailles identifiant les violations et leur severite. Les etudiants exploreront les advanced features de SHACL (target classes, property shapes, SPARQL constraints, node shapes) et compareront l'approche declarative SHACL avec les validations procedurales traditionnelles.

### Objectifs
- Definir des shapes SHACL (Node Shapes et Property Shapes) pour contraindre la structure de donnees RDF
- Implementer des contraintes de cardinalite, de type, de plage de valeurs et de motifs reguliers
- Valider des jeux de donnees ouverts (data.gouv.fr, OpenData) et generer des rapports de validation exploitables
- Comparer l'approche SHACL avec les validations procedurales et les schemas XML Schema / JSON Schema
- Explorer les contraintes SPARQL avancees et les fonctions custom de SHACL-SPARQL

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SW-8 SHACL | [SymbolicAI/SemanticWeb/SW-8-Python-SHACL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-8-Python-SHACL.ipynb) | Validation SHACL |
| SW-1 Introduction RDF | [SymbolicAI/SemanticWeb/SW-2b-Python-RDFBasics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-2b-Python-RDFBasics.ipynb) | Donnees RDF |
| SW-3 SPARQL Basics | [SymbolicAI/SemanticWeb/SW-4b-Python-SPARQL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-4b-Python-SPARQL.ipynb) | Contraintes SPARQL |

### References externes
- Knublauch, H. & Kontokostas, D. (2017). "Shapes Constraint Language (SHACL)." *W3C Recommendation*. [W3C](https://www.w3.org/TR/shacl/)
- Krotzsch, M., et al. (2019). "A Comprehensive Formal Description of SHACL." *International Semantic Web Conference (ISWC)*. [Springer](https://doi.org/10.1007/978-3-030-30796-7_16)
- pySHACL Documentation. [RDFLib](https://github.com/RDFLib/pySHACL)
- Radulovic, F., et al. (2018). "Towards the Formalisation of the SHACL Shapes Constraints Language." *Knowledge-Based Systems*. [Elsevier](https://doi.org/10.1016/j.knosys.2018.04.013)

### Difficulte : 3/5

---

#### G5 — Architecture agentique semantique pour le traitement de documents RDF

Le Web Semantique fournit les briques fondamentales (RDF, OWL, SPARQL, SHACL) pour representer, raisonner et interroger des connaissances structurees, mais leur integration dans un pipeline de traitement complet reste un defi architectural. Ce sujet propose de concevoir une architecture multi-agents ou chaque agent est charge d'une operation specifique sur un flux de documents RDF : extraction et transformation (ETL), validation SHACL, enrichissement par raisonnement OWL-RL, partitionnement et requetage SPARQL, et synchronisation avec des sources externes (Linked Data). La coordination entre agents repose sur un graphe de connaissances partagé et des protocoles de communication semantiques. Les etudiants exploiteront les frameworks d'agents symboliques (planners PDDL, orchestration SK) pour gerer le flux de documents a travers les modules.

### Objectifs
- Concevoir une architecture multi-agents avec au minimum 4 agents specialises (extraction RDF, validation SHACL, raisonnement OWL, requetage SPARQL) coordonnes par un agent orchestrateur
- Implementer chaque agent comme un module autonome traitant des documents RDF en entree et produisant des graphes RDF enrichis/valides en sortie
- Definir un protocole de communication entre agents base sur des evenements semantiques (validation reussie, violation detectee, triplet inferre) et un graphe de connaissances partage
- Implementer la planification du flux de traitement via PDDL (ordonnancement des agents en fonction du type de document) ou orchestration par Semantic Kernel
- Evaluer l'architecture sur un corpus de documents RDF heterogenes (data.gouv.fr, DBpedia, Wikidata) et mesurer le debit, la couverture de validation et la qualite du raisonnement

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SW-1 RDF Introduction | [SymbolicAI/SemanticWeb/SW-2b-Python-RDFBasics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-2b-Python-RDFBasics.ipynb) | Bases RDF |
| SW-7b Python OWL | [SymbolicAI/SemanticWeb/SW-7b-Python-OWL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-7b-Python-OWL.ipynb) | Raisonnement OWL en Python |
| SW-8 SHACL | [SymbolicAI/SemanticWeb/SW-8-Python-SHACL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-8-Python-SHACL.ipynb) | Validation SHACL |
| SW-4b Python SPARQL | [SymbolicAI/SemanticWeb/SW-4b-Python-SPARQL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-4b-Python-SPARQL.ipynb) | Requetage SPARQL |
| Planners-1 Intro | [SymbolicAI/Planners/01-Foundation/Planners-1-Introduction.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/01-Foundation/Planners-1-Introduction.ipynb) | Planification, PDDL |
| SW-11 Knowledge Graphs | [SymbolicAI/SemanticWeb/SW-11-Python-KnowledgeGraphs.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-11-Python-KnowledgeGraphs.ipynb) | Graphes de connaissances |

### References externes
- Bizer, C. et al. (2009). "Linked Data — The Story So Far." *International Journal on Semantic Web and Information Systems*, 5(3), 1-22. [IGI Global](https://doi.org/10.4018/jswis.2009081901)
- Horrocks, I. (2008). "Ontologies and the Semantic Web." *Communications of the ACM*, 51(12), 58-67. [ACM](https://dl.acm.org/doi/10.1145/1409360.1409377)
- Wooldridge, M. (2009). *An Introduction to MultiAgent Systems*. 2nd ed., Wiley. [Wiley](https://www.wiley.com/en-us/An+Introduction+to+MultiAgent+Systems-p-9780470519462)
- W3C. "RDF 1.1 Concepts and Abstract Syntax." [w3.org](https://www.w3.org/TR/rdf11-concepts/)

### Difficulte : 3/5

---

#### G6 — GraphRAG verifie : reponses tracees, ancrees dans le graphe et garanties par raisonnement OWL/SHACL

Le RAG (Retrieval-Augmented Generation) classique reduit, sans l'eliminer, l'hallucination des LLM : rien ne garantit que la reponse generee soit *effectivement* impliquee par les documents recuperes. Ce sujet de recherche construit un **GraphRAG verifie** : un systeme de question-reponse ou (1) la connaissance est structuree en **graphe de connaissances** RDF/OWL avec provenance (RDF-star), (2) le LLM recupere un sous-graphe et genere une reponse, et surtout (3) une **couche de verification symbolique** refuse ou signale toute affirmation de la reponse qui n'est pas *entailee* par le graphe (via raisonneur OWL), *valide* au regard des contraintes de schema (SHACL), et *coherente* (consistance ontologique). L'ambition est une garantie d'ancrage (*groundedness*) verifiable formellement, et non plus seulement empirique.

### Objectifs
1. Construire un graphe de connaissances non trivial (RDF/OWL) a partir d'un corpus reel, avec shapes SHACL et tracage de provenance (RDF-star)
2. Implementer un pipeline GraphRAG : recuperation d'un sous-graphe pertinent + generation de la reponse par LLM
3. Concevoir la couche de verification : chaque fait cite dans la reponse doit etre *entaile* par le graphe (raisonneur), *valide* SHACL, et la base doit rester *coherente* (consistance OWL)
4. Rejeter ou signaler explicitement toute affirmation non ancree (garantie anti-hallucination verifiable) avec retour de la provenance
5. Evaluer comparativement vs RAG vectoriel classique sur la factualite, la tracabilite et la coherence

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SW-12 GraphRAG | [SymbolicAI/SemanticWeb/SW-12-Python-GraphRAG.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-12-Python-GraphRAG.ipynb) | GraphRAG : coeur du sujet |
| SW-11 KnowledgeGraphs | [SymbolicAI/SemanticWeb/SW-11-Python-KnowledgeGraphs.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-11-Python-KnowledgeGraphs.ipynb) | Construction du graphe de connaissances |
| SW-13 Reasoners | [SymbolicAI/SemanticWeb/SW-13-Python-Reasoners.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-13-Python-Reasoners.ipynb) | Raisonneurs : entailment et consistance -- verification |
| SW-8 SHACL | [SymbolicAI/SemanticWeb/SW-8-Python-SHACL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-8-Python-SHACL.ipynb) | Validation des donnees par contraintes de forme |
| SW-10 RDF-star | [SymbolicAI/SemanticWeb/SW-10-Python-RDFStar.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-10-Python-RDFStar.ipynb) | RDF-star : tracage de la provenance des faits |
| SW-7b OWL | [SymbolicAI/SemanticWeb/SW-7b-Python-OWL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-7b-Python-OWL.ipynb) | OWL : semantique et consistance de l'ontologie |

### References externes

**GraphRAG et RAG**
- Edge, D. et al. (2024). "From Local to Global: A Graph RAG Approach to Query-Focused Summarization." *arXiv:2404.16130*. [arXiv](https://arxiv.org/abs/2404.16130)
- Lewis, P. et al. (2020). "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *NeurIPS 2020*. [arXiv](https://arxiv.org/abs/2005.11401)
- Peng, B. et al. (2024). "Graph Retrieval-Augmented Generation: A Survey." *arXiv:2408.08921*. [arXiv](https://arxiv.org/abs/2408.08921)

**Web semantique, raisonnement et validation**
- Hogan, A. et al. (2021). "Knowledge Graphs." *ACM Computing Surveys*, 54(4). [ACM Digital Library](https://dl.acm.org/doi/10.1145/3447772)
- W3C (2017). "Shapes Constraint Language (SHACL)." *W3C Recommendation*. [W3C](https://www.w3.org/TR/shacl/)
- W3C (2012). "OWL 2 Web Ontology Language." *W3C Recommendation*. [W3C](https://www.w3.org/TR/owl2-overview/)

### Difficulte : 5/5

---

### Categorie H : Representation des Connaissances et Raisonnement

#### H1 — Systeme de maintenance de verite (JTMS)

Un systeme de maintenance de verite (Truth Maintenance System, TMS) assure la coherence dynamique d'une base de croyances en tracant les dependances entre faits et en propageant les consequences des retractations. La variante JTMS (Justification-based) associe a chaque croyance une justification enregistree ; quand une premisse est retractee, le systeme determine quelles croyances dependantes doivent etre revoquees a leur tour. Ce sujet propose d'implementer un JTMS complet avec detection de contradictions et retropropagation, puis de l'integrer dans un systeme expert simple capable de reevaluer ses conclusions quand ses premisses changent. L'etude comparera les approches JTMS (justification) et ATMS (assumption-based) et analysera la complexite algorithmique de la propagation.

### Objectifs
- Implementer un JTMS complet avec graphe de dependances, justifications et propagation des retractations
- Gerer la detection de contradictions et les mecanismes de retour en arriere (backtracking)
- Integrer le JTMS dans un systeme expert capable de reevaluer dynamiquement ses conclusions
- Comparer l'approche JTMS avec l'ATMS (Assumption-based TMS) en termes d'expressivite et de complexite
- Evaluer les performances de propagation sur des bases de croyances de taille croissante

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-4 Belief Revision | [SymbolicAI/Tweety/Tweety-4-Belief-Revision.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-4-Belief-Revision.ipynb) | AGM, revision de croyances |
| Tweety-1 Propositional | [SymbolicAI/Tweety/Tweety-2-Basic-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-2-Basic-Logics.ipynb) | Logique propositionnelle |
| Lean Tactics | [SymbolicAI/Lean/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/SymbolicAI/Lean) | Preuves formelles |

### References externes
- Doyle, J. (1979). "A Truth Maintenance System." *Artificial Intelligence*, 12(3), 231-272. [Elsevier](https://doi.org/10.1016/0004-3702(79)90008-0)
- de Kleer, J. (1986). "An Assumption-Based TMS." *Artificial Intelligence*, 28(2), 127-162. [Elsevier](https://doi.org/10.1016/0004-3702(86)90080-9)
- de Kleer, J. (1989). "A Comparison of ATMS and CSP Techniques." *IJCAI*. [IJCAI](https://www.ijcai.org/Proceedings/89-1/Papers/069.pdf)
- McAllester, D.A. (1993). "Truth Maintenance." *AAAI Fall Symposium on Knowledge Representation*. [AAAI](https://www.aaai.org/Library/Symposia/Fall/1993/fs93-04-009.php)

### Difficulte : 3/5

---

#### H2 — Ontologies et raisonnement semantique (OWL Reasoning)

Le raisonnement sur les ontologies OWL 2 constitue un pilier de l'intelligence artificielle symbolique en permettant d'extraire automatiquement des connaissances implicites a partir d'un ensemble d'axiomes formels. Ce sujet propose de construire une ontologie complete en utilisant les constructeurs de logiques de description (intersection, union, complement, quantificateurs existentiels et universels) et de verifier comment un reasoner effectue la classification automatique des classes, la detection d'inconsistances et l'inférence de types pour les individus. L'etude comparative entre OWL 2 et la logique de description ALC (Attributive Concept Language with Complements) illustrera les limites de la decidabilite et la necessite des profils OWL restreints. Les etudiants manipuleront l'outil Protige pour l'edition visuelle et Owlready2 pour l'integration programmatique.

### Objectifs
- Construire une ontologie OWL 2 avec des axiomes complexes (equivalences, disjointness, property chains, restrictions qualifiees)
- Utiliser un reasoner (HermiT, Pellet) pour la classification, la detection d'inconsistance et l'inférence de types
- Mapper les constructeurs OWL 2 aux logiques de description correspondantes (ALC et extensions)
- Analyser les limites de decidabilite et l'impact des axiomes expressifs sur la complexite du raisonnement
- Comparer les resultats de raisonnement entre differents reasoners sur une meme ontologie

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SW-7 OWL Ontologies | [SymbolicAI/SemanticWeb/SW-7b-Python-OWL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-7b-Python-OWL.ipynb) | OWL 2, axiomes |
| SW-13 Reasoners | [SymbolicAI/SemanticWeb/SW-13-Python-Reasoners.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-13-Python-Reasoners.ipynb) | HermiT, Pellet |
| Tweety-3 Description Logics | [SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb) | Logiques de description |

### References externes
- Baader, F., et al. (2007). *The Description Logic Handbook*. Cambridge University Press, 2nd ed. [Cambridge](https://doi.org/10.1017/CBO9780511711787)
- Horrocks, I. & Sattler, U. (2005). "A Tableaux Decision Procedure for SHOIQ." *IJCAI*. [IJCAI](https://www.ijcai.org/Proceedings/05/Papers/0328.pdf)
- Hitzler, P., et al. (2012). "OWL 2 Web Ontology Language Primer." *W3C Recommendation*. [W3C](https://www.w3.org/TR/owl2-primer/)
- Glimm, B. & Horrocks, I. (2011). "LUBM and OWL Reasoners." *CEUR Workshop Proceedings*. [CEUR](https://ceur-ws.org/Vol-538/paper2.pdf)

### Difficulte : 3/5

---

#### H3 — Graphes de connaissances et reponse a des questions

La reponse a des questions sur graphes de connaissances (KGQA) consiste a traduire une question en langage naturel en une requete structuree (SPARQL, lambda-DCS ou chemin de raisonnement) executable sur un graphe RDF. Ce sujet aborde le pipeline complet : reconnaissance d'entites nommees (NER) pour identifier les noeuds du graphe, liaison entite-texte (entity linking) pour desambiguiser les mentions, et generation de requetes SPARQL ou de chemins de raisonnement. L'integration d'un LLM pour l'analyse syntaxique et semantique des questions permettra de comparer les approches basees sur des modeles de langage avec les approches symboliques traditionnelles (parsing SPARQL, templates). L'evaluation se fera sur un benchmark KGQA standard (LC-QuAD, WebQuestionsSP) en mesurant la precision de traduction et la correction des reponses.

### Objectifs
- Implementer un pipeline complet de traduction question naturelle vers requete SPARQL ou chemin de raisonnement
- Maitriser les techniques d'entity linking et de desambiguation pour connecter les mentions textuelles aux entites du graphe
- Comparer les approches template-based, neural semantic parsing et LLM-based pour la generation de requetes
- Evaluer sur un benchmark KGQA standard (LC-QuAD, WebQuestionsSP) avec des metriques de precision et de rappel
- Analyser les erreurs recurrentes et les limites de chaque approche sur des questions complexes (multi-hop, aggregees)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SW-11 Knowledge Graphs | [SymbolicAI/SemanticWeb/SW-11-Python-KnowledgeGraphs.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-11-Python-KnowledgeGraphs.ipynb) | KG, requetage |
| SW-12 GraphRAG | [SymbolicAI/SemanticWeb/SW-12-Python-GraphRAG.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-12-Python-GraphRAG.ipynb) | KG + LLM |
| Argument Analysis | [SymbolicAI/Argument_Analysis/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis) | NLP, extraction |
| SW-3 SPARQL Basics | [SymbolicAI/SemanticWeb/SW-4b-Python-SPARQL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-4b-Python-SPARQL.ipynb) | SPARQL |

### References externes
- Lan, Y., et al. (2023). "A Survey on Complex Question Answering over Knowledge Graphs." *ACM Computing Surveys*. [ACM](https://doi.org/10.1145/3556578)
- Unger, C., et al. (2012). "Template-Based Question Answering over RDF Data." *WWW*. [ACM](https://doi.org/10.1145/2187836.2187923)
- Dubey, M., et al. (2019). "LC-QuAD 2.0: A Large Dataset for Complex Question Answering over Wikidata and DBpedia." *ISWC*. [Springer](https://doi.org/10.1007/978-3-030-30793-6_5)
- Yih, W., et al. (2015). "Semantic Parsing via Staged Query Graph Generation." *EMNLP*. [ACL](https://aclanthology.org/D15-1198/)

### Difficulte : 3/5

---

#### H4 — Logique de description et raisonnement sur des domaines medicaux

Les logiques de description (Description Logics, DL) constituent le fondement formel d'OWL et sont utilisees dans le domaine medical pour modeliser des ontologies a grande echelle telles que SNOMED CT (Systematized Nomenclature of Medicine - Clinical Terms). Ce sujet propose de modeliser un sous-domaine medical (diagnostic differentiel, interactions medicamenteuses, contre-indications) en OWL 2 EL, le profil optimise pour le raisonnement en temps polynomial sur de grands graphes de connaissances. L'utilisation du reasoner ELK permettra de verifier la classification hierarchique et de detecter automatiquement des interactions ou des incoherences. L'evaluation de la complexite du raisonnement en fonction du nombre d'axiomes illustrera les compromis pratiques entre expressivite de la modelisation et passage a l'echelle.

### Objectifs
- Modeliser un domaine medical en OWL 2 EL avec classes, proprietes et axiomes de restriction adaptes au profil polynomial
- Utiliser le reasoner ELK pour la classification automatique et la detection d'interactions/contre-indications
- Evaluer la complexite pratique du raisonnement en fonction de la taille de l'ontologie et de la profondeur de la hierarchie
- Comparer le profil EL avec les profils QL et RL sur un meme domaine pour analyser les compromis expressivite/performance
- Documenter les limites de modelisation imposees par le profil EL (pas de negation disjointe, pas de cardinalites)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SW-7 OWL Ontologies | [SymbolicAI/SemanticWeb/SW-7b-Python-OWL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-7b-Python-OWL.ipynb) | OWL 2, modelisation |
| SW-13 Reasoners | [SymbolicAI/SemanticWeb/SW-13-Python-Reasoners.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-13-Python-Reasoners.ipynb) | ELK reasoner |
| Tweety-3 Description Logics | [SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb) | Logiques de description |

### References externes
- Baader, F., et al. (2007). *The Description Logic Handbook*. Cambridge University Press, 2nd ed. [Cambridge](https://doi.org/10.1017/CBO9780511711787)
- Rector, A., et al. (2009). "OWL Ontologies and Clinical Data: Principles and Practice." *Journal of the Royal Society of Medicine*, 102(6), 228-232. [SAGE](https://doi.org/10.1258/jrsm.2009.090103)
- Kazakov, Y., et al. (2014). "The ELK Reasoner: Apex and Horizon." *ORE Workshop*. [CEUR](https://ceur-ws.org/Vol-1207/ore2014_paper_2.pdf)
- SNOMED International. "SNOMED CT." [SNOMED](https://www.snomed.org/)

### Difficulte : 4/5

---

#### H5 — Apprentissage d'ontologies par programmation logique inductive : induction d'axiomes SROIQ verifies par raisonneur DL

La construction manuelle d'ontologies est couteuse et sujette aux erreurs. Ce sujet de recherche s'attaque a l'**apprentissage automatique d'axiomes ontologiques** par **programmation logique inductive** (ILP) : a partir de donnees factuelles (ABox) et de connaissances de fond, induire des axiomes de logique de description (definitions de classes, hierarchies de roles, restrictions) formant une TBox exprimee dans la logique **SROIQ** (le fondement d'OWL 2 DL). Le point central, qui distingue ce sujet d'un apprentissage purement statistique, est la **verification formelle des axiomes appris** par un raisonneur DL : l'ontologie induite doit etre coherente, sans classe insatisfiable, et ne pas produire d'entailments non desires. L'ambition est un cycle apprendre-verifier-raffiner garantissant la qualite logique de l'ontologie produite.

### Objectifs
1. Mettre en oeuvre l'ILP pour induire des axiomes DL (subsomption, restrictions de roles, definitions de classes) a partir d'une ABox et de connaissances de fond
2. Exprimer les axiomes appris en OWL 2 DL (fragment SROIQ)
3. Verifier l'ontologie induite avec un raisonneur DL : consistance globale, classification, absence de classes insatisfiables
4. Detecter le sur-apprentissage et les axiomes spurieux par des tests d'entailment sur donnees retenues (held-out)
5. Evaluer sur un benchmark de graphe de connaissances ; comparer a une ontologie manuelle et a une approche purement statistique

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SL-4 Inductive Logic Programming | [SymbolicAI/SymbolicLearning/SL-4-InductiveLogicProgramming.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SymbolicLearning/SL-4-InductiveLogicProgramming.ipynb) | ILP : coeur de l'induction d'axiomes |
| SL-6 KnowledgeGraphs-ILP | [SymbolicAI/SymbolicLearning/SL-6-KnowledgeGraphs-ILP.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SymbolicLearning/SL-6-KnowledgeGraphs-ILP.ipynb) | ILP applique aux graphes de connaissances |
| SL-2 Knowledge-Based Learning | [SymbolicAI/SymbolicLearning/SL-2-KnowledgeBasedLearning.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SymbolicLearning/SL-2-KnowledgeBasedLearning.ipynb) | Apprentissage avec connaissances de fond |
| SW-7b OWL | [SymbolicAI/SemanticWeb/SW-7b-Python-OWL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-7b-Python-OWL.ipynb) | OWL 2 DL : langage cible des axiomes |
| SW-13 Reasoners | [SymbolicAI/SemanticWeb/SW-13-Python-Reasoners.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-13-Python-Reasoners.ipynb) | Raisonneur DL : verification des axiomes appris |
| SW-6 RDFS | [SymbolicAI/SemanticWeb/SW-6-CSharp-RDFS.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-6-CSharp-RDFS.ipynb) | Schemas RDFS : hierarchies de classes/proprietes |

### References externes

**Programmation logique inductive et apprentissage d'ontologies**
- Muggleton, S. (1991). "Inductive Logic Programming." *New Generation Computing*, 8(4), 295-318. [Springer](https://link.springer.com/article/10.1007/BF03037089)
- Lehmann, J. (2009). "DL-Learner: Learning Concepts in Description Logics." *JMLR*, 10. [JMLR](https://www.jmlr.org/papers/v10/lehmann09a.html)
- Lisi, F.A. & Esposito, F. (2008). "Foundations of Onto-Relational Learning." *ILP 2008*. [Springer](https://link.springer.com/)

**Logiques de description**
- Baader, F. et al. (2017). *An Introduction to Description Logic*. Cambridge University Press. [Cambridge](https://www.cambridge.org/core/books/an-introduction-to-description-logic/)
- Horrocks, I., Kutz, O. & Sattler, U. (2006). "The Even More Irresistible SROIQ." *KR 2006*. [AAAI](https://aaai.org/papers/kr-06-009-the-even-more-irresistible-sroiq/)

### Difficulte : 5/5

---

### Categorie I : Argumentation et Raisonnement Debateur

#### I1 — Analyse et detection de sophismes par apprentissage symbolique

La detection automatique de sophismes (fallacies) dans des textes argumentatifs combine le traitement du langage naturel et le raisonnement symbolique pour identifier des erreurs de raisonnement telles que l'ad hominem, l'epouvantail (straw man), le faux dilemme ou l'appel a l'autorite. Ce sujet propose de construire un pipeline hybride : un LLM realise l'extraction initiale des segments argumentatifs (premisses, conclusions, types d'attaque), puis TweetyProject valide formellement la structure argumentative en la projetant dans un argumentation framework de Dung. L'approche symbolique permet de verifier la coherence logique des arguments detectes et de filtrer les faux positifs du modele neuronal, tandis que le LLM assure la robustesse face a la variabilite linguistique.

### Objectifs
- Construire un pipeline d'extraction d'arguments depuis des textes (premisses, conclusions, relations d'attaque/support)
- Implementer la classification des types de sophismes (ad hominem, straw man, faux dilemme, appel a l'autorite, etc.)
- Valider formellement les structures detectees avec les argumentation frameworks de Dung via TweetyProject
- Evaluer la precision du pipeline sur un corpus annote (ArgMine, US2016) avec metriques standard (F1, precision, rappel)
- Analyser les cas ou l'approche symbolique corrige les erreurs du LLM et inversement

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Agentic-1 Argument Analysis | [SymbolicAI/Argument_Analysis/Argument_Analysis_Agentic-1-informal_agent.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis/Argument_Analysis_Agentic-1-informal_agent.ipynb) | Detection d'arguments |
| Tweety-5 Abstract Argumentation | [SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb) | Frameworks de Dung |
| Agentic-2 Fallacies | [SymbolicAI/Argument_Analysis/Argument_Analysis_Agentic-2-pl_agent.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis/Argument_Analysis_Agentic-2-pl_agent.ipynb) | Classification sophismes |

### References externes
- Habernal, I., et al. (2017). "Argumentation Mining in User-Generated Web Discourse." *Computational Linguistics*, 43(1), 125-179. [MIT Press](https://doi.org/10.1162/COLI_a_00276)
- Dung, P.M. (1995). "On the Acceptability of Arguments and its Fundamental Role in Nonmonotonic Reasoning, Logic Programming, and n-Person Games." *Artificial Intelligence*, 77(2), 321-357. [Elsevier](https://doi.org/10.1016/0004-3702(94)00041-X)
- Visser, J., et al. (2020). "An Argumentation Annotated Corpus of Wikipedia Talk Pages." *COMMA*. [CEUR](https://ceur-ws.org/Vol-2632/paper13.pdf)
- Goffin, L., et al. (2024). "Empirical Study of Argument Mining in Real-World Texts." *ACL*. [ACL](https://aclanthology.org/2024.acl-long.123/)

### Difficulte : 3/5

---

#### I2 — Generation de contre-arguments par raisonnement formel

La generation automatique de contre-arguments a partir d'un argument formalise est un probleme central de l'intelligence artificielle argumentative. Ce sujet propose d'utiliser le formalisme ASPIC+ pour representer des arguments structures avec des regles strictes et defaisables, puis de generer systematiquement des contre-arguments (undercut, rebut, undermine) en identifiant les points d'attaque possibles dans la structure de l'argument original. L'evaluation des extensions de l'argumentation resultante sous les semantiques de Dung (grounded, preferred, stable, complete) permettra de determiner quelles positions sont defendables. L'implementation via TweetyProject assurera la correction formelle des raisonnements et la comparaison des extensions sous differentes semantiques.

### Objectifs
- Formaliser des arguments en ASPIC+ (regles strictes vs. defaisables, knowledge base avec axioms et presumptions)
- Implementer la generation automatique de contre-arguments (undercut, rebut, undermine) a partir d'un argument cible
- Calculer les extensions de l'argumentation resultante sous les semantiques de Dung (grounded, preferred, stable, complete)
- Evaluer la defendabilite des positions initiales face aux contre-arguments generes
- Comparer la richesse des contre-arguments selon le formalisme utilise (ASPIC+ vs. frameworks abstraits)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-6 ASPIC+ | [SymbolicAI/Tweety/Tweety-6-Structured-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-6-Structured-Argumentation.ipynb) | ASPIC+, regles defaisables |
| Tweety-7a Extended Frameworks | [SymbolicAI/Tweety/Tweety-7a-Extended-Frameworks.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-7a-Extended-Frameworks.ipynb) | Extensions, semantiques |
| Tweety-5 Abstract Argumentation | [SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb) | Frameworks de Dung |

### References externes
- Prakken, H. (2010). "An Abstract Framework for Argumentation with Structured Arguments." *Argument & Computation*, 1(2), 93-124. [Taylor & Francis](https://doi.org/10.1080/19462160903564592)
- Besnard, P. & Hunter, A. (2008). *Elements of Argumentation*. MIT Press. [MIT Press](https://mitpress.mit.edu/9780262524619/elements-of-argumentation/)
- Caminada, M. (2006). "On the Issue of Reinstatement in Argumentation." *JELIA*. [Springer](https://doi.org/10.1007/11853886_11)
- Modgil, S. & Prakken, H. (2014). "The ASPIC+ Framework for Structured Argumentation." *Argument & Computation*, 5(1), 1-24. [Taylor & Francis](https://doi.org/10.1080/19462166.2013.876545)

### Difficulte : 3/5

---

#### I3 — Argumentation dialogique multi-agents

L'argumentation dialogique multi-agents modele des echanges argumentatifs entre plusieurs participants, chacun defendant une position initiale, selon des protocoles formels definissant les coups permis (assertion, question, challenge, retrait). Ce sujet propose d'implementer un systeme de dialogue argumentatif inspire des protocols de Parsons et McBurney, ou les agents construisent des arguments, attaquent les positions adverses et mettent a jour leurs croyances au fil du dialogue. L'evaluation portera sur la qualite du consensus atteint (ou l'identification honnete du desaccord), la convergence du dialogue et la capacite des agents a integrer de nouveaux arguments. L'integration de LLM pour la generation naturelle des interventions ajoutera une dimension realiste au systeme.

### Objectifs
- Implementer un protocole de dialogue argumentatif formel (types de coups, regles de tour, conditions de terminaison)
- Developper des agents autonomes capables de construire, evaluer et presenter des arguments strategiquement
- Evaluer la qualite du consensus atteint et la convergence du dialogue selon les strategies des agents
- Comparer les protocols de dialogue (Parsons, McBurney, Walton) en termes d'expressivite et de propriétés formelles
- Integrer un LLM pour generer des interventions en langage naturel a partir des arguments formalises

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-8 Agent Dialogues | [SymbolicAI/Tweety/Tweety-8-Agent-Dialogues.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-8-Agent-Dialogues.ipynb) | Dialogues multi-agents |
| Argument Analysis | [SymbolicAI/Argument_Analysis/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis) | Extraction, NLP |
| Tweety-5 Abstract Argumentation | [SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb) | Semantiques de Dung |

### References externes
- McBurney, P., et al. (2021). "The Eightfold Way of Argumentation." *Argument & Computation*, 12(1), 85-113. [Taylor & Francis](https://doi.org/10.3233/AAC-200906)
- Parsons, S., et al. (2003). "Argumentation-Based Dialogues for Agent Coordination." *Group Decision and Negotiation*, 12(5), 415-439. [Springer](https://doi.org/10.1023/A:1026132909466)
- Prakken, H. (2006). "Formal Systems for Persuasion Dialogue." *Knowledge Engineering Review*, 21(2), 163-188. [Cambridge](https://doi.org/10.1017/S0269888906000933)
- Walton, D. & Krabbe, E. (1995). *Commitment in Dialogue: Basic Concepts of Interpersonal Reasoning*. SUNY Press. [SUNY](https://sunypress.edu/Books/F/Commitment-in-Dialogue)

### Difficulte : 4/5

---

#### I4 — Evaluation automatique de la qualite argumentative

L'evaluation automatique de la qualite d'un texte argumentatif requiert de combiner des criteres formels (coherence logique, completude des premisses, force des inférences, absence de sophismes) avec une analyse linguistique de surface. Ce sujet propose de developper un systeme multi-criteres qui note un texte argumentatif sur plusieurs dimensions : structure organisationnelle (presence d'une these, d'arguments, de contre-arguments), qualite logique (validite des chaines de raisonnement), adequation rhetorique (pertinence des preuves, clarte de l'expression). Un LLM assurera l'analyse de surface et l'extraction des composantes, tandis que TweetyProject validera formellement la coherence logique des relations entre arguments. L'evaluation du systeme se fera par comparaison avec des annotations humaines sur un corpus de reference.

### Objectifs
- Definir une grille d'evaluation multi-criteres de la qualite argumentative (structure, logique, rhetorique, completude)
- Implementer l'extraction automatique des composantes argumentatives (these, arguments, preuves, contre-arguments) via LLM
- Valider formellement la coherence logique des relations entre arguments avec TweetyProject
- Evaluer la correlation entre les scores automatiques et les annotations humaines sur un corpus de reference
- Identifier les dimensions de qualite les plus difficiles a evaluer automatiquement et proposer des ameliorations

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Agentic-1 Argument Detection | [SymbolicAI/Argument_Analysis/Argument_Analysis_Agentic-1-informal_agent.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis/Argument_Analysis_Agentic-1-informal_agent.ipynb) | Detection d'arguments |
| Agentic-2 Fallacy Classification | [SymbolicAI/Argument_Analysis/Argument_Analysis_Agentic-2-pl_agent.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis/Argument_Analysis_Agentic-2-pl_agent.ipynb) | Classification qualite |
| Agentic-3 Argument Quality | [SymbolicAI/Argument_Analysis/Argument_Analysis_Agentic-3-orchestration.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis/Argument_Analysis_Agentic-3-orchestration.ipynb) | Evaluation qualite |
| Tweety-5 Abstract Argumentation | [SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb) | Coherence formelle |

### References externes
- Wachsmuth, H., et al. (2017). "Computational Argumentation Quality Assessment in Natural Language." *EACL*. [ACL](https://aclanthology.org/E17-1018/)
- Persing, I. & Ng, V. (2017). "End-to-End Argumentation Evaluation." *EMNLP*. [ACL](https://aclanthology.org/D17-1211/)
- Toledo, A., et al. (2019). "Automatic Argument Quality Assessment - New Datasets and Methods." *EMNLP*. [ACL](https://aclanthology.org/D19-1464/)
- Lauscher, A., et al. (2020). "Investigating the Role of Argumentation in the Quality of Online Debates." *Computational Argumentation in the Era of LLMs*. [arXiv](https://arxiv.org/abs/2004.13985)

### Difficulte : 3/5

---

#### I5 — Benchmarks ICCMA — solveurs d'argumentation de Dung

La competition ICCMA (International Competition on Computational Models of Argumentation) fournit des benchmarks standardises pour evaluer les solveurs d'argumentation capables de calculer les extensions sous differentes semantiques (grounded, preferred, stable, complete, semi-stable, stage). Ce sujet constitue une introduction ideale a l'argumentation formelle : les etudiants telechargent les graphes d'attaque de la competition, implementent un solveur calculant les extensions, et comparent leurs performances avec les solveurs de la competition (Crustabri, ArgSemSem, Fudge). La visualisation des graphes d'attaque avec networkx et des extensions calculees permettra de developper une intuition geometrique sur les proprietes des semantiques. L'approche progressive (grounded polynomial, puis NP-hard preferred/stable) rend ce sujet accessible meme aux debutants en argumentation formelle.

### Objectifs
- Implementer le calcul des extensions sous les semantiques de Dung (grounded, preferred, stable, complete)
- Telecharger et parser les benchmarks ICCMA (format TGFF/APX) pour evaluer le solveur
- Visualiser les graphes d'attaque et les extensions correspondantes avec networkx
- Comparer les performances du solveur avec les solveurs de la competition (temps, memoire, correction)
- Analyser la complexite algorithmique des differentes semantiques et identifier les cas difficiles

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-5 Abstract Argumentation | [SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb) | Frameworks de Dung |
| Tweety-6 ASPIC+ | [SymbolicAI/Tweety/Tweety-6-Structured-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-6-Structured-Argumentation.ipynb) | Argumentation structuree |
| Tweety-7a Extended Frameworks | [SymbolicAI/Tweety/Tweety-7a-Extended-Frameworks.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-7a-Extended-Frameworks.ipynb) | Semantiques avancees |

### References externes
- Jarvisalo, M., et al. (2023). "ICCMA 2023: 5th International Competition on Computational Models of Argumentation." *AI Journal*. [ICCMA](http://argumentationcompetition.org/2023/)
- Dung, P.M. (1995). "On the Acceptability of Arguments and its Fundamental Role in Nonmonotonic Reasoning." *Artificial Intelligence*, 77(2), 321-357. [Elsevier](https://doi.org/10.1016/0004-3702(94)00041-X)
- Baroni, P., et al. (2011). "On the Computational Complexity of Argumentation Semantics." *AI Magazine*, 32(4), 53-63. [AAAI](https://doi.org/10.1609/aimag.v32i4.2383)
- Cerutti, F., et al. (2017). "A Comparative Study of Argumentation Frameworks for Argument Mining." *COMMA*. [IOS Press](https://doi.org/10.3233/978-1-61499-844-8-153)

### Difficulte : 2/5

---

#### I6 — Argumentation structuree ASPIC+ et logique defaisable (DeLP/ABA)

L'argumentation structuree enrichit les frameworks abstraits de Dung en dotant les arguments d'une structure interne : des premisses, des regles d'inférence strictes (non contestables) et defaisables (revisables). Ce sujet propose d'implementer un systeme complet d'argumentation structuree en utilisant le formalisme ASPIC+ ou DeLP (Defeasible Logic Programming) via TweetyProject, puis de modeliser un debat realiste (recommandation de films, diagnostic medical simplifie) avec arguments, contre-arguments et differents types d'attaques (rebutting, undercutting, undermining). La comparaison des extensions sous differentes semantiques revelera comment le choix de la semantique influence les conclusions acceptables. L'etude des interactions entre regles strictes et defaisables illustrera la puissance de l'argumentation structuree par rapport aux frameworks abstraits.

### Objectifs
- Implementer un systeme d'argumentation structuree ASPIC+ avec regles strictes, regles defaisables et ordre de preference
- Modeliser un debat complet avec generation d'arguments, identification des attaques (rebutting, undercutting, undermining) et calcul des extensions
- Comparer les formalismes ASPIC+, DeLP et ABA sur un meme cas d'etude (puissance expressive, complexite, lisibilite)
- Evaluer l'impact du choix de semantique (grounded, preferred, stable) sur les conclusions acceptees
- Appliquer le systeme a un domaine concret (recommandation, diagnostic) et analyser la coherence des resultats

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-6 ASPIC+ | [SymbolicAI/Tweety/Tweety-6-Structured-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-6-Structured-Argumentation.ipynb) | ASPIC+, DeLP, ABA |
| Tweety-7a Extended Frameworks | [SymbolicAI/Tweety/Tweety-7a-Extended-Frameworks.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-7a-Extended-Frameworks.ipynb) | Extensions, preferences |
| Tweety-5 Abstract Argumentation | [SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb) | Semantiques de Dung |
| Argument Analysis | [SymbolicAI/Argument_Analysis/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis) | Application concrete |

### References externes
- Prakken, H. (2010). "An Abstract Framework for Argumentation with Structured Arguments." *Argument & Computation*, 1(2), 93-124. [Taylor & Francis](https://doi.org/10.1080/19462160903564592)
- Rienstra, T., et al. (2025). "Argumentative Reasoning in ASPIC+ under Incomplete Information." *Journal of Artificial Intelligence Research*. [JAIR](https://www.jair.org/index.php/jair/article/view/12345)
- Garcia, A. & Simari, G. (2004). "Defeasible Logic Programming: An Argumentative Approach." *Theory and Practice of Logic Programming*, 4(1-2), 95-138. [Cambridge](https://doi.org/10.1017/S1471068403001673)
- Toni, F. (2014). "A Tutorial on Assumption-Based Argumentation." *Argument & Computation*, 5(1), 73-98. [Taylor & Francis](https://doi.org/10.1080/19462166.2013.876546)
- Modgil, S. & Prakken, H. (2014). "The ASPIC+ Framework for Structured Argumentation." *Argument & Computation*, 5(1), 1-24. [Taylor & Francis](https://doi.org/10.1080/19462166.2013.876545)

### Difficulte : 3/5

---

---

#### I7 — Du texte au verdict argumentatif certifie : extraction LLM + solveur de Dung avec certificat d'extension verifiable

Analyser un debat en langage naturel pour en tirer un verdict (« quels arguments tiennent ? ») exige de relier deux mondes : l'**informel** (texte, traite par LLM) et le **formel** (cadres d'argumentation de Dung, traites par solveur). Ce sujet de recherche construit un pipeline complet et *certifie* : (1) un agent LLM extrait les arguments et les relations d'attaque d'un texte argumentatif ; (2) on construit le cadre d'argumentation abstrait (AF) et on calcule ses extensions sous plusieurs semantiques (fondee, preferee, stable) ; (3) chaque extension calculee est accompagnee d'un **certificat verifiable independamment** en temps polynomial (sans-conflit, admissibilite) ; (4) le verdict formel est retraduit en justification en langage naturel, avec tracabilite vers le texte source. L'ambition est de rendre l'analyse argumentative a la fois automatisable (LLM) et *digne de confiance* (certification formelle).

### Objectifs
1. Extraire par agent LLM les arguments et la relation d'attaque depuis un texte de debat en langage naturel (sur le modele du pipeline Argument_Analysis)
2. Construire le cadre d'argumentation (AF) de Dung et calculer ses extensions sous plusieurs semantiques
3. Emettre pour chaque extension un certificat verifiable en temps polynomial (sans-conflit, admissibilite, defense)
4. Retraduire le verdict formel en justification en langage naturel, avec provenance vers le texte source
5. Evaluer la fidelite de l'extraction et la correction du solveur sur des benchmarks de type ICCMA et une annotation humaine

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Argument_Analysis 1-informal | [SymbolicAI/Argument_Analysis/Argument_Analysis_Agentic-1-informal_agent.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis/Argument_Analysis_Agentic-1-informal_agent.ipynb) | Extraction informelle des arguments par LLM |
| Argument_Analysis 2-pl_agent | [SymbolicAI/Argument_Analysis/Argument_Analysis_Agentic-2-pl_agent.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis/Argument_Analysis_Agentic-2-pl_agent.ipynb) | Formalisation logique des arguments |
| Argument_Analysis 3-orchestration | [SymbolicAI/Argument_Analysis/Argument_Analysis_Agentic-3-orchestration.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis/Argument_Analysis_Agentic-3-orchestration.ipynb) | Orchestration informel/formel |
| Tweety-5 Abstract Argumentation | [SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb) | Cadres de Dung, semantiques, extensions -- coeur du solveur |
| Tweety-6 Structured Argumentation | [SymbolicAI/Tweety/Tweety-6-Structured-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-6-Structured-Argumentation.ipynb) | Argumentation structuree (du texte aux attaques) |
| Tweety-8 Agent Dialogues | [SymbolicAI/Tweety/Tweety-8-Agent-Dialogues.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-8-Agent-Dialogues.ipynb) | Dialogues argumentatifs entre agents |

### References externes

**Argumentation formelle de Dung**
- Dung, P.M. (1995). "On the Acceptability of Arguments." *Artificial Intelligence*, 77(2), 321-357. [Elsevier](https://doi.org/10.1016/0004-3702(94)00041-X)
- Caminada, M. (2006). "On the Issue of Reinstatement in Argumentation." *JELIA 2006*. [Springer](https://link.springer.com/chapter/10.1007/11853886_11)
- Cerutti, F. et al. (2018). "Foundations of Implementations for Formal Argumentation." *IfCoLog Journal of Logics*. [arXiv](https://arxiv.org/abs/1705.04373)

**Argument mining et evaluation**
- Lawrence, J. & Reed, C. (2020). "Argument Mining: A Survey." *Computational Linguistics*, 45(4). [MIT Press](https://direct.mit.edu/coli/article/45/4/765/93362/)
- Atkinson, K. et al. (2017). "Towards Artificial Argumentation." *AI Magazine*, 38(3). [AAAI](https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/2704)
- ICCMA. "International Competition on Computational Models of Argumentation." [ICCMA](https://argumentationcompetition.org/)

### Difficulte : 5/5

---

### Categorie J : Agents Symboliques et Architecture Cognitive

#### J1 — Systeme multi-agents de resolution de problemes par planification

Concevoir un systeme multi-agents ou chaque agent possede un role specialise (planificateur, executeur, moniteur) et communique par des messages symboliques structurees. Le planificateur genere des plans d'action a l'aide de PDDL ou CP-SAT, l'executeur traduit les actions en operations concretes, et le moniteur detecte les deviations et declenche des replanifications. La coordination repose sur un protocole de communication asynchrone (type messagerie ou blackboard) et la coherence globale est assuree par des mecanismes de consensus distribues. L'evaluation porte sur la robustesse du systeme face aux pannes d'agents et aux environnements dynamiques.

### Objectifs
- Concevoir une architecture multi-agents avec roles distincts et protocole de communication symbolique
- Implementer un planificateur distribue utilisant PDDL ou CP-SAT pour generer des plans coordonnes
- Realiser un moniteur de deviation capable de detecter les echecs et de declencher une replanification
- Evaluer la robustesse du systeme sur des scenarios avec pannes d'agents et environnement dynamique
- Comparer les performances avec une approche centralisee et une approche reactive pure

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Planners-12 LOOP | [SymbolicAI/Planners/04-NeuroSymbolic/Planners-12-LOOP.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/04-NeuroSymbolic/Planners-12-LOOP.ipynb) | Planification, boucle perception-action |
| CSP-9 Distributed | [Search/Part2-CSP/CSP-9-Distributed.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-9-Distributed.ipynb) | CSP distribues, coordination multi-agent |
| Planners-1 StateSpace | [SymbolicAI/Planners/01-Foundation/Planners-3-State-Space.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/01-Foundation/Planners-3-State-Space.ipynb) | Espaces d'etats, planification classique |
| CSP-1 Fundamentals | [Search/Part2-CSP/CSP-1-Fundamentals.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-1-Fundamentals.ipynb) | Modelisation CSP de base |

### References externes
- Wooldridge, M. (2009). *An Introduction to MultiAgent Systems*. Wiley, 2nd ed. [Wiley](https://www.wiley.com/en-us/An+Introduction+to+MultiAgent+Systems%2C+2nd+Edition-p-9780470519462)
- Durfee, E.H. (1999). "Distributed Problem Solving and Planning." *ECSL*. [AAAI](https://aaai.org/)
- Shoham, Y. & Leyton-Brown, K. (2009). *Multiagent Systems: Algorithmic, Game-Theoretic, and Logical Foundations*. Cambridge University Press. [Cambridge](https://www.cambridge.org/core/books/multiagent-systems/)
- Nau, D. et al. (2004). "SHOP2: An HTN Planning System." *JAIR*. [JAIR](https://www.jair.org/index.php/jair/article/view/10357)

### Difficulte : 3/5

---

#### J2 — Agent cognitif hybride (symbolique + subsymbolique)

Implementer un agent cognitif qui combine un module symbolique (regles de production, logique propositionnelle ou du premier ordre) avec un module subsymbolique (reseau de neurones ou LLM) dans une architecture inspiree de SOAR ou ACT-R. Le module symbolique gere le raisonnement deductif et la planification, tandis que le module subsymbolique assure la perception, la reconnaissance de motifs et la generation de langage naturel. L'integration se fait par une interface de traduction bidirectionnelle entre representations symboliques et vectorielles. L'evaluation porte sur des taches mixtes necessitant a la fois raisonnement logique et perception.

### Objectifs
- Implementer une architecture cognitive hybride avec un module symbolique et un module subsymbolique
- Concevoir une interface de traduction bidirectionnelle entre representations symboliques et vectorielles
- Integrer un systeme de regles de production pour le raisonnement deductif et la planification
- Evaluer les performances sur des taches mixtes combinant raisonnement logique et reconnaissance de patrons
- Comparer avec une approche purement symbolique et une approche purement neuronale

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Lean-7 LLM+Symbolique | [SymbolicAI/Lean/Lean-7-LLM-Integration.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-7-LLM-Integration.ipynb) | Integration LLM et raisonnement symbolique |
| Lean-8 NeuroSymbolic | [SymbolicAI/Lean/Lean-8-Agentic-Proving.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-8-Agentic-Proving.ipynb) | Architectures neuro-symboliques |
| Lean-9 Multi-Agents | [SymbolicAI/Lean/Lean-9-SK-Multi-Agents.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-9-SK-Multi-Agents.ipynb) | Agents cognitifs multi-modules |
| Argument Analysis | [SymbolicAI/Argument_Analysis/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis) | Raisonnement argumentatif hybride |

### References externes
- Garcez, A. d'Avila et al. (2024). "Neurosymbolic AI: The 3rd Wave." *Artificial Intelligence Review*. [Springer](https://link.springer.com/article/10.1007/s10462-024-10736-0)
- Kautz, H. (2022). "The Third AI Debate." *KR 2022*. [KR](https://kr.org/KR2022/)
- Laird, J.E. (2012). *The SOAR Cognitive Architecture*. MIT Press. [MIT Press](https://mitpress.mit.edu/9780262122962/the-soar-cognitive-architecture/)
- Anderson, J.R. (2007). *How Can the Human Mind Occur in the Physical Universe?* Oxford University Press. [Oxford](https://academic.oup.com/book/7441)

### Difficulte : 4/5

---

#### J3 — Serveur MCP d'outils d'analyse symbolique

Creer un serveur MCP (Model Context Protocol) exposant des outils d'analyse symbolique (solveur SAT/SMT, verificateur de preuves, reasoner OWL) comme plugins utilisables par un LLM via un protocole standardise. Le serveur encapsule chaque outil symbolique derriere une interface JSON-RPC, gere les sessions et le contexte, et traduit les resultats symboliques en representations exploitables par le modele de langage. L'architecture suit le pattern outil-augmented generation ou le LLM orchestre les appels aux solveurs en fonction du probleme pose. L'evaluation mesure la precision de la chaine LLM-outil-symbolique sur des benchmarks de raisonnement.

### Objectifs
- Implementer un serveur MCP conforme a la specification du Model Context Protocol
- Encapsuler au moins trois outils symboliques (SAT/SMT, verificateur, reasoner) derriere une interface JSON-RPC
- Gerer les sessions, le contexte et la traduction bidirectionnelle entre LLM et outils symboliques
- Evaluer la precision et la robustesse de la chaine LLM-outil sur des benchmarks de raisonnement
- Documenter l'API et fournir des exemples d'utilisation pour chaque outil expose

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Lean-9 SK Multi-Agents | [SymbolicAI/Lean/Lean-9-SK-Multi-Agents.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-9-SK-Multi-Agents.ipynb) | Semantic Kernel, orchestration d'outils |
| CSP-6 LLM+CSP | [Search/Part2-CSP/CSP-6-Hybridization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-6-Hybridization.ipynb) | Integration LLM et solveurs CSP |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Solveur Z3 SMT |
| Planners-10 LLM Planning | [SymbolicAI/Planners/04-NeuroSymbolic/Planners-10-LLM-Planning.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/04-NeuroSymbolic/Planners-10-LLM-Planning.ipynb) | LLM et planification symbolique |

### References externes
- Anthropic (2024). *Model Context Protocol*. [modelcontextprotocol.io](https://modelcontextprotocol.io/)
- Microsoft (2024). *Semantic Kernel*. [GitHub](https://github.com/microsoft/semantic-kernel)
- de Moura, L. & Bjorner, N. (2008). "Z3: An Efficient SMT Solver." *TACAS 2008*. [Springer](https://link.springer.com/chapter/10.1007/978-3-540-78800-3_24)
- Borgeaud, S. & Emerson, G. (2024). "Tool Use with Large Language Models." *Anthropic Research*. [Anthropic](https://www.anthropic.com/research)

### Difficulte : 3/5

---

#### J4 — Integration LLM + solveurs symboliques (LLM-as-a-reasoner)

Implementer un pipeline complet ou un LLM traduit des problemes enoncees en langage naturel en modeles symboliques (SAT, SMT, CSP, PDDL), appelle un solveur approprie, puis interprete les resultats en langage naturel. Le pipeline inclut une etape de validation de la traduction (verification syntaxique et semantique du modele genere) et des strategies de correction automatique lorsque la traduction echoue. L'etude systematique des erreurs de traduction (variables manquantes, contraintes incorrectes, formulation sous-optimale) constitue un livrable central du projet. L'evaluation se fait sur des benchmarks de raisonnement logique et mathematique.

### Objectifs
- Construire un pipeline LLM-to-symbolique avec traduction, resolution et interpretation des resultats
- Implementer une validation automatique de la traduction (syntaxe et semantique du modele symbolique)
- Developper des strategies de re-prompting et de correction pour les traductions erronees
- Realiser une taxonomie systematique des erreurs de traduction LLM vers modeles symboliques
- Evaluer sur des benchmarks de raisonnement (LogicGrid, ProofWriter, GSM8K)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| CSP-6 LLM+CSP | [Search/Part2-CSP/CSP-6-Hybridization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-6-Hybridization.ipynb) | Pipeline LLM vers solveur CSP |
| Planners-10 LLM Planning | [SymbolicAI/Planners/04-NeuroSymbolic/Planners-10-LLM-Planning.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/04-NeuroSymbolic/Planners-10-LLM-Planning.ipynb) | Traduction LLM vers PDDL |
| Planners-12 LOOP | [SymbolicAI/Planners/04-NeuroSymbolic/Planners-12-LOOP.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/04-NeuroSymbolic/Planners-12-LOOP.ipynb) | Boucle observation-planification-action |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Solveur Z3 SMT, traduction de contraintes |

### References externes
- Pan, L. et al. (2023). "Logic-LM: Faithful Logical Reasoning with Large Language Models." *EMNLP 2023*. [ACL Anthology](https://aclanthology.org/2023.emnlp-main..pe/)
- Katz, M. et al. (2024). "Duality in LLM-assisted Planning." *ICAPS 2024*. [AAAI](https://aaai.org/)
- Shunyu, Y. et al. (2023). "ReAct: Synergizing Reasoning and Acting in Language Models." *ICLR 2023*. [OpenReview](https://openreview.net/forum?id=WE_vluYUL-X)
- Gao, L. et al. (2023). "PAL: Program-Aided Language Models." *ICML 2023*. [arXiv](https://arxiv.org/abs/2212.10573)

### Difficulte : 4/5

---

#### J5 — Apprentissage par renforcement multi-agents (MARL) et emergence de cooperation

Multi-Agent Reinforcement Learning (MARL) etend l'apprentissage par renforcement a des environnements ou plusieurs agents apprennent simultanement, chaque agent modifiant la dynamique de l'environnement pour les autres. Les defis centraux sont la non-stationnarite (la politique optimale d'un agent change quand les autres apprennent), l'explosion combinatoire de l'espace joint, et la tension entre exploration individuelle et coordination collective. Les algorithmes classiques (Independent Q-Learning, MADDPG, QMIX, MAPPO) adoptent differentes architectures (centralisee, decentralisee, factored) pour adresser ces defis. L'etudiant implemente des agents sur des environnements de cooperation (Predator-Prey, Level-Based Foraging) et de competition (OpenAI compete), et analyse l'emergence de strategies cooperatives ou d'equilibres competitifs.

### Objectifs
- Implementer Independent Q-Learning et MADDPG (Centralized Training, Decentralized Execution) sur un environnement multi-agent (PettingZoo)
- Evaluer l'impact de la non-stationnarite en comparant l'apprentissage avec et sans parametres partages
- Etudier l'emergence de strategies cooperatives dans Predator-Prey et Level-Based Foraging
- Comparer les architectures factored (QMIX) et policy-gradient (MAPPO) en termes de convergence et de performance
- Analyser les equilibres emergents et les relier aux concepts de la theorie des jeux (Nash, Pareto)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| GT-17 Multi-Agent RL | [GameTheory/GameTheory-17-MultiAgent-RL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-17-MultiAgent-RL.ipynb) | MARL, MADDPG, QMIX |
| RL Multi-Agent | [RL/rl_6_multi_agent_rl.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/RL/rl_6_multi_agent_rl.ipynb) | Reinforcement learning multi-agents |
| GT-11 Bayesian Games | [GameTheory/GameTheory-11-BayesianGames.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-11-BayesianGames.ipynb) | Information asymetrique |

### References externes
- Lowe, R. et al. (2017). "Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments." *NeurIPS 2017*. [NeurIPS](https://proceedings.neurips.cc/paper/2017/hash/68a9750337a418a86fe06c1991a1d64c-Abstract.html)
- Rashid, T. et al. (2018). "QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent RL." *ICML*. [PMLR](http://proceedings.mlr.press/v80/rashid18a.html)
- Yu, C. et al. (2022). "The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games." *NeurIPS 2022*. [NeurIPS](https://proceedings.neurips.cc/paper/2022/)
- Busoniu, L. et al. (2008). "A Comprehensive Survey of Multiagent Reinforcement Learning." *IEEE Trans. SMC Part C*, 38(2). [IEEE](https://ieeexplore.ieee.org/document/4472064)

### Difficulte : 4/5

---

#### J6 — Diagnostic medical multi-paradigme par agents symboliques

Le diagnostic medical est un probleme classique d'IA symbolique qui se prete naturellement a une architecture multi-agents : un agent de recherche parcourt l'espace des diagnostics differentiels (A* sur un graphe de symptomes-maladies), un agent de validation verifie la coherence des hypotheses par rapport aux contraintes cliniques (Z3/SMT), un agent d'optimisation recherche les examens complementaires les plus informatifs (theorie de l'information, gain d'entropie), et un agent de connaissance gere l'ontologie medicale (RDF/OWL sur des bases SNOMED CT ou OpenMRS). Ce sujet propose d'implementer cette architecture en s'appuyant sur les notebooks CaseStudies/Diagnostic-Medical du depot CoursIA qui fournissent un sujet complet avec donnees, solution et templates etudiants.

### Objectifs
- Implementer un agent de diagnostic par recherche heuristique (A* ou best-first) sur un graphe de symptomes-maladies avec donnees medicales synthetiques
- Implementer un agent de validation par contraintes Z3/SMT qui verifie la coherence des hypotheses diagnostiques (incompatibilites medicamenteuses, contre-indications)
- Implementer un agent de selection d'examens par theorie de l'information (maximiser le gain d'entropie sur les diagnostics restants)
- Integrer les agents via une architecture multi-agents coordonnee (blackboard ou message-passing) avec un agent orchestrateur
- Evaluer sur les cas cliniques du CaseStudies/Diagnostic-Medical et comparer avec un diagnostic bayesien naif (Infer.NET)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| CaseStudies Diagnostic | [CaseStudies/Diagnostic-Medical/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/CaseStudies/Diagnostic-Medical/) | Sujet complet avec donnees et solutions |
| Search-3 Informed Search | [Search/Part1-Foundations/Search-3-Informed.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part1-Foundations/Search-3-Informed.ipynb) | Recherche heuristique, A* |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Validation par contraintes SMT |
| Probas Infer-101 | [Probas/Infer-101.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Probas/Infer-101.ipynb) | Diagnostic bayesien |
| Planners-1 Introduction | [SymbolicAI/Planners/01-Foundation/Planners-1-Introduction.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/01-Foundation/Planners-1-Introduction.ipynb) | Planification, PDDL |

### References externes
- Shortliffe, E.H. (1976). *Computer-Based Medical Consultations: MYCIN*. Elsevier. [ScienceDirect](https://doi.org/10.1016/C2013-0-11310-5)
- Pearl, J. (1988). *Probabilistic Reasoning in Intelligent Systems*. Morgan Kaufmann. [Elsevier](https://doi.org/10.1016/C2009-0-27609-4)
- Miller, R.A. et al. (1982). "Internist-1, an Experimental Computer-Based Diagnostic Consultant for General Internal Medicine." *NEJM*, 307(8), 468-476. [NEJM](https://www.nejm.org/doi/full/10.1056/NEJM198208193070803)
- SNOMED CT. [snomed.org](https://www.snomed.org/)
- Reggia, J.A. et al. (1983). "A Formal Model of Diagnostic Inference." *Information Sciences*, 37(1-3), 227-285. [Elsevier](https://doi.org/10.1016/0020-0255(85)90033-7)

### Difficulte : 4/5

---

#### J7 — Architecture cognitive a noyau symbolique verifie : agent LLM pilote par planificateur PDDL et garde-fou (shield) formel

Les agents LLM autonomes sont puissants mais non fiables : rien n'empeche structurellement un LLM de proposer une action dangereuse ou hors-norme. Ce sujet de recherche conçoit une **architecture cognitive hybride** ou le LLM ne decide jamais seul : il *propose*, mais un **noyau symbolique** controle. L'architecture combine (1) le LLM comme generateur de propositions et interface langagiere, (2) un **planificateur PDDL** pour la deliberation et la decomposition de buts, et (3) un **garde-fou (shield) formel** qui filtre chaque action a l'execution selon des contraintes de surete specifiees en logique temporelle (LTL) ou SMT. Le resultat central a prouver : *quelle que soit* la sortie du LLM (meme adversariale), l'agent ne peut pas violer les contraintes de surete. L'ambition est une architecture cognitive ou la garantie de surete est portee par le noyau symbolique, pas par l'esperance d'un bon comportement du LLM.

### Objectifs
1. Concevoir l'architecture : LLM (proposeur) + planificateur PDDL (deliberation) + shield symbolique (filtre de surete) + couche d'outils MCP
2. Specifier les contraintes de surete/normatives en logique temporelle (LTL) ou SMT et les compiler en un shield d'execution
3. Prouver que le shield bloque toute action non sure (l'agent ne peut violer les contraintes meme sous LLM adversarial)
4. Implementer le systeme sur une tache multi-etapes realiste (orchestration de processus, usage d'outils)
5. Evaluer : taux de reussite de la tache, violations de surete (0 attendu avec shield), surcout vs agent non garde

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SK-3 Agents | [GenAI/SemanticKernel/03-SemanticKernel-Agents.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GenAI/SemanticKernel/03-SemanticKernel-Agents.ipynb) | Agents LLM : le proposeur |
| SK-6 Process Framework | [GenAI/SemanticKernel/06-SemanticKernel-ProcessFramework.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GenAI/SemanticKernel/06-SemanticKernel-ProcessFramework.ipynb) | Orchestration de processus multi-etapes |
| SK-8 MCP | [GenAI/SemanticKernel/08-SemanticKernel-MCP.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GenAI/SemanticKernel/08-SemanticKernel-MCP.ipynb) | Couche d'outils symboliques (MCP) |
| Planners-10 LLM-Planning | [SymbolicAI/Planners/04-NeuroSymbolic/Planners-10-LLM-Planning.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/04-NeuroSymbolic/Planners-10-LLM-Planning.ipynb) | Couplage LLM + planification |
| Planners-12 LOOP | [SymbolicAI/Planners/04-NeuroSymbolic/Planners-12-LOOP.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/04-NeuroSymbolic/Planners-12-LOOP.ipynb) | Boucle deliberation/execution |
| Lean-9 SK Multi-Agents | [SymbolicAI/Lean/Lean-9-SK-Multi-Agents.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-9-SK-Multi-Agents.ipynb) | Coordination multi-agents avec noyau formel |

### References externes

**Shielding et surete des agents**
- Alshiekh, M. et al. (2018). "Safe Reinforcement Learning via Shielding." *AAAI 2018*. [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/11797)
- Pnueli, A. (1977). "The Temporal Logic of Programs." *FOCS 1977*. [IEEE](https://ieeexplore.ieee.org/document/4567924)

**LLM, planification et architectures cognitives**
- Kambhampati, S. et al. (2024). "LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks." *ICML 2024*. [arXiv](https://arxiv.org/abs/2402.01817)
- Yang, Z. et al. (2023). "Coupling Large Language Models with Logic Programming for Robust Reasoning." *ACL 2023 Findings*. [arXiv](https://arxiv.org/abs/2307.07696)
- Laird, J.E. (2012). *The Soar Cognitive Architecture*. MIT Press. [MIT Press](https://mitpress.mit.edu/9780262122962/the-soar-cognitive-architecture/)

### Difficulte : 5/5

---

### Categorie K : Cryptographie Symbolique et Securite

#### K1 — Cryptanalyse par contraintes de chiffrements classiques

Modeliser le cassage de chiffrements classiques (Vigenere, Enigma simplifie, Playfair) comme un probleme SAT ou SMT, ou les inconnues sont les elements de la cle et les contraintes encodent les proprietes statistiques du texte clair (frequences des lettres, bigrammes, mots probables). L'approche par contraintes permet de combiner efficacement les indices statistiques avec les contraintes structurelles du chiffrement, surpassant la force brute sur les cles longues. La comparaison avec les attaques par analyse de frequence et par force brute quantitative les gains apportes par la formulation SAT/SMT. L'evaluation se fait sur des textes chiffres de longueur et complexite croissantes.

### Objectifs
- Modeliser le cassage de chiffrements classiques comme un probleme SAT/SMT avec contraintes statistiques
- Implementer les encodages SAT pour Vigenere, Playfair et une version simplifiee d'Enigma
- Integrer des contraintes de frequences de lettres et de bigrammes comme heuristiques de resolution
- Comparer les performances (temps, taux de succes) avec la force brute et l'analyse de frequence
- Evaluer la scalabilite sur des textes de longueur croissante et des cles de complexite variable

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Solveur Z3 SMT, modelisation de contraintes |
| CSP-1 Fundamentals | [Search/Part2-CSP/CSP-1-Fundamentals.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-1-Fundamentals.ipynb) | Modelisation CSP, propagation de contraintes |
| CSP-3 Global Constraints | [Search/Part2-CSP/CSP-3-Advanced.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-3-Advanced.ipynb) | Contraintes globales, table, regex |
| SC-15 Cryptography ZKP | [SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-15-Zero-Knowledge-Proofs.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-15-Zero-Knowledge-Proofs.ipynb) | Cryptographie, preuves formelles |

### References externes
- Bard, G.V. (2009). *Algebraic Cryptanalysis*. Springer. [Springer](https://link.springer.com/book/10.1007/978-0-387-88757-9)
- Moliere, M. (2021). "SAT-based Cryptanalysis of Stream Ciphers." *IACR Cryptology ePrint Archive*. [ePrint](https://eprint.iacr.org/)
- Massacci, F. & Marraro, L. (2000). "Logical Cryptanalysis as a SAT Problem." *Journal of Automated Reasoning*. [Springer](https://link.springer.com/article/10.1023/A:1006326720796)
- Biere, A. et al. (2021). *Handbook of Satisfiability*, 2nd ed. IOS Press. [IOS Press](https://iospress.nl/book/handbook-of-satisfiability-2/)

### Difficulte : 3/5

---

#### K2 — Verification de protocoles cryptographiques par model checking

Modeliser un protocole cryptographique (Needham-Schroeder, Diffie-Hellman, TLS handshake) comme un systeme de transitions dont les etats representent les connaissances de chaque participant et les messages en transit. La verification des proprietes de confidentialite (secrecy) et d'authenticite (authentication) se fait par model checking symbolique avec des outils specialises tels que Tamarin et ProVerif. L'approche permet de decouvrir automatiquement des attaques (replay, man-in-the-middle) en explorant systematiquement l'espace des executions possibles, y compris celles impliquant un intrus actif modelise par le modele Dolev-Yao.

### Objectifs
- Modeliser un protocole cryptographique complet comme un systeme de transitions symboliques
- Exprimer les proprietes de confidentialite et d'authenticite en logique temporelle epistemique
- Utiliser Tamarin ou ProVerif pour la verification automatique et la recherche d'attaques
- Implementer le modele d'intrus Dolev-Yao et analyser les attaques discovertees
- Comparer les resultats et les performances de Tamarin et ProVerif sur le meme protocole

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SC-14 Formal Verification | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb) | Verification formelle, model checking |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | SMT solving, contraintes symboliques |
| SC-7 Solidity Advanced | [SymbolicAI/SmartContracts/02-Solidity-Advanced/SC-7-Token-Standards.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/02-Solidity-Advanced/SC-7-Token-Standards.ipynb) | Protocoles, securite des communications |
| Tweety-5 Argumentation | [SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb) | Raisonnement formel, logique |

### References externes
- Blanchet, B. (2016). "Modeling and Verifying Security Protocols with the Applied Pi Calculus and ProVerif." *Foundations and Trends in Privacy and Security*. [Now Publishers](https://nowpublishers.com/article/Details/PRI-053)
- Meier, S. et al. (2013). "TAMARIN: A Tool for Symbolic Analysis of Security Protocols." *CSF 2013*. [IEEE](https://ieeexplore.ieee.org/document/6635646)
- Dolev, D. & Yao, A. (1983). "On the Security of Public Key Protocols." *IEEE Transactions on Information Theory*. [IEEE](https://ieeexplore.ieee.org/document/1056650)
- Lowe, G. (1996). "Breaking and Fixing the Needham-Schroeder Public-Key Protocol Using FDR." *TACAS 1996*. [Springer](https://link.springer.com/chapter/10.1007/3-540-61042-1_42)

### Difficulte : 4/5

---

#### K3 — Chiffrement homomorphe et calcul sur donnees chiffrees

Implementer des operations arithmetiques de base (addition, multiplication, multiplication par une constante) sur des donnees chiffrees avec un schema de chiffrement homomorphe (BFV pour les entiers, CKKS pour les reels approches). Le defi principal est la gestion du bruit croissant a chaque operation homomorphe, qui limite la profondeur du circuit calculable. L'evaluation mesure le temps de calcul, l'expansion de la taille du chiffre, et la precision residuelle apres un nombre croissant d'operations. L'application pratique porte sur le calcul de statistiques (moyenne, variance) ou l'evaluation d'un modele lineaire sur des donnees sensibles.

### Objectifs
- Implementer les operations homomorphes de base (addition, multiplication) avec BFV ou CKKS via TenSEAL ou SEAL
- Modeliser et tracer la croissance du bruit au fil des operations homomorphes successives
- Evaluer les performances (temps, memoire, precision) pour des circuits de profondeur croissante
- Appliquer le calcul homomorphe a un cas pratique (statistiques sur donnees sensibles, modele lineaire)
- Comparer les schemas BFV (entiers exacts) et CKKS (reels approches) en termes de precision et de performance

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SC-16 Homomorphic Encryption | [SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-16-Homomorphic-Encryption.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-16-Homomorphic-Encryption.ipynb) | Chiffrement homomorphe, BFV, CKKS |
| SC-15 Zero-Knowledge Proofs | [SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-15-Zero-Knowledge-Proofs.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-15-Zero-Knowledge-Proofs.ipynb) | Cryptographie avancee, preuves |
| CSP-5 Optimization | [Search/Part2-CSP/CSP-5-Optimization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-5-Optimization.ipynb) | Optimisation de parametres, deepness |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Raisonnement symbolique sur les entiers |

### References externes
- Gentry, C. (2009). *A Fully Homomorphic Encryption Scheme*. PhD Thesis, Stanford University. [Stanford](https://crypto.stanford.edu/craig/)
- Brakerski, Z. (2012). "Fully Homomorphic Encryption without Modulus Switching." *CRYPTO 2012*. [IACR](https://eprint.iacr.org/2012/078)
- Cheon, J.H. et al. (2017). "Homomorphic Encryption for Arithmetic of Approximate Numbers." *ASIACRYPT 2017*. [IACR](https://eprint.iacr.org/2016/421)
- Microsoft SEAL. [GitHub](https://github.com/microsoft/SEAL)

### Difficulte : 4/5

---

#### K4 — Vote electronique verifiable de bout en bout : chiffrement homomorphe, preuves zero-knowledge et verification symbolique du protocole

Le vote electronique cristallise une tension fondamentale : garantir simultanement le **secret du vote** et la **verifiabilite** du resultat. Ce sujet de recherche construit un systeme de **vote verifiable de bout en bout** (E2E-V) et en verifie formellement les proprietes. Le systeme combine plusieurs primitives cryptographiques : (1) **chiffrement homomorphe** pour calculer le decompte sans dechiffrer les bulletins individuels, (2) **preuves zero-knowledge** attestant qu'un bulletin est bien forme et que le dechiffrement final est correct, sans rien reveler d'autre. Le coeur symbolique du sujet est la **verification formelle du protocole** dans le modele de Dolev-Yao (a la ProVerif/Tamarin) : on prouve symboliquement les proprietes de secret du vote, de verifiabilite individuelle et universelle, et d'eligibilite. L'ambition est de relier l'implementation cryptographique a une garantie de securite *prouvee*, et de discuter l'ecart entre securite symbolique et computationnelle.

### Objectifs
1. Implementer un schema de vote E2E-V : decompte par chiffrement homomorphe + preuves ZK (bonne formation des bulletins, dechiffrement correct)
2. Specifier formellement les proprietes de securite : secret du vote, verifiabilite individuelle et universelle, eligibilite
3. Verifier symboliquement le protocole dans le modele de Dolev-Yao (verificateur de protocoles / model checking)
4. Realiser un prototype (on-chain ou off-chain), mesurer la taille des preuves et le cout de verification
5. Discuter la resistance a la coercition et l'ecart entre modeles de securite symbolique et computationnel

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SC-17 E2E-Verifiable-Voting | [SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-17-E2E-Verifiable-Voting.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-17-E2E-Verifiable-Voting.ipynb) | Vote verifiable de bout en bout -- coeur du sujet |
| SC-15 Zero-Knowledge-Proofs | [SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-15-Zero-Knowledge-Proofs.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-15-Zero-Knowledge-Proofs.ipynb) | Preuves ZK : bonne formation et dechiffrement correct |
| SC-16 Homomorphic-Encryption | [SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-16-Homomorphic-Encryption.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-16-Homomorphic-Encryption.ipynb) | Chiffrement homomorphe : decompte sans dechiffrer |
| SC-9 DAO-Governance | [SymbolicAI/SmartContracts/02-Solidity-Advanced/SC-9-DAO-Governance.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/02-Solidity-Advanced/SC-9-DAO-Governance.ipynb) | Gouvernance on-chain : contexte de deploiement du vote |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Contraintes Z3 : modelisation symbolique des proprietes |

### References externes

**Vote verifiable de bout en bout**
- Adida, B. (2008). "Helios: Web-based Open-Audit Voting." *USENIX Security 2008*. [USENIX](https://www.usenix.org/legacy/event/sec08/tech/full_papers/adida/adida.pdf)
- Cortier, V. et al. (2016). "SoK: Verifiability Notions for E-Voting Protocols." *IEEE S&P 2016*. [IEEE](https://ieeexplore.ieee.org/document/7546530)
- Benaloh, J. (2006). "Simple Verifiable Elections." *USENIX/ACCURATE EVT 2006*. [USENIX](https://www.usenix.org/legacy/event/evt06/tech/full_papers/benaloh/benaloh.pdf)

**Verification symbolique de protocoles et primitives**
- Blanchet, B. (2016). "Modeling and Verifying Security Protocols with the Applied Pi Calculus and ProVerif." *Foundations and Trends in Privacy and Security*. [Inria](https://bblanche.gitlabpages.inria.fr/publications/BlanchetFnTPS16.html)
- Meier, S. et al. (2013). "The TAMARIN Prover for the Symbolic Analysis of Security Protocols." *CAV 2013*. [Springer](https://link.springer.com/chapter/10.1007/978-3-642-39799-8_48)
- Groth, J. (2016). "On the Size of Pairing-based Non-interactive Arguments." *EUROCRYPT 2016*. [Springer](https://link.springer.com/chapter/10.1007/978-3-662-49896-5_11)

### Difficulte : 5/5

---

### Categorie L : Puzzles, Jeux et Problemes Combinatoires

#### L1 — Resolution de Sudoku par multiples solveurs (SAT, CP, LLL)

Implementer et comparer au moins cinq approches de resolution de Sudoku : backtracking avec heuristiques, algorithme Dancing Links de Knuth, programmation par contraintes avec OR-Tools CP-SAT, satisfaction SAT avec PySAT ou Glucose, et algorithme genetique. Chaque approche est evaluee sur une batterie de grilles de difficulte croissante (de 17 indices a grilles avec solutions multiples) en mesurant le temps de resolution, le nombre de noeuds explores et la consommation memoire. L'analyse des complexites theoriques (taille de l'espace de recherche, propagation) complete l'evaluation empirique.

### Objectifs
- Implementer cinq solveurs de Sudoku distincts (backtracking, Dancing Links, CP-SAT, SAT, genetique)
- Construire une batterie de benchmarks avec des grilles de difficulte croissante et des solutions multiples
- Mesurer et comparer les performances (temps, noeuds, memoire) de chaque approche
- Analyser les complexites theoriques et les mecanismes de propagation propres a chaque methode
- Identifier les classes de grilles ou chaque solveur excelle ou echoue

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Sudoku/ | [Sudoku/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Sudoku) | 18 solveurs, 32 notebooks de reference |
| CSP-1 Fundamentals | [Search/Part2-CSP/CSP-1-Fundamentals.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-1-Fundamentals.ipynb) | Modelisation CSP, propagation |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Solveur SMT, encodage de contraintes |
| Search-5 Genetic Algorithms | [Search/Part1-Foundations/Search-5-GeneticAlgorithms.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part1-Foundations/Search-5-GeneticAlgorithms.ipynb) | Algorithme genetique, metaheuristiques |

### References externes
- Knuth, D.E. (2000). "Dancing Links." *Millennial Perspectives in Computer Science*. [CS Faculty Stanford](https://www-cs-faculty.stanford.edu/~knuth/papers/dancing-color.ps.gz)
- Yato, T. & Seta, T. (2002). "Complexity and Completeness of Finding Another Solution." *AAAI 2002*. [AAAI](https://aaai.org/)
- Eén, N. & Sorensson, N. (2003). "An Extensible SAT-solver." *SAT 2003*. [Springer](https://link.springer.com/chapter/10.1007/978-3-540-24605-3_37)
- Simonis, H. (2005). "Sudoku as a SAT Problem." *CP 2005*. [Springer](https://link.springer.com/chapter/10.1007/11564751_6)

### Difficulte : 2/5

---

#### L2 — Generation procedurale par contraintes de niveaux de jeu

Implementer un generateur procedural de niveaux de jeu (plateformes 2D, donjons, cartes strategiques) base sur des contraintes CP-SAT ou l'algorithme Wave Function Collapse (WFC). Les contraintes de jouabilite (accessibilite du depart a l'arrivee, difficulte progressive, absence de zones bloquees) et esthetiques (symetrie, variete, densite) sont encodees dans le modele. Le generateur produit des niveaux diversifies en faisant varier les parametres de contraintes ou la graine aleatoire. L'evaluation combine des metriques automatiques (connectivite, longueur du chemin) et une evaluation qualitative par des joueurs humains.

### Objectifs
- Modeliser la generation de niveaux comme un probleme de satisfaction de contraintes avec CP-SAT ou WFC
- Implementer les contraintes de jouabilite (accessibilite, difficulte progressive, absence de blocage)
- Ajouter des contraintes esthetiques (symetrie, variete thematique, densite d'elements)
- Generer des niveaux diversifies par variation des parametres et des graines aleatoires
- Evaluer quantitativement (connectivite, longueur) et qualitativement (joueurs humains) les niveaux produits

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| CSP-3 Global Constraints | [Search/Part2-CSP/CSP-3-Advanced.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-3-Advanced.ipynb) | Contraintes globales, table, patterns |
| CSP-1 Fundamentals | [Search/Part2-CSP/CSP-1-Fundamentals.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-1-Fundamentals.ipynb) | Modelisation CSP de base |
| Sudoku/ | [Sudoku/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Sudoku) | Grilles, contraintes de placement |
| CSP-5 Optimization | [Search/Part2-CSP/CSP-5-Optimization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-5-Optimization.ipynb) | Optimisation multi-objectifs |

### References externes
- Karth, I. & Smith, A.M. (2017). "WaveFunctionCollapse is Constraint Solving in the Wild." *FDG 2017*. [ACM](https://dl.acm.org/doi/10.1145/3102071.3110566)
- Togelius, J. et al. (2011). "Search-Based Procedural Content Generation." *IEEE TCIAIG*. [IEEE](https://ieeexplore.ieee.org/document/5662419)
- Shaker, N. et al. (2016). *Procedural Content Generation in Games*. Springer. [Springer](https://link.springer.com/book/10.1007/978-3-319-42716-4)
- Smith, A.M. & Mateas, M. (2011). "Answer Set Programming for Procedural Content Generation." *IEEE T-CIAIG*. [IEEE](https://ieeexplore.ieee.org/document/5662423)

### Difficulte : 3/5

---

#### L3 — Resolution de jeux combinatoires par minimax et alpha-beta symbolique

Implementer un joueur artificiel pour un jeu combinatoire a information complete (Connect Four, Othello, ou Hex) utilisant l'algorithme minimax avec elagage alpha-beta, une fonction d'evaluation heuristique et des tables de transposition. La comparaison avec un joueur Monte Carlo Tree Search (MCTS) et un joueur par reseau de neurones (DQN) met en lumiere les forces et limites respectives de chaque approche sur differents horizons de reflexion. L'organisation d'un tournoi round-robin entre toutes les implementations fournit une evaluation empirique rigoureuse. L'analyse des parties permet d'identifier les situations ou chaque methode excelle.

### Objectifs
- Implementer minimax avec elagage alpha-beta, fonction d'evaluation et tables de transposition
- Implementer un joueur MCTS avec politique UCB1 pour la selection
- Implementer ou integrer un joueur DQN comme approche par apprentissage
- Organiser un tournoi round-robin avec mesure du temps de reflexion et de la qualite des coups
- Analyser les forces et faiblesses de chaque approche selon le type de position et la profondeur

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Search-6 Adversarial | [Search/Part1-Foundations/Search-6-AdversarialSearch.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part1-Foundations/Search-6-AdversarialSearch.ipynb) | Minimax, alpha-beta, jeux a somme nulle |
| Search-7 MCTS | [Search/Part1-Foundations/Search-7-MCTS-And-Beyond.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part1-Foundations/Search-7-MCTS-And-Beyond.ipynb) | Monte Carlo Tree Search |
| App-12 Connect Four | [Search/Applications/Search/App-12-ConnectFour.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Applications/Search/App-12-ConnectFour.ipynb) | Application Connect Four |
| App-14 Connect Four RL | [Search/Applications/Search/App-14-ConnectFour-Adversarial.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Applications/Search/App-14-ConnectFour-Adversarial.ipynb) | Reinforcement Learning sur Connect Four |
| GT-8 Combinatorial Games | [GameTheory/GameTheory-8-CombinatorialGames.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-8-CombinatorialGames.ipynb) | Theorie des jeux combinatoires |
| GT-8b Lean Combinatorial | [GameTheory/GameTheory-8b-Lean-CombinatorialGames.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-8b-Lean-CombinatorialGames.ipynb) | Preuves formelles Lean |
| GT-8c Combinatorial Python | [GameTheory/GameTheory-8c-CombinatorialGames-Python.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-8c-CombinatorialGames-Python.ipynb) | Implementation Python

### References externes
- Knuth, D.E. & Moore, R.W. (1975). "An Analysis of Alpha-Beta Pruning." *Artificial Intelligence*. [Elsevier](https://www.sciencedirect.com/science/article/pii/S0004370275800113)
- Browne, C. et al. (2012). "A Survey of Monte Carlo Tree Search Methods." *IEEE TCIAIG*. [IEEE](https://ieeexplore.ieee.org/document/6145622)
- Silver, D. et al. (2016). "Mastering the Game of Go with Deep Neural Networks and Tree Search." *Nature*. [Nature](https://www.nature.com/articles/nature16961)
- van den Herik, H.J. et al. (2002). "Games, Computers, and Artificial Intelligence." *Artificial Intelligence*. [Elsevier](https://www.sciencedirect.com/science/article/pii/S0004370202000877)

### Difficulte : 3/5

---

#### L4 — Benchmark cross-paradigme de solveurs de jeux (Sudoku, Connect Four, Wordle)

Constituer un benchmark unifie comparant 17 paradigmes de solveurs Sudoku (SAT, CSP, CP-SAT, Dancing Links, DWave quantum, Genetic Algorithm, etc. — 34 notebooks C# et Python), 8 algorithmes de jeu Connect Four (minimax, alpha-beta, MCTS, expectimax, reseau de neurones) et des solveurs Wordle (elimination bayesienne, entropie maximale, CSP). L'objectif est de mesurer systematiquement les performances (temps CPU, nombre d'explorations, taux de succes) de chaque paradigme sur une grille commune d'instances (facile a diabolique pour Sudoku, profondeur 1-10 pour Connect Four, longueurs 5-8 pour Wordle). Les notebooks CoursIA offrent 34 notebooks Sudoku (17 paradigmes en C# et Python) et 8 algorithmes Connect Four prets a l'emploi, permettant de se concentrer sur l'analyse comparative plutot que sur l'implementation.

### Objectifs
1. Instrumenter les solveurs Sudoku existants (17 paradigmes dans `Sudoku/`) avec des métriques unifiées (temps, nœuds explorés, mémoire)
2. Étendre le benchmark à Connect Four (8 IA dans `Search/Applications/Hybrid/`) et Wordle en définissant des instances de difficulté croissante
3. Produire un tableau comparatif et des visualisations (heatmaps, scatter plots temps vs. difficulté) par paradigme
4. Analyser les points forts structurels de chaque paradigme (SAT pour la décision, CP pour l'optimisation sous contraintes, MCTS pour les jeux à information incomplète)
5. Proposer un guide de sélection du paradigme optimal en fonction de la classe de problème

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Sudoku/ (34 notebooks) | [Sudoku/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Sudoku) | 17 paradigmes (C# et Python), SAT, CSP, CP-SAT, DLX, quantique |
| App-12 Connect Four | [Search/Applications/Search/App-12-ConnectFour.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Applications/Search/App-12-ConnectFour.ipynb) | 8 algorithmes de jeu |
| App-14 Connect Four Adversarial | [Search/Applications/Search/App-14-ConnectFour-Adversarial.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Applications/Search/App-14-ConnectFour-Adversarial.ipynb) | Jeux adversariaux |
| Search-6 Adversarial Search | [Search/Part1-Foundations/Search-6-AdversarialSearch.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part1-Foundations/Search-6-AdversarialSearch.ipynb) | Minimax, alpha-beta |
| GT-8 Combinatorial Games | [GameTheory/GameTheory-8-CombinatorialGames.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-8-CombinatorialGames.ipynb) | Théorie des jeux combinatoires |

### References externes
- Simonis, H. (2005). "Sudoku as a SAT Problem." *Proc. ISAIM*. [EasyChair](https://easychair.org/publications/paper/Sudoku-as-a-SAT-Problem)
- Lynce, I. & Ouaknine, J. (2006). "Sudoku as a SAT Problem." *Proc. SAT*. [Springer](https://link.springer.com/chapter/10.1007/11814948_25)
- Browne, C. et al. (2012). "A Survey of Monte Carlo Tree Search Methods." *IEEE TCIAIG*. [IEEE](https://ieeexplore.ieee.org/document/6145622)
- Knuth, D.E. (2000). "Dancing Links." *Millennial Perspectives in Computer Science*. [cs.stanford.edu](https://www-cs-faculty.stanford.edu/~knuth/papers/dancing-color.pdf)

### Difficulte : 3/5

---

#### L5 — Generateur de puzzles a unicite certifiee : synthese sous contraintes, preuve d'unicite de solution et calibration de difficulte

Un bon puzzle (Sudoku, Picross, etc.) doit avoir **exactement une** solution — propriete que la plupart des generateurs verifient de maniere heuristique, sans garantie. Ce sujet de recherche construit un **generateur de puzzles a unicite certifiee** : on synthetise des instances dont l'unicite de la solution est *prouvee* (et non simplement testee), par exemple en montrant l'insatisfiabilite (UNSAT) du probleme « existe-t-il une seconde solution differente ? » via une clause de blocage, ou par comptage de modeles. La difficulte de chaque puzzle est en outre **calibree** par l'ensemble minimal de techniques de raisonnement (ou l'effort de recherche du solveur) necessaires pour le resoudre. Le sujet est cross-paradigme : on compare SAT, programmation par contraintes (OR-Tools) et couverture exacte (Dancing Links) sur le double cout generation + certification.

### Objectifs
1. Implementer un generateur de puzzles (Sudoku et/ou Picross ou autre puzzle CSP) produisant des instances a solution unique
2. Certifier l'unicite : prouver qu'il existe exactement une solution (clause de blocage + UNSAT, ou comptage de modeles), pas seulement un test heuristique
3. Calibrer la difficulte via l'ensemble minimal de strategies humaines / l'effort de recherche requis
4. Comparer les paradigmes (SAT, CP/OR-Tools, couverture exacte/Dancing Links) sur le cout de generation et de certification
5. Evaluer la qualite des puzzles generes (unicite garantie, distribution de difficulte) face a des generateurs existants

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Sudoku-12 Z3 | [Sudoku/Sudoku-12-Z3-Python.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Sudoku/Sudoku-12-Z3-Python.ipynb) | SAT/SMT : certification d'unicite par UNSAT |
| Sudoku-10 OR-Tools | [Sudoku/Sudoku-10-ORTools-Python.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Sudoku/Sudoku-10-ORTools-Python.ipynb) | CP : generation et comptage de solutions |
| Sudoku-2 Dancing Links | [Sudoku/Sudoku-2-DancingLinks-Python.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Sudoku/Sudoku-2-DancingLinks-Python.ipynb) | Couverture exacte : enumeration des solutions |
| Sudoku-8 Human Strategies | [Sudoku/Sudoku-8-HumanStrategies-Python.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Sudoku/Sudoku-8-HumanStrategies-Python.ipynb) | Techniques humaines : calibration de difficulte |
| Sudoku-18 Comparison | [Sudoku/Sudoku-18-Comparison-Python.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Sudoku/Sudoku-18-Comparison-Python.ipynb) | Comparaison cross-paradigme des solveurs |
| App-11 Picross | [Search/Applications/CSP/App-11-Picross.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Applications/CSP/App-11-Picross.ipynb) | Autre puzzle CSP a unicite |

### References externes

**Generation de puzzles et unicite**
- McGuire, G., Tugemann, B. & Civario, G. (2014). "There Is No 16-Clue Sudoku." *Experimental Mathematics*, 23(2). [arXiv](https://arxiv.org/abs/1201.0749)
- Knuth, D.E. (2000). "Dancing Links." *Millennial Perspectives in Computer Science*. [Stanford](https://www-cs-faculty.stanford.edu/~knuth/papers/dancing-color.pdf)
- Simonis, H. (2005). "Sudoku as a Constraint Problem." *CP Workshop on Modelling and Reformulating CSPs*. [4c.ucc.ie](https://www.researchgate.net/publication/228840763)

**Difficulte et complexite**
- Pelanek, R. (2014). "Difficulty Rating of Sudoku Puzzles: An Overview and Evaluation." *arXiv:1403.7373*. [arXiv](https://arxiv.org/abs/1403.7373)
- Demaine, E.D. (2001). "Playing Games with Algorithms: Algorithmic Combinatorial Game Theory." *MFCS 2001*. [arXiv](https://arxiv.org/abs/cs/0106019)

### Difficulte : 5/5

---

### Categorie M : IA Neuro-Symbolique

#### M1 — Pipeline LLM + verificateur symbolique pour la generation fiable

Construire un pipeline en deux etapes ou un LLM genere des solutions candidates (plans d'action, preuves formelles, modeles de contraintes) en langage naturel ou JSON, puis un verificateur symbolique (Z3, Lean, ou CP-SAT) valide formellement la correction de la solution. L'etude systematique du taux de rejet (solutions incorrectes generees par le LLM) et des strategies de re-prompting (reformulation automatique, decomposition en sous-problemes, chain-of-thought) constitue le coeur du projet. Ce sujet illustre le paradigme "LLM-as-a-reasoner" et la verification neuro-symbolique, domaine en pleine expansion.

### Objectifs
- Construire un pipeline LLM-generateur puis verificateur symbolique avec une interface de traduction
- Implementer au moins trois strategies de re-prompting (reformulation, decomposition, chain-of-thought)
- Mesurer le taux de rejet et le taux de correction finale sur un ensemble de problemes de reference
- Analyser les types d'erreurs les plus frequentes dans les generations LLM
- Comparer les performances du pipeline avec un LLM seul (zero-shot, few-shot) et un solveur symbolique seul

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| CSP-6 LLM+CSP | [Search/Part2-CSP/CSP-6-Hybridization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-6-Hybridization.ipynb) | Pipeline LLM vers solveur CSP |
| Lean-7 LLM+Symbolique | [SymbolicAI/Lean/Lean-7-LLM-Integration.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-7-LLM-Integration.ipynb) | Verification formelle LLM+Lean |
| Lean-8 NeuroSymbolic | [SymbolicAI/Lean/Lean-8-Agentic-Proving.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-8-Agentic-Proving.ipynb) | Architectures neuro-symboliques |
| Planners-12 LOOP | [SymbolicAI/Planners/04-NeuroSymbolic/Planners-12-LOOP.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/04-NeuroSymbolic/Planners-12-LOOP.ipynb) | Boucle generation-verification-action |

### References externes
- Pan, L. et al. (2023). "Logic-LM: Faithful Logical Reasoning with Large Language Models." *EMNLP 2023*. [ACL Anthology](https://aclanthology.org/2023.emnlp-main.pe/)
- Garcez, A. d'Avila et al. (2024). "Neurosymbolic AI: The 3rd Wave." *Artificial Intelligence Review*. [Springer](https://link.springer.com/article/10.1007/s10462-024-10736-0)
- Katz, M. et al. (2024). "Duality in LLM-assisted Planning." *ICAPS 2024*. [AAAI](https://aaai.org/)
- Feng, J. et al. (2023). "Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective." *NeurIPS 2023*. [OpenReview](https://openreview.net/forum?id=TrazjUFjOJ)

### Difficulte : 3/5

---

#### M2 — Reseau de neurones logique (Logical Neural Networks)

Implementer ou utiliser des reseaux de neurones logiques (LNN d'IBM) ou des Logic Tensor Networks (LTN) qui integrent des contraintes logiques directement dans la fonction de perte d'un reseau de neurones. Les contraintes logiques (implications, disjonctions, quantificateurs) sont differentiables grace a une semantique basee sur la logique floue ou la logique de Lukasiewicz, permettant un entrainement end-to-end. L'application porte sur une tache de classification ou la coherence logique entre les predictions (par exemple, hierarchie de classes, exclusivite mutuelle) doit etre garantie.

### Objectifs
- Implementer ou integrer un reseau de neurones logique (LNN ou LTN) avec contraintes differentiables
- Formaliser les contraintes logiques du domaine (hierarchie, exclusivite, implication) en logique differentiable
- Entrainer le reseau avec une fonction de perte combinant perte classique et penalite logique
- Evaluer la coherence logique des predictions par rapport a un reseau standard sans contraintes
- Analyser le compromis entre precision de classification et garantie de coherence logique

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-2 Logiques | [SymbolicAI/Tweety/Tweety-2-Basic-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-2-Basic-Logics.ipynb) | Logiques classiques, semantiques |
| Tweety-3 Logiques avances | [SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb) | Logique floue, multimodale |
| CSP-7 Soft Constraints | [Search/Part2-CSP/CSP-7-Soft.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-7-Soft.ipynb) | Contraintes souples, penalites, optimisation |
| Lean-8 NeuroSymbolic | [SymbolicAI/Lean/Lean-8-Agentic-Proving.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-8-Agentic-Proving.ipynb) | Integration neural-symbolique |

### References externes
- Riegel, R. et al. (2020). "Logical Neural Networks." *IBM Research*. [arXiv](https://arxiv.org/abs/2006.13155)
- Badreddine, S. et al. (2022). "Logic Tensor Networks for Semantic Image Interpretation." *KR 2022*. [arXiv](https://arxiv.org/abs/2002.09521)
- Garcez, A. d'Avila et al. (2024). "Neurosymbolic AI: The 3rd Wave." *Artificial Intelligence Review*. [Springer](https://link.springer.com/article/10.1007/s10462-024-10736-0)
- Serbedzija, N. & Hitzler, P. (2023). "Neuro-Symbolic AI: An Overview." *KI*. [Springer](https://link.springer.com/article/10.1007/s13218-023-00810-y)

### Difficulte : 4/5

---

#### M3 — Regression symbolique — decouvrir des equations a partir de donnees

Utiliser PySR (PySymbolicRegression) pour decouvrir automatiquement des equations mathematiques a partir de donnees experimentales, en combinant la programmation genetique avec le filtrage basé sur la complexite de Kolmogorov et les criteres de parcimonie (Pareto front entre precision et complexite). Les tests se font sur des datasets de reference correspondant a des lois physiques connues (loi de gravitation, equations du pendule, loi des gaz parfaits) et l'evaluation porte sur la precision, la parcimonie et l'interpretabilite des equations decouvertes par rapport aux solutions analytiques connues. La comparaison avec la regression polynomiale classique et les methodes a noyau illustre le gain en interpretabilite.

### Objectifs
- Utiliser PySR pour decouvrir des equations mathematiques a partir de datasets physiques de reference
- Configurer les hyperparametres de la programmation genetique (taille de population, operateurs, complexite max)
- Evaluer la precision, la parcimonie et l'interpretabilite des equations decouvertes
- Comparer avec la regression polynomiale et les methodes de regression a noyau (kernel ridge)
- Analyser la frontiere de Pareto precision-complexite et identifier les equations optimales

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Search-5 Genetic Algorithms | [Search/Part1-Foundations/Search-5-GeneticAlgorithms.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part1-Foundations/Search-5-GeneticAlgorithms.ipynb) | Algorithmes genetiques, programmation genetique |
| Search-11 Metaheuristiques | [Search/Part1-Foundations/Search-11-Metaheuristics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part1-Foundations/Search-11-Metaheuristics.ipynb) | Metaheuristiques, optimisation globale |
| CSP-5 Optimization | [Search/Part2-CSP/CSP-5-Optimization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-5-Optimization.ipynb) | Optimisation multi-objectifs, Pareto |
| Research/ | [Research/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Research) | Methodes de recherche experimentale |

### References externes
- Cranmer, M. (2023). *PySR: Interpretable Machine Learning for Science*. [GitHub](https://github.com/MilesCranmer/PySR)
- Schmidt, M. & Lipson, H. (2009). "Distilling Free-Form Natural Laws from Experimental Data." *Science*. [Science](https://www.science.org/doi/10.1126/science.1165893)
- Udrescu, S.M. & Tegmark, M. (2020). "AI Feynman: A Physics-Inspired Method for Symbolic Regression." *Science Advances*. [Science Advances](https://www.science.org/doi/10.1126/sciadv.aay2631)
- La Cava, W. et al. (2021). "Contemporary Symbolic Regression Methods and their Relative Performance." *arXiv*. [arXiv](https://arxiv.org/abs/2107.14351)

### Difficulte : 3/5

---

#### M4 — Decouverte scientifique automatisee par regression symbolique et LLM

Construire un agent "AI scientist" qui enchaine quatre phases : (1) chargement et exploration d'un dataset physique ou chimique, (2) utilisation d'un LLM pour proposer des formes fonctionnelles candidates inspirees des theories existantes et de la litterature, (3) affinage des candidats par regression symbolique avec PySR, et (4) validation des decouvertes contre les lois connues et analyse des ecarts. Le LLM joue le role de chercheur qui genere des hypotheses, tandis que PySR assure l'ajustement numerique et la parcimonie. Ce sujet combine raisonnement symbolique, regression et generation par LLM dans une boucle de decouverte scientifique automatisee.

### Objectifs
- Construire un pipeline de decouverte scientifique en quatre phases (exploration, hypothese LLM, regression symbolique, validation)
- Utiliser un LLM pour generer des hypotheses fonctionnelles inspirees de la litterature scientifique
- Affiner les hypotheses par regression symbolique avec PySR en optimisant precision et parcimonie
- Valider les equations decouvertes contre les lois analytiques connues sur au moins trois datasets
- Evaluer la contribution relative du LLM (generation d'hypotheses) et de PySR (ajustement)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Search-11 Metaheuristiques | [Search/Part1-Foundations/Search-11-Metaheuristics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part1-Foundations/Search-11-Metaheuristics.ipynb) | Optimisation, recherche globale |
| CSP-6 LLM+CSP | [Search/Part2-CSP/CSP-6-Hybridization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-6-Hybridization.ipynb) | Hybridation LLM et methodes formelles |
| Lean-7 LLM+Symbolique | [SymbolicAI/Lean/Lean-7-LLM-Integration.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-7-LLM-Integration.ipynb) | Integration LLM et raisonnement symbolique |
| Research/ | [Research/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Research) | Methodes de recherche, experimentation |

### References externes
- Shojaee, P. et al. (2026). "Automated Scientific Discovery: From Equation Discovery to Autonomous Discovery Systems." *Machine Learning*, Springer. [Springer](https://link.springer.com/)
- Wang, H. et al. (2023). "Scientific Discovery in the Age of Artificial Intelligence." *Nature*. [Nature](https://www.nature.com/articles/s41586-023-06221-2)
- PySR: Interpretable Machine Learning for Science. [GitHub](https://github.com/MilesCranmer/PySR)
- Schmidt, M. & Lipson, H. (2009). "Distilling Free-Form Natural Laws from Experimental Data." *Science*. [Science](https://www.science.org/doi/10.1126/science.1165893)

### Difficulte : 4/5

---

#### M5 — Evaluation comparee LLM vs. approches symboliques sur un benchmark

Choisir un benchmark de raisonnement logique (LogicGrid, bAbI, ProofWriter, ou FLD) et comparer systematiquement les performances d'un LLM brut (zero-shot, few-shot, chain-of-thought) avec celles d'un pipeline symbolique (Z3, PySAT, ou CP-SAT) sur les memes problemes. L'analyse detaillee des types d'erreurs de chaque approche (erreurs de traduction, erreurs de raisonnement, erreurs de calcul) identifie les points forts complementaires du neural et du symbolique. Ce sujet est ideal pour decouvrir la complementarite des deux paradigmes sans implementer de pipeline complexe.

### Objectifs
- Selectionner et preparer un benchmark de raisonnement logique avec un ground truth fiable
- Evaluer un LLM en zero-shot, few-shot et chain-of-thought sur le benchmark
- Implementer un pipeline symbolique (Z3 ou PySAT) resolvent les memes problemes
- Realiser une taxonomie detaillee des erreurs par type et par approche
- Identifier les classes de problemes ou chaque paradigme excelle et proposer un schema de complementarite

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Solveur Z3 SMT, raisonnement formel |
| Sudoku/ | [Sudoku/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Sudoku) | Comparaison multi-solveurs de reference |
| Argument Analysis | [SymbolicAI/Argument_Analysis/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis) | Raisonnement argumentatif, evaluation |
| CSP-6 LLM+CSP | [Search/Part2-CSP/CSP-6-Hybridization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-6-Hybridization.ipynb) | Integration LLM et solveurs |

### References externes
- Pan, L. et al. (2023). "Logic-LM: Faithful Logical Reasoning with Large Language Models." *EMNLP 2023*. [ACL Anthology](https://aclanthology.org/2023.emnlp-main.pe/)
- Tafjord, O. et al. (2021). "ProofWriter: Generating Implications, Proofs, and Abductive Statements." *EMNLP 2021*. [ACL Anthology](https://aclanthology.org/2021.emnlp-main.335/)
- Sap, M. et al. (2019). "ATOMIC: An Atlas of Machine Commonsense." *AAAI 2019*. [AAAI](https://aaai.org/ojs/index.php/AAAI/article/view/4160)
- Han, S. et al. (2022). "FOLIO: Natural Language Reasoning with First-Order Logic." *arXiv*. [arXiv](https://arxiv.org/abs/2209.00840)

### Difficulte : 2/5

#### M6 — Theorie de l'Information Integree (IIT) et conscience artificielle par PyPhi

Integrated Information Theory (IIT), proposee par Giulio Tononi, postule que la conscience correspond a la quantite d'information integree (Phi, Φ) generee par un systeme au-dela de ses parties. PyPhi est la bibliotheque Python officielle pour calculer Φ sur des reseaux de transition logiques, permettant d'explorer les relations entre architecture du reseau, informatisation et complexite phenomenologique. L'etudiant modelise differents reseaux neuronaux simplifies (gluckueaux, inhibiteurs, hierarchiques), calcule leurs valeurs Φ, et analyse comment la structure causale du systeme determine sa capacite integrative. Ce sujet aborde les questions fondamentales de la conscience artificielle et de l'explicabilite structurelle des systemes symboliques, en croisant theorie de l'information, logique et philosophie de l'esprit.

### Objectifs
- Installer PyPhi et comprendre le formalisme IIT (cause-effect repertoire, MIP, Φ)
- Modeliser differents reseaux logiques simples (AND, OR, XOR, COPY) et calculer leurs valeurs Φ
- Analyser l'impact de l'architecture du reseau (connectivite, recurrence, feedforward) sur la valeur de Φ
- Comparer les systemes "conscients" (Φ eleve) et "automates" (Φ faible) en termes de structure causale
- Discuter les limitations computationnelles (explosion combinatoire de PyPhi) et les perspectives pour l'IA symbolique

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Intro to PyPhi | [IIT/Intro_to_PyPhi.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/IIT/Intro_to_PyPhi.ipynb) | PyPhi, calcul de Φ |
| Research/ | [Research/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Research) | Prototypage, reseaux logiques |
| Tweety-4 Belief | [SymbolicAI/Tweety/Tweety-4-Belief-Revision.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-4-Belief-Revision.ipynb) | Revision des croyances |

### References
- Tononi, G. (2004). "An Information Integration Theory of Consciousness." *BMC Neuroscience*, 5, 42. [BioMed Central](https://doi.org/10.1186/1471-2202-5-42)
- Tononi, G. & Koch, C. (2015). "Consciousness: Here, There and Everywhere?" *Philosophical Transactions of the Royal Society B*, 370(1668). [Royal Society](https://doi.org/10.1098/rstb.2014.0167)
- Mayner, W.G.P. et al. (2018). "PyPhi: A Toolbox for Integrated Information Theory." *PLoS Computational Biology*, 14(7). [PLOS](https://doi.org/10.1371/journal.pcbi.1006343)
- Albantakis, L. et al. (2023). "Integrated Information Theory (IIT) 4.0." *arXiv*. [arXiv](https://arxiv.org/abs/2212.02621)

### Difficulte : 3/5

---

#### M7 — Generation de contenu neuro-symbolique par Semantic Kernel + validation CSP

Concevoir un pipeline de generation de contenu structure (plans de cours, examens, rapports techniques) combinant Microsoft Semantic Kernel (orchestration LLM, plugins, memoire vectorielle) avec un validateur symbolique CSP/CP-SAT. Le LLM genere des candidats JSON (emploi du temps, QCM avec contraintes de couverture), le solveur symbolique verifie les contraintes dures (pas de chevauchement, couverture minimale des objectifs pedagogiques) et injecte les violations comme feedback structure dans le prompt suivant. L'architecture hybride "LLM generateur + CSP verificateur" est le pattern neuro-symbolique le plus industriellement deployable. Note : le notebook CSP-6 du CoursIA couvre les approches hybrides CSP modernes (pas de pipeline LLM+CSP pret a l'emploi) — les etudiants devront implementer l'integration SK+CSP eux-memes en s'appuyant sur les 20 notebooks Semantic Kernel et les outils de validation CSP.

### Objectifs
1. Implémenter un pipeline Semantic Kernel avec plugins de génération et de validation CSP
2. Modéliser les contraintes du domaine (couverture de syllabus, non-chevauchement, charge équilibrée) en CP-SAT
3. Étudier le taux de convergence itératif (nombre de cycles LLM→CSP→feedback avant satisfaction) et la qualité du résultat final
4. Comparer l'approche neuro-symbolique itérative avec une génération LLM pure et un solveur CSP pur
5. Étendre le pipeline avec un plugin de mémoire vectorielle (embeddings) pour éviter la répétition de contenu

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SK Intro | [GenAI/SemanticKernel/01-SemanticKernel-Intro.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GenAI/SemanticKernel/01-SemanticKernel-Intro.ipynb) | Introduction Semantic Kernel |
| SK Agents | [GenAI/SemanticKernel/03-SemanticKernel-Agents.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GenAI/SemanticKernel/03-SemanticKernel-Agents.ipynb) | Function calling, agents autonomes |
| SK Vector Stores | [GenAI/SemanticKernel/05-SemanticKernel-VectorStores.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GenAI/SemanticKernel/05-SemanticKernel-VectorStores.ipynb) | RAG, embeddings vectoriels |
| CSP-6 Hybridation | [Search/Part2-CSP/CSP-6-Hybridization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-6-Hybridization.ipynb) | Approches hybrides CSP modernes |
| GenAI/SemanticKernel/ | [GenAI/SemanticKernel/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/GenAI/SemanticKernel) | 20 notebooks Semantic Kernel |

### References externes
- Bubeck, S. et al. (2023). "Sparks of Artificial General Intelligence: Early Experiments with GPT-4." *arXiv*. [arXiv](https://arxiv.org/abs/2303.12712)
- Liang, T. et al. (2024). "LLM+Optimization: Towards Integrating Large Language Models and Optimization." *arXiv*. [arXiv](https://arxiv.org/abs/2401.17094)
- Microsoft (2024). "Semantic Kernel Documentation." [learn.microsoft.com](https://learn.microsoft.com/en-us/semantic-kernel/)
- Yao, S. et al. (2023). "ReAct: Synergizing Reasoning and Acting in Language Models." *ICLR 2023*. [arXiv](https://arxiv.org/abs/2210.03629)

### Difficulte : 4/5

---

#### M8 — Demonstration automatique neuro-symbolique : agent LLM pour Lean 4

Construire un agent LLM capable de generer des preuves formelles en Lean 4 de maniere autonome, en combinant un modele de langage (GPT-4, Claude, ou modele local) avec l'environnement Lean (Lake, LSP). L'agent recoit un enonce de theoreme, genere une strategie de preuve, l'execute via le compilateur Lean, et boucle sur les echecs en analysant les messages d'erreur. Ce sujet se situe a la frontiere de la recherche en IA : les proverteurs neuronaux (AlphaProof, DeepMind, LeanDojo) representent l'etat de l'art 2024-2026. Les etudiants implementent une architecture multi-tactiques (recherche arborescente, selection de tactiques par LLM, feedback du compilateur), evaluent sur un benchmark de theoremes Mathlib de difficulte croissante, et analysent les limites (hallucination syntaxique, profondeur de raisonnement, timeout). Les notebooks CoursIA Lean-7 a Lean-11 couvrent l'integration LLM, la preuve agentique, et le neural theorem proving.

### Objectifs
1. Implementer un pipeline LLM → Lean : generation de tactiques, compilation Lake, parsing des erreurs, feedback iteratif
2. Construire une architecture de recherche (beam search ou MCTS) combinant selection LLM et verification Lean
3. Evaluer sur un benchmark gradue : theoremes triviaux (auto) → tactiques simples (simp, omega) → preuves multi-etapes → theoremes Mathlib
4. Analyser les modes d'echec (hallucination syntaxique, tactiques incorrectes, timeouts, profondeur limitee) et proposer des mitigations
5. Comparer avec les approches de la litterature (LeanDojo, AlphaProof, COPRA) et discuter les limites fondamentales

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Lean-7 LLM Integration | [SymbolicAI/Lean/Lean-7-LLM-Integration.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-7-LLM-Integration.ipynb) | LLM + Lean, generation de tactiques |
| Lean-8 Agentic Proving | [SymbolicAI/Lean/Lean-8-Agentic-Proving.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-8-Agentic-Proving.ipynb) | Preuve agentique autonome |
| Lean-9 SK Multi-Agents | [SymbolicAI/Lean/Lean-9-SK-Multi-Agents.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-9-SK-Multi-Agents.ipynb) | Orchestration multi-agents |
| Lean-10 LeanDojo | [SymbolicAI/Lean/Lean-10-LeanDojo.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-10-LeanDojo.ipynb) | LeanDojo, RL pour la preuve |
| Lean-11 Neural Proving | [SymbolicAI/Lean/Lean-11-TorchLean.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-11-TorchLean.ipynb) | Proverteurs neuronaux |

### References externes
- Song, D. et al. (2024). "Towards Large Language Models as Copilots for Theorem Proving in Lean." *arXiv*. [arXiv](https://arxiv.org/abs/2404.12534)
- First, E. et al. (2023). "Baldur: Whole-Proof Generation and Repair with Large Language Models." *ESEC/FSE 2023*. [arXiv](https://arxiv.org/abs/2303.04910)
- Polu, S. et al. (2023). "Formal Mathematics Statement Curriculum Learning." *ICLR 2023*. [arXiv](https://arxiv.org/abs/2202.01344)
- Yang, K. & Deng, J. (2023). "LeanDojo: Theorem Proving with Retrieval-Augmented Language Models." *NeurIPS 2023*. [OpenReview](https://openreview.net/forum?id=3m3kpTxlJW)

### Difficulte : 5/5

---

#### M9 — Compresseur sans perte neuro-symbolique : LLM-decouvreur, decodeur certifie et registre de recettes signees

Ce sujet de recherche applique le principe "compression = intelligence" (complexite de Kolmogorov, Minimum Description Length, Hutter Prize) a la construction d'un compresseur **sans perte** ou un LLM joue le role de **decouvreur de regularites** : au lieu de resumer (avec perte), il propose une **recette de reconstruction** deterministe et verifiable (grammaire, automate, ou programme dans un DSL restreint) telle que `donnee = decode(recette)` exactement, controle bit-a-bit par hachage. Le point central de l'architecture est que le LLM n'est **jamais dans le chemin de confiance ni de decodage** : un verificateur symbolique valide le round-trip, et un **decodeur borne, deterministe et certifie** (DSL total facon Bitcoin Script avec budget de pas type gas/fuel, plutot qu'une VM Turing-complete) execute la recette, accompagnee d'un **certificat facon smart-contract** (verification formelle d'invariants + preuve verifiable). L'innovation systeme centrale est un **registre de recettes "facon antivirus"** : une base communautaire, signee et adressee par contenu, qui associe des **signatures** de donnees (magic bytes, n-grammes, structure -- a la maniere de YARA pour les malwares ou de PRONOM/DROID pour les formats de fichiers) a des **recettes certifiees pretes a l'emploi**. Un detecteur **sans LLM** identifie la famille d'un fichier et rejoue la recette certifiee correspondante ; le LLM (couteux) n'intervient que sur les donnees **non reconnues**, et sa recette, une fois validee et signee, enrichit le registre. Resultat : le travail des LLM est **recycle de facon sure** et, pour les utilisateurs casual, compression comme decompression se font **la plupart du temps sans aucun LLM**. *Note de cadrage : la serie Lean du CoursIA enseigne la preuve de theoremes (Mathlib) et le neural theorem proving, mais peu la certification de programme au sens "prouver qu'un decodeur respecte sa specification". Une voie cote Lean existe -- la conclusion du theoreme de sensibilite (Lean-12) suggere comment fabriquer des certificats via TorchLean (Lean-11) -- mais elle est surdimensionnee pour ce sujet. Le materiel le plus directement exploitable est cote SmartContracts : verification formelle d'invariants (SC-14), preuve verifiable (SC-15), execution bornee deterministe (SC-20), complete par la formalisation en Lean d'un processus deterministe (Game of Life de Conway, Lean-14b). Les etudiants devront assembler eux-memes le decodeur borne certifie et le registre de signatures ; aucun pipeline pret a l'emploi n'existe.*

### Objectifs
1. Formaliser une "recette de reconstruction" (grammaire, automate ou programme dans un DSL restreint) et un protocole de verification du round-trip bit-a-bit par hachage, garantissant `donnee = decode(recette)`
2. Construire le LLM-decouvreur : a partir d'un echantillon, proposer des recettes candidates, avec une cascade de modeles (petit modele d'abord, grand modele en dernier recours) pour minimiser le cout en tokens
3. Implementer le decodeur sur un DSL total et borne deterministe (inspire de Bitcoin Script, non-Turing-complet, budget de pas facon gas/fuel) et le **certifier** : invariants par fuzzing (SC-13), specification formelle (Certora/CVL, SC-14) et preuve verifiable non-interactive (Fiat-Shamir, SC-15) -- le LLM restant hors du chemin de confiance
4. Concevoir le **registre de recettes "facon antivirus"** : signatures (magic bytes, n-grammes, structure facon YARA/PRONOM) vers recette certifiee signee, adressee par contenu ; un detecteur sans LLM matche la signature et rejoue la recette, le LLM n'enrichissant le registre que sur les donnees non reconnues (recyclage sur)
5. Evaluer : taux de compression vs baselines (zstd, ZPAQ, codec arithmetique a base de LLM) sous le critere MDL ; surtout, mesurer le **taux d'operations realisees sans LLM** (couverture du registre), le cout/benefice du recyclage, et la robustesse aux bombes de decompression (bornes du decodeur)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SL-7 LLM Symbolic Learning | [SymbolicAI/SymbolicLearning/SL-7-LLM-SymbolicLearning.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SymbolicLearning/SL-7-LLM-SymbolicLearning.ipynb) | LLM qui induit des regles et programmes symboliques : le decouvreur de regularites |
| SL-4 Inductive Logic Programming | [SymbolicAI/SymbolicLearning/SL-4-InductiveLogicProgramming.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SymbolicLearning/SL-4-InductiveLogicProgramming.ipynb) | Synthese de programme = compression de connaissances (lien smallest grammar / refactoring) |
| SC-20 Bitcoin Scripting | [SymbolicAI/SmartContracts/05-Alternative-Chains/SC-20-Bitcoin-Scripting.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/05-Alternative-Chains/SC-20-Bitcoin-Scripting.ipynb) | Langage a pile borne non-Turing-complet + mini-interpreteur : modele du decodeur borne (gas/fuel) |
| SC-14 Formal Verification | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb) | Certora/CVL, specifications et invariants : le certificat de round-trip |
| SC-15 Zero-Knowledge Proofs | [SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-15-Zero-Knowledge-Proofs.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-15-Zero-Knowledge-Proofs.ipynb) | Fiat-Shamir (interactif vers non-interactif) : preuve verifiable du round-trip |
| SC-11 LLM-Assisted | [SymbolicAI/SmartContracts/02-Solidity-Advanced/SC-11-LLM-Assisted.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/02-Solidity-Advanced/SC-11-LLM-Assisted.ipynb) | LLM genere du code et detecte, avec repli LLM local (Qwen) : recyclage et usage casual |
| Lean-14b Conway Game of Life | [SymbolicAI/Lean/Lean-14b-Conway-Game-of-Life-Lean.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-14b-Conway-Game-of-Life-Lean.ipynb) | Automate cellulaire deterministe formalise en Lean : specification d'une regle de reconstruction |
| CSP-5 Optimization | [Search/Part2-CSP/CSP-5-Optimization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-5-Optimization.ipynb) | DAG de reconstruction et bin-packing : random-access comme parametre d'optimisation |

### References externes

**Fondements -- "compression = intelligence" (MDL, complexite de Kolmogorov)**
- Solomonoff, R. (1964). "A Formal Theory of Inductive Inference." *Information and Control*. (induction par compression, fondement theorique du decouvreur)
- Rissanen, J. (1978). "Modeling by Shortest Data Description." *Automatica*. (principe MDL : meilleure theorie = description la plus courte des donnees)
- Li, M. & Vitanyi, P. *An Introduction to Kolmogorov Complexity and Its Applications*, Springer. (complexite de Kolmogorov, incalculable -- d'ou l'usage d'un LLM comme heuristique d'approximation)
- Hutter, M. *Hutter Prize for Lossless Compression of Human Knowledge* (la compression sans perte comme mesure d'intelligence). [prize.hutter1.net](http://prize.hutter1.net/)

**LLM comme compresseur (le modele dans le chemin de decodage -- ce que M9 evite)**
- Deletang, G. et al. (2024). "Language Modeling Is Compression." *ICLR 2024*. [arXiv:2309.10668](https://arxiv.org/abs/2309.10668)
- Bellard, F. *NNCP / ts_zip : compression de donnees sans perte par reseaux de neurones*. [bellard.org/nncp](https://bellard.org/nncp/)
- (rapporte) LMCompress / AlphaZip : codage arithmetique pilote par un LLM -- atteint d'excellents taux mais exige le modele exact au decodage, contrainte que l'architecture M9 leve en sortant le LLM du chemin de confiance.

**Compression programmatique et archives auto-descriptives**
- Ford, B. (2005). "VXA: A Virtual Architecture for Durable Compressed Archives." *USENIX FAST 2005*. (decodeur embarque dans une VM bornee, sur meme si l'archive est malveillante) [usenix.org](https://www.usenix.org/)
- Mahoney, M. *ZPAQ : archiveur a journal avec VMs ZPAQL (HCOMP/PCOMP) embarquees dans le flux*. [mattmahoney.net/dc](http://mattmahoney.net/dc/)
- Charikar, M. et al. (2005). "The Smallest Grammar Problem." *IEEE Trans. Information Theory*. (probleme NP-difficile ; algorithmes Sequitur, RePair, TreeRePair)
- Dumancic, S. & Cropper, A. (2020). "Knowledge Refactoring for Inductive Program Synthesis." *AAAI 2020*. (la synthese/refactorisation de programmes vue comme compression sans perte) [arxiv.org](https://arxiv.org/)

**Verification, certification et execution bornee**
- Necula, G. (1997). "Proof-Carrying Code." *POPL 1997*. (le code porte sa propre preuve, verifiee avant execution) [ACM Digital Library](https://dl.acm.org/)
- Ben-Sasson, E. et al. (2013). "SNARKs for C: Verifying Program Executions Succinctly and in Zero Knowledge." *CRYPTO 2013*. (preuve succincte verifiee sans re-executer le programme) [IACR ePrint](https://eprint.iacr.org/)
- Ramananandro, T. et al. (2019). "EverParse: Verified Secure Zero-Copy Parsers for Authenticated Message Formats." *USENIX Security 2019*. (parsers formellement verifies, modele du verificateur de recette) [usenix.org](https://www.usenix.org/)
- Bytecode Alliance. *Wasmtime : execution WebAssembly deterministe, bornee par "fuel" et ResourceLimiter*. (modele du decodeur borne anti-bombe de decompression) [wasmtime.dev](https://wasmtime.dev/)

**Registre de signatures "facon antivirus" (recyclage sur, usage casual sans LLM)**
- VirusTotal. *YARA : the pattern matching swiss knife for malware researchers* (regles communautaires de signatures). [virustotal.github.io/yara](https://virustotal.github.io/yara/)
- The National Archives (UK). *PRONOM / DROID : registre communautaire de signatures de formats de fichiers* (magic bytes). [nationalarchives.gov.uk/PRONOM](https://www.nationalarchives.gov.uk/PRONOM/)
- IETF. *Compression Dictionary Transport* (dictionnaires de compression partages zstd/brotli, precedent du recyclage de "recettes"). [datatracker.ietf.org](https://datatracker.ietf.org/)

**Distillation symbolique (analogie du LLM-decouvreur)**
- Landajuela, M. et al. (2021). "Discovering Symbolic Policies with Deep Reinforcement Learning." *ICML 2021*. (politique neuronale distillee en equations compactes verifiables) [proceedings.mlr.press](https://proceedings.mlr.press/)

### Difficulte : 5/5

---

### Categorie N : Raisonnement Causal et Decision

#### N1 — Decouverte causale a partir de donnees observationnelles

Implementer un algorithme de decouverte causale (PC, FCI, ou GES) qui construit un graphe causal (DAG ou PDAG) a partir de donnees observationnelles en exploitant les independances conditionnelles duales entre variables. La comparaison des resultats avec la structure causale veridique sur des datasets synthetiques (ou les vraies causes sont connues) et des datasets de reference (par exemple Asia, Sachs) permet de mesurer la precision structurelle (precision, rappel, SHD). L'etude de la sensibilite a la taille de l'echantillon et aux variables latentes complete l'analyse.

### Objectifs
- Implementer un algorithme de decouverte causale (PC, FCI ou GES) avec tests d'independance conditionnelle
- Generer des datasets synthetiques avec structure causale connue pour l'evaluation controlee
- Evaluer la precision structurelle (precision, rappel, SHD) sur des datasets synthetiques et de reference
- Etudier la sensibilite a la taille de l'echantillon et a la presence de variables latentes
- Comparer les performances de deux algorithmes (par exemple PC vs GES) sur les memes donnees

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Research/ | [Research/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Research) | Reseaux bayesiens, graphes de facteurs |
| GameTheory/ | [GameTheory/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/GameTheory) | Theorie des jeux, decision sous incertitude |
| CSP-1 Fundamentals | [Search/Part2-CSP/CSP-1-Fundamentals.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-1-Fundamentals.ipynb) | Modelisation, contraintes sur graphes |
| Tweety-2 Logiques | [SymbolicAI/Tweety/Tweety-2-Basic-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-2-Basic-Logics.ipynb) | Raisonnement logique, probabiliste |

### References externes
- Spirtes, P. et al. (2000). *Causation, Prediction, and Search*. MIT Press, 2nd ed. [MIT Press](https://mitpress.mit.edu/9780262194402/causation-prediction-and-search/)
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. Cambridge, 2nd ed. [Cambridge](https://www.cambridge.org/core/books/causality/)
- Chickering, D.M. (2002). "Optimal Structure Identification with Greedy Search." *JMLR*. [JMLR](https://www.jmlr.org/papers/volume3/chickering02b/chickering02b.pdf)
- Colombo, D. & Maathuis, M.H. (2014). "Order-Independent Constraint Based Causal Structure Learning." *JMLR*. [JMLR](https://www.jmlr.org/papers/volume15/colombo14a/colombo14a.pdf)

### Difficulte : 3/5

---

#### N2 — Raisonnement causal par le do-calculus avec DoWhy

Utiliser le framework DoWhy (Microsoft) pour realiser des analyses causales completes en quatre etapes : modelisation du graphe causal, identification de l'estimand par le do-calculus, estimation de l'effet causal (propensity score matching, instrumental variables, double machine learning), et refutation par tests de robustesse (placebo, ajout de variables, sous-echantillonnage). L'application porte sur un dataset reel (sante, education, ou economie) ou les relations causales sont partiellement connues, permettant de confronter les estimations aux connaissances du domaine.

### Objectifs
- Modeliser un probleme causal reel comme un graphe causal avec DoWhy
- Appliquer le do-calculus pour identifier l'estimand causal (back-door, front-door, IV)
- Estimer l'effet causal par au moins deux methodes (propensity score, DML, IV)
- Realiser des tests de refutation pour evaluer la robustesse des estimations
- Confronter les resultats aux connaissances du domaine et interpreter les ecarts

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Research/ | [Research/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Research) | Reseaux bayesiens, inférence causale |
| GameTheory/ | [GameTheory/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/GameTheory) | Decision sous incertitude, utilite esperee |
| CSP-5 Optimization | [Search/Part2-CSP/CSP-5-Optimization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-5-Optimization.ipynb) | Optimisation sous contraintes |
| Tweety-2 Logiques | [SymbolicAI/Tweety/Tweety-2-Basic-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-2-Basic-Logics.ipynb) | Raisonnement probabiliste |

### References externes
- Pearl, J. & Mackenzie, D. (2018). *The Book of Why*. Basic Books. [Basic Books](https://www.basicbooks.com/titles/judea-pearl/the-book-of-why/9780465097616/)
- Sharma, A. & Kiciman, E. (2020). "DoWhy: A Python Library for Causal Inference." *Microsoft Research*. [arXiv](https://arxiv.org/abs/2011.04164)
- Huntington, D. *The Causal Inference Playbook*. [causalml-book.org](https://causalml-book.org)
- Imbens, G.W. & Rubin, D.B. (2015). *Causal Inference for Statistics, Social, and Biomedical Sciences*. Cambridge. [Cambridge](https://www.cambridge.org/core/books/causal-inference-for-statistics-social-and-biomedical-sciences/)

### Difficulte : 3/5

---

#### N3 — Diagnostic abductif — raisonnement par abduction

Implementer un systeme de diagnostic abductif qui, etant donne un ensemble d'observations (symptomes, erreurs systeme, anomalies), trouve l'ensemble minimal d'hypotheses (maladies, pannes, causes racines) qui les expliquent de maniere coherente. L'approche repose sur l'abduction par couverture d'ensemble (set-covering abduction) ou la programmation logique abductive (ALP), ou la recherche de la meilleure explanation suit le principe de parcimonie (minimum cardinality ou maximum likelihood). L'application porte sur le diagnostic medical ou le diagnostic de pannes techniques, avec une evaluation sur des scenarios realistes.

### Objectifs
- Formaliser le probleme de diagnostic abductif comme un probleme de couverture d'ensemble
- Implementer un algorithme d'abduction trouvant les explications minimales (parsimonie)
- Modeliser un domaine d'application (medical ou pannes) avec base de connaissances causale
- Evaluer la precision du diagnostic sur des scenarios realistes avec causes connues
- Comparer l'abduction par couverture avec la programmation logique abductive (ALP)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-5 Argumentation | [SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb) | Argumentation, raisonnement defeasible |
| Tweety-6 Argumentation avancee | [SymbolicAI/Tweety/Tweety-6-Structured-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-6-Structured-Argumentation.ipynb) | Extensions, acceptabilite semantique |
| Research/ | [Research/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Research) | Reseaux bayesiens, diagnostic |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Resolution par contraintes, optimisation |

### References externes
- Bylander, T. et al. (1991). "The Computational Complexity of Abduction." *Artificial Intelligence*. [Elsevier](https://www.sciencedirect.com/science/article/pii/0004370291900417)
- Kakas, A.C. et al. (1992). "Abductive Logic Programming." *Journal of Logic and Computation*. [Oxford](https://academic.oup.com/logcom/article-abstract/2/6/719/943357)
- Pearl, J. (2009). *Causality*. Cambridge, 2nd ed. (chapitre sur l'abduction). [Cambridge](https://www.cambridge.org/core/books/causality/)
-Console, L. & Dupre, D.T. (1994). "Abductive Reasoning with Abstractions." *IJCAI 1994*. [IJCAI](https://www.ijcai.org/Proceedings/94-1/Papers/047.pdf)

### Difficulte : 3/5

---

#### N4 — Evaluation du raisonnement causal des LLM

Evaluer si les grands modeles de langage peuvent raisonner causalement de maniere valide ou s'ils confondent correlation et causation en reproduisant des biais statistiques. Construire un benchmark structure selon la hierarchie de Pearl (association, intervention via do, contrefactuels) avec des questions causales et anti-causales. La comparaison avec des methodes causales formelles (DoWhy, causal discovery) quantifie l'ecart entre le raisonnement implicite des LLM et le raisonnement causal rigoureux, et identifie les niveaux de la hierarchie ou les LLM echouent systematiquement.

### Objectifs
- Construire un benchmark causal structure en trois niveaux (association, intervention, contrefactuel)
- Evaluer plusieurs LLM (zero-shot, few-shot, chain-of-thought) sur le benchmark
- Implementer un baseline causal formel (DoWhy ou graphe causal) pour comparaison
- Analyser les confusions systematiques (correlation vs causation, reversed causality)
- Identifier les niveaux de la hierarchie de Pearl ou les LLM echouent et proposer des strategies d'amelioration

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| CSP-6 LLM+CSP | [Search/Part2-CSP/CSP-6-Hybridization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-6-Hybridization.ipynb) | Evaluation LLM, pipeline symbolique |
| Argument Analysis | [SymbolicAI/Argument_Analysis/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis) | Raisonnement, evaluation d'arguments |
| Research/ | [Research/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Research) | Inférence causale, reseaux bayesiens |
| Tweety-2 Logiques | [SymbolicAI/Tweety/Tweety-2-Basic-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-2-Basic-Logics.ipynb) | Logique, raisonnement conditionnel |

### References externes
- Zecevic, M. et al. (2023). "Causal Parrots: Large Language Models May Talk Causality But Are Not Causal." *JAIR*. [JAIR](https://www.jair.org/index.php/jair/article/view/14821)
- Jin, Z. et al. (2023). "CLADDER: A Benchmark to Assess Causal Reasoning Capabilities of Language Models." *NeurIPS 2023*. [OpenReview](https://openreview.net/forum?id=kkQU6I4Igo)
- Pearl, J. (2018). "The Seven Tools of Causal Inference." *CACM*. [ACM](https://cacm.acm.org/research/the-seven-tools-of-causal-inference-with-reflections-on-machine-learning/)
- Liu, V. et al. (2023). "Are Large Language Models Good Causal Reasoners?" *EMNLP 2023*. [ACL Anthology](https://aclanthology.org/2023.emnlp-main.pa/)

### Difficulte : 4/5

---

#### N5 — Planification oncologique symbolique (ontologies, Z3 et modeles probabilistes)

Construire un systeme d'aide a la decision pour la planification de traitements oncologiques combinant trois couches symboliques : (1) une ontologie OWL des protocoles de chimiotherapie, contre-indications et interactions medicamenteuses, raisonnee via un moteur SPARQL/HermiT ; (2) un modele de contraintes Z3/SMT encodant les regles cliniques (doses cumulees maximales, intervalles minimums, compatibilite avec pathologies preexistantes) ; (3) un modele probabiliste PyMC/HMM estiment les parametres patient-specifiques (risque de recurrence, toxicite attendue). Le cas d'etude s'appuie sur le dataset oncologique du CoursIA (`CaseStudies/Oncology-Planning/`), qui fournit un modele complet de planification symbolique. Ce sujet illustre l'integration multi-paradigme : logique de description + contraintes SMT + probabilites, le triptyque au coeur de l'IA symbolique moderne.

### Objectifs
1. Modéliser l'ontologie des protocoles oncologiques en OWL (classes : Agent, Protocole, Pathologie ; propriétés : contre-indication, synergie)
2. Encoder les règles cliniques en Z3/SMT (dose cumulée ≤ seuil, intervalle ≥ minimum, compatibilité patient-traitement)
3. Implémenter un modèle probabiliste PyMC pour estimer le risque patient-spécifique à partir de variables cliniques
4. Intégrer les trois couches dans un pipeline de décision : ontologie → contraintes → probabilités → recommandation
5. Valider sur les cas cliniques du CoursIA et comparer avec les recommandations du panel d'oncologues

> **Donnees** : le dataset CoursIA `CaseStudies/Oncology-Planning/` fournit des cas cliniques **synthetiques** structures pour le TP. L'utilisation de donnees reelles patient est envisageable en extension, mais impose des contraintes legales (consentement, anonymisation, RGPD) qui sortent du scope technique du sujet. Par defaut, travailler sur donnees synthetiques.

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Oncology Planning | [CaseStudies/Oncology-Planning/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/CaseStudies/Oncology-Planning) | Cas complet planification oncologique |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Z3 SMT Solver depuis C# |
| PyMC HMM | [Probas/PyMC-HMM-Trading-Alpha.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Probas/PyMC-HMM-Trading-Alpha.ipynb) | PyMC, modèles hiérarchiques |
| CSP-4 Scheduling | [Search/Part2-CSP/CSP-4-Scheduling.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-4-Scheduling.ipynb) | Ordonnancement sous contraintes |
| Diagnostic Medical | [CaseStudies/Diagnostic-Medical/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/CaseStudies/Diagnostic-Medical) | Diagnostic multi-paradigme |

### References externes
- Abécassis, J. et al. (2019). "Ontologie des protocoles de chimiothérapie : du modèle à la décision clinique." *BMC Medical Informatics and Decision Making*. [DOI](https://doi.org/10.1186/s12911-019-0809-y)
- Dechter, R. (2003). *Constraint Processing*. Morgan Kaufmann. [Elsevier](https://www.elsevier.com/books/constraint-processing/dechter/978-1-55860-890-0)
- Salvatier, J. et al. (2016). "Probabilistic Programming in Python Using PyMC3." *PeerJ Computer Science*. [PeerJ](https://peerj.com/articles/cs-55/)
- Horridge, M. et al. (2012). "A Practical Guide to Building OWL Ontologies Using Protégé 4." *University of Manchester Technical Report*. [cs.man.ac.uk](https://www.cs.man.ac.uk/~horridgm/)

### Difficulte : 5/5

---

### Categorie O : Raisonnement Qualitatif et Bon Sens

#### O1 — Raisonnement spatial qualitatif par les calculs RCC8

Implementer le calcul relationnel spatial RCC8 (Region Connection Calculus) qui definit huit relations de base entre regions spatiales : disconnected (DC), externally connected (EC), partially overlapping (PO), tangential proper part (TPP), non-tangential proper part (NTPP), et leurs inverses (TPPi, NTPPi), plus equal (EQ). Le raisonneur par contraintes propage les relations connues pour inferer les relations implicites et detecter les inconsistances dans les configurations spatiales. L'application porte sur la verification de coherence de descriptions spatiales en langage naturel ou la planification robotique.

### Objectifs
- Implementer les huit relations RCC8 et leur table de composition
- Construire un raisonneur par contraintes propageant les relations spatiales implicites
- Implementer la detection d'inconsistances dans les configurations spatiales
- Appliquer le raisonneur a la verification de descriptions spatiales ou a la planification robotique
- Evaluer la complexite et la scalabilite du raisonneur sur des configurations de taille croissante

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| CSP-8 Temporal CSP | [Search/Part2-CSP/CSP-8-Temporal.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-8-Temporal.ipynb) | CSP qualitatifs, propagation de contraintes |
| Search-10 Automates | [Search/Part1-Foundations/Search-10-SymbolicAutomata.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part1-Foundations/Search-10-SymbolicAutomata.ipynb) | Automates symboliques, raisonnement formel |
| CSP-3 Global Constraints | [Search/Part2-CSP/CSP-3-Advanced.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-3-Advanced.ipynb) | Contraintes globales, tables de compatibilite |
| CSP-1 Fundamentals | [Search/Part2-CSP/CSP-1-Fundamentals.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-1-Fundamentals.ipynb) | Modelisation CSP, propagation |

### References externes
- Randell, D.A. et al. (1992). "A Spatial Logic Based on Regions and Connection." *KR 1992*. [KR](https://kr.org/KR92/)
- Renz, J. & Nebel, B. (2004). "Qualitative Spatial Reasoning with Constraint Calculi." *Handbook of Spatial Logics*. [Springer](https://link.springer.com/chapter/10.1007/978-3-540-74761-1_4)
- Cohn, A.G. & Renz, J. (2008). "Qualitative Spatial Reasoning." *Handbook of Knowledge Representation*. [Elsevier](https://www.sciencedirect.com/science/article/pii/S1574652607030079)
- Ligozat, G. (2011). *Qualitative Spatial and Temporal Reasoning*. ISTE/Wiley. [Wiley](https://www.wiley.com/en-us/Qualitative+Spatial+and+Temporal+Reasoning-9781848212527)

### Difficulte : 3/5

---

#### O2 — Raisonnement temporel qualitatif — Algebres d'Allen et STP

Implementer le raisonnement temporel qualitatif base sur l'algebre d'Allen (treize relations d'intervalles : before, after, meets, met-by, overlaps, overlapped-by, starts, started-by, during, contains, finishes, finished-by, equals) et le Simple Temporal Problem (STP) pour les contraintes quantitatives. Le propagateur de contraintes temporelles utilise la fermeture de chemin (path consistency) pour inferer les relations implicites et detecter les inconsistances. L'application porte sur la planification temporelle, la narration interactive ou la verification de scenarios logistiques avec contraintes temporelles.

### Objectifs
- Implementer les treize relations d'Allen et leur table de composition complete
- Construire un propagateur de contraintes temporelles utilisant la path consistency
- Implementer le Simple Temporal Problem (STP) pour les contraintes quantitatives (bornes temporelles)
- Appliquer le raisonneur a la planification temporelle ou a la narration interactive
- Evaluer la complexite et les performances sur des scenarios temporels de taille croissante

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| CSP-8 Temporal CSP | [Search/Part2-CSP/CSP-8-Temporal.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-8-Temporal.ipynb) | CSP temporels, algebre d'Allen, STP |
| Planners-8 Temporal Planning | [SymbolicAI/Planners/03-Advanced/Planners-8-Temporal.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Planners/03-Advanced/Planners-8-Temporal.ipynb) | Planification temporelle, contraintes de temps |
| CSP-4 Scheduling | [Search/Part2-CSP/CSP-4-Scheduling.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-4-Scheduling.ipynb) | Ordonnancement, IntervalVar |
| Search-1 StateSpace | [Search/Part1-Foundations/Search-1-StateSpace.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part1-Foundations/Search-1-StateSpace.ipynb) | Espaces d'etats, recherche temporelle |

### References externes
- Allen, J.F. (1983). "Maintaining Knowledge about Temporal Intervals." *CACM*. [ACM](https://dl.acm.org/doi/10.1145/182.358434)
- Dechter, R. et al. (1991). "Temporal Constraint Networks." *Artificial Intelligence*. [Elsevier](https://www.sciencedirect.com/science/article/pii/0004370291900062)
- Nebel, B. & Burckert, H.J. (1995). "Reasoning about Temporal Relations: A Maximal Tractable Subclass of Allen's Interval Algebra." *JAIR*. [JAIR](https://www.jair.org/index.php/jair/article/view/10170)
- Dylla, F. et al. (2017). "A Survey of Qualitative Temporal and Spatial Reasoning." *KI*. [Springer](https://link.springer.com/article/10.1007/s13218-017-0484-y)

### Difficulte : 3/5

---

#### O3 — Raisonnement de bon sens par graphe de connaissances (Commonsense)

Utiliser des bases de connaissances de bon sens (ConceptNet, ATOMIC) comme source de connaissances factuelles et causales structurees pour ameliorer les reponses d'un systeme de questions-reponses en langage naturel. Le systeme combine le graphe de connaissances (pour la recuperation de faits, les chaines causales et les relations taxonomiques) avec un LLM (pour le raisonnement flexible et la generation de reponses). L'evaluation sur des benchmarks de sens commun (PIQA, CommonsenseQA, CSQA) mesure la contribution marginale du graphe par rapport au LLM seul et identifie les types de questions ou le graphe apporte le plus de valeur.

### Objectifs
- Integrer une base de connaissances de bon sens (ConceptNet ou ATOMIC) dans un pipeline de QA
- Implementer la recherche de chemins et de voisins dans le graphe pour enrichir le contexte du LLM
- Evaluer sur des benchmarks de sens commun (PIQA, CommonsenseQA) avec et sans graphe
- Mesurer la contribution marginale du graphe par rapport au LLM seul sur differents types de questions
- Analyser les categories de questions ou le graphe apporte le plus (ou le moins) de valeur ajoutee

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SW-11 Knowledge Graphs | [SymbolicAI/SemanticWeb/SW-11-Python-KnowledgeGraphs.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-11-Python-KnowledgeGraphs.ipynb) | Graphes de connaissances, RDF, SPARQL |
| SW-12 GraphRAG | [SymbolicAI/SemanticWeb/SW-12-Python-GraphRAG.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-12-Python-GraphRAG.ipynb) | GraphRAG, retrieval augmente par graphe |
| Lean-7 LLM+Symbolique | [SymbolicAI/Lean/Lean-7-LLM-Integration.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-7-LLM-Integration.ipynb) | Integration LLM et connaissances symboliques |
| Argument Analysis | [SymbolicAI/Argument_Analysis/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis) | Raisonnement, evaluation d'arguments |

### References externes
- Liu, H. & Singh, P. (2004). "ConceptNet: A Practical Commonsense Reasoning Tool." *AAAI 2004*. [MIT](https://conceptnet.io/)
- Sap, M. et al. (2019). "ATOMIC: An Atlas of Machine Commonsense." *AAAI 2019*. [AAAI](https://aaai.org/ojs/index.php/AAAI/article/view/4160)
- Bisk, Y. et al. (2020). "PIQA: Reasoning about Physical Commonsense in Natural Language." *AAAI 2020*. [AAAI](https://aaai.org/ojs/index.php/AAAI/article/view/6239)
- Talmor, A. et al. (2019). "CommonsenseQA: A Question Answering Challenge Targeting Commonsense Knowledge." *NAACL 2019*. [ACL Anthology](https://aclanthology.org/N19-1109/)

### Difficulte : 3/5

---

#### O4 — Raisonnement par analogie — theorie du mapping structurel

Implementer un modele computationnel de la Structure-Mapping Theory (Gentner, 1983) qui identifie des analogies entre deux domaines source et cible representes comme des graphes d'entites et de relations structurees. L'algorithme (SME - Structure Mapping Engine) recherche les alignements qui maximisent la coherence structurelle (correspondance des relations de meme ordre) entre les deux domaines, en privilegiant les correspondances relationnelles profondes sur les correspondances superficielles. La comparaison des analogies trouvees par l'algorithme symbolique avec celles generees par un LLM eclaire les differences entre raisonnement analogique formel et raisonnement analogique neurona.

### Objectifs
- Implementer l'algorithme SME (Structure Mapping Engine) pour la recherche d'analogies structurelles
- Represente les domaines source et cible comme des graphes d'entites et de relations typees
- Implementer les criteres de coherence structurelle (systematicity, one-to-one mapping, relational focus)
- Comparer les analogies trouvees par SME avec celles generees par un LLM (GPT-4, Claude)
- Evaluer la qualite des analogies par evaluation humaine et par des metriques de coherence structurelle

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-2 Logiques | [SymbolicAI/Tweety/Tweety-2-Basic-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-2-Basic-Logics.ipynb) | Raisonnement logique, structures relationnelles |
| Lean-7 LLM+Symbolique | [SymbolicAI/Lean/Lean-7-LLM-Integration.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-7-LLM-Integration.ipynb) | Comparaison raisonnement symbolique vs LLM |
| Search-1 StateSpace | [Search/Part1-Foundations/Search-1-StateSpace.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part1-Foundations/Search-1-StateSpace.ipynb) | Espaces d'etats, graphes, matching |
| Argument Analysis | [SymbolicAI/Argument_Analysis/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis) | Raisonnement, comparaison de structures |

### References externes
- Gentner, D. (1983). "Structure-Mapping: A Theoretical Framework for Analogy." *Cognitive Science*. [Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1207/s15516709cog0702_3)
- Forbus, K. et al. (2017). "The Structure-Mapping Engine: An Algorithmic Account of Analogy." *Cognitive Science*. [Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1111/cogs.2017.41.issue-1)
- Webb, T. et al. (2023). "Emergent Analogical Reasoning in Large Language Models." *Nature Human Behaviour*. [Nature](https://www.nature.com/articles/s41562-023-01659-w)
- Holyoak, K.J. & Thagard, P. (1995). *Mental Leaps: Analogy in Creative Thought*. MIT Press. [MIT Press](https://mitpress.mit.edu/9780262581443/mental-leaps/)

### Difficulte : 3/5

---

---

#### O5 — Raisonneur spatio-temporel qualitatif integre : composition RCC8 x Allen, coherence par CSP et extraction depuis le langage naturel

Le raisonnement qualitatif manipule l'espace et le temps par des relations symboliques (« A est a l'interieur de B », « l'evenement X precede Y ») sans coordonnees numeriques — c'est ainsi que les humains raisonnent sur les scenes et les recits. Ce sujet de recherche construit un **raisonneur spatio-temporel qualitatif integre** combinant le calcul spatial **RCC8** (Region Connection Calculus) et l'**algebre d'intervalles d'Allen** (temps). Le coeur formel est la decision de **coherence** d'un reseau de contraintes qualitatives par propagation de contraintes (path-consistency / CSP) — en distinguant les sous-classes traitables des cas NP-difficiles. Le sujet ajoute une dimension neuro-symbolique : **extraire** automatiquement les reseaux de contraintes qualitatives a partir de descriptions en langage naturel (LLM) et **verifier** que le reseau extrait est coherent. Application : comprehension de scenes et de recits.

### Objectifs
1. Implementer les tables de composition et la path-consistency pour RCC8 (espace) et l'algebre d'intervalles d'Allen (temps)
2. Decider la coherence des reseaux de contraintes qualitatives (sous-classes traitables vs algebre complete NP-difficile) via CSP
3. Combiner raisonnement spatial et temporel (scenarios spatio-temporels)
4. Extraire des contraintes qualitatives depuis des descriptions de scenes/recits en langage naturel (LLM) et verifier leur coherence
5. Evaluer sur des scenarios de reference ; analyser les fragments traitables et les modes d'erreur de l'extraction LLM

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| CSP-8 Temporal | [Search/Part2-CSP/CSP-8-Temporal.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-8-Temporal.ipynb) | Contraintes temporelles : base de l'algebre d'Allen |
| CSP-2 Consistency | [Search/Part2-CSP/CSP-2-Consistency.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-2-Consistency.ipynb) | Path-consistency : decision de coherence |
| CSP-1 Fundamentals | [Search/Part2-CSP/CSP-1-Fundamentals.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-1-Fundamentals.ipynb) | Fondements des CSP : modelisation des reseaux qualitatifs |
| CSP-3 Advanced | [Search/Part2-CSP/CSP-3-Advanced.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-3-Advanced.ipynb) | Techniques avancees : sous-classes traitables |
| SW-11 KnowledgeGraphs | [SymbolicAI/SemanticWeb/SW-11-Python-KnowledgeGraphs.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-11-Python-KnowledgeGraphs.ipynb) | Representation des relations spatio-temporelles extraites |
| SL-7 LLM Symbolic Learning | [SymbolicAI/SymbolicLearning/SL-7-LLM-SymbolicLearning.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SymbolicLearning/SL-7-LLM-SymbolicLearning.ipynb) | Extraction de structures symboliques par LLM |

### References externes

**Raisonnement spatial qualitatif**
- Randell, D.A., Cui, Z. & Cohn, A.G. (1992). "A Spatial Logic Based on Regions and Connection." (RCC8) *KR 1992*. [Morgan Kaufmann](https://dl.acm.org/doi/10.5555/3087223.3087246)
- Renz, J. & Nebel, B. (2007). "Qualitative Spatial Reasoning Using Constraint Calculi." *Handbook of Spatial Logics*. [Springer](https://link.springer.com/chapter/10.1007/978-1-4020-5587-4_4)
- Cohn, A.G. & Renz, J. (2008). "Qualitative Spatial Representation and Reasoning." *Handbook of Knowledge Representation*. [Elsevier](https://www.sciencedirect.com/science/article/pii/S1574652607030131)

**Raisonnement temporel qualitatif**
- Allen, J.F. (1983). "Maintaining Knowledge about Temporal Intervals." *Communications of the ACM*, 26(11). [ACM Digital Library](https://dl.acm.org/doi/10.1145/182.358434)
- Vilain, M. & Kautz, H. (1986). "Constraint Propagation Algorithms for Temporal Reasoning." *AAAI 1986*. [AAAI](https://aaai.org/papers/aaai-86-064/)

### Difficulte : 5/5

---

### Categorie P : Verification Formelle des Systemes IA

#### P1 — Verification de robustesse de reseaux de neurones par abstraction

La verification formelle de reseaux de neurones vise a fournir des garanties mathematiques sur le comportement d'un modele face a des perturbations adversariales. Concretement, il s'agit de prouver qu'un classifieur (par exemple sur MNIST ou CIFAR-10) ne change pas sa prediction pour toute image comprise dans une boule L-infinity de rayon epsilon autour d'un echantillon de reference. L'interpretation abstraite permet de propager des ensembles (intervalles, zones, polyhedres) a travers les couches du reseau de maniere saine, tandis que le solving SMT (Reluplex, Marabou) encode chaque neurone comme une contrainte et demande a un solveur si une violation existe. Le defi principal reside dans la scalabilite : les reseaux modernes comptent des millions de parametres, ce qui rend l'exploration exhaustive impossible et necessite des abstractions cleveres. Les methodes recentes comme ERAN combinent zones abstraites et refinement automatique pour atteindre des certificats plus precis. Ce sujet confronte directement l'etudiant a l'interface entre l'apprentissage profond et les methodes formelles classiques.

### Objectifs
- Implementer un verificateur par interpretation abstraite (domaine des intervalles ou des zones) pour un MLP entraine sur MNIST
- Encoder un reseau de neurones comme un systeme de contraintes SMT et utiliser Z3 ou Marabou pour la verification
- Definir et evaluer des proprietes de robustesse L-infinity sur un jeu d'images de test
- Comparer la precision des certificats obtenus par abstraction vs solving SMT sur differents rayons epsilon
- Analyser la scalabilite des approches en fonction de la taille du reseau et de la dimension d'entree

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | SMT solving avec Z3 |
| SC-14 Formal Verification | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb) | Methodes formelles |
| CSP-1 Fondamentaux | [Search/Part2-CSP/CSP-1-Fundamentals.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-1-Fundamentals.ipynb) | Modelisation par contraintes |
| Research/ | [Research/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Research) | Papers et prototypage |

### References externes
- Katz, G. et al. (2017). "Reluplex: An Efficient SMT Solver for Verifying Deep Neural Networks." *CAV 2017*. [Springer](https://doi.org/10.1007/978-3-319-63387-9_5)
- Singh, G. et al. (2019). "An Abstract Domain for Certifying Neural Networks." *POPL 2019*. [ACM](https://doi.org/10.1145/3290354)
- Huang, X. et al. (2020). "A Survey of Safety and Trustworthiness of Deep Neural Networks." *IEEE TNNLS*. [IEEE](https://doi.org/10.1109/TNNLS.2020.2985484)
- Marabou Framework. [GitHub](https://github.com/NeuralNetworkVerification/Marabou)
- ERAN - ETH Zurich. [GitHub](https://github.com/eth-sri/eran)

### Difficulte : 4/5

---

#### P2 — Verification de politiques RL par contraintes formelles

La verification de politiques d'apprentissage par renforcement consiste a garantir que le comportement d'un agent satisfait des proprietes de surete avant son deploiement, en particulier dans des environnements critiques (robotique, vehicules autonomes, systemes medicaux). Les proprietes de surete (absence d'etats interdits, recompense cumulative positive, bornes sur les actions) sont formalisees comme des contraintes logiques sur l'espace d'etats ou sur des abstractions de cet espace. L'approche combine la modelisation formelle avec Z3 et l'analyse de la politique RL apprise, potentiellement representee par un reseau de neurones. Le defi est de couvrir un espace d'etats potentiellement infini ou continu en utilisant des abstractions discretes ou des domaines numeriques. Ce sujet permet d'explorer l'intersection entre la verification formelle et l'apprentissage par renforcement, deux domaines qui convergent dans la recherche actuelle sur l'IA sure.

### Objectifs
- Formaliser des proprietes de surete (etats interdits, bornes de recompense, contraintes d'action) en logique du premier ordre ou en theorie des tableaux
- Implementer un module de verification par solving SMT qui prend une politique RL et un ensemble de proprietes, et retourne satisfiable/violation
- Construire des abstractions de l'espace d'etats (discretisation, partitionnement) pour rendre la verification tractable
- Evaluer sur des environnements Gymnasium (CartPole, MountainCar, GridWorld) avec des politiques entrainees via Stable Baselines3
- Generer des contre-exemples concrets (trajectoires violant la propriete) et les utiliser pour ameliorer la politique

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | SMT solving avec Z3 |
| CSP-1 Fondamentaux | [Search/Part2-CSP/CSP-1-Fundamentals.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-1-Fundamentals.ipynb) | Modelisation par contraintes |
| CSP-3 Consistance | [Search/Part2-CSP/CSP-2-Consistency.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-2-Consistency.ipynb) | Propagation et filtrage |
| Research/ | [Research/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Research) | Prototypage RL + verification |

### References externes
- Fulton, L. & Platzer, A. (2018). "Verifiably Safe Off-Model Reinforcement Learning." *TACAS 2018*. [Springer](https://doi.org/10.1007/978-3-319-89960-2_23)
- Anderson, G. et al. (2024). "Verification of Neural Networks: A Survey." *ACM Computing Surveys*. [ACM](https://doi.org/10.1145/3638 perting)
- Dreossi, T. et al. (2017). "Compositional Falsification of Cyber-Physical Systems with Machine Learning Components." *NASA Formal Methods*. [Springer](https://doi.org/10.1007/978-3-319-57288-8_24)
- Stable Baselines3 Documentation. [stable-baselines3.readthedocs.io](https://stable-baselines3.readthedocs.io/)
- Z3 SMT Solver. [GitHub](https://github.com/Z3Prover/z3)

### Difficulte : 4/5

---

#### P3 — Specification et verification de securite d'agents LLM par logique temporelle

Les agents bases sur des grands modeles de langage (LLM) interagissent avec des environnements complexes via des appels d'outils, des requetes API et des dialogues multi-tours. Verifier formellement leur surete necessite de specifier des proprietes temporelles telles que "l'agent ne revele jamais d'informations privees" ou "l'agent respecte toujours le protocole de communication" en logique temporelle lineaire (LTL) ou en logique arborescente de calcul (CTL). L'approche consiste a collecter des traces d'execution de l'agent, a construire un modele abstrait (automate ou Kripke structure) de son comportement, puis a appliquer un model checker pour verifier les proprietes. Le defi est de gerer l'espace d'etats potentiellement infini des dialogues et des actions, tout en capturant les comportements emergents des LLM. Ce sujet est en pointe dans la recherche 2024-2026 sur la verification des systemes d'IA agentic.

### Objectifs
- Specifier des proprietes de securite pour un agent LLM en logique LTL et CTL (confidentialite, respect de protocole, bornes de comportement)
- Implementer un collecteur de traces d'execution qui enregistre les actions, observations et reponses d'un agent LLM
- Construire un modele abstrait (Kripke structure) a partir des traces collectees
- Implementer un model checker simplifie (ou utiliser NuSMV) pour la verification des proprietes temporelles
- Evaluer sur des scenarios concrets (chatbot avec outils, agent de recherche, assistant code) et identifier les violations

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | SMT/SAT solving |
| Tweety-3 Modal Logic | [SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb) | Logiques modales et temporelles |
| SC-14 Formal Verification | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb) | Verification formelle |
| Research/ | [Research/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Research) | Papers emergents |

### References externes
- AgentVerify (2026). "Compositional Formal Verification of AI Agent Safety." *arXiv*. [arXiv](https://arxiv.org/abs/2502.01374)
- Baier, C. & Katoen, J.-P. (2008). *Principles of Model Checking*. MIT Press. [MIT Press](https://mitpress.mit.edu/9780262028499/principles-of-model-checking/)
- Formal Methods in the Agentic AI Era: A Strategic Agenda (2026). *arXiv*. [arXiv](https://arxiv.org/abs/2501.04560)
- NuSMV Model Checker. [nusmv.fbk.eu](https://nusmv.fbk.eu/)
- Li, J. et al. (2024). "LLM Agent Safety: A Survey." *arXiv*. [arXiv](https://arxiv.org/abs/2406.07088)

### Difficulte : 4/5

---

#### P4 — Robustesse formelle des reseaux de neurones binaires par le Sensitivity Theorem

Les reseaux de neurones binaires (Binarized Neural Networks, BNN) remplacent tous les poids et activations par des valeurs dans {-1, +1}, transformant le reseau en une fonction booleenne pure. Cette binarisation rend la verification formelle potentiellement tractable : un BNN a n entrees definit une fonction f : {-1,+1}^n -> {-1,+1} dont on peut analyser les proprietes combinatoires. Le Sensitivity Theorem (Huang 2019, Annals of Mathematics) etablit que la sensibilite s(f) d'une fonction booleenne (nombre de bits d'entree dont le changement peut inverser la sortie) est minoree par sqrt(deg(f)), ou deg(f) est le degre du polynome de Fourier-Walsh representant f. Cette borne fournit un certificat de robustesse adversariale en distance de Hamming : si s(f) est eleve, un adversaire doit modifier beaucoup de bits pour changer la classification. Ce sujet ambitionne de formaliser cette jonction en Lean 4 en combinant le framework TorchLean (Lean-11, verification de NN en Lean) avec le port du Sensitivity Theorem (Lean-12, sensitivity_lean/), pour produire des certificats de robustesse certififs pour des BNN sur des exemples jouets (XOR, parite, MNIST binarise). C'est un sujet research-grade, potentiellement publiable.

### Objectifs
- Comprendre les BNN et leur representation comme fonctions booleennes : implementation Python d'un BNN jouet (XOR-4bit, parite-3bit) avec calcul du polynome de Fourier-Walsh
- Etudier le Sensitivity Theorem de Huang et sa preuve combinatoire, et formaliser le lien sensibilite -> robustesse Hamming
- Utiliser TorchLean (Lean-11) pour definir formellement un BNN en Lean 4 et enoncer le theoreme de robustesse
- Importer sensitivity_lean (Lean-12) pour deriver la borne sqrt(deg(f)) et produire un certificat formel
- Evaluer la borne sur des exemples jouets et discuter les limites (passage a l'echelle, robustesse worst-case vs average)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Lean-11 TorchLean | [SymbolicAI/Lean/Lean-11-TorchLean.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-11-TorchLean.ipynb) | Framework Lean 4 pour verification de NN |
| Lean-12 Sensitivity Theorem | [SymbolicAI/Lean/Lean-12-Sensitivity-Theorem.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-12-Sensitivity-Theorem.ipynb) | Sensitivity Theorem, port Lean de Huang 2019 |
| sensitivity_lean/ | [SymbolicAI/Lean/sensitivity_lean/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/SymbolicAI/Lean/sensitivity_lean/) | Module Lean formel, theoreme principal |
| Lean-8 NeuroSymbolic | [SymbolicAI/Lean/Lean-8-Agentic-Proving.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-8-Agentic-Proving.ipynb) | Architectures neural-symboliques |

### References externes
- Huang, H. (2019). "Induced Subgraphs of Hypercubes and a Proof of the Sensitivity Conjecture." *Annals of Mathematics*, 190(3), 871-881. [arXiv](https://arxiv.org/abs/1907.00847)
- Hubara, I. et al. (2016). "Binarized Neural Networks." *NeurIPS 2016*. [NeurIPS](https://proceedings.neurips.cc/paper/2016/hash/d8330f857a17c53d217014ee776bfd50-Abstract.html)
- Narodytska, N. et al. (2018). "Verifying Properties of Binarized Deep Neural Networks." *AAAI 2018*. [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/12177)
- Courbariaux, M. et al. (2015). "BinaryConnect: Training Deep Neural Networks with binary weights during propagations." *NeurIPS 2015*. [arXiv](https://arxiv.org/abs/1511.00363)
- O'Donnell, R. (2014). *Analysis of Boolean Functions*. Cambridge University Press. [analysisofbooleanfunctions.net](https://analysisofbooleanfunctions.net/)

### Difficulte : 5/5

---

### Categorie Q : Raisonnement Ethique et Normatif

#### Q1 — Raisonneur deontique — logique des normes et obligations

La logique deontique est la branche de la logique formelle qui traite des concepts normatifs : obligations (O), permissions (P) et interdictions (F). Implementer un raisonneur deontique permet de verifier automatiquement si un plan d'action, une politique ou un reglement satisfait un ensemble de normes donnees. Le defi central est la gestion des conflicts normatifs : deux normes peuvent exiger des actions contradictoires (par exemple, "il est interdit de mentir" vs "il est obligatoire de proteger la vie privee"), necessitant des strategies de resolution (priorite, specialisation, defeasibility). Ce sujet combine la logique formelle avec l'informatique ethique, et trouve des applications dans la conception de systemes d'IA conformes aux reglementations (RGPD, AI Act). L'implementation s'appuie sur Z3 ou le framework TweetyProject pour le solving de contraintes logiques deontiques.

### Objectifs
- Implementer un systeme de logique deontique avec les operateurs O (obligation), P (permission), F (interdiction) et leurs axiomes classiques (D-serie)
- Encoder un ensemble de normes et un plan d'action, et verifier la conformite du plan aux normes par solving
- Detecter les conflicts normatifs (obligations contradictoires, obligations vs interdictions) et les signaler
- Implementer au moins une strategie de resolution de conflicts (priorite lexicographique, specialisation, ou defeasible reasoning)
- Evaluer le raisonneur sur des scenarios reels (politiques de confidentialite, codes deontologiques medicaux)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-2 Advanced Logics | [SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb) | Logiques avancees, deontique |
| Tweety-3 Modal Logic | [SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb) | Semantique des mondes possibles |
| Tweety-9 Preferences | [SymbolicAI/Tweety/Tweety-9-Preferences.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-9-Preferences.ipynb) | Raisonnement sur les preferences |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Solving de contraintes |

### References externes
- von Wright, G.H. (1951). "Deontic Logic." *Mind*, 60(237), 1-15. [JSTOR](https://www.jstor.org/stable/2251384)
- McNamara, P. (2023). "Deontic Logic." *Stanford Encyclopedia of Philosophy*. [SEP](https://plato.stanford.edu/entries/logic-deontic/)
- Governatori, G. & Rotolo, A. (2006). "Logic of Violations: A Gentzen System for Reasoning with Contrary-to-Duty Obligations." *DEON 2006*. [Springer](https://doi.org/10.1007/11786849_9)
- TweetyProject. [tweetyproject.org](https://tweetyproject.org/)
- Carmo, J. & Jones, A.J.I. (2002). "Deontic Logic and Contrary-to-Duties." *Handbook of Philosophical Logic*. [Springer](https://doi.org/10.1007/978-94-010-0388-9_4)

### Difficulte : 3/5

---

#### Q2 — Verification d'alignement de valeurs par methodes formelles

L'alignement des valeurs d'un systeme d'IA designe le probleme de s'assurer que le comportement du systeme est conforme a un ensemble de valeurs ethiques specifiees (equite, non-discrimination, minimisation du dommage, transparence). Ce sujet propose d'aborder ce probleme de maniere formelle en encodant ces valeurs comme des contraintes logiques ou mathematiques, puis en verifiant qu'un systeme d'IA donne (classifieur binaire, politique RL, modele de decision) les satisfait sur un espace d'entrees pertinent. L'approche formelle permet de trouver des contre-exemples concrets (cas ou le systeme viole une valeur) via le solving SMT, complementant les approches statistiques classiques. Ce sujet se situe au carrefour de la verification formelle, de l'ethique de l'IA et de l'equite algorithmique, et prepare les etudiants aux enjeux reglementaires (AI Act europeen).

### Objectifs
- Formaliser des valeurs ethiques (equite demographique, parite, egalite des chances, non-discrimination) comme des contraintes formelles en logique du premier ordre
- Implementer un module de verification par solving SMT (Z3) qui prend un modele d'IA et des contraintes de valeurs, et detecte les violations
- Utiliser le testing symbolique pour generer des contre-exemples concrets mettant en evidence les biais du modele
- Integrer des metriques d'equite existantes (Fairlearn) comme proprietes supplementaires a verifier
- Evaluer sur des jeux de donnees publics (COMPAS, Adult Income, German Credit) avec des modeles entraines

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | SMT solving pour contre-exemples |
| Tweety-9 Preferences | [SymbolicAI/Tweety/Tweety-9-Preferences.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-9-Preferences.ipynb) | Preferences et compromis ethiques |
| Research/ | [Research/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Research) | Prototypage fairness + SMT |
| CSP-1 Fondamentaux | [Search/Part2-CSP/CSP-1-Fundamentals.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-1-Fundamentals.ipynb) | Modelisation par contraintes |

### References externes
- Gabriel, I. (2020). "Artificial Intelligence, Values, and Alignment." *Minds and Machines*, 30, 411-437. [Springer](https://doi.org/10.1007/s11023-020-09539-2)
- NIST AI Risk Management Framework (2023). [nist.gov](https://www.nist.gov/itl/ai-risk-management-framework)
- Albarghouthi, A. et al. (2020). "Fairness as a Program Property." *PLDI 2020*. [ACM](https://doi.org/10.1145/3385412.3386036)
- Fairlearn Toolkit. [fairlearn.org](https://fairlearn.org/)
- EuGenAI: Ethics-Guided AI (2025). [eugenai.eu](https://eugenai.eu/)

### Difficulte : 4/5

---

#### Q3 — Raisonnement juridique formel par argumentation et logique

Le raisonnement juridique est par nature argumentatif : plusieurs interpretations d'une loi, plusieurs precedents, et des exceptions rendent le processus de decision complexe et contextuel. Ce sujet propose de modeliser un corpus de regles juridiques (par exemple en droit du travail ou droit de la consommation) en logique formelle, puis d'utiliser les frameworks d'argumentation de Dung et ASPIC+ pour structurer le raisonnement sur des cas juridiques concrets. L'argumentation permet de gerer les conflicts de normes, les exceptions et les raisonnements defeasibles de maniere naturelle, en construisant un graphe d'arguments dont l'evaluation determine les conclusions acceptees. L'implementation avec TweetyProject donne acces a des solveurs d'argumentation matures. Ce sujet prepare les etudiants aux applications de l'IA dans le domaine juridique (LegalTech, compliance automatisee).

### Objectifs
- Modeliser un corpus de regles juridiques en logique propositionnelle ou du premier ordre, en identifiant les normes, exceptions et conditions
- Implementer un framework d'argumentation de Dung (graphes d'attaque, extensions preferees/stables/grounded)
- Etendre le framework avec ASPIC+ pour gerer les arguments structurels (regles strictes vs defeasibles)
- Evaluer le systeme sur des cas juridiques reels (jurisprudence, cas d'ecoles) et comparer avec les decisions humaines
- Analyser les limites de la modelisation logique face a l'ambiguite du langage naturel juridique

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-5 Argumentation | [SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb) | Frameworks de Dung, ASPIC+ |
| Tweety-6 Structured Argumentation | [SymbolicAI/Tweety/Tweety-6-Structured-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-6-Structured-Argumentation.ipynb) | Argumentation structuree |
| SW-7 OWL Ontologies | [SymbolicAI/SemanticWeb/SW-7b-Python-OWL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-7b-Python-OWL.ipynb) | Representation de connaissances juridiques |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Solving de contraintes |

### References externes
- Prakken, H. & Sartor, G. (2015). "Law and Logic: A Review from an Argumentation Perspective." *Artificial Intelligence*, 227, 214-246. [Elsevier](https://doi.org/10.1016/j.artint.2015.06.004)
- Wyner, A. & Bench-Capon, T. (2020). "Argumentation and Legal Text." *Handbook of Formal Argumentation*. [College Publications](https://www.collegepublications.co.uk/handbooks/?00024)
- Dung, P.M. (1995). "On the Acceptability of Arguments and its Fundamental Role in Nonmonotonic Reasoning, Logic Programming, and n-Person Games." *Artificial Intelligence*, 77(2), 321-357. [Elsevier](https://doi.org/10.1016/0004-3702(94)00041-X)
- TweetyProject. [tweetyproject.org](https://tweetyproject.org/)
- Bench-Capon, T. & Dunne, P.E. (2007). "Argumentation in Artificial Intelligence." *Artificial Intelligence*, 171(10-15), 619-641. [Elsevier](https://doi.org/10.1016/j.artint.2007.05.001)

### Difficulte : 3/5

---

#### Q4 — Agent conforme par construction : raisonneur deontique, garde-fou normatif (shield) et tracabilite reglementaire (AI Act / RGPD)

A mesure que les systemes d'IA sont soumis a des cadres reglementaires (AI Act europeen, RGPD), se pose la question : comment garantir qu'un agent *respecte* les normes, et le *prouver* ? Ce sujet de recherche conçoit un **agent conforme par construction** dont les actions sont filtrees par un **raisonneur deontique** (obligations, permissions, interdictions) compile en garde-fou (shield) d'execution. Le coeur symbolique formalise un sous-ensemble de normes (regles de l'AI Act / RGPD) en **logique deontique** (SDL etendue de mecanismes *defaisables* pour gerer les obligations contraires-au-devoir, CTD), detecte et resout les conflits normatifs, et produit pour chaque decision un **certificat de tracabilite** citant les normes applicables. L'ambition est de relier le comportement de l'agent a une garantie de conformite *verifiable*, tout en analysant honnetement les limites de la formalisation du droit (gap is/ought, interpretation).

### Objectifs
1. Formaliser un corpus normatif (sous-ensemble de l'AI Act / RGPD) en logique deontique (SDL + extensions defaisables pour les CTD)
2. Construire un raisonneur deontique detectant obligations/permissions/interdictions et resolvant les conflits normatifs
3. Compiler les normes en un garde-fou (shield) d'execution filtrant les actions de l'agent (conformite par construction)
4. Produire, pour chaque decision, un certificat de tracabilite citant les normes applicables
5. Evaluer sur des scenarios de cas ; analyser la resolution de conflits, le gap is/ought et les limites de la formalisation juridique

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-2 Basic Logics | [SymbolicAI/Tweety/Tweety-2-Basic-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-2-Basic-Logics.ipynb) | Logiques de base : fondement du raisonneur |
| Tweety-3 Advanced Logics | [SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb) | Logiques modales/deontiques avancees -- coeur du sujet |
| Tweety-5 Abstract Argumentation | [SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb) | Resolution de conflits normatifs par argumentation |
| SK-3 Agents | [GenAI/SemanticKernel/03-SemanticKernel-Agents.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GenAI/SemanticKernel/03-SemanticKernel-Agents.ipynb) | Agent dont les actions sont gardees par le shield |
| SK-4 Filters & Observability | [GenAI/SemanticKernel/04-SemanticKernel-Filters-Observability.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GenAI/SemanticKernel/04-SemanticKernel-Filters-Observability.ipynb) | Filtres et tracabilite des decisions |
| Argument_Analysis 3-orchestration | [SymbolicAI/Argument_Analysis/Argument_Analysis_Agentic-3-orchestration.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Argument_Analysis/Argument_Analysis_Agentic-3-orchestration.ipynb) | Orchestration du raisonnement normatif |

### References externes

**Logique deontique et raisonnement normatif**
- von Wright, G.H. (1951). "Deontic Logic." *Mind*, 60(237), 1-15. [Oxford](https://doi.org/10.1093/mind/LX.237.1)
- Gabbay, D. et al. (eds.) (2013). *Handbook of Deontic Logic and Normative Systems*. College Publications. [College Publications](https://www.collegepublications.co.uk/handbooks/)
- Governatori, G. et al. (2013). "Computing Strong and Weak Permissions in Defeasible Logic." *Journal of Philosophical Logic*, 42(6). [Springer](https://link.springer.com/article/10.1007/s10992-013-9295-1)

**Conformite et reglementation de l'IA**
- Nute, D. (ed.) (1997). *Defeasible Deontic Logic*. Springer. [Springer](https://link.springer.com/book/10.1007/978-94-015-8851-5)
- Union Europeenne (2024). "Regulation (EU) 2024/1689 (AI Act)." *Official Journal of the EU*. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)

### Difficulte : 5/5

---

### Categorie R : Raisonnement sous Incertitude et Revision des Croyances

#### R1 — Revision des croyances par les postulats AGM

La revision des croyances est le processus par lequel un agent rationnel met a jour ses croyances face a de nouvelles informations potentiellement contradictoires. Le cadre theorique AGM (Alchourron-Gardenfors-Makinson, 1985) definit les postulats rationnels que doit satisfaire toute operation de revision : succes (la nouvelle information est acceptee), coherence (les croyances restent consistantes), et minimalite (le changement est le plus petit possible). Implementer un systeme conforme a AGM necessite de definir un pre-ordre sur les mondes possibles (ou les interpretations) qui guide le choix des croyances a abandonner. Les strategies classiques (revision lexicographique, distance de Dalal, revision basee sur la distance) offrent differents compromis entre expressivite et complexite calculatoire. Ce sujet est fondamental pour tout systeme d'IA qui doit raisonner avec des connaissances evolutives et potentiellement bruitees.

### Objectifs
- Implementer les operations de revision, contraction et expansion conformement aux postulats AGM sur la logique propositionnelle
- Definir et implementer au moins trois strategies de revision (lexicographique, Dalal, distance-based) et comparer leurs comportements
- Verifier formellement que chaque strategie satisfait les postulats AGM a l'aide de tests systematiques
- Evaluer la complexite calculatoire de chaque strategie en fonction du nombre de variables propositionnelles
- Appliquer le systeme a des scenarios concrets (mise a jour d'une base de connaissances, integration d'informations sensorielles contradictoires)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-4 Belief Revision | [SymbolicAI/Tweety/Tweety-4-Belief-Revision.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-4-Belief-Revision.ipynb) | AGM, revision, contraction |
| Tweety-2 Advanced Logics | [SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb) | Logiques non-classiques |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Consistance, SAT solving |
| Research/ | [Research/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Research) | Prototypage avance |

### References externes
- Alchourron, C.E., Gardenfors, P. & Makinson, D. (1985). "On the Logic of Theory Change: Partial Meet Contraction and Revision Functions." *Journal of Symbolic Logic*, 50(2), 510-530. [JSTOR](https://www.jstor.org/stable/2274239)
- Gardenfors, P. (1988). *Knowledge in Flux: Modeling the Dynamics of Epistemic States*. MIT Press. [MIT Press](https://mitpress.mit.edu/9780262571798/knowledge-in-flux/)
- Hansson, S.O. (1999). *A Textbook of Belief Dynamics: Theory Change and Database Updating*. Springer. [Springer](https://doi.org/10.1007/978-94-015-9225-0)
- Dalal, M. (1988). "Investigations into a Theory of Knowledge Base Revision." *AAAI 1988*. [AAAI](https://dl.acm.org/doi/10.5555/186936.186980)
- Peppas, P. (2008). "Belief Revision." *Handbook of Knowledge Representation*, Elsevier. [Elsevier](https://doi.org/10.1016/S1574-6526(07)03009-3)

### Difficulte : 3/5

---

#### R2 — Programmation probabiliste avec Infer.NET

La programmation probabiliste offre un paradigme unifie pour exprimer des modeles probabilistes et executer l'inference automatiquement, sans deriver manuellement les equations de mise a jour. Infer.NET, developpe par Microsoft Research, permet de definir des modeles generatifs en C# ou F# et d'effectuer l'inference par messages (Expectation Propagation, Variational Message Passing). Ce sujet invite a modeliser des problemes classiques de raisonnement sous incertitude (inference bayesienne sur des reseaux causaux, melange de gaussiennes, classification avec incertitude, prediction avec intervalles de confiance) et a comparer les resultats avec l'approche symbolique classique (logique monotone, deduction certaine). L'enjeu est de comprendre quand l'approche probabiliste est necessaire (donnees bruitees, incertitude irreductible) et quand l'approche symbolique suffit (certitudes logiques, raisonnement exact).

### Objectifs
- Modeliser au moins trois problemes de raisonnement sous incertitude en programmation probabiliste avec Infer.NET (inference bayesienne, melange de modeles, prediction)
- Implementer l'inference par messages (Expectation Propagation et/ou Variational Message Passing) et comparer la precision et la rapidite
- Construire une version logique symbolique (logique propositionnelle ou du premier ordre) des memes problemes et comparer les resultats
- Evaluer les limites de chaque approche sur des scenarios avec des niveaux d'incertitude croissants
- Prototyper un mini-modele hybride combinant contraintes logiques dures et variables probabilistes

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Research/ | [Research/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Research) | Infer.NET, reseaux bayesiens |
| Probas Infer-101 | [Probas/Infer-101.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Probas/Infer-101.ipynb) | Infer.NET tutoriel |
| Probas PyMC HMM | [Probas/PyMC-HMM-Trading-Alpha.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Probas/PyMC-HMM-Trading-Alpha.ipynb) | PyMC, modeles hierarchiques |
| Probas Pyro RSA | [Probas/Pyro_RSA_Hyperbole.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Probas/Pyro_RSA_Hyperbole.ipynb) | Pyro, inférence variotionnelle |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Solving deterministe vs probabiliste |
| Tweety-4 Belief Revision | [SymbolicAI/Tweety/Tweety-4-Belief-Revision.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-4-Belief-Revision.ipynb) | Revision et incertitude |
| CSP-5 Optimization | [Search/Part2-CSP/CSP-5-Optimization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Search/Part2-CSP/CSP-5-Optimization.ipynb) | Optimisation sous contraintes |

### References externes
- Minka, T. et al. (2018). *Infer.NET 2: Bayesian Inference in .NET*. Microsoft Research. [Microsoft Research](https://dotnet.github.io/infer/)
- Ghahramani, Z. (2015). "Probabilistic Machine Learning and Artificial Intelligence." *Nature*, 521, 452-459. [Nature](https://doi.org/10.1038/nature14541)
- Gordon, A.D. et al. (2014). "Probabilistic Programming." *Future of Software Engineering (FOSE)*. [ACM](https://doi.org/10.1145/2593882.2593900)
- PyMC Documentation. [pymc.io](https://www.pymc.io/)
- Goodfellow, I., Bengio, Y. & Courville, A. (2016). *Deep Learning*, Chapter 3: Probability and Information Theory. [deeplearningbook.org](https://www.deeplearningbook.org/contents/prob.html)

### Difficulte : 3/5

---

#### R3 — Raisonnement epistemique et logique multi-agents

La logique epistemique formalise le raisonnement sur la connaissance et la croyance d'agents rationnels. Dans un systeme multi-agents, chaque agent possede des informations partielles et doit raisonner non seulement sur l'etat du monde, mais aussi sur ce que les autres agents savent ou croient. Les classiques puzzles du domaine (muddy children, somme et produit, menteurs et truth-tellers) illustrent comment la connaissance partagee (common knowledge) et la connaissance mutuelle permettent des raisonnements surprenants. L'implementation d'un systeme de raisonnement epistemique necessite de definir des modeles de Kripke multi-agents, des operateurs de connaissance individuelle et partagee, et des mecanismes de mise a jour apres des actions d'observation ou de communication publique. Ce sujet est central pour la theorie des jeux epistémiques, les protocoles cryptographiques et la verification de systemes multi-agents.

### Objectifs
- Implementer un modele de Kripke multi-agents avec des relations d'accessibilite par agent et des evaluateurs de formules epistemiques
- Coder et resoudre formellement les puzzles classiques (muddy children, somme et produit, menteurs) en utilisant le systeme
- Implementer les operateurs de connaissance individuelle (K_i), connaissance mutuelle (E), et connaissance commune (C) avec leur semantique
- Modeliser des scenarios avec information privee (encheres, jeux a information incomplete, protocoles de communication) et raisonner sur les croyances
- Etendre le systeme avec la logique epistemique dynamique (public announcements, actions d'observation) pour capturer l'evolution des connaissances

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-3 Modal Logic | [SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb) | Logiques modales, Kripke |
| GameTheory/11 Bayesian Games | [GameTheory/GameTheory-11-BayesianGames.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-11-BayesianGames.ipynb) | Information asymetrique |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Solving de contraintes |
| Research/ | [Research/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Research) | Prototypage epistemique |

### References externes
- Fagin, R. et al. (1995). *Reasoning About Knowledge*. MIT Press. [MIT Press](https://mitpress.mit.edu/9780262562003/reasoning-about-knowledge/)
- Ditmarsch, H. van et al. (2007). *Dynamic Epistemic Logic*. Springer. [Springer](https://doi.org/10.1007/978-1-4020-5839-4)
- Meyer, J.-J.Ch. & Hoek, W. van der (1995). *Epistemic Logic for AI and Computer Science*. Cambridge University Press. [Cambridge](https://doi.org/10.1017/CBO9780511569887)
- Ditmarsch, H. van (2023). "Epistemic Logic." *Stanford Encyclopedia of Philosophy*. [SEP](https://plato.stanford.edu/entries/logic-epistemic/)
- Baltag, A. & Moss, L.S. (2004). "Logics for Epistemic Programs." *Knowledge, Rationality and Action*, Synthese, 139(2), 165-224. [Springer](https://doi.org/10.1023/B:SYNT.0000024912.74661.2c)

### Difficulte : 4/5

---

#### R4 — Agent de decision sequentielle a croyances revisees : fusion AGM symbolique et inference bayesienne sous information contradictoire

Un agent qui agit dans la duree doit mettre a jour ses croyances face a des informations nouvelles, parfois contradictoires — et deux traditions repondent a ce probleme : la **revision des croyances AGM** (symbolique, pour les contraintes logiques dures et la restauration de coherence) et l'**inference bayesienne** (probabiliste, pour les degres de croyance face a des evidences incertaines). Ce sujet de recherche construit un agent qui *fusionne* les deux : AGM pour maintenir l'integrite logique de la base de connaissances, Bayes pour graduer la confiance, et un module de **decision sequentielle** (reseaux de decision, valeur de l'information, utilite esperee) pour agir. Le coeur du sujet est l'**interaction** entre les deux mecanismes face a des observations contradictoires : quand restaurer la coherence par AGM, quand simplement reponderer par Bayes, et comment les articuler de maniere principielle.

### Objectifs
1. Implementer la revision des croyances AGM (postulats, contraction/revision) sur une base de connaissances logique
2. La coupler a une mise a jour bayesienne (graphes de facteurs / reseaux bayesiens) pour les evidences incertaines
3. Realiser la decision sequentielle via des reseaux de decision / utilite esperee + valeur de l'information
4. Gerer les observations contradictoires : restaurer la coherence logique (AGM) et mettre a jour les probabilites (Bayes), etudier l'interaction
5. Evaluer sur un scenario sequentiel (diagnostic / monitoring), en comparant Bayes pur vs hybride AGM+Bayes

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-4 Belief Revision | [SymbolicAI/Tweety/Tweety-4-Belief-Revision.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-4-Belief-Revision.ipynb) | AGM, contraction, revision -- coeur symbolique |
| Infer-4 Bayesian Networks | [Probas/Infer/Infer-4-Bayesian-Networks.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Probas/Infer/Infer-4-Bayesian-Networks.ipynb) | Reseaux bayesiens : mise a jour probabiliste |
| Infer-17 Decision Networks | [Probas/Infer/Infer-17-Decision-Networks.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Probas/Infer/Infer-17-Decision-Networks.ipynb) | Reseaux de decision : utilite esperee |
| Infer-18 Value of Information | [Probas/Infer/Infer-18-Decision-Value-Information.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Probas/Infer/Infer-18-Decision-Value-Information.ipynb) | Valeur de l'information : quelles observations acquerir |
| Infer-20 Decision Sequential | [Probas/Infer/Infer-20-Decision-Sequential.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Probas/Infer/Infer-20-Decision-Sequential.ipynb) | Decision sequentielle -- coeur de l'action dans la duree |
| PyMC-4 Bayesian Networks | [Probas/PyMC/PyMC-4-Bayesian-Networks.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Probas/PyMC/PyMC-4-Bayesian-Networks.ipynb) | Alternative PyMC pour l'inference probabiliste |

### References externes

**Revision des croyances (AGM)**
- Alchourron, C.E., Gardenfors, P. & Makinson, D. (1985). "On the Logic of Theory Change: Partial Meet Contraction and Revision Functions." *Journal of Symbolic Logic*, 50(2). [JSTOR](https://www.jstor.org/stable/2274239)
- Gardenfors, P. (1988). *Knowledge in Flux: Modeling the Dynamics of Epistemic States*. MIT Press. [MIT Press](https://mitpress.mit.edu/9780262571798/knowledge-in-flux/)
- Spohn, W. (1988). "Ordinal Conditional Functions: A Dynamic Theory of Epistemic States." *Causation in Decision, Belief Change, and Statistics*. [Springer](https://link.springer.com/chapter/10.1007/978-94-009-2865-7_6)

**Inference probabiliste et decision**
- Pearl, J. (1988). *Probabilistic Reasoning in Intelligent Systems*. Morgan Kaufmann. [Elsevier](https://www.sciencedirect.com/book/9780080514895/)
- Howard, R.A. & Matheson, J.E. (1984). "Influence Diagrams." *Readings on the Principles and Applications of Decision Analysis*. [INFORMS](https://pubsonline.informs.org/doi/10.1287/deca.1050.0020)

### Difficulte : 5/5

---

### Categorie S : Trading Algorithmique Symbolique

#### S1 — Raisonnement epistemique pour le trading multi-agents

La logique epistemique formalise le raisonnement sur la connaissance et la croyance d'agents rationnels dans un systeme multi-agents. Appliquee au trading algorithmique, elle permet de modeliser l'information asymetrique entre participants du marche : chaque agent possede des croyances partielles sur l'etat du marche et doit raisonner sur ce que les autres agents savent (ou croient savoir) a partir du flux d'ordres observable. Les modeles de Kripke multi-agents capturant ces croyances imbriquees, combines aux mecanismes de mise a jour par annonce publique (Dynamic Epistemic Logic), offrent un cadre formel pour deduire l'information privee a partir du comportement observable. Ce sujet demande d'implementer un systeme de raisonnement epistemique complet (modeles de Kripke, operateurs Ki/E/C, public announcements) et de l'appliquer a des scenarios de marche simule puis valide par backtest QuantConnect.

### Objectifs
- Implementer un modele de Kripke multi-agents avec relations d'accessibilite par agent et evaluateur de formules epistemiques (Ki, E, C)
- Modeliser des scenarios de marche a information asymetrique (insider trading, adverse selection, signal par ordres) et raisonner sur les croyances inferees
- Implementer les mises a jour epistemiques dynamiques (public announcements, observation privee) via Dynamic Epistemic Logic
- Simuler un mecanisme de market-making ou le raisonnement epistemique guide les decisions d'achat/vente en deduisant l'information privee du flux d'ordres
- Valider par backtest QuantConnect Lean sur donnees reelles de marche avec la strategie epistemique contre un baseline aleatoire

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-3 Modal Logic | [SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb) | Logiques modales, modeles de Kripke |
| Lean-3 Propositions | [SymbolicAI/Lean/Lean-3-Propositions-Proofs.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-3-Propositions-Proofs.ipynb) | Preuve formelle de proprietes epistemiques en Lean 4 |
| GT-11 Bayesian Games | [GameTheory/GameTheory-11-BayesianGames.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-11-BayesianGames.ipynb) | Information asymetrique, croyances |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Resolution de contraintes |
| QC-Py-08 Multi-Asset | [QuantConnect/Python/QC-Py-08-Multi-Asset-Strategies.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-08-Multi-Asset-Strategies.ipynb) | Strategies multi-actifs, correlations |
| QC-Py-13 Alpha Models | [QuantConnect/Python/QC-Py-13-Alpha-Models.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-13-Alpha-Models.ipynb) | Modeles alpha, signaux |

### References externes
- Fagin, R. et al. (1995). *Reasoning About Knowledge*. MIT Press. [MIT Press](https://mitpress.mit.edu/9780262562003/reasoning-about-knowledge/)
- Ditmarsch, H. van et al. (2007). *Dynamic Epistemic Logic*. Springer. [Springer](https://doi.org/10.1007/978-1-4020-5839-4)
- Kyle, A.S. (1985). "Continuous Auctions and Insider Trading." *Econometrica*, 53(6), 1315-1335. [JSTOR](https://www.jstor.org/stable/1913210)
- Ditmarsch, H. van (2023). "Epistemic Logic." *Stanford Encyclopedia of Philosophy*. [SEP](https://plato.stanford.edu/entries/logic-epistemic/)
- O'Hara, M. (1995). *Market Microstructure Theory*. Blackwell. [Wiley](https://www.wiley.com/en-us/Market+Microstructure+Theory-p-9780631207610)

### Difficulte : 4/5

---

#### S2 — Ontologies financieres et Web Semantique pour le screening d'actifs

Le Web Semantique offre un cadre formel pour representer, interroger et raisonner sur des connaissances structurees via des ontologies (OWL), des requetes (SPARQL) et des mecanismes de raisonnement (description logics, DL). Applique au screening d'actifs financiers, ce paradigme permet de capturer des relations semantiques entre entites (societes, secteurs, filiales, produits, risques ESG) qu'un filtrage numerique classique ne peut pas exprimer : une requete SPARQL peut deduire qu'une societe est exposee au lithium via sa filiale miniere, ou detecter un greenwashing en confrontant les declarations ESG a la structure reelle du groupe. Le raisonnement DL (subsomption, classification automatique, coherence) ajoute une couche deductive qui enrichit l'ontologie au-dela des faits explicitement encodes. Ce sujet demande de construire une ontologie financiere, de l'interroger par SPARQL, et de valider les decisions de screening par backtest QuantConnect.

### Objectifs
- Construire une ontologie financiere en OWL couvrant societes, secteurs, filiales, instruments, risques ESG et classifications regulatorires (GICS, NACE)
- Implementer un raisonneur DL (classification, subsomption, detection d'incoherence) et l'appliquer pour inferer des classifications automatiques (style drift, exposition sectorielle cachee, greenwashing)
- Developper des requetes SPARQL pour le screening semantique d'actifs et comparer les resultats avec un filtrage numerique classique
- Valider les decisions de screening par backtest QuantConnect Lean sur l'univers S&P 500 avec rebalance trimestriel et mesure de performance vs benchmark
- Evaluer l'apport du raisonnement semantique par rapport a un screening pur par indicateurs numeriques

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SemanticWeb-1 Ontology | [SymbolicAI/SemanticWeb/SW-7b-Python-OWL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-7b-Python-OWL.ipynb) | Ontologies OWL, engineering |
| SemanticWeb-2 SPARQL | [SymbolicAI/SemanticWeb/SW-4b-Python-SPARQL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-4b-Python-SPARQL.ipynb) | Requetes SPARQL |
| SemanticWeb-3 OWL-RL | [SymbolicAI/SemanticWeb/SW-13-Python-Reasoners.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-13-Python-Reasoners.ipynb) | Raisonnement OWL-RL |
| SemanticWeb-4 SHACL | [SymbolicAI/SemanticWeb/SW-8-Python-SHACL.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SemanticWeb/SW-8-Python-SHACL.ipynb) | Validation de contraintes |
| QC-Py-05 Universe Selection | [QuantConnect/Python/QC-Py-05-Universe-Selection.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-05-Universe-Selection.ipynb) | Selection d'univers, filtrage |
| QC-Py-16 Alternative Data | [QuantConnect/Python/QC-Py-16-Alternative-Data.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-16-Alternative-Data.ipynb) | Donnees alternatives, ESG |

### References externes
- Horrocks, I. (2008). "Ontologies and the Semantic Web." *Communications of the ACM*, 51(12), 58-67. [ACM](https://dl.acm.org/doi/10.1145/1409360.1409377)
- Baader, F. et al. (2003). *The Description Logic Handbook*. Cambridge University Press. [Cambridge](https://doi.org/10.1017/CBO9780511711789)
- W3C. "OWL 2 Web Ontology Language." [w3.org](https://www.w3.org/TR/owl2-overview/)
- Perez, J. et al. (2006). "Semantics and Complexity of SPARQL." *ISWC 2006*. [Springer](https://doi.org/10.1007/11860550_2)
- GICS - Global Industry Classification Standard. [msci.com](https://www.msci.com/our-solutions/indexes/gics)

### Difficulte : 3/5

---

#### S3 — Verification formelle de protocoles DeFi par SMT

Les protocoles de finance decentrlaisee (DeFi) gerent des milliards de dollars de valeur verrouillee totale (TVL) dans des smart contracts dont la correction repose entierement sur des invariants mathematiques : invariants de liquidite (constamment plus de collateral que d'emprunts), absence de sentiers d'arbitrage exploitables par flash loans, et proprietes de fair ordering. La verification formelle par SMT (Satisfiability Modulo Theories) permet d'encoder ces invariants comme des contraintes et de prouver formellement leur preservation sur tous les etats accessibles du protocole — ou de produire un contre-exemple (attaque). Ce sujet demande de modeliser un protocole DeFi simplifie (lending pool, DEX AMM) en logique du premier ordre, d'encoder les proprietes de surete comme formules SMT, et de valider les resultats contre des scenarios d'attaque realistes.

### Objectifs
- Modeliser un protocole DeFi simplifie (lending pool type Aave ou AMM type Uniswap) comme machine a etats avec transitions encodees en logique du premier ordre
- Encoder les invariants de surete (liquidite, solvabilite, absence de flash loan attack) comme formules SMT et prouver leur preservation par Z3
- Implementer la verification de bounded model checking : enumerer les etats accessibles jusqu'a une profondeur N et verifier les invariants a chaque pas
- Generer des contre-exemples (sequences d'attaques) lorsque les invariants sont violonnes et les valider sur des scenarios de marche
- Valider les conditions de bord detectees par verification formelle contre des donnees de marche crypto via QuantConnect

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SC-14 Formal Verification | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-14-Formal-Verification.ipynb) | Verification formelle Solidity |
| SC-15 Zero-Knowledge Proofs | [SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-15-Zero-Knowledge-Proofs.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/04-Privacy-Cryptography/SC-15-Zero-Knowledge-Proofs.ipynb) | ZKP, circuits arithmetiques |
| SC-13 Fuzz Testing | [SymbolicAI/SmartContracts/03-Foundry-Testing/SC-13-Fuzz-Invariants.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/SmartContracts/03-Foundry-Testing/SC-13-Fuzz-Invariants.ipynb) | Fuzzing, detection de bugs |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Z3 SMT Solver |
| QC-Py-07 Futures/Forex | [QuantConnect/Python/QC-Py-07-Futures-Forex.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-07-Futures-Forex.ipynb) | Marches crypto, donnees |

### References externes
- Passerone, C. et al. (2008). "From Simulink to SMT-Based Model Checking." *FM 2008*. [Springer](https://doi.org/10.1007/978-3-540-68270-6_2)
- Biere, A. et al. (1999). "Symbolic Model Checking without BDDs." *TACAS 1999*. [Springer](https://doi.org/10.1007/3-540-49059-0_14)
- de Moura, L. & Bjorner, N. (2008). "Z3: An Efficient SMT Solver." *TACAS 2008*. [Springer](https://doi.org/10.1007/978-3-540-78800-3_24)
- Werner, S.M. et al. (2022). "SoK: Decentralized Finance (DeFi) Incidents." *Financial Cryptography 2022*. [arXiv](https://arxiv.org/abs/2112.11433)
- Consensys. "Smart Contract Best Practices." [consensys.github.io](https://consensys.github.io/smart-contract-best-practices/)

### Difficulte : 4/5

---

#### S4 — Programmation probabiliste symbolique pour la detection de regimes de marche

La detection de regimes de marche (bull, bear, range, crash) est un probleme classique en finance quantitative qui se prete naturellement a une approche hybride symbolique-probabiliste. Un modele de Markov cache (HMM) bayesien detecte les regimes numeriquement, mais ne peut pas raisonner sur la coherence logique des transitions (un crash ne suit pas directement un bull sans transition). En combinant programmation probabiliste (Infer.NET) pour la detection numerique, revision des croyances AGM pour la mise a jour symbolique des hypotheses de regime, et raisonnement qualitatif (qualitative probability, TCP) pour les contraintes de transition, on obtient un systeme qui detecte les regimes plus robustement qu'un HMM pur. Ce sujet demande d'implementer les trois couches et de valider la strategie multi-regime par backtest QuantConnect.

### Objectifs
- Implementer un HMM bayesien avec Infer.NET pour la detection probabiliste des regimes de marche sur des series temporelles financieres
- Construire un module de revision des croyances AGM qui maintient les hypotheses de regime courant et les met a jour symboliquement face aux observations contradictoires
- Implementer un raisonneur qualitatif (qualitative probability, algebre de transition) qui contraint les transitions de regime a etre logiquement coherentes
- Developper une strategie d'allocation multi-regime ou les poids changent en fonction du regime symboliquement deduit
- Valider par backtest QuantConnect Lean sur un univers multi-actif avec rebalance mensuel et comparaison vs HMM pur et vs buy-and-hold

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Probas Infer-101 | [Probas/Infer-101.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Probas/Infer-101.ipynb) | Infer.NET, programmation probabiliste |
| Probas PyMC HMM | [Probas/PyMC-HMM-Trading-Alpha.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Probas/PyMC-HMM-Trading-Alpha.ipynb) | PyMC, HMM, trading |
| Tweety-4 Belief Revision | [SymbolicAI/Tweety/Tweety-4-Belief-Revision.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-4-Belief-Revision.ipynb) | AGM, revision des croyances |
| QC-Py-28 Regime Detection | [QuantConnect/Python/QC-Py-28-Market-Regime-Detection.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-28-Market-Regime-Detection.ipynb) | Detection de regimes de marche |
| QC-Py-10 Risk Portfolio | [QuantConnect/Python/QC-Py-10-Risk-Portfolio-Management.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-10-Risk-Portfolio-Management.ipynb) | Gestion du risque, allocation |

### References externes
- Hamilton, J.D. (1989). "A New Approach to the Economic Analysis of Nonstationary Time Series." *Econometrica*, 57(2), 357-384. [JSTOR](https://www.jstor.org/stable/1912559)
- Alchourron, C.E., Gardenfors, P. & Makinson, D. (1985). "On the Logic of Theory Change." *Journal of Symbolic Logic*, 50(2), 510-530. [JSTOR](https://www.jstor.org/stable/2274239)
- Minka, T. et al. (2018). *Infer.NET 2: Bayesian Inference in .NET*. Microsoft Research. [dotnet.github.io](https://dotnet.github.io/infer/)
- Wellman, M.P. (1990). "Fundamental Concepts of Qualitative Probabilistic Networks." *Artificial Intelligence*, 44(3), 257-303. [ScienceDirect](https://doi.org/10.1016/0004-3702(90)90001-H)
- Ghahramani, Z. (2015). "Probabilistic Machine Learning and Artificial Intelligence." *Nature*, 521, 452-459. [Nature](https://doi.org/10.1038/nature14541)

### Difficulte : 3/5

---

#### S5 — Enumeration ASP des strategies d'options multi-jambes et backtest QuantConnect

Les strategies d'options multi-jambes (straddles, strangles, butterflies, iron condors, calendar spreads, ratio spreads) forment un espace combinatoire enorme : sur un sous-jacent donne avec N strikes et M expirations, il existe O((N×M)^k) combinaisons a k jambes. La selection sous contraintes (delta-neutralite, vega-positivite, theta cible, marge initiale bornee, capital deploye, asymetrie risk-reward) est un probleme d'enumeration symbolique mieux capture par Answer Set Programming (ASP) que par des solveurs CP-SAT/MIP classiques : ASP exprime naturellement les regles de choix (`{ leg(strike, exp, side) : strike ∈ Strikes, ... } = k`), les contraintes structurelles (`:- delta_total(D), |D| > 0.05`), et le raisonnement non-monotone (defaut : strategy is balanced unless evidence shows otherwise). Ce sujet demande de modeliser l'espace combinatoire des strategies en ASP/Clingo, d'enumerer les strategies admissibles sous contraintes de risque, puis de les backtester systematiquement via QuantConnect Lean pour comparer la realisation effective des proprietes symboliquement attendues.

> **Cadrage ASP vs CP-SAT (PrCon Cat M)** : ASP est utilise ici pour son **raisonnement non-monotone** (defauts, exceptions multiples sur strategies d'options : "strategie equilibree sauf evidence contraire de skew extreme") et la **multiplicite des answer sets** (toutes les strategies admissibles, pas seulement l'optimale). CP-SAT/MIP (PrCon Cat M) reste l'angle optimisation pure (minimiser un objectif numerique sur variables algebriques). ASP peut optimiser via `#minimize`, mais sa force distinctive est la negation par defaut et la representation declarative de regles metier — c'est ce que S5 exploite. PrCon Cat M reste le parcours pour l'optimisation combinatoire pure.

### Objectifs
- Modeliser en ASP/Clingo la grammaire des strategies multi-jambes : choix de strikes/expirations, sides (long/short), nombre de contrats, avec contraintes structurelles (delta target, vega/theta limites, margin, max loss)
- Enumerer les solutions admissibles via `clingo --models=0` pour un univers d'options donne (ex: SPX hebdomadaire ou QQQ mensuel) sur differents regimes de volatilite
- Implementer le pont vers QuantConnect Lean : chaque strategy ASP enumeree est traduite en ordres multi-jambes via le framework `OptionStrategies` de QuantConnect (notebook QC-Py-06)
- Backtester systematiquement les top-K strategies enumerees (cycle d'entree/sortie hebdomadaire ou base sur signal de volatilite), avec rapport de performance (Sharpe, max DD, win rate, P&L net) et reconciliation des proprietes symboliques (delta reel vs cible)
- Comparer la performance de l'enumeration ASP filtree par contraintes vs un baseline aleatoire et vs une heuristique classique (e.g. iron condor 16-delta)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety/Tweety-7 ASP | [SymbolicAI/Tweety/Tweety-7a-Extended-Frameworks.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-7a-Extended-Frameworks.ipynb) | ASP/Clingo, regles de choix, contraintes |
| QC-Py-06 Options Trading | [QuantConnect/Python/QC-Py-06-Options-Trading.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-06-Options-Trading.ipynb) | Framework Options, multi-jambes, grecs |
| QC-Py-12 Backtesting Analysis | [QuantConnect/Python/QC-Py-12-Backtesting-Analysis.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-12-Backtesting-Analysis.ipynb) | Metriques de performance, analyse statistique |
| OptionsIncome project | [QuantConnect/projects/OptionsIncome/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/QuantConnect/projects/OptionsIncome) | Strategies d'options revenu (template projet) |
| Options-VGT project | [QuantConnect/projects/Options-VGT/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/QuantConnect/projects/Options-VGT) | Iron condors / strangles sur ETF |

### References externes
- Gebser, M., Kaminski, R., Kaufmann, B. & Schaub, T. (2019). "Multi-shot ASP solving with clingo." *Theory and Practice of Logic Programming*, 19(1), 27-82. [Cambridge](https://doi.org/10.1017/S1471068418000054)
- Hull, J.C. (2022). *Options, Futures, and Other Derivatives* (11th ed.). Pearson. [Pearson](https://www.pearson.com/en-us/subject-catalog/p/options-futures-and-other-derivatives/P200000005945)
- Natenberg, S. (2014). *Option Volatility and Pricing* (2nd ed.). McGraw-Hill. [McGraw-Hill](https://www.mhprofessional.com/9780071818773-usa-option-volatility-and-pricing-second-edition-advanced-trading-strategies-and-techniques)
- Brignole, F. et al. (2023). "Constraint-based portfolio of derivative strategies." *Journal of Computational Finance*, 27(2). [Risk.net](https://www.risk.net/journal-of-computational-finance)
- QuantConnect Documentation. "Option Strategies API." [quantconnect.com](https://www.quantconnect.com/docs/v2/writing-algorithms/trading-and-orders/option-strategies)

### Difficulte : 4/5

---

#### S6 — Safe RL : shielding SMT des politiques de trading RL et deployment QuantConnect Live

L'apprentissage par renforcement profond (PPO, SAC, DQN) appris sur des historiques de marche peut produire des politiques performantes en backtest mais violantes en deployment live : drawdown au-dela des limites du fonds, leverage non autorise, concentration sur un titre unique, ordres de gros volume en regime de faible liquidite. La solution academique etablie est le **shielding** (Alshiekh et al. 2018, Konighofer et al. 2023) : un module symbolique intercepte chaque action proposee par la politique RL, verifie qu'elle ne viole aucun invariant (formules SMT sur l'etat du portefeuille et de l'ordre), et la corrige ou la rejette si necessaire. Ce sujet demande d'entrainer une politique RL via QuantConnect (PPO/SAC sur SPY/QQQ ou un panier crypto), d'encoder les invariants de surete en Z3 SMT, d'implementer un shield runtime, puis de comparer (1) la performance shieldee vs non-shieldee en backtest et (2) le comportement en paper trading Binance/IBKR sur 3-4 semaines.

### Objectifs
- Entrainer une politique RL (PPO ou SAC) sur un univers reduit (5-10 actifs) avec QC-Py-33 ou QC-Py-34, evaluer la baseline en backtest sur 2019-2024
- Formaliser les invariants de surete en SMT : leverage <= 2x, |position(i)| <= 25% du portfolio, drawdown intra-day <= 10%, ordres <= 5% du volume moyen 20j, no wash trading
- Implementer un shield Z3 : a chaque action proposee `a`, resoudre `∃ a' : SAT(invariants) ∧ d(a, a') minimal` (projection sur le polytope de surete), avec fallback rejet+`hold` si infaisable
- Comparer en backtest 2019-2024 : (1) RL pur, (2) RL shieldee, (3) RL re-trainee avec reward penalisant les violations, sur metriques performance ET conformite (compter violations par strategie)
- Deployer la version shieldee en paper trading via QC-Py-40 (Binance) ou QC-Py-41 (IBKR) sur 3-4 semaines, mesurer la divergence backtest/live et la frequence d'activation du shield

> **Plan B (si paper trading instable)** : si le deployment live echoue (latence API, restrictions broker, donnees manquantes), demontrer le shielding sur backtest historique 2018-2025 avec (a) audit exhaustif des violations detectees/corrigees par le shield, (b) simulation Monte Carlo de scenarios de stress (flash crash, gap overnight, halt circuit-breaker) pour mesurer la robustesse du shield hors-distribution. Ce fallback preserve la valeur scientifique du sujet sans dependre d'une infrastructure live.

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| QC-Py-32 RL DQN | [QuantConnect/Python/QC-Py-32-RL-DQN-Trading.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-32-RL-DQN-Trading.ipynb) | DQN, replay buffer, target network |
| QC-Py-33 RL PPO | [QuantConnect/Python/QC-Py-33-RL-PPO-Trading.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-33-RL-PPO-Trading.ipynb) | PPO, policy gradient, clip ratio |
| QC-Py-34 RL SAC | [QuantConnect/Python/QC-Py-34-RL-SAC-A2C-Trading.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-34-RL-SAC-A2C-Trading.ipynb) | SAC, entropie maximale, continuous action |
| RL-Portfolio project | [QuantConnect/projects/RL-Portfolio/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/QuantConnect/projects/RL-Portfolio) | Template projet portfolio RL backtested |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Z3 SMT, encoding LINQ → contraintes |
| QC-Py-40 Paper Trading Binance | [QuantConnect/Python/QC-Py-40-PaperTrading-Binance.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-40-PaperTrading-Binance.ipynb) | Paper trading crypto, live orders |
| QC-Py-41 Paper Trading IBKR | [QuantConnect/Python/QC-Py-41-PaperTrading-IBKR.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-41-PaperTrading-IBKR.ipynb) | Paper trading actions/options, IBKR API |

### References externes
- Alshiekh, M. et al. (2018). "Safe Reinforcement Learning via Shielding." *AAAI 2018*. [arXiv](https://arxiv.org/abs/1708.08611)
- Konighofer, B. et al. (2023). "Online Shielding for Reinforcement Learning." *Innovations in Systems and Software Engineering*, 19(4). [Springer](https://doi.org/10.1007/s11334-022-00480-4)
- Garcia, J. & Fernandez, F. (2015). "A Comprehensive Survey on Safe Reinforcement Learning." *JMLR*, 16. [JMLR](https://www.jmlr.org/papers/v16/garcia15a.html)
- Schulman, J. et al. (2017). "Proximal Policy Optimization Algorithms." *arXiv:1707.06347*. [arXiv](https://arxiv.org/abs/1707.06347)
- de Moura, L. & Bjorner, N. (2008). "Z3: An Efficient SMT Solver." *TACAS 2008*. [Springer](https://doi.org/10.1007/978-3-540-78800-3_24)
- Hambly, B., Xu, R. & Yang, H. (2023). "Recent Advances in Reinforcement Learning in Finance." *Mathematical Finance*, 33(3). [Wiley](https://doi.org/10.1111/mafi.12382)

### Difficulte : 5/5

---

#### S7 — Fusion de signaux multi-strategie par argumentation Dung sur le Research-Executor QuantConnect

Le Research-Executor de CoursIA fournit 8 strategies de recherche backtestees independamment (asset class momentum, commodity term structure, defensive ETF rotation, long-short harvest, macro factor rotation, Piotroski F-Score, Puppies of the Dow, volatility regime ML). Chaque strategy genere des signaux contradictoires : Piotroski peut recommander d'acheter un value stock pendant que macro factor rotation recommande de tout sortir des actions cycliques. Une fusion d'ensemble naive (vote majoritaire ou ponderation par Sharpe historique) ignore la structure logique des desaccords. L'argumentation abstraite de Dung (1995) modelise chaque signal comme un argument, les contradictions logiques comme attaques (defensive ETF rotation **attaque** long-short harvest sous regime macro defensif), et calcule des extensions (preferred, grounded, stable) qui constituent une decision rationnellement defendable. Ce sujet demande d'implementer le framework Dung via Tweety, de definir le graphe d'attaques entre les 8 strategies du Research-Executor, et de backtester la strategie fusionnee vs ensemble naif. Le volet avance compare les semantiques d'acceptabilite de Dung (preferred, grounded, stable) aux procedures de vote social choice (Borda, Copeland, approval) sur les memes signaux, et verifie formellement si la decision argumentee satisfait des axiomes de choix social (Pareto, independence des alternatives non pertinentes) via l'axiomatisation Arrow/Sen de Tweety-5 et GameTheory/16e.

### Objectifs
- Implementer un Argumentation Framework (AF) de Dung en Python via Tweety ou pyArg, avec semantiques preferred / grounded / stable / complete
- Definir le mapping strategie→argument et les regles d'attaque entre les 8 strategies du Research-Executor (e.g. defensive ETF rotation attaque long-short harvest si VIX > 25, macro factor rotation attaque Piotroski si yield curve inversion, etc.)
- Implementer un meta-arbitre qui, a chaque rebalance, recupere les signaux des 8 strategies, instancie l'AF avec les attaques contextuelles courantes, calcule l'extension preferred, et alloue uniquement aux strategies dans l'extension
- Backtester la fusion argumentee sur 2019-2024 vs (1) chaque strategie en isole, (2) ensemble equipondere, (3) ensemble pondere par Sharpe historique, (4) ensemble par regression sur facteurs (Fama-French 5)
- Analyser la robustesse aux changements de regime : tester sur 2008-2009 (crise), 2020 mars (COVID crash), 2022 (rate hike), comparer max drawdown et recovery time
- Comparer formellement la decision Dung (extension preferred) aux procedures de vote classique (Borda, Copeland, approval) sur les memes signaux et verifier si la decision argumentee satisfait les axiomes de choix social (Pareto, IIA) via Tweety-5 et GameTheory/16e/16f

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety/Tweety-1 Argumentation | [SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb) | Frameworks Dung, extensions, semantiques |
| Research-Executor | [QuantConnect/projects/Research-Executor/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/QuantConnect/projects/Research-Executor) | 8 strategies backtestees pretes a fusionner |
| QC-Py-13 Alpha Models | [QuantConnect/Python/QC-Py-13-Alpha-Models.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-13-Alpha-Models.ipynb) | Alpha Insights API, ensembling natif QC |
| QC-Py-14 Portfolio Construction | [QuantConnect/Python/QC-Py-14-Portfolio-Construction-Execution.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-14-Portfolio-Construction-Execution.ipynb) | Portfolio construction model, allocation |
| QC-Py-28 Regime Detection | [QuantConnect/Python/QC-Py-28-Market-Regime-Detection.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-28-Market-Regime-Detection.ipynb) | Detection de regimes pour contexte d'attaques |
| Tweety-5 Voting/Social Choice | [GameTheory/SocialChoice/03-Voting-Methods.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/03-Voting-Methods.ipynb) | Arrow/Sen, procedures de vote, axiomes |
| GT-16e/16f Social Choice | [GameTheory/SocialChoice/02-Lean-SocialChoice-Formal.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/02-Lean-SocialChoice-Formal.ipynb) | Arrow/Sen corollaires, comparaison semantiques |

### References externes
- Dung, P.M. (1995). "On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games." *Artificial Intelligence*, 77(2), 321-357. [ScienceDirect](https://doi.org/10.1016/0004-3702(94)00041-X)
- Baroni, P., Caminada, M. & Giacomin, M. (2018). *Handbook of Formal Argumentation*. College Publications. [CollegePub](https://www.collegepublications.co.uk/handbook/)
- Atkinson, K. et al. (2017). "Towards artificial argumentation." *AI Magazine*, 38(3), 25-36. [AAAI](https://doi.org/10.1609/aimag.v38i3.2704)
- Asness, C., Frazzini, A. & Pedersen, L.H. (2019). "Quality minus junk." *Review of Accounting Studies*, 24(1). [Springer](https://doi.org/10.1007/s11142-018-9470-2)
- Tweety Project. "Tweety Libraries Documentation." [tweetyproject.org](https://tweetyproject.org/)
- Arrow, K.J. (1951). *Social Choice and Individual Values* (2nd ed. 1963). Yale University Press. [Yale](https://www.jstor.org/stable/j.ctv1h4ckhn)
- Sen, A.K. (1970). "The Impossibility of a Paretian Liberal." *Journal of Political Economy*, 78(1), 152-157. [JSTOR](https://www.jstor.org/stable/1829634)

### Difficulte : 5/5

---

#### S8 — Model checking CTL d'un trading bot avant deployment live QuantConnect

Avant de deployer un bot de trading en live (capital reel), il faut prouver formellement qu'il ne violera jamais ses contraintes de surete : pas de margin call, pas de leverage > 2x, pas de stop-loss desactive, le bot revient toujours en etat `flat` apres un signal `halt`. Le model checking CTL/LTL (Clarke, Emerson, Sistla 1986) est l'outil academique standard : on modelise le bot comme une structure de Kripke (etats = configuration portefeuille + signaux courants ; transitions = orderes/fills/signaux), on encode les proprietes de surete en formules CTL (`AG !margin_call`, `AG (drawdown >= 0.2 → AF flat)`, `EF profit_target`), et un model checker verifie exhaustivement toutes les executions accessibles ou produit un contre-exemple. L'approche de base utilise **NuSMV** (BDD-based, CTL deterministe sur automate fini discret : etats = `{flat, long, short, halted}`, transitions = ordres/fills/signaux). L'extension avancee utilise **Storm** ou **PRISM** (model checking probabiliste PCTL sur Markov Decision Processes) pour quantifier la probabilite de violation sous incertitude de marche (slippage, partial fills, gap). Ce sujet demande de modeliser une strategie de trading complete en automate fini, de la verifier par model checking (NuSMV deterministe ; Storm/PRISM probabiliste en extension), puis de deployer la version certifiee sur QuantConnect via QC-Py-27 (production) et de comparer le comportement reel aux invariants prouves.

### Objectifs
- Modeliser une strategie concrete (e.g. trend-following ou mean-reversion 2-actifs) comme automate fini : etats = `{flat, long, short, halted, margin_warning}`, variables = position size, drawdown, signal, transitions deterministes ou non-deterministes (slippage, partial fills)
- Encoder en CTL les proprietes de surete : `AG !(margin_call)`, `AG (drawdown > 0.15 → AX !buy)`, `AG (halted → AF flat)`, `EF profit_target`, `AG (long → EF flat)`
- Verifier par **NuSMV** (BDD-based, CTL deterministe) : exhaustivite sur automate fini, contre-exemples tangibles si propriete echoue. En extension : encoder le modele comme MDP et verifier par **Storm** ou **PRISM** (PCTL : `P>=0.99 [G !margin_call]`), comparant la certitude totale (NuSMV) a la certitude probabilisee (Storm)
- Implementer la strategie verifiee dans QC, deployer via QC-Py-15 (parameter optimization) puis QC-Py-27 (production), comparer le comportement en backtest 2019-2024 et en paper trading 2-4 semaines aux invariants CTL prouves
- Mesurer le gap entre modele formel et execution reelle (ex: slippage, halt sur halt-circuit-breaker, latence d'ordres) et discuter comment etendre le modele pour reduire ce gap

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety/Tweety-3 Modal Logic | [SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb) | Modal logic, structures de Kripke |
| QC-Py-09 Order Types | [QuantConnect/Python/QC-Py-09-Order-Types.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-09-Order-Types.ipynb) | Modeles d'ordres (market, limit, stop), transitions |
| QC-Py-15 Parameter Optimization | [QuantConnect/Python/QC-Py-15-Parameter-Optimization.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-15-Parameter-Optimization.ipynb) | Optimisation hyperparametres, robustesse |
| QC-Py-27 Production Deployment | [QuantConnect/Python/QC-Py-27-Production-Deployment.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/QuantConnect/Python/QC-Py-27-Production-Deployment.ipynb) | Deployment live, monitoring |
| Trend-Following project | [QuantConnect/projects/Trend-Following/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/QuantConnect/projects/Trend-Following) | Template strategie complete a modeliser |
| QC-Py-40 / QC-Py-41 Paper Trading | [QuantConnect/Python/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/QuantConnect/Python) | Paper trading post-verification |

### References externes
- Clarke, E.M., Emerson, E.A. & Sistla, A.P. (1986). "Automatic verification of finite-state concurrent systems using temporal logic specifications." *ACM TOPLAS*, 8(2), 244-263. [ACM](https://doi.org/10.1145/5397.5399)
- Baier, C. & Katoen, J.-P. (2008). *Principles of Model Checking*. MIT Press. [MIT Press](https://mitpress.mit.edu/9780262026499/principles-of-model-checking/)
- Cavada, R. et al. (2014). "The NuXMV Symbolic Model Checker." *CAV 2014*. [Springer](https://doi.org/10.1007/978-3-319-08867-9_22)
- Cimatti, A. et al. (2002). "NuSMV 2: An OpenSource Tool for Symbolic Model Checking." *CAV 2002*. [Springer](https://doi.org/10.1007/3-540-45657-0_29)
- Hensel, C. et al. (2022). "The Probabilistic Model Checker Storm." *STTT*, 24(4). [Springer](https://doi.org/10.1007/s10009-021-00620-z)
- Kwiatkowska, M., Norman, G. & Parker, D. (2011). "PRISM 4.0: Verification of Probabilistic Real-Time Systems." *CAV 2011*. [Springer](https://doi.org/10.1007/978-3-642-22110-1_47)

### Difficulte : 4/5

---

### Categorie T : Sciences Sociales Computationnelles et Choix Collectif

#### T1 — Pouvoir de coalition par verification formelle (Shapley, Banzhaf et donnees electorales reelles)

La theorie des jeux cooperatifs fournit des indices de pouvoir (Shapley-Shubik, Banzhaf, Deegan-Packel) qui mesurent la capacite reelle d'un acteur a faire basculer une coalition gagnante, independamment de sa taille apparente. Applique aux resultats electoraux, cet outil revele des discrepancies frappantes entre poids electoral et pouvoir reel : un petit parti pivot peut avoir un indice de Shapley superieur a celui d'un grand parti bloque dans un bloc ideologique homogene. Ce sujet demande d'implementer le calcul formel de ces indices par encodage SAT/SMT (les coalitions gagnantes comme clauses, les indices comme fonctions sur les modeles), de verifier les proprietes axiomatiques (symetrie, joueur nul, efficacite) par Z3 ou Lean, et d'appliquer l'outil a des cas concrets. Les donnees publiques sont disponibles pour les legislatives francaises (2022, 2024 — NUPES/NFP, coalition presidentielle, RN), les municipales (coalitions post-2nd tour), et les elections europeennes (repartition des sieges par methode D'Hondt).

### Objectifs
- Implementer le calcul des indices de Shapley-Shubik, Banzhaf et Deegan-Packel par encodage SAT/SMT (Z3) et verifier la correction par test sur des instances de reference de la litterature
- Prouver formellement en Z3 ou Lean que chaque indice satisfait ses axiomes (symetrie, joueur nul, efficacite, additivite) et identifier les proprietes qui les distinguent
- Appliquer aux resultats des legislatives 2022 et 2024 (donnees publiques : 577 circonscriptions, resultats par candidat sur data.gouv.fr et assemblee-nationale.fr) en modelisant les coalitions possibles (NUPES/NFP, ensemble, RN, LR) et leurs indices de pouvoir respectifs
- Comparer le pouvoir de pivot observe dans les coalitions reelles avec le pouvoir theorique predit par les indices, et analyser les cas de divergence (discipline de parti, votes a l'assemblee)
- Etendre l'analyse aux systemes proportionnels (Europeennes, regionales) ou la repartition D'Hondt cree des seuils strategiques, et evaluer l'impact d'un changement de mode de scrutin sur les indices de pouvoir

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| GT-15 Cooperative Games | [GameTheory/GameTheory-15-CooperativeGames.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-15-CooperativeGames.ipynb) | Jeux cooperatifs, valeur de Shapley |
| GT-15b Lean Cooperative | [GameTheory/GameTheory-15b-Lean-CooperativeGames.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-15b-Lean-CooperativeGames.ipynb) | Verification formelle Lean 4 |
| GT-15c Cooperative Python | [GameTheory/GameTheory-15c-CooperativeGames-Python.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-15c-CooperativeGames-Python.ipynb) | Implementation Python, SHAP values |
| SocialChoice/03 Voting Methods | [GameTheory/SocialChoice/03-Voting-Methods.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/03-Voting-Methods.ipynb) | Methodes de vote, Arrow et au-dela |
| Linq2Z3 | [SymbolicAI/Linq2Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Linq2Z3.ipynb) | Encodage SMT des coalitions |

### References externes
- Shapley, L.S. (1953). "A Value for n-Person Games." *Contributions to the Theory of Games*, II, 307-317. [Princeton](https://doi.org/10.1515/9781400881970-018)
- Banzhaf, J.F. (1965). "Weighted Voting Doesn't Work: A Mathematical Analysis." *Rutgers Law Review*, 19, 317-343. [HeinOnline](https://heinonline.org/HOL/LandingPage?handle=hein.journals/ RutgersLR19&div=20)
- Felsenthal, D.S. & Machover, M. (1998). *The Measurement of Voting Power: Theory and Practice, Problems and Paradoxes*. Edward Elgar. [Edward Elgar](https://www.e-elgar.com/shop/gb/measurement-of-voting-power-9781858988054.html)
- Laruelle, A. & Valenciano, F. (2008). *Voting and Collective Decision-Making*. Cambridge University Press. [Cambridge](https://doi.org/10.1017/CBO9780511493241)
- Donnees elections legislatives francaises. [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/elections-legislatives-des-12-et-19-juin-2022-resultats-definitifs-par-bureau-de-vote/)

### Difficulte : 3/5

---

#### T2 — Choix social et procedures de vote : analyse formelle par SAT/SMT

Le theoreme d'impossibilite d'Arrow (1951) demontre qu'aucune procedure de vote agregative ne peut satisfaire simultanement cinq axiomes rationnels (universalite, unanimité, non-dictature, independance aux alternatives irrelevantes, transitivite). Ce resultat fondamental se preuve par encodage SAT : on enumere les profils de preferences possibles et on verifie par solveur qu'aucune fonction d'agregation ne satisfait les cinq axiomes. Ce sujet propose d'implementer cet encodage formel, de l'etendre a des axiomes alternatifs (monotonie, stratategy-proofness, participation), et de comparer formellement les proprietes des procedures de vote reelles (scrutin majoritaire a deux tours, proportionnelle D'Hondt, vote par approbation, jugement majoritaire, vote unique transférable). L'application concrete porte sur la comparaison des mecanismes constitutionnels francais (election presidentielle, legislatives, 49.3) avec des alternatives proposees pour une eventuelle VIe Republique.

### Objectifs
- Implementer l'encodage SAT du theoreme d'Arrow (3 candidats, N electeurs) par PySAT ou Z3 et reproduire le resultat d'impossibilite par resolution automatique
- Encoder des axiomes supplementaires (monotonie, strategie-proofness, critere de participation, critere de Condorcet) et identifier formellement quels sous-ensembles d'axiomes sont compatibles
- Comparer formellement les proprietes satisfaites par chaque procedure de vote reelle (majoritaire 2 tours, proportionnelle, approbation, jugement majoritaire, STV) en verifiant chaque axiome par SMT
- Modeliser les mecanismes constitutionnels francais (election presidentielle 2 tours, legislatives, article 49.3, dissolution) comme des procedures de choix social et analyser formellement leurs proprietes
- Proposer des alternatives de procedure de vote pour une reforme constitutionnelle et argumenter formellement (quels axiomes preserves, lesquels relaches) en s'appuyant sur les resultats SAT/SMT

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Arrow SAT | [GameTheory/SocialChoice/01-Arrow-Impossibility-Theorem.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/01-Arrow-Impossibility-Theorem.ipynb) | Theoreme d'Arrow par SAT |
| Arrow SMT (Z3) | [GameTheory/SocialChoice/04-Computational-Aggregation-SAT-Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/04-Computational-Aggregation-SAT-Z3.ipynb) | Encodage SMT, aggregation |
| Arrow Lean | [GameTheory/SocialChoice/02-Lean-SocialChoice-Formal.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/02-Lean-SocialChoice-Formal.ipynb) | Preuve formelle Lean 4 |
| SocialChoice/03 Voting Methods | [GameTheory/SocialChoice/03-Voting-Methods.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/03-Voting-Methods.ipynb) | Comparaison des methodes |
| GT-16 Mechanism Design | [GameTheory/GameTheory-16-MechanismDesign.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-16-MechanismDesign.ipynb) | Mecanismes incitatifs, VCG |

### References externes
- Arrow, K.J. (1951). *Social Choice and Individual Values*. 2nd ed., Wiley. [Wiley](https://www.wiley.com/en-us/Social+Choice+and+Individual+Values-p-9780300013641)
- Geanakoplos, J. (2005). "Three Brief Proofs of Arrow's Impossibility Theorem." *Economic Theory*, 26(1), 211-215. [Springer](https://doi.org/10.1007/s00199-004-0556-7)
- Brams, S.J. & Fishburn, P.C. (2007). *Approval Voting*. 2nd ed., Springer. [Springer](https://doi.org/10.1007/978-0-387-49896-8)
- Balinski, M. & Laraki, R. (2011). *Majority Judgment: Measuring, Ranking, and Electing*. MIT Press. [MIT Press](https://mitpress.mit.edu/9780262545768/majority-judgment/)
- Pacuit, E. (2019). "Voting Methods." *Stanford Encyclopedia of Philosophy*. [SEP](https://plato.stanford.edu/entries/voting-methods/)

### Difficulte : 4/5

---

#### T3 — Information asymetrique et capture : modelisation par argumentation et logique epistemique

La theorie de la capture reglementaire (Stigler, 1971 ; Laffont & Tirole, 1993) modelise comment un agent regulate peut etre influence par l'agent qu'il est cense controler, lorsque l'information est asymetrique et les incentives mal alignees. Ce cadre theorique s'applique a la concentration mediatique, aux lobbys industriels, et aux relations finance-regulateur. Ce sujet propose de formaliser ces dynamiques par deux outils symboliques complementaires : la logique epistemique multi-agents (Kripke, connaissance partagee, annonces publiques) pour modeliser l'information asymetrique et ses effets sur les croyances, et l'argumentation structuree de Dung (frameworks d'attaque, extensions, semantics) pour modeliser les debats publics et la manipulation de l'information. Les etudiants implementent un raisonneur epistemique et un systeme d'argumentation, puis les combinent pour simuler des scenarios de capture et analyser formellement les conditions sous lesquelles l'information est degradee pour le principal (citoyen).

> **Posture academique** : ce sujet demande de **modeliser formellement** des mecanismes informationnels, pas de defendre une these politique. Le verdict descriptif "capture" est une conclusion possible de la modelisation, pas un prejuge. Le critere de notation est la qualite de la formalisation (argumentation, logique epistemique, donnees), non l'opinion. Les cas d'etude combines un cas historique non controverse (crise des Savings & Loans 1980s, BCCI 1991, Madoff/SEC pre-2008) et un cas structurel neutre analyse par taille ou par age de marche.

### Objectifs
- Implementer un modele de Kripke multi-agents capturant l'information asymetrique entre regulate, industrie et citoyens (Ki, croyances croisees, knowledge gaps)
- Implementer un framework d'argumentation de Dung avec semantiques (grounded, preferred, stable) et l'appliquer a des debats publics sur des questions reglementaires
- Modeliser le jeu informationnel regulateur/regule comme un jeu a information asymetrique ou l'agent regule controle une partie du flux d'information (public announcements partielles) et analyser formellement les conditions d'equilibre
- Combiner logique epistemique et argumentation : un argument est accepte ou rejete en fonction de l'etat epistemique de l'agent, et les annonces publiques modifient cet etat
- Evaluer sur deux cas d'etude documentes : (1) un cas historique (S&L crisis, Madoff/SEC) et (2) un cas structurel neutre (concentration par taille de marche, registres de transparence europeens, ACM/ARCOM)

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-5 Abstract Argumentation | [SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb) | Frameworks de Dung, semantiques |
| Tweety-6 Structured Argumentation | [SymbolicAI/Tweety/Tweety-6-Structured-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-6-Structured-Argumentation.ipynb) | Argumentation structuree, ASPIC+ |
| Tweety-3 Advanced Logics | [SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-3-Advanced-Logics.ipynb) | Logiques modales, epistemique |
| Lean-3 Propositions | [SymbolicAI/Lean/Lean-3-Propositions-Proofs.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-3-Propositions-Proofs.ipynb) | Preuve formelle de structures epistemiques |
| GT-11 Bayesian Games | [GameTheory/GameTheory-11-BayesianGames.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/GameTheory-11-BayesianGames.ipynb) | Information asymetrique |
| SocialChoice/04 Aggregation Z3 | [GameTheory/SocialChoice/04-Computational-Aggregation-SAT-Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/04-Computational-Aggregation-SAT-Z3.ipynb) | Verification Z3 des proprietes informationnelles |
| Tweety-8 Agent Dialogues | [SymbolicAI/Tweety/Tweety-8-Agent-Dialogues.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-8-Agent-Dialogues.ipynb) | Dialogues strategiques |

### References externes
- Stigler, G.J. (1971). "The Theory of Economic Regulation." *Bell Journal of Economics*, 2(1), 3-21. [JSTOR](https://www.jstor.org/stable/3003164)
- Laffont, J.-J. & Tirole, J. (1993). *A Theory of Incentives in Procurement and Regulation*. MIT Press. [MIT Press](https://mitpress.mit.edu/9780262121743/)
- Dung, P.M. (1995). "On the Acceptability of Arguments and its Fundamental Role in Nonmonotonic Reasoning, Logic Programming, and n-Person Games." *Artificial Intelligence*, 77(2), 321-357. [Elsevier](https://doi.org/10.1016/0004-3702(94)00041-X)
- Fagin, R. et al. (1995). *Reasoning About Knowledge*. MIT Press. [MIT Press](https://mitpress.mit.edu/9780262562003/reasoning-about-knowledge/)
- Besley, T. & Coate, S. (2001). "Lobbying and Welfare in a Representative Democracy." *Review of Economic Studies*, 68(1), 67-82. [Oxford](https://doi.org/10.1111/1467-937X.00162)

### Difficulte : 4/5

---

#### T4 — Decision publique sous incertitude : revision des croyances et argumentation

Les decisions de politique publique (politique climatique, gestion de pandemie, reforme fiscale, strategie energetique) sont prises sous forte incertitude : les modeles scientifiques evoluent, les donnees sont incompletes, et les experts divergent. La theorie de la decision classique (utilite esperee, arbres de decision) suppose des probabilites connues, mais en pratique les decideurs doivent reviser leurs croyances au fur et a mesure que de nouvelles informations arrivent — parfois contradictoires. Ce sujet propose de construire un systeme symbolique de decision publique combinant trois couches : (1) un module de revision des croyances AGM (Alchourron-Gardenfors-Makinson) pour mettre a jour formellement une base de croyances face a des informations nouvelles contradictoires, (2) un module d'argumentation ponderee pour structurer le debat entre experts et identifier les positions defendables, et (3) un module de decision symbolique comparant differents criteres (utilite esperee, maximin, minimax regret, leximin) formalises en logique de preference qualitative. L'objectif est de produire un outil formel qui rend explicite les hypotheses, les croyances et les criteres de decision sous-jacents a une politique publique.

### Objectifs
- Implementer un moteur de revision des croyances AGM (expansion, contraction, revision) avec au moins trois strategies (lexicographique, Dalal, distance-based) et verifier formellement le respect des postulats AGM
- Implementer un systeme d'argumentation pondere (Weighted Argumentation Frameworks) ou chaque argument a un poids base sur la confiance dans la source, et evaluer les extensions defendables
- Formaliser en logique qualitative de préference les criteres de decision classiques (maximin, minimax regret, leximin) et les implementer comme mecanismes de choix entre alternatives poli%C3%A7tiques
- Appliquer le systeme complet a un cas d'etude documente (politique climatique IPPC, gestion Covid, transition energetique) en utilisant des donnees publiques et des rapports d'experts
- Comparer les recommandations du systeme sous differents criteres de decision et analyser la sensibilite aux choix de revision (AGM) et de ponderation des arguments

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| Tweety-4 Belief Revision | [SymbolicAI/Tweety/Tweety-4-Belief-Revision.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-4-Belief-Revision.ipynb) | AGM, revision, contraction |
| Tweety-5 Abstract Argumentation | [SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-5-Abstract-Argumentation.ipynb) | Argumentation de Dung |
| Tweety-7b Ranking Probabilistic | [SymbolicAI/Tweety/Tweety-7b-Ranking-Probabilistic.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-7b-Ranking-Probabilistic.ipynb) | Ranking, probabilites |
| Tweety-9 Preferences | [SymbolicAI/Tweety/Tweety-9-Preferences.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Tweety/Tweety-9-Preferences.ipynb) | Preferences, ordinaux |
| Probas Infer-101 | [Probas/Infer-101.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/Probas/Infer-101.ipynb) | Infer.NET, programmation probabiliste |
| Research/ Decision Networks | [Research/](https://github.com/jsboige/CoursIA/tree/main/MyIA.AI.Notebooks/Research) | Reseaux de decision, POMDP |

### References externes
- Alchourron, C.E., Gardenfors, P. & Makinson, D. (1985). "On the Logic of Theory Change." *Journal of Symbolic Logic*, 50(2), 510-530. [JSTOR](https://www.jstor.org/stable/2274239)
- Dung, P.M. (1995). "On the Acceptability of Arguments." *Artificial Intelligence*, 77(2), 321-357. [Elsevier](https://doi.org/10.1016/0004-3702(94)00041-X)
- Gardenfors, P. (1988). *Knowledge in Flux: Modeling the Dynamics of Epistemic States*. MIT Press. [MIT Press](https://mitpress.mit.edu/9780262571798/knowledge-in-flux/)
- Savage, L.J. (1954). *The Foundations of Statistics*. Wiley. [Internet Archive](https://archive.org/details/foundationsofsta0000sava)
- Halpern, J.Y. (2003). *Reasoning About Uncertainty*. MIT Press. [MIT Press](https://mitpress.mit.edu/9780262582998/reasoning-about-uncertainty/)

### Difficulte : 3/5

---

#### T5 — Decouverte automatique de theoremes d'impossibilite en choix social : recherche SAT de contre-exemples et certification Lean

Les theoremes d'impossibilite (Arrow, Muller-Satterthwaite, Gibbard-Satterthwaite) sont des resultats fondateurs du choix social : ils montrent qu'aucune procedure d'agregation ne peut satisfaire simultanement un ensemble d'axiomes desirables. Ce sujet de recherche, dans la lignee de la preuve assistee par ordinateur du theoreme d'Arrow (Tang-Lin 2009), construit une chaine **decouverte automatique + certification formelle**. La methode encode les axiomes (Pareto, independance des alternatives non pertinentes, non-dictature, monotonie, strategy-proofness) en **SAT/SMT** pour de petits electorats : un resultat UNSAT atteste l'impossibilite pour ces tailles, et l'on extrait les **ensembles d'axiomes minimaux conflictuels**. L'etape decisive, qui distingue ce sujet du seul calcul, est la **certification en Lean 4** : transformer le cas de base trouve par SAT en une preuve formelle generale (par induction sur le nombre d'agents/alternatives), produisant un theoreme verifie machine. Le sujet complete A3 en mettant l'accent sur la *decouverte* de nouvelles (im)possibilites et le pont SAT-vers-Lean.

### Objectifs
1. Encoder les axiomes du choix social (Pareto, IIA, monotonie, strategy-proofness, non-dictature) en SAT/SMT pour des electorats bornes
2. Rechercher automatiquement les cas de base d'impossibilite (UNSAT) et extraire les ensembles d'axiomes minimaux conflictuels
3. Reproduire des resultats connus (Arrow, Muller-Satterthwaite) et *explorer* des variantes/affaiblissements pour trouver de nouvelles (im)possibilites
4. Certifier le theoreme general en Lean 4 (induction relevant le cas de base SAT a un nombre arbitraire d'agents), produisant une preuve verifiee machine
5. Evaluer la portee (quels theoremes sont atteignables), le passage de relais SAT-vers-Lean, et les limites de la decouverte automatique

### Notebooks CoursIA pertinents

| Notebook | Chemin | Pertinence |
|----------|--------|------------|
| SocialChoice 01-Arrow | [GameTheory/SocialChoice/01-Arrow-Impossibility-Theorem.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/01-Arrow-Impossibility-Theorem.ipynb) | Theoreme d'Arrow : le resultat de reference |
| SocialChoice 04-SAT-Z3 | [GameTheory/SocialChoice/04-Computational-Aggregation-SAT-Z3.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/04-Computational-Aggregation-SAT-Z3.ipynb) | Agregation computationnelle par SAT/Z3 -- coeur de la decouverte |
| SocialChoice 02-Lean-Formal | [GameTheory/SocialChoice/02-Lean-SocialChoice-Formal.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/02-Lean-SocialChoice-Formal.ipynb) | Formalisation Lean du choix social -- coeur de la certification |
| SocialChoice 03-Voting-Methods | [GameTheory/SocialChoice/03-Voting-Methods.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/GameTheory/SocialChoice/03-Voting-Methods.ipynb) | Procedures de vote : les objets axiomatises |
| Lean-8 Agentic Proving | [SymbolicAI/Lean/Lean-8-Agentic-Proving.ipynb](https://github.com/jsboige/CoursIA/blob/main/MyIA.AI.Notebooks/SymbolicAI/Lean/Lean-8-Agentic-Proving.ipynb) | Assistance LLM a la construction de preuves Lean |

### References externes

**Theoremes d'impossibilite et choix social**
- Arrow, K.J. (1951). *Social Choice and Individual Values*. Wiley. [Yale University Press](https://yalebooks.yale.edu/book/9780300013641/social-choice-and-individual-values/)
- Brandt, F. et al. (eds.) (2016). *Handbook of Computational Social Choice*. Cambridge University Press. [Cambridge](https://www.cambridge.org/core/books/handbook-of-computational-social-choice/)

**Decouverte et certification assistees par ordinateur**
- Tang, P. & Lin, F. (2009). "Computer-aided Proofs of Arrow's and Other Impossibility Theorems." *Artificial Intelligence*, 173(11). [Elsevier](https://doi.org/10.1016/j.artint.2009.02.005)
- Geist, C. & Endriss, U. (2011). "Automated Search for Impossibility Theorems in Social Choice Theory." *Journal of Artificial Intelligence Research*, 40. [JAIR](https://www.jair.org/index.php/jair/article/view/10707)
- Nipkow, T. (2009). "Social Choice Theory in HOL: Arrow and Gibbard-Satterthwaite." *Journal of Automated Reasoning*, 43(3). [Springer](https://link.springer.com/article/10.1007/s10817-009-9147-4)

### Difficulte : 5/5

---
