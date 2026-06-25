---
version: alpha
name: Neuro-Symbolic Deck System
description: Direction visuelle claire, colorée et animée pour une présentation IA symbolique.
colors:
  background: "#F9F7F0"
  surface: "#FFF8E7"
  text: "#3A2E39"
  muted: "#6E5D68"
  border: "#E7D8CD"
  accent: "#D7263D"
  secondary: "#F46036"
  info: "#7CC6FE"
typography:
  display:
    fontFamily: "Space Grotesk"
    fontSize: "66px"
    fontWeight: 700
    lineHeight: 1
  body:
    fontFamily: "Archivo"
    fontSize: "32px"
    fontWeight: 500
    lineHeight: 1.35
rounded:
  sm: "14px"
  md: "24px"
  lg: "40px"
spacing:
  sm: "16px"
  md: "32px"
  lg: "74px"
components:
  slide-background:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text}"
  graph-node:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text}"
  attack-arrow:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.background}"
---

## Overview
Deck 16:9 pour un projet d'IA neuro-symbolique : énergique, pédagogique, moins sombre, avec des fonds crème ou prune coloré plutôt que noirs.

## Colors
La palette canonique est `#d7263d`, `#f46036`, `#3a2e39`, `#7cc6fe`, `#f9f7f0`. Les fonds principaux doivent privilégier crème/énergie ; le prune sert de profondeur, jamais de noir plat.

## Typography
Titres en Space Grotesk, corps en Archivo, annotations techniques en Space Mono. Titres formulés comme des phrases d'action.

## Layout
Une idée par slide, grandes marges, schémas horizontaux, composants sur cartes crème avec bordures colorées.

## Motion
Entrées séquencées fortes, flèches dessinées, nœuds en pop, fonds animés par grilles et halos continus.

## Do's and Don'ts
- Do: raccourcir les flèches pour que les pointes restent visibles hors des nœuds.
- Do: utiliser des fonds crème + halos rouge/orange/bleu.
- Don't: employer un fond noir ou quasi-noir plein écran.
- Don't: masquer les pointes de flèches derrière des nœuds ou un viewport SVG trop serré.
