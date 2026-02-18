# Tuto LLM - Creer son mini-LLM (pour les 10-14 ans)

> Cours progressif pour comprendre et construire un modele de langage,
> inspire de [microgpt.py](https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95) d'Andrej Karpathy.

## Qu'est-ce que microgpt.py ?

L'implementation la plus minimaliste possible d'un GPT en Python pur,
**sans aucune dependance** (pas de PyTorch, NumPy, ou quoi que ce soit).

Karpathy resume :

> *"This file is the complete algorithm. Everything else is just efficiency."*

C'est vrai : l'algorithme est complet. Mais le code brut suppose de maitriser
des notions avancees. Voici ce qu'il contient, ce que ca veut dire en langage
simple, et ce que ce tuto fait pour rendre chaque notion accessible.

---

## Ce que le code suppose -- et comment ce tuto le traduit

### 1. Les derivees et la chaine de derivation

**Dans le code** : microgpt.py implemente un systeme d'"autograd" -- chaque
operation mathematique enregistre comment elle a ete calculee, puis le programme
remonte toute la chaine en sens inverse pour savoir "de combien chaque nombre
a contribue a l'erreur". C'est du calcul differentiel (programme de Terminale/Prepa).

**Traduction simple** : Imagine que tu rates un lancer au panier. Tu sais que
la balle est allee trop a droite. Tu corriges un petit peu a gauche au prochain
essai. Le "de combien corriger" c'est le gradient. La "chaine de derivation"
c'est le fait de remonter chaque etape du lancer (angle du bras, force, position)
pour savoir laquelle corriger.

**Dans le tuto** : La lecon 2 utilise directement cette analogie. On calcule la
correction (le gradient) de facon simplifiee, sans jamais ecrire une derivee.
L'eleve voit la loss baisser et comprend le principe sans les maths.

---

### 2. Les multiplications matricielles

**Dans le code** : Quasiment toute l'intelligence du modele passe par des
multiplications de matrices -- des grilles de nombres multipliees entre elles.
C'est de l'algebre lineaire (programme de fac/ecole d'ingenieur).

**Traduction simple** : Une matrice c'est un "filtre" qui transforme une liste
de nombres en une autre liste de nombres. Comme un filtre Instagram qui
transforme les couleurs d'une photo : les pixels entrent, le filtre fait
ses calculs, de nouveaux pixels sortent. Ici les "pixels" ce sont les nombres
qui representent les lettres.

**Dans le tuto** : Les lecons 3 et 5 font des multiplications matrice x vecteur
avec des boucles Python simples (`for i... for j...`). L'eleve n'a pas besoin
de savoir ce qu'est une matrice -- il voit juste que des nombres entrent,
d'autres sortent, et ca donne des predictions.

---

### 3. L'optimisation par descente de gradient

**Dans le code** : microgpt.py utilise l'optimiseur Adam, un algorithme avance
qui ajuste les poids du modele en tenant compte de la vitesse et de l'acceleration
des corrections passees. Il inclut aussi un "learning rate decay" (la vitesse
de correction ralentit au fil du temps). C'est de l'optimisation numerique
(programme de Master/Doctorat).

**Traduction simple** : Au debut de l'entrainement, le modele fait des grosses
corrections parce qu'il est completement perdu. Au fur et a mesure, il fait
des corrections de plus en plus fines, comme un sculpteur qui passe du marteau
au papier de verre. Adam, c'est un sculpteur intelligent qui se souvient de
ses gestes precedents pour mieux ajuster les suivants.

**Dans le tuto** : La lecon 2 utilise une descente de gradient basique avec un
seul parametre (`vitesse`). Pas d'Adam, pas de decay -- juste "on corrige un
peu dans la bonne direction a chaque fois". L'eleve voit que ca marche,
et c'est suffisant pour comprendre le principe.

---

### 4. Le softmax

**Dans le code** : La fonction softmax transforme des scores bruts (qui peuvent
etre n'importe quel nombre, positif ou negatif) en probabilites (entre 0 et 1,
somme = 1). Elle utilise la fonction exponentielle, ce qui amplifie les
differences : un score un peu plus haut devient beaucoup plus probable.

**Traduction simple** : Imagine un vote. Chaque lettre a un score de popularite.
Le softmax c'est comme transformer ces scores en pourcentages : "la lettre 'e'
a 40% des voix, 'a' a 25%, etc." Les lettres avec un meilleur score raflent
une plus grosse part du gateau.

**Dans le tuto** : On l'introduit dans la lecon 1 sans la nommer (on fait
juste "diviser par le total pour avoir des pourcentages"). Le vrai softmax
avec exponentielle apparait dans la lecon 3, presente comme "une facon plus
maligne de transformer des scores en probabilites".

---

### 5. Les embeddings

**Dans le code** : Chaque caractere est represente par un vecteur de nombres
(par exemple 48 dimensions dans microgpt.py). Ces vecteurs sont appris
pendant l'entrainement. Deux lettres qui se comportent de facon similaire
finissent avec des vecteurs proches dans cet espace a 48 dimensions.

