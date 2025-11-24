# Python - Annotations de Variables

<div align="right">
  <a href="README.md">🇬🇧 English</a> | <a href="README.fr.md">🇫🇷 Français</a>
</div>

![Python Variable Annotations](../images/python_annotations_header.png)

## Description

Ce projet explore les annotations de type en Python 3, une fonctionnalité puissante qui vous permet de spécifier les types attendus des variables, des paramètres de fonction et des valeurs de retour. À travers des exercices pratiques, vous apprendrez à écrire du code plus maintenable et auto-documenté, à comprendre les principes du duck typing et à valider votre code à l'aide de vérificateurs de types statiques comme mypy.

Les annotations de type améliorent la lisibilité du code, aident à détecter les bogues tôt pendant le développement et fournissent un meilleur support IDE avec autocomplétion et vérification de types. Ce projet vous donnera une expérience pratique avec le module `typing` de Python et vous enseignera les meilleures pratiques pour l'annotation de types dans les applications Python modernes.

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer sans aide :

### Concepts généraux
- Les annotations de type en Python 3
- Comment utiliser les annotations de type pour spécifier les signatures de fonctions et les types de variables
- Le duck typing
- Comment valider votre code avec mypy
- La différence entre les indications de type et la vérification de type à l'exécution
- Comment utiliser le module `typing` pour les annotations de type complexes
- Les meilleures pratiques pour l'annotation de types en Python

## Ressources

