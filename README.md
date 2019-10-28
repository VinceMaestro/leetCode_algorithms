Attention !!

Python utilise ce qu’on appelle le PYTHON PATH pour chercher les modules importables.
C’est une variable système qui contient une liste de dossiers.
Si il n’en trouve pas, il va lever une ImportError.
Le dossier qui contient le module sur lequel vous lancez la commande python est
automatiquement ajouté au PYTHON PATH.
Si je lance un shell Python depuis la racine, je peux faire import sur tous les fichiers
de ce dossier ou des sous dossiers, car .../leetCode_algorithms est automatiquement ajouté au PYTHON PATH.

Le meilleurs moyen de résoudre c'est en réfléchissant bien à la structure du projet !!
D'où le choix de cet arborescence.

Plus d'infos (http://sametmax.com/les-imports-en-python/)
