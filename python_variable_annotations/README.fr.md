![Python Variable Annotations](images/python_annotations_header.png)

# Python - Annotations de Variables

**Master**
Par : Emmanuel Turlay, Staff Software Engineer chez Cruise
Poids : 1

## Description

Pour ce projet, nous attendons de vous que vous examiniez ces concepts :
*   **Python Avancé**

## Ressources

**Lire ou regarder :**
*   [Documentation Python 3 typing](https://docs.python.org/3/library/typing.html)
*   [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Objectifs d'apprentissage

### Général

À la fin de ce projet, vous êtes censé être capable d'expliquer à n'importe qui, sans l'aide de Google :

*   Les annotations de type en Python 3
*   Comment utiliser les annotations de type pour spécifier les signatures de fonctions et les types de variables
*   Le Duck typing
*   Comment valider votre code avec mypy

## Prérequis

### Général

*   Éditeurs autorisés : `vi`, `vim`, `emacs`
*   Tous vos fichiers seront interprétés/compilés sur Ubuntu 20.04 LTS en utilisant python3 (version 3.9)
*   Tous vos fichiers doivent se terminer par une nouvelle ligne
*   La première ligne de tous vos fichiers doit être exactement `#!/usr/bin/env python3`
*   Un fichier `README.md`, à la racine du dossier du projet, est obligatoire
*   Votre code doit utiliser le style pycodestyle (version 2.5.)
*   Tous vos fichiers doivent être exécutables
*   La longueur de vos fichiers sera testée en utilisant `wc`
*   Tous vos modules doivent avoir une documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   Toutes vos classes doivent avoir une documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
*   Toutes vos fonctions (à l'intérieur et à l'extérieur d'une classe) doivent avoir une documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` et `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
*   Une documentation n'est pas un simple mot, c'est une vraie phrase expliquant le but du module, de la classe ou de la méthode (la longueur sera vérifiée)

## Tâches

| Tâche | Fichier | Description |
| :--- | :--- | :--- |
| **0. Annotations de base - add** | `0-add.py` | Écrivez une fonction annotée `add` qui prend un flottant `a` et un flottant `b` comme arguments et retourne leur somme en tant que flottant. |
| **1. Annotations de base - concat** | `1-concat.py` | Écrivez une fonction annotée `concat` qui prend une chaîne `str1` et une chaîne `str2` comme arguments et retourne une chaîne concaténée. |
| **2. Annotations de base - floor** | `2-floor.py` | Écrivez une fonction annotée `floor` qui prend un flottant `n` comme argument et retourne la partie entière inférieure (floor) du flottant. |
| **3. Annotations de base - to string** | `3-to_str.py` | Écrivez une fonction annotée `to_str` qui prend un flottant `n` comme argument et retourne la représentation en chaîne du flottant. |
| **4. Définir des variables** | `4-define_variables.py` | Définissez et annotez les variables suivantes avec les valeurs spécifiées : `a`, `pi`, `i_understand_annotations`, `school`. |
| **5. Types complexes - liste de flottants** | `5-sum_list.py` | Écrivez une fonction annotée `sum_list` qui prend une liste `input_list` de flottants comme argument et retourne leur somme en tant que flottant. |
| **6. Types complexes - liste mixte** | `6-sum_mixed_list.py` | Écrivez une fonction annotée `sum_mixed_list` qui prend une liste `mxd_lst` d'entiers et de flottants et retourne leur somme en tant que flottant. |
| **7. Types complexes - chaîne et int/float vers tuple** | `7-to_kv.py` | Écrivez une fonction annotée `to_kv` qui prend une chaîne `k` et un int OU float `v` comme arguments et retourne un tuple. |
| **8. Types complexes - fonctions** | `8-make_multiplier.py` | Écrivez une fonction annotée `make_multiplier` qui prend un flottant `multiplier` comme argument et retourne une fonction qui multiplie un flottant par `multiplier`. |
| **9. Duck typing d'un objet itérable** | `9-element_length.py` | Annotez les paramètres et les valeurs de retour de la fonction ci-dessous avec les types appropriés. |
