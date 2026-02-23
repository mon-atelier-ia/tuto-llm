# Pratiques pedagogiques pour notebooks Jupyter (10-14 ans)

Recherche documentaire realisee le 2026-02-23 pour le projet Tuto LLM.
Synthese des conventions et bonnes pratiques identifiees dans les projets
de reference ciblant le meme public (colleges, ateliers decouverte IA).

---

## Sources de reference

### 1. Capytale (Education nationale, France)

[Capytale](https://capytale2.ac-paris.fr/) est la plateforme officielle
de l'Education nationale pour les notebooks Python au college et lycee.
~80 000 utilisateurs/semaine.

**Conventions identifiees** :

- **Cellules de consigne en markdown** : l'enseignant redige les
  instructions dans des cellules markdown non editables, l'eleve
  ecrit dans des cellules code separees.
- **Protection des cellules** : les cellules de cours sont verrouillees
  (`"editable": false` dans les metadonnees). L'eleve ne peut modifier
  que les cellules d'exercice.
- **Progression sequentielle** : les cellules sont executees de haut
  en bas. Sauter une cellule casse l'execution.
- **Activites de type "completer le code"** : code a trous avec
  commentaires `# A COMPLETER` ou `# VOTRE CODE ICI`.

### 2. EPFL - Les 4 cles de la pedagogie (Suisse)

Recherche en sciences de l'education de l'EPFL, appliquee aux cours
de programmation pour debutants.

**Les 4 cles** :

| Cle | Description | Application notebooks |
|-----|-------------|----------------------|
| **Progression** | Du simple au complexe, une notion a la fois | 6 lecons progressives, chaque concept construit sur le precedent |
| **Resolution de problemes** | L'eleve fait, pas seulement lit | Exercices avec cellules vides a completer |
| **Feedback immediat** | L'eleve voit le resultat tout de suite | Shift+Entree affiche le resultat instantanement |
| **Objectifs visibles** | L'eleve sait ou il va | Chaque notebook annonce ce qu'on va apprendre |

### 3. jupyter4edu - Catalogue de 23 patterns (UC Berkeley)

Le projet [jupyter4edu](https://jupyter4edu.github.io/jupyter-edu-book/)
de UC Berkeley documente 23 patterns pedagogiques pour Jupyter.

**Patterns les plus pertinents pour Tuto LLM** :

| Pattern | Description | Application |
|---------|-------------|-------------|
| **Shift-Enter for the Win** | La premiere cellule doit etre executable immediatement, sans prerequis. L'eleve apprend le geste Shift+Entree des la premiere interaction. | Cellule d'accueil avec instructions + premier `print()` |
| **Fill in the Blanks** | Code a trous : la structure est donnee, l'eleve complete les parties manquantes. Reduit l'angoisse de la page blanche. | `# --- EXERCICE : Ecris ton code ici ---` |
| **Target Practice** | L'eleve voit le resultat attendu avant de coder. Il sait a quoi son code doit aboutir. | "Execute la cellule pour verifier tes reponses" |
| **Tweak Twiddle Frob** | L'eleve modifie une valeur dans du code fonctionnel et observe l'effet. Pas de creation ex nihilo. | `nombre = 10  # <-- Mets 50 ici !` |
| **Narrative Arc** | Le notebook raconte une histoire avec debut, milieu, fin. Pas une collection de cellules decousues. | Progression : compter -> probabilites -> generer |
| **Scaffolding** | Structure fournie, complexite progressive. Les premieres cellules sont entierement donnees, les dernieres demandent plus d'autonomie. | Exercice 1 = executer, Exercice 4 = modifier |

### 4. py-edu-fr - Conventions Python pedagogique (France)

Conventions emergentes de la communaute Python educative francaise
(NSI, ISN, SNT, ateliers decouverte).

**Conventions identifiees** :

- **Variables en francais** : `compteur`, `lettre`, `prenom` plutot
  que `counter`, `letter`, `name`. Le public ne parle pas anglais.
- **Commentaires explicatifs** : chaque bloc de code est commente
  en francais, expliquant le "pourquoi" pas seulement le "quoi".
- **`print()` genereux** : afficher les resultats intermediaires
  pour que l'eleve voie ce qui se passe a chaque etape.
- **Pas de one-liners** : privilegier la lisibilite sur la concision.
  `for i in range(10): print(i)` plutot que des comprehensions.
- **Analogies avant le code** : chaque concept est introduit par
  une analogie du quotidien avant toute ligne de code.

### 5. Callysto (Canada)

[Callysto](https://www.callysto.ca/) -- programme canadien de
notebooks educatifs pour les 10-18 ans, finance par Cybera et PIMS.

**Conventions identifiees** :

- **Titre clair en haut** : chaque notebook commence par un titre
  et un paragraphe d'objectif ("Dans ce notebook, tu vas...").
- **Emojis et visuels** : utilises avec parcimonie pour attirer
  l'attention sur les points importants.
- **Sections courtes** : maximum 3-4 cellules entre deux exercices.
  L'attention des 10-14 ans est limitee (~10 minutes par bloc).
- **Cellules de validation** : apres un exercice, une cellule
  "verifie ta reponse" donne un feedback immediat.

### 6. ML for Kids (Royaume-Uni)

[ML for Kids](https://machinelearningforkids.co.uk/) -- plateforme
d'initiation au machine learning pour les 8-14 ans, par Dale Lane (IBM).

**Conventions identifiees** :

- **Vocabulaire adapte** : eviter le jargon technique. "Le modele
  devine" plutot que "inference probabiliste".
- **Resultats tangibles** : chaque lecon produit quelque chose de
  visible et amusant (un nom genere, un dessin, un jeu).
- **Pas de prerequis mathematiques** : les maths sont cachees
  derriere des analogies. L'eleve ne voit jamais une formule.

### 7. Kaggle Learn (international)

[Kaggle Learn](https://www.kaggle.com/learn) -- micro-cours
interactifs sur la data science et le ML.

**Conventions identifiees** :

- **Exercices a difficulte croissante** : chaque lecon a 3-5
  exercices, du plus simple au plus ouvert.
- **Code de demarrage fourni** : l'eleve ne part jamais d'une
  cellule vide. Il y a toujours du code a modifier ou completer.
- **Indices progressifs** : un bouton "indice" revele une aide
  avant la solution complete.

---

## Conventions appliquees a Tuto LLM

Synthese des conventions retenues pour les 6 notebooks du projet,
basee sur l'analyse des sources ci-dessus.

### Structure de chaque notebook

```
[Cellule 0]  Titre + accueil + mode d'emploi Jupyter
             "Comment ca marche ? 1. Clique... 2. Shift+Entree..."

[Cellule 1]  Introduction du concept (markdown)
             Analogie du quotidien, vocabulaire simple

[Cellule 2]  Code de demonstration
             L'eleve execute, observe le resultat

[Cellule 3]  Exercice explicite (markdown)
             "A toi de jouer ! (Exercice N)"

[Cellule 4]  Cellule code vide/editable
             "# --- EXERCICE N : Ecris ton code ici ---"

  ... (repetition du cycle demonstration/exercice) ...

[Avant-derniere]  Resume "Ce qu'on a appris"
                  3-4 bullet points, lien vers lecon suivante

[Derniere]  Sources (ISO 42001)
            Citations, copyright, references
```

### Regles de redaction

| Regle | Justification | Source |
|-------|---------------|--------|
| **Cellule d'accueil** avec mode d'emploi Jupyter | L'eleve n'a peut-etre jamais vu un notebook | jupyter4edu "Shift-Enter for the Win" |
| **Separateurs `---`** entre sections | Repere visuel dans le flot de cellules | Callysto, Capytale |
| **"A toi de jouer !"** en titre d'exercice | Marqueur explicite, pas de confusion cours/exercice | Capytale, EPFL "Resolution de problemes" |
| **Cellules code vides** pour les exercices | L'eleve sait ou ecrire | jupyter4edu "Fill in the Blanks" |
| **Commentaire `# <-- Change cette valeur !`** | Guide l'oeil vers le point d'action | jupyter4edu "Tweak Twiddle Frob" |
| **`print()` apres chaque etape** | Feedback visuel immediat | EPFL "Feedback immediat", py-edu-fr |
| **Variables en francais** | Public francophone de 10-14 ans | py-edu-fr |
| **Analogie avant le code** | Ancrage dans le concret | ML for Kids, EPFL "Progression" |
| **Maximum 4 cellules entre exercices** | Attention limitee (~10 min par bloc) | Callysto |
| **Difficulte croissante des exercices** | Du "execute" au "modifie" au "cree" | Kaggle Learn, jupyter4edu "Scaffolding" |
| **Resume en fin de notebook** | L'eleve sait ce qu'il a appris | EPFL "Objectifs visibles" |
| **Sources citees** | Transparence, anti-hallucination | ISO 42001, AI_POLICY.md |

### Progression des exercices (scaffolding)

La difficulte des exercices progresse au sein de chaque notebook :

| Niveau | Type | Exemple | Pattern jupyter4edu |
|--------|------|---------|---------------------|
| 1 | **Executer** | "Execute la cellule pour voir le resultat" | Shift-Enter for the Win |
| 2 | **Observer** | "Que remarques-tu dans le resultat ?" | Target Practice |
| 3 | **Modifier** | "Change le nombre 10 en 50" | Tweak Twiddle Frob |
| 4 | **Completer** | "Ecris le code pour afficher le dernier element" | Fill in the Blanks |
| 5 | **Creer** | "Invente ta propre fonction" | (notebooks avances uniquement) |

Les notebooks 01-03 vont du niveau 1 au niveau 4.
Les notebooks 04-06 atteignent le niveau 5 pour certains exercices.

### Marqueurs visuels dans les cellules

**Markdown (cours)** :
```markdown
---
## Titre de section

Explication avec **mots cles en gras** et analogie.
```

**Markdown (exercice)** :
```markdown
---
### A toi de jouer ! (Exercice N)

Consigne claire en 1-3 lignes. Indice entre backticks : `code`.
```

**Code (demonstration)** :
```python
# Execute cette cellule pour ... (Shift + Entree)
resultat = calcul()
print(f"Le resultat est : {resultat}")
```

**Code (exercice editable)** :
```python
# --- EXERCICE N : Ecris ton code ici, puis Shift + Entree ---

# Consigne 1 :


# Consigne 2 :

```

**Code (valeur a modifier)** :
```python
# --- EXERCICE N : Change la valeur, puis Shift + Entree ---
ma_variable = 10  # <-- Change cette valeur !

print(f"Resultat avec {ma_variable} : ...")
```

---

## Ce que Tuto LLM ne fait PAS (et pourquoi)

| Pratique | Raison du rejet |
|----------|-----------------|
| **Protection de cellules** (`"editable": false`) | Non supporte par JupyterLite. Capytale le fait mais on n'utilise pas Capytale. |
| **Auto-grading** (nbgrader) | Trop complexe pour un atelier decouverte. Pas de serveur pour la correction. |
| **Widgets interactifs** (ipywidgets) | Dependance externe, incompatible avec la contrainte zero-install stdlib. |
| **Emojis dans le code** | Distraction. Reserves aux titres markdown si necessaire. |
| **Indices masquables** (bouton "hint") | Pas de support HTML interactif fiable dans JupyterLite. Indices donnes directement dans la consigne. |
| **Tests automatiques dans les cellules** | Ajoute du bruit visuel. Le `print()` suffit comme feedback pour ce public. |

---

## References

1. **Capytale** -- Plateforme de l'Education nationale :
   https://capytale2.ac-paris.fr/

2. **EPFL - 4 cles de la pedagogie** :
   https://www.epfl.ch/education/educational-initiatives/

3. **jupyter4edu - Teaching and Learning with Jupyter** :
   https://jupyter4edu.github.io/jupyter-edu-book/

4. **Callysto - Computational Thinking for K-12** :
   https://www.callysto.ca/

5. **ML for Kids** -- Dale Lane, IBM :
   https://machinelearningforkids.co.uk/

6. **Kaggle Learn** -- Micro-cours interactifs :
   https://www.kaggle.com/learn

7. **py-edu-fr** -- Communaute Python educative francaise :
   conventions observees dans les manuels NSI/SNT (Bordas, Hatier, Hachette)
