#### M3 — Regression symbolique — decouvrir des equations a partir de donnees

Utiliser PySR (PySymbolicRegression) pour decouvrir automatiquement des equations mathematiques a partir de donnees experimentales, en combinant la programmation genetique avec le filtrage basé sur la complexite de Kolmogorov et les criteres de parcimonie (Pareto front entre precision et complexite). Les tests se font sur des datasets de reference correspondant a des lois physiques connues (loi de gravitation, equations du pendule, loi des gaz parfaits) et l'evaluation porte sur la precision, la parcimonie et l'interpretabilite des equations decouvertes par rapport aux solutions analytiques connues. La comparaison avec la regression polynomiale classique et les methodes a noyau illustre le gain en interpretabilite.

### Objectifs

- Utiliser PySR pour decouvrir des equations mathematiques a partir de datasets physiques de reference
- Configurer les hyperparametres de la programmation genetique (taille de population, operateurs, complexite max)
- Evaluer la precision, la parcimonie et l'interpretabilite des equations decouvertes
- Comparer avec la regression polynomiale et les methodes de regression a noyau (kernel ridge)
- Analyser la frontiere de Pareto precision-complexite et identifier les equations optimales

## Lois physiques traitees

- Gravitation normalisee: `F = m1*m2/r**2`
- Gaz parfait normalise: `P = n*T/V`
- Pendule simple: `alpha = -(g/L)*sin(theta)`

Les constantes physiques sont normalisees (`G=1`, `R=1`) afin que la recherche
symbolique se concentre sur la structure mathematique.

## Installation

```powershell
python -m pip install -e .
```

PySR installe et utilise Julia via `juliacall` si Julia n'est pas deja presente.
Le premier import peut donc prendre plusieurs minutes.

## Execution rapide

```powershell
m3-symbolic-regression --samples 180 --niterations 8 --populations 4 --population-size 16 --maxsize 18 --procs 1
```

Pour tester seulement la generation de donnees et les baselines classiques:

```powershell
m3-symbolic-regression --skip-pysr
```

Pour une recherche plus serieuse:

```powershell
m3-symbolic-regression --samples 600 --noise 0.005 --niterations 120 --populations 12 --population-size 32 --maxsize 28 --procs 4
```

## Sorties

Le dossier `outputs/` contient:

- `data/*.csv`: datasets synthetiques generes;
- `results/*_pysr_equations.csv`: equations candidates PySR avec RMSE,
  complexite, score d'interpretabilite et proxy de complexite de Kolmogorov;
- `results/metrics.csv`: comparaison PySR / polynomial / kernel ridge;
- `figures/*_pareto.png`: frontieres precision-complexite;
- `figures/model_comparison.png`: comparaison globale;
- `reports/report.md`: synthese experimentale.

## Mesures

- Precision: RMSE, MAE, R2, MAPE.
- Parcimonie: complexite PySR ou nombre de coefficients actifs pour la
  regression polynomiale.
- Proxy Kolmogorov: longueur compressee de la chaine symbolique.
- Interpretabilite: score decroissant avec la complexite et la longueur
  compressee.

## Tests

```powershell
python -m unittest discover -s tests
```

## Notes

La regression symbolique est stochastique. Pour des resultats stables, augmenter
`--niterations`, `--populations` et `--population-size`. Le mode rapide sert
surtout a verifier que toute la chaine experimentale fonctionne. 51)