- [Documentation Python 3 typing](https://docs.python.org/fr/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [Aide-mémoire des indications de type (Python 3)](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [Real Python: Python Type Checking](https://realpython.com/python-type-checking/)

## Exigences

### Général
- Éditeurs autorisés : `vi`, `vim`, `emacs`
- Tous vos fichiers seront interprétés/compilés sur Ubuntu 20.04 LTS avec `python3` (version 3.9)
- Tous vos fichiers doivent se terminer par une nouvelle ligne
- La première ligne de tous vos fichiers doit être exactement `#!/usr/bin/env python3`
- Un fichier `README.md`, à la racine du dossier du projet, est obligatoire
- Votre code doit respecter le style `pycodestyle` (version 2.5.)
- Tous vos fichiers doivent être exécutables
- La longueur de vos fichiers sera testée avec `wc`
- Tous vos modules doivent avoir une documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Toutes vos classes doivent avoir une documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- Toutes vos fonctions (à l'intérieur et à l'extérieur d'une classe) doivent avoir une documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` et `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Une documentation n'est pas un simple mot, c'est une vraie phrase expliquant le but du module, de la classe ou de la méthode (la longueur sera vérifiée)

## Structure du projet

```
python_variable_annotations/
├── 0-add.py                    # Annotations de base - addition
├── 1-concat.py                 # Annotations de base - concaténation
├── 2-floor.py                  # Annotations de base - floor
├── 3-to_str.py                 # Annotations de base - to string
├── 4-define_variables.py       # Annotations de variables
├── 5-sum_list.py               # Types complexes - liste de flottants
├── 6-sum_mixed_list.py         # Types complexes - liste mixte
├── 7-to_kv.py                  # Types complexes - tuple
├── 8-make_multiplier.py        # Types complexes - fonctions
├── 9-element_length.py         # Duck typing - objet itérable
└── README.md
```

## Aperçu des tâches

### 0. Annotations de base - add
**Fichier :** `0-add.py`

Écrivez une fonction annotée `add` qui prend un flottant `a` et un flottant `b` comme arguments et retourne leur somme en tant que flottant.

**Exemple :**
```python
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
```

**Sortie :**
```
True
{'a': <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```

### 1. Annotations de base - concat
**Fichier :** `1-concat.py`

Écrivez une fonction annotée `concat` qui prend une chaîne `str1` et une chaîne `str2` comme arguments et retourne une chaîne concaténée.

**Exemple :**
```python
#!/usr/bin/env python3
concat = __import__('1-concat').concat

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)
```

**Sortie :**
```
True
{'str1': <class 'str'>, 'str2': <class 'str'>, 'return': <class 'str'>}
```

### 2. Annotations de base - floor
**Fichier :** `2-floor.py`

Écrivez une fonction annotée `floor` qui prend un flottant `n` comme argument et retourne la partie entière inférieure (floor) du flottant.

**Exemple :**
```python
#!/usr/bin/env python3

import math

floor = __import__('2-floor').floor

ans = floor(3.14)

print(ans == math.floor(3.14))
print(floor.__annotations__)
print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
```

**Sortie :**
```
True
{'n': <class 'float'>, 'return': <class 'int'>}
floor(3.14) returns 3, which is a <class 'int'>
```

### 3. Annotations de base - to string
**Fichier :** `3-to_str.py`

Écrivez une fonction annotée `to_str` qui prend un flottant `n` comme argument et retourne la représentation en chaîne du flottant.

**Exemple :**
```python
#!/usr/bin/env python3
to_str = __import__('3-to_str').to_str

pi_str = to_str(3.14)
print(pi_str == str(3.14))
print(to_str.__annotations__)
print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))
```

**Sortie :**
```
True
{'n': <class 'float'>, 'return': <class 'str'>}
to_str(3.14) returns 3.14, which is a <class 'str'>
```

### 4. Définir des variables
**Fichier :** `4-define_variables.py`

Définissez et annotez les variables suivantes avec les valeurs spécifiées :

- `a`, un entier avec une valeur de 1
- `pi`, un flottant avec une valeur de 3.14
- `i_understand_annotations`, un booléen avec une valeur de True
- `school`, une chaîne avec une valeur de "Holberton"

**Exemple :**
```python
#!/usr/bin/env python3

a = __import__('4-define_variables').a
pi = __import__('4-define_variables').pi
i_understand_annotations = __import__('4-define_variables').i_understand_annotations
school = __import__('4-define_variables').school

print("a is a {} with a value of {}".format(type(a), a))
print("pi is a {} with a value of {}".format(type(pi), pi))
print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations), i_understand_annotations))
print("school is a {} with a value of {}".format(type(school), school))
```

**Sortie :**
```
a is a <class 'int'> with a value of 1
pi is a <class 'float'> with a value of 3.14
i_understand_annotations is a <class 'bool'> with a value of True
school is a <class 'str'> with a value of Holberton
```

### 5. Types complexes - liste de flottants
**Fichier :** `5-sum_list.py`

Écrivez une fonction annotée `sum_list` qui prend une liste `input_list` de flottants comme argument et retourne leur somme en tant que flottant.

**Exemple :**
```python
#!/usr/bin/env python3

sum_list = __import__('5-sum_list').sum_list

floats = [3.14, 1.11, 2.22]
floats_sum = sum_list(floats)
print(floats_sum == sum(floats))
print(sum_list.__annotations__)
print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))
```

**Sortie :**
```
True
{'input_list': typing.List[float], 'return': <class 'float'>}
sum_list(floats) returns 6.470000000000001 which is a <class 'float'>
```

### 6. Types complexes - liste mixte
**Fichier :** `6-sum_mixed_list.py`

Écrivez une fonction annotée `sum_mixed_list` qui prend une liste `mxd_lst` d'entiers et de flottants et retourne leur somme en tant que flottant.

**Exemple :**
```python
#!/usr/bin/env python3

sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list

print(sum_mixed_list.__annotations__)
mixed = [5, 4, 3.14, 666, 0.99]
ans = sum_mixed_list(mixed)
print(ans == sum(mixed))
print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))
```

**Sortie :**
```
{'mxd_lst': typing.List[typing.Union[int, float]], 'return': <class 'float'>}
True
sum_mixed_list(mixed) returns 679.13 which is a <class 'float'>
```

### 7. Types complexes - chaîne et int/float vers tuple
**Fichier :** `7-to_kv.py`

Écrivez une fonction annotée `to_kv` qui prend une chaîne `k` et un int OU float `v` comme arguments et retourne un tuple. Le premier élément du tuple est la chaîne `k`. Le deuxième élément est le carré de l'int/float `v` et doit être annoté comme un float.

**Exemple :**
```python
#!/usr/bin/env python3

to_kv = __import__('7-to_kv').to_kv

print(to_kv.__annotations__)
print(to_kv("eggs", 3))
print(to_kv("school", 0.02))
```

**Sortie :**
```
{'k': <class 'str'>, 'v': typing.Union[int, float], 'return': typing.Tuple[str, float]}
('eggs', 9)
('school', 0.0004)
```

### 8. Types complexes - fonctions
**Fichier :** `8-make_multiplier.py`

Écrivez une fonction annotée `make_multiplier` qui prend un flottant `multiplier` comme argument et retourne une fonction qui multiplie un flottant par `multiplier`.

**Exemple :**
```python
#!/usr/bin/env python3

make_multiplier = __import__('8-make_multiplier').make_multiplier
print(make_multiplier.__annotations__)
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))
```

**Sortie :**
```
{'multiplier': <class 'float'>, 'return': typing.Callable[[float], float]}
4.928400000000001
```

### 9. Duck typing d'un objet itérable
**Fichier :** `9-element_length.py`

Annotez les paramètres et les valeurs de retour de la fonction ci-dessous avec les types appropriés :

```python
def element_length(lst):
    return [(i, len(i)) for i in lst]
```

**Exemple :**
```python
#!/usr/bin/env python3

element_length =  __import__('9-element_length').element_length

print(element_length.__annotations__)
```

**Sortie :**
```
{'lst': typing.Iterable[typing.Sequence], 'return': typing.List[typing.Tuple[typing.Sequence, int]]}
```

## Concepts clés expliqués

### Annotations de type

Les annotations de type sont un moyen de déclarer explicitement les types attendus des variables, des paramètres et des valeurs de retour en Python :

```python
def greet(name: str) -> str:
    return f"Bonjour, {name}!"

age: int = 25
```

### Le module typing

Le module `typing` fournit un support pour les indications de type complexes :

```python
from typing import List, Dict, Tuple, Union, Optional, Callable

# Liste d'entiers
numbers: List[int] = [1, 2, 3]

# Dictionnaire avec clés de type chaîne et valeurs de type entier
scores: Dict[str, int] = {"Alice": 95, "Bob": 87}

# Tuple avec des types spécifiques
point: Tuple[float, float] = (3.14, 2.71)

# Type Union (peut être l'un de plusieurs types)
id_value: Union[int, str] = "ABC123"

# Optional (peut être None)
middle_name: Optional[str] = None

# Type fonction
callback: Callable[[int, int], int] = lambda x, y: x + y
```

### Duck typing

Le duck typing est un concept où le type ou la classe d'un objet est moins important que les méthodes qu'il définit. En Python : "Si ça marche comme un canard et que ça cancane comme un canard, alors ça doit être un canard."

```python
from typing import Iterable

def process_items(items: Iterable[str]) -> None:
    for item in items:
        print(item)

# Fonctionne avec différents types itérables
process_items(["a", "b", "c"])      # list
process_items(("x", "y", "z"))      # tuple
process_items({"key1", "key2"})     # set
```

### Validation avec mypy

`mypy` est un vérificateur de type statique pour Python. Installez-le avec :

```bash
pip install mypy
```

Vérifiez votre code :

```bash
mypy votre_fichier.py
```

**Exemple :**

```python
def add_numbers(a: int, b: int) -> int:
    return a + b

result: int = add_numbers(5, 10)      # ✓ OK
wrong: int = add_numbers(5, "10")     # ✗ Erreur: Argument 2 a un type incompatible
```

### Annotations de type courantes

**Types de base :**
```python
x: int = 42
y: float = 3.14
name: str = "Alice"
is_valid: bool = True
```

**Collections :**
```python
from typing import List, Dict, Set, Tuple

numbers: List[int] = [1, 2, 3]
mapping: Dict[str, int] = {"a": 1, "b": 2}
unique: Set[str] = {"pomme", "banane"}
coordinates: Tuple[float, float] = (10.5, 20.3)
```

**Union et Optional :**
```python
from typing import Union, Optional

# Peut être int ou str
id_value: Union[int, str] = 123

# Peut être str ou None
name: Optional[str] = None  # Identique à Union[str, None]
```

**Callable :**
```python
from typing import Callable

# Fonction qui prend deux entiers et retourne un entier
operation: Callable[[int, int], int] = lambda x, y: x + y
```

## Utilisation

### Exécuter vos scripts

```bash
# Rendre le fichier exécutable
chmod +x 0-add.py

# Exécuter avec le fichier de test
./0-main.py
```

### Vérification de type avec mypy

```bash
# Vérifier un seul fichier
mypy 0-add.py

# Vérifier tous les fichiers Python
mypy *.py

# Mode strict
mypy --strict 0-add.py
```

### Afficher les annotations

```python
# Dans l'interpréteur Python
>>> from typing import get_type_hints
>>> import 0-add
>>> get_type_hints(0-add.add)
{'a': <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}

# Utilisation de __annotations__
>>> 0-add.add.__annotations__
{'a': <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```

## Conseils pour réussir

1. **Commencez simplement** - Commencez par des annotations de type de base avant de passer aux types complexes
2. **Utilisez le module typing** - Importez les types nécessaires depuis `typing` pour les annotations complexes
3. **Soyez cohérent** - Annotez tous les paramètres de fonction et les valeurs de retour
4. **Testez avec mypy** - Validez régulièrement votre code avec mypy pour détecter les erreurs de type
5. **Lisez la documentation** - La documentation officielle Python typing est votre meilleure amie
6. **Considérez la lisibilité** - Les indications de type doivent rendre le code plus lisible, pas moins

## Pièges courants

- Oublier d'importer les types du module `typing`
- Utiliser `list`, `dict`, `tuple` en minuscules au lieu de `List`, `Dict`, `Tuple` depuis typing (en Python < 3.9)
- Ne pas comprendre la différence entre `Union[int, str]` et `Optional[int]`
- Sur-annotation - toutes les variables n'ont pas besoin d'une indication de type
- Confondre les indications de type avec la vérification de type à l'exécution (Python n'applique pas les types à l'exécution)

## Technologies utilisées

- **Python 3.9** : Langage de programmation principal avec support amélioré de l'annotation de types
- **mypy** : Vérificateur de type statique pour Python
- **module typing** : Module de bibliothèque standard pour les indications de type

## Bonnes pratiques

- Toujours annoter les signatures de fonction (paramètres et valeurs de retour)
- Utiliser des noms de variables descriptifs avec des indications de type appropriées
- Utiliser `Union` pour la flexibilité quand un paramètre peut accepter plusieurs types
- Utiliser `Optional` pour les paramètres qui peuvent être `None`
- Documenter les indications de type complexes avec des commentaires si nécessaire
- Exécuter mypy régulièrement pendant le développement pour détecter les erreurs de type tôt

## Auteur

[rpokman](https://github.com/rpokman)

## Licence

Ce projet est destiné à des fins éducatives dans le cadre du programme Holberton School.
