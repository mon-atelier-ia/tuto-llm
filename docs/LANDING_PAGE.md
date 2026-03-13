# Landing page tuto-llm — Analyse et recommandations

> Date : 2026-03-13
> Contexte : les liens dans la ConclusionPage de microgpt-visualizer-fr pointent vers le repo GitHub brut — un ado de 10-14 ans ne sait pas quoi faire d'un `.ipynb` sur GitHub.

---

## Le standard pour des notebooks pédagogiques

**Google Colab** est le standard de facto pour des notebooks éducatifs, surtout pour des 10-14 ans :

- Zero install, ça tourne dans le navigateur
- Gratuit, GPU dispo si besoin
- Lien direct depuis un README ou une landing page
- Badge "Open in Colab" reconnu partout

Les notebooks GitHub s'ouvrent en Colab via une URL préfixée :

```
https://colab.research.google.com/github/mon-atelier-ia/tuto-llm/blob/main/notebooks/01_deviner_la_suite.ipynb
```

### Liens Colab des 6 notebooks

| # | Notebook | Lien Colab |
|---|----------|------------|
| 1 | Deviner la suite | [Ouvrir](https://colab.research.google.com/github/mon-atelier-ia/tuto-llm/blob/main/notebooks/01_deviner_la_suite.ipynb) |
| 2 | Apprendre des erreurs | [Ouvrir](https://colab.research.google.com/github/mon-atelier-ia/tuto-llm/blob/main/notebooks/02_apprendre_des_erreurs.ipynb) |
| 3 | La mémoire du modèle | [Ouvrir](https://colab.research.google.com/github/mon-atelier-ia/tuto-llm/blob/main/notebooks/03_la_memoire_du_modele.ipynb) |
| 4 | L'attention | [Ouvrir](https://colab.research.google.com/github/mon-atelier-ia/tuto-llm/blob/main/notebooks/04_lattention.ipynb) |
| 5 | Mon premier LLM | [Ouvrir](https://colab.research.google.com/github/mon-atelier-ia/tuto-llm/blob/main/notebooks/05_mon_premier_llm.ipynb) |
| 6 | Entraîner le modèle | [Ouvrir](https://colab.research.google.com/github/mon-atelier-ia/tuto-llm/blob/main/notebooks/06_entrainer_le_modele.ipynb) |

---

## Options pour la landing page

Vu l'écosystème (Vercel, React/Vite, cible jeune) :

### Option 1 — Page statique dans le repo tuto-llm (recommandée)

Un simple `index.html` déployé sur Vercel ou GitHub Pages :
- 6 cartes visuelles (une par notebook) avec liens Colab directs
- Mode d'emploi visuel : 3 étapes max ("1. Clique → 2. Connecte ton compte Google → 3. Joue ▶️")
- Badges progression
- Léger, cohérent, autonome

### Option 2 — Section dans microgpt-visualizer-fr

Ajouter tuto-llm comme parcours complémentaire dans la ConclusionPage (déjà presque en place). Le lien pointerait vers la future landing plutôt que vers le repo GitHub brut.

### Option 3 — Site dédié Vite/React

Overkill sauf si on veut un vrai parcours interactif avec suivi de progression.

---

## Recommandation pour la cible 10-14 ans

- **Landing = page statique simple** (HTML ou Vite minimal) déployée sur Vercel
- **Cartes visuelles** par notebook avec icônes/illustrations qui parlent aux ados
- **Liens Colab directs**, pas des liens GitHub bruts
- **Mode d'emploi visuel** : 3 étapes max
- **Cohérence visuelle** avec microgpt-visualizer-fr (même palette oklch, même typo)

---

## Impact sur microgpt-visualizer-fr

Le lien dans ConclusionPage (`href="https://github.com/mon-atelier-ia/tuto-llm"`) devrait pointer vers la future landing page une fois déployée, plutôt que vers le repo GitHub brut.

En attendant, pointer vers le dossier notebooks est déjà mieux :
```
https://github.com/mon-atelier-ia/tuto-llm/tree/main/notebooks
```