**Traduction simple** : Imagine que tu dois decrire chaque lettre de l'alphabet
avec 3 notes sur 10 : "frequence a debut de mot", "frequence apres une voyelle",
"frequence en fin de mot". La lettre 'q' et la lettre 'x' auraient des notes
similaires (rares, positions speciales). Ces notes, c'est l'embedding.
Sauf que le modele choisit tout seul quelles "notes" utiliser -- et il en
utilise beaucoup plus que 3.

**Dans le tuto** : La lecon 3 commence avec des vecteurs de taille 8
(au lieu de 48). L'eleve cree les embeddings, les voit changer pendant
l'entrainement, et comprend que le modele "place" les lettres similaires
proches les unes des autres.

---

### 6. Le mecanisme d'attention

**Dans le code** : Le self-attention calcule pour chaque position un triplet
Query/Key/Value. La Query est comparee a toutes les Keys via un produit
scalaire, les scores passent par un softmax, puis les Values sont aggregees
en somme ponderee. Un masque causal empeche de regarder le futur.
Tout ca est repete sur 4 tetes en parallele.

**Traduction simple** : Imagine une salle de classe. Chaque eleve (= chaque
lettre) peut lever la main pour poser une question (Query). Les autres eleves
montrent une pancarte avec leur specialite (Key). L'eleve choisit a qui
demander en comparant sa question avec les pancartes. Puis il recupere
l'information (Value) de ceux qui correspondent le mieux. Le masque causal
c'est simple : tu ne peux poser de questions qu'aux eleves assis **devant toi**
-- pas a ceux derriere (le futur).

**Dans le tuto** : La lecon 4 decompose tout avec le mot "chat" comme exemple
concret. L'eleve calcule les scores a la main, voit les poids d'attention,
et comprend pourquoi certaines lettres "comptent" plus que d'autres.

---

### 7. Ce que microgpt.py ne fait PAS

Meme si l'algorithme est complet, ce script minimaliste omet volontairement :

| Fonctionnalite | Pourquoi c'est absent | Impact |
|---|---|---|
| **GPU / CUDA** | Python pur, pas de parallelisme | 1000x plus lent qu'avec PyTorch |
| **Tenseurs / Vectorisation** | Boucles for au lieu d'operations matricielles batch | Chaque calcul se fait nombre par nombre |
| **Tokenizer BPE** | Utilise des caracteres individuels | Ne peut pas apprendre des mots entiers |
| **Plusieurs couches** | 1 seule couche transformer | Capacite tres limitee (patterns courts seulement) |
| **LayerNorm complet** | Utilise RMSNorm (plus simple) | Moins stable sur de gros modeles |
| **GeLU** | Utilise ReLU (plus simple) | Performances legerement inferieures |
| **Dropout** | Pas de regularisation | Risque de sur-apprentissage sur de gros datasets |
| **RLHF / Fine-tuning** | Pas d'alignement humain | Ne peut pas "suivre des instructions" comme ChatGPT |
| **Fenetre de contexte longue** | ~16-32 caracteres | Ne peut pas "se souvenir" de phrases entieres |
| **Inference optimisee** | Pas de KV-cache, pas de quantization | Chaque token regenere tout le calcul |

**En resume** : microgpt.py demontre le "quoi" (l'algorithme), pas le "comment
aller vite" (l'ingenierie). C'est exactement ce qui le rend ideal pour apprendre.

---

## Objectif du tuto

A la fin du cours, l'eleve :

1. Comprend comment une IA "devine" le mot suivant
2. A entraine son propre mini-modele
3. Genere des prenoms ou mots inventes avec son modele
4. Sait expliquer les mots "embedding", "attention", "loss" et "gradient"
5. Comprend ce qui differencie son mini-modele de ChatGPT (l'echelle, pas l'algorithme)

## Pre-requis

- Python 3.10+
- Jupyter Notebook (`pip install jupyter`)
- Savoir ecrire des boucles et des fonctions en Python (niveau debutant)
- Aucune notion de maths avancees requise

## Structure du cours

| # | Notebook | Concept cle | Analogie | Duree |
|---|---------|-------------|----------|-------|
| 1 | `01_deviner_la_suite.ipynb` | Probabilites, bigrammes | T9 / clavier predictif | 30 min |
| 2 | `02_apprendre_des_erreurs.ipynb` | Loss, gradient, entrainement | Lancer au panier | 45 min |
| 3 | `03_la_memoire_du_modele.ipynb` | Embeddings, contexte, reseau | Notes sur 10 pour chaque lettre | 30 min |
| 4 | `04_lattention.ipynb` | Attention, Q/K/V, masque causal | Salle de classe | 45 min |
| 5 | `05_mon_premier_llm.ipynb` | Assemblage complet, generation | De 0 a GPT | 45 min |

## Lancer

```bash
cd "tuto llm"
jupyter notebook
```

## References

- [microgpt.py - Karpathy](https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95) -- le script source
- [micrograd - Karpathy](https://github.com/karpathy/micrograd) -- autograd seul, encore plus minimal
- [nanoGPT - Karpathy](https://github.com/karpathy/nanoGPT) -- version PyTorch, entrainable pour de vrai
- [Video "Let's build GPT"](https://www.youtube.com/watch?v=kCc8FmEb1nY) -- explication complete en 2h (anglais)
