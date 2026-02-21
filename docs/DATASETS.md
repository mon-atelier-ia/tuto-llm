# Datasets - Référence complète

Ce document liste tous les datasets intégrés au projet et les datasets
découverts pour une extension future du mini-LLM.

## Vocabulaire actuel

Le mini-LLM utilise un vocabulaire de 27 tokens : `.` (début/fin) + `a-z`.
Les datasets marqués "compatible" fonctionnent directement avec ce vocabulaire.
Les autres nécessitent un vocabulaire étendu.

---

## Datasets intégrés

### 1. Prénoms INSEE

| Champ | Valeur |
|-------|--------|
| Fichier | `data/prenoms.txt` |
| Source | [INSEE - Fichier des prénoms depuis 1900](https://www.insee.fr/fr/statistiques/7633685) |
| Licence | Licence ouverte Etalab 2.0 |
| Taille | ~30 800 prénoms uniques (min 2 caractères) |
| Format | Un prénom par ligne, trié alphabétiquement |
| Nettoyage | Lowercase, accents supprimés (NFKD), filtré a-z, min 2 chars |
| Compatible vocab | Oui |

**Usage** : Dataset principal pour entraîner le mini-LLM à générer
des prénoms français lettre par lettre (notebooks 3-5).

### 2. Dinosaures

| Champ | Valeur |
|-------|--------|
| Fichier | `data/dinosaures.txt` |
| Source | [dinos.txt - Dvelezs94](https://gist.github.com/Dvelezs94/24bfcc8ab6042613ab5d94275e2e395a) |
| Licence | Public domain (gist public) |
| Taille | ~1 524 noms uniques |
| Format | Un nom par ligne, trié alphabétiquement |
| Nettoyage | Lowercase, filtré a-z uniquement |
| Compatible vocab | Oui |

**Usage** : Dataset alternatif compact. Inspiré du cours de Karpathy
([makemore](https://github.com/karpathy/makemore)), idéal pour montrer
que le même modèle apprend des distributions différentes.

### 3. Haiku (usage futur)

| Champ | Valeur |
|-------|--------|
| Fichier | `data/haiku.csv` |
| Source | [haikurnn - docmarionum1](https://github.com/docmarionum1/haikurnn) |
| Licence | **Incertaine** (voir note ci-dessous) |
| Taille | 1 000 haiku (échantillon) |
| Format | CSV : line1, line2, line3, source |
| Compatible vocab | Non (espaces, ponctuation, majuscules) |

**Note licence** : Le plan initial prévoyait le dataset
[bfbarry/haiku-dataset](https://www.kaggle.com/datasets/bfbarry/haiku-dataset)
(CC0) sur Kaggle, mais le téléchargement Kaggle nécessite une authentification.
La source de substitution (haikurnn) collecte des haiku depuis des sites
publics (tempslibres, haikuhut, etc.) sans fichier LICENSE dans le repo.
Le statut juridique est donc incertain. Ce dataset est stocké uniquement
comme référence pour un usage futur et ne doit pas être redistribué
sans vérification préalable des droits.

**Usage futur** : Nécessite un vocabulaire étendu (caractères spéciaux,
espaces, ponctuation). Pourrait servir pour un notebook avancé sur
la génération de texte libre.

---

## Datasets compatibles char-level (extensions possibles)

Ces datasets sont compatibles avec le vocabulaire actuel (a-z) après
nettoyage, et pourraient être intégrés facilement.

### Communes de France

| Champ | Valeur |
|-------|--------|
| Source | [INSEE - Code officiel géographique](https://www.insee.fr/fr/information/2560452) |
| Licence | Licence ouverte Etalab 2.0 |
| Taille estimée | ~35 000 noms |
| Concept ML | Distribution plus complexe que les prénoms |
| Notes | Noms composés fréquents (saint-, le-, la-) à nettoyer |

### Mythologie grecque

| Champ | Valeur |
|-------|--------|
| Source | Listes Wikipédia (divinités, héros, créatures) |
| Licence | CC BY-SA 3.0 |
| Taille estimée | ~500 noms |
| Concept ML | Petit dataset, risque de surapprentissage |
| Notes | Noms romanisés, déjà en caractères latins |

### Minéraux et pierres

| Champ | Valeur |
|-------|--------|
| Source | [Mindat.org](https://www.mindat.org/) ou Wikidata |
| Licence | Variable (Wikidata : CC0) |
| Taille estimée | ~5 000 noms |
| Concept ML | Vocabulaire technique, suffixes récurrents (-ite, -ase) |
| Notes | Bonne illustration des patterns morphologiques |

### Pokémon (noms anglais)

| Champ | Valeur |
|-------|--------|
| Source | [PokéAPI](https://pokeapi.co/) |
| Licence | API publique |
| Taille estimée | ~1 000 noms |
| Concept ML | Noms inventés avec des patterns reconnaissables |
| Notes | Populaire auprès du public cible (10-14 ans) |

---

## Autres datasets pour concepts ML avancés

Ces datasets nécessitent un vocabulaire étendu mais illustrent
des concepts ML intéressants pour de futurs notebooks.

### Fables de La Fontaine

| Champ | Valeur |
|-------|--------|
| Source | [Projet Gutenberg](https://www.gutenberg.org/ebooks/56327) |
| Licence | Domaine public |
| Taille estimée | ~240 fables, ~10 000 lignes |
| Concept ML | Génération de texte long, structure poétique |
| Notes | Texte en français classique, riche en vocabulaire |

### SMS Spam Collection

| Champ | Valeur |
|-------|--------|
| Source | [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection) |
| Licence | CC BY 4.0 |
| Taille | 5 574 SMS (747 spam, 4 827 ham) |
| Concept ML | Classification binaire, NLP de base |
| Notes | En anglais, introduction à la classification |

### Tatoeba (phrases bilingues)

| Champ | Valeur |
|-------|--------|
| Source | [Tatoeba](https://tatoeba.org/fr/downloads) |
| Licence | CC BY 2.0 FR |
| Taille | ~400 000 paires français-anglais |
| Concept ML | Traduction, séquence à séquence |
| Notes | Trop avancé pour le cours actuel |

### Proverbes français

| Champ | Valeur |
|-------|--------|
| Source | Collections Wikiquote / domaine public |
| Licence | Domaine public / CC BY-SA |
| Taille estimée | ~2 000 proverbes |
| Concept ML | Patterns syntaxiques récurrents |
| Notes | Nécessite vocab étendu (espaces, ponctuation) |

### Fromages AOC/AOP

| Champ | Valeur |
|-------|--------|
| Source | [data.gouv.fr - Fromages AOP](https://www.data.gouv.fr/) |
| Licence | Licence ouverte Etalab |
| Taille estimée | ~50 noms |
| Concept ML | Très petit dataset, démonstration du surapprentissage |
| Notes | Compatible a-z après nettoyage des accents |

### Trivia / Questions-Réponses

| Champ | Valeur |
|-------|--------|
| Source | [Open Trivia Database](https://opentdb.com/) |
| Licence | CC BY-SA 4.0 |
| Taille | ~4 000 questions |
| Concept ML | Question answering, compréhension de texte |
| Notes | En anglais, nécessite vocab complet |

---

## Reproduction des datasets

Le script `scripts/build_datasets.py` télécharge les sources brutes
et produit les fichiers finaux. Il peut être relancé à tout moment
pour régénérer les datasets à l'identique :

```bash
python scripts/build_datasets.py
```

## Chargement des datasets

Utiliser les fonctions de `src/tuto_llm/data.py` :

```python
from tuto_llm.data import (
    charger_csv,
    charger_dataset,
    formater_training,
    nettoyer_mot,
    valider_vocab,
)

# Charger un dataset texte (un mot par ligne)
noms = charger_dataset("data/prenoms.txt")

# Charger un dataset CSV (haiku)
haiku = charger_csv("data/haiku.csv")  # -> list[dict]

# Nettoyer un mot avec accents
clean = nettoyer_mot("Éloïse")  # -> "eloise"

# Valider la compatibilité vocab (min 2 chars)
valides = valider_vocab(noms, min_len=2)

# Formater pour l'entraînement du mini-LLM
training = formater_training(valides)  # -> [".alice.", ".bob.", ...]
```
