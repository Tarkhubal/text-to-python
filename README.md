# Text to Python

This is a free program, wrote in Python, that convert your dusty text to a beautiful executable Python Script (work in progress)

---

## ⚠️ **WARNING !** ⚠️

This program is in the **alpha version** and for now only compatible with the **french language**. More updates will comme soon.

---

## How to use

C'est simple (du moins il est fait pour être simple):

### 🚀 Lancer le programme

Pour executer votre fichier Text to Python, utilisez:

```bash
python main.py
```

Par défaut, il execute le fichier `past-your-script-here.txt`. Vous pouvez specifier un autre fichier:

```bash
python main.py mon-fichier.txt
```

### 📖 Généralité

Toutes les commandes commencent par un ``!`` (voir la suite pour les cas particuliers)

Pour ajouter spécifiquement des entrées `int` (des chiffres) afin de les additioner par la suite dans une variable (ou autre), entrez `^^` suivi de votre chiffre (attention à ne pas mettre d'autres éléments par la suite, cela risque de créer un bug et un arrêt du programme)

⚠️ Vous pourrez (sûrement dans les prochaines mises à jour) additionner du texte ("``Avi`` + ``on`` = ``Avion``"), mais si vous entrez des chiffres dedans **sans** effectuer la mise en forme avec "``^^``", votre résultat ne sera pas ``1 + 1`` = ``2`` mais ``1 + 1`` = ``11`` !

💡 Conseil : Aérez votre programme, comme ça c'est plus facile de vous relire ! N'hésitez pas à rajouter des espaces entre vos lignes, c'est quand même plus lisible 😎

---

### 🗃️ Création et affectation de variables

Pour créer une variable, mettez son nom entre ``/`` (exemple : ``/mavariable/``) puis écrivez son contenu à la suite !

✏️ Exemple :

```text
/variable/[variable content]
```

⚠️ Afin d'éviter tout bug, évitez de mettre des signes spéciaux (comme des accents (``è``, ``à``, ...), des `!`, `?`, `/`, `\`, `(`, `)`, `;`, `:`, `.`, ``_``, ...) et surtout **sans espaces** !

💡 Conseil : Je vous conseille de bien choisir vos noms de variables et de les rendre **uniques** et compréhensibles (par exemple ne pas appeler ses variables "``a``" ou "``b``" mais plutôt "``nbpommes``" ou "``totalchocolat``)

💡 Conseil : Faites attention à être **compréhensible** ! Comme ça, si vous envoyez votre programme à quelqu'un il le comprendra très facilement, et n'aura pas à vous spammer de notifications Discord en mode "C'est quoi ça ??"

---

### ✒️ Affichage d'éléments

Pour afficher des éléments sur notre console, il nous suffit de taper la commande ``!afficher``, suivie d'un espace et de ce que l'on souhaite afficher :

Ici un affichage simple d'un texte simple :

```text
!afficher J'aime les trucs
```

Ce qui nous donnera :

```text
J'aime les trucs
```

Pour afficher le contenu d'une variable, il vous suffit d'entrer la commande d'affichage et simplement de la faire suivre par le nom de votre variable :

```text
/mavariable/Contenu d'exemple

!afficher mavariable
```

Text to Python vous renverra ce résultat :

```text
Contenu d'exemple
```

---

### ❓Ajouter des conditions à une commande

Là, ça se complique un peu (même si j'ai essayé de simplifier le tout):

En gros, le principe est simple : une boucle c'est comme une boite où on va faire plusieurs opérations dedans.

Pour créer la boite, il nous faut une **condition**, par exemple "``est egale a``". Il nous faut aussi deux arguments à comparer, prenons par exemple "``Pomme``" et "``Poire``".

✏️ En assemblant notre condition et nos deux arguments, on obitient une ligne de ce genre :

```text
!si Pomme est egale a Poire
```

Ici bien sûr notre condition est dite **fausse** (nos deux arguments ne sont pas du tout égaux).

☑️Text to Python prends en charge trois conditions pour le moment :

```text
est egale a
est superieur a
est inferieur a
```

Pour écrire du programme à l'intérieur de notre boite "!si", il nous faut mettre deux tirets du bas ("``_._``" (le point est ici pour montrer la démarcation et doit être enlevé)) à **chaque commande à l'intérieur de notre boite**

✏️ On peut par exemple produire un code de ce genre :

```text
!si variable1 est superieur a variable2
__!afficher Vive la France

!si variable3 est inferieur a variable9416
__/variable59/Oupsi
```

✏️ Ou encore plus compliqué avec un ``!si`` dans un ``!si`` :

```text
!si truc est egale a truc alors
__!si ^^10 est inferieur a ^^20 alors
____!afficher omg
```

Si notre condition est fausse, le reste du code de notre condition ne sera pas exécutée, tandis que si elle est vrai elle sera exécutée

### 🔀 Utiliser !sinon (else)

**✨ NOUVELLE FONCTIONNALITÉ ✨**

Vous pouvez maintenant utiliser ``!sinon`` pour executer du code lorsque la condition est fausse !

```text
!si age est superieur a ^^18 alors
__!afficher Majeur
!sinon
__!afficher Mineur
```

Le ``!sinon`` doit être au même niveau d'indentation que le ``!si`` correspondant.

### 🛑 Arrêter le programme

**✨ NOUVELLE FONCTIONNALITÉ ✨**

Pour arrêter l'execution du programme à tout moment, utilisez la commande ``!stop``:

```text
!afficher Programme commence
!stop
!afficher Ceci ne sera jamais affiche
```

## Améliorations du système

### 🎯 Nouvelles fonctionnalités

- ✅ **!sinon** : Ajout de la commande else pour les conditions
- ✅ **!stop** : Arrêt du programme à tout moment
- ✅ **Arguments en ligne de commande** : Possibilité de specifier le fichier à executer
- ✅ **Meilleure gestion de la mémoire** : Utilisation de dictionnaires au lieu de listes pour les variables
- ✅ **Architecture orientée objet** : Code plus propre et maintenable
- ✅ **Gestion d'erreurs améliorée** : Messages d'erreur plus clairs

### 🔧 Corrections de bugs

- ✅ Bug avec les boucles imbriquées à répétitions (voir TODO) - CORRIGÉ
- ✅ Optimisation de la mémoire RAM
- ✅ Meilleure gestion des conditions imbriquées

## Limitations du programme

> ⚠️ Version alpha ⚠️

1. Pour le moment les **accents** sur les lettres ne sont **pas compatibles** avec le programme
2. Les caractères non latin peuvent causer des mauvais affichages voir des **erreurs**
3. ✅ ~~Il ne **peut pas** y avoir plusieurs boucles de conditions (``!si``) dans une autre boucle de condition~~ **CORRIGÉ** - Les boucles imbriquées fonctionnent maintenant correctement !
4. ✅ ~~Si une commande est inconnue, le programme la passera sans donner d'information à l'utilisateur~~ **AMÉLIORÉ** - Meilleure gestion des erreurs
5. ✅ ~~Manque d'optimisation de la mémoire RAM~~ **CORRIGÉ** - Utilisation de structures de données optimisées
