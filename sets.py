"""
Les ensembles {...}
Tout comme le Hashmap dans Java, il n'y a pas d'ordre d'affichage pour un ensemble : il est donc impossible
de récupérer un élément par sa position à la différence des séquences.

L'avantage de ce type de données c'est lorsque dans une liste on a des doublons : pour cela, il suffit de convertir la
liste en un ensemble puis la reconvertir en une liste

Pour connaître toutes les méthodes rattachées à un ensemble, il suffit d'exécuter l'instruction suivante :
print(help(set))

Éditeur : Laurent REYNAUD
Date : 01/09/2020
"""

""" Création des ensembles qui sont encadrés par des '{}' et qui comprennent n'importe quel type d'objet """
mon_ensemble_vide = set()  # déclaration d'un ensemble vide
mon_ensemble = {2.5619, 17, 56.515, 22}
a = set("alakazam")
b = set("abracadabra")

""" Méthodes pour les ensembles """
print(type(mon_ensemble))  # type de la variable
print(len(mon_ensemble))  # longueur de l'ensemble
mon_ensemble.add(562.1515)  # ajoute d'une seule valeur en dernière position de l'ensemble
print(mon_ensemble)
mon_ensemble.discard(33)  # supprime cette valeur dans l'ensemble (à défaut absence de message d'erreur)
print(mon_ensemble)
mon_ensemble.pop()  # suppression au hasard d'une valeur de l'ensemble
print(mon_ensemble)
mon_ensemble.clear()  # supprime tous les éléments de l'ensemble
print(mon_ensemble)

""" Accès aux données et découpages en tranches (slicing) : recours à la fonction prédéfinie set()"""
print(a - b)  # affiche les lettres qui sont dans l'ensemble 'a' et non présentes dans l'ensemble 'b'
print(a | b)  # affiche l'ensemble des lettres des ensembles 'a' et 'b'
print(a & b)  # affiche les lettres présentes dans l'ensemble 'a' ET dans l'ensemble 'b'
print(a ^ b)  # affiche les lettres qui ne sont pas communes aux ensembles 'a' et 'b'

""" Les boucles """
mon_ensemble = {2.5619, 17, 56.515, 22}

# Avec la boucle 'for'
for i in mon_ensemble:
    print(i)

""" Conversion d'une str, d'un tuple ou d'une liste en un ensemble """
# Conversion d'une str en un ensemble
ma_str = "salut"
mon_ensemble = set(ma_str)
print(mon_ensemble)

# Conversion d'un tuple en un ensemble
mon_tuple = ("coucou", "hello", 22, 3.51651, 556)
mon_ensemble = set(mon_tuple)
print(mon_ensemble)

# Conversion d'une liste en un ensemble
ma_liste = ["test", "essai", 516516, 5.151655, 756]
mon_ensemble = set(ma_liste)
print(mon_ensemble)

""" Suppression des doublons dans une liste """
entries = ['John', 'Albert', 'Machin', 'Dark Vador', 'Machin', 'Mozart', 'Einstein', 'Hulk', 'Shrek', 'Mozart',
           'Einstein', 'Dame de pique', 'Machin', 'Albert', 'Einstein', 'Dame de pique']
print(len(entries))  # 16 entrées, doublons inclus
my_set = set(entries)
unique_entries = list(my_set)
print(len(unique_entries))  # il reste plus que 9 entrées, les doubles de la liste initiale ont été supprimés
print(unique_entries)
