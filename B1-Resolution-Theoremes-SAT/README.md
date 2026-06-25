# B1 - Resolution automatique de theoremes par SAT

Projet EPITA 2026 de Programmation par Contraintes et IA symbolique pour le sujet B1.

Le probleme consiste a encoder des enonces combinatoires en formules booleennes CNF, puis a utiliser un solveur SAT pour decider leur satisfiabilite. Le rendu couvre la transformation de Tseitin, les encodages DIMACS, trois familles classiques de problemes et une comparaison avec un encodage SMT Z3.

## Livrables

- `rapport.md`: rapport final du projet, avec formulation, encodages, resultats et limites.
- `README.md`: presentation rapide du rendu et commandes de reproduction.
- `benchmark_overview.png`: synthese graphique du benchmark SAT/SMT.
- `src/`: code source des encodeurs, solveurs, validations et experiences.
- `run_experiments.py`: script de reproduction du benchmark.
- `results/`: sorties CSV, exemples DIMACS, tentatives de preuves et figures produites par les experiences.
- `notebook.ipynb`: annexe explicative et exploratoire.

## Structure du code

- `src/cnf.py`: structure CNF, clauses, export DIMACS et verification de modeles.
- `src/tseitin.py`: AST propositionnel et transformation de Tseitin.
- `src/encodings.py`: encodages graph coloring, pigeonhole principle et Ramsey `R(3,3)`.
- `src/solver_sat.py`: interface PySAT et fallback DPLL pour petites instances.
- `src/solver_smt.py`: encodages SMT Z3 equivalants.
- `src/proof.py`: export de CNF UNSAT et verification optionnelle de preuves externes avec `drat-trim`.
- `src/validation.py`: interpretation et validation des modeles SAT.
- `src/experiments.py`: pipeline de benchmark et agregations.
- `src/plotting.py`: generation des visualisations.
- `src/test_solver.py`: test de fumee reproductible.

## Installation

```bash
python -m pip install -r requirements.txt
```

`drat-trim` n'est pas une dependance Python: il doit etre installe separement et disponible dans le `PATH` pour verifier les certificats UNSAT.

## Verification rapide

```bash
python -m src.test_solver
```

Le test reste executable sans PySAT grace au solveur DPLL minimal inclus.

## Reproduire les resultats

```bash
python run_experiments.py
```

Sorties generees:

- `results/benchmark_raw.csv`
- `results/benchmark_summary.csv`
- `results/dimacs/*.cnf`
- `results/proofs/`
- `results/figures/benchmark_overview.png`
- `benchmark_overview.png`
