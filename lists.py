"""
Les listes [valeur1, valeur2...]
À la différence des tuples, on peut ajouter, modifier, supprimer 
des valeurs de la liste : chaque valeur aura un indice dont on commencera 
à compter à partir de 0.
Les listes sont plus utilisées que les tuples car on souhaite généralement 
changer facilement les valeurs des éléments de la liste.

Les listes sont mutables à la différences des str et des tuples qui sont immuables.
À titre d'exemple :
a = [1, 2, 3]
b = a
a += [4, 5, 6]
a -> [1, 2, 3, 4, 5, 6]
b -> [1, 2, 3, 4, 5, 6]
La liste "a" a le même objet que la liste "b"

Éditeur : Laurent REYNAUD
Date : 28-08-2020
"""

""" Création de listes qui sont encadrées par des '[]' 
et qui comprennent n'importe quel type d'objet """
ma_liste = [325, 2, 32.7565, 5, 329, 330]
print(f"ma_liste : {ma_liste}")
ma_liste_bis = ["test", "essai"]
print(f"ma_liste_bis : {ma_liste_bis}")

# Fonctions natives pour les listes
print("\nFONCTIONS NATIVES SUR LES LISTES\n\n")
print(f"Type de l'objet 'ma_liste': {type(ma_liste)}")
print(f"Longueur de 'ma_liste' : {len(ma_liste)}")
print(f"Plus petite valeur de 'ma_liste' : {min(ma_liste)}")
print(f"Composant minimum de 'ma_liste_bis' : {min(ma_liste_bis)}")
print(f"Plus grande valeur de 'ma_liste' : {max(ma_liste)}")
print(f"Composant maximum de 'ma_liste_bis' : {max(ma_liste_bis)}")
print(f"Somme de tous les éléments de 'ma_liste' : {sum(ma_liste)}")
print("Les fonctions natives ci-après ne portent que sur la liste 'ma_liste'")
print(f"N° d'indice de la 1ère valeur 5 : {ma_liste.index(5)}")
for i, element in enumerate(ma_liste):
    print("Pour l'indice n°", (i + 1), "l'élément est :", element)
ma_liste.insert(3, 22)
print(f"Insertion de la valeur 22 à la position 3 : {ma_liste}")
ma_liste.append(17)
print(f"Ajout de la valeur 17 qui se trouve en fin de liste : {ma_liste}")
ma_liste.extend([3.141592657, 59599, 566.5165])
print(f"Ajout de plusieurs valeurs en fin de liste : {ma_liste}")
ma_liste.remove(330)
print(f"Suppression de la valeur 330 dans la liste : {ma_liste}")
del ma_liste[5]
print(f"Supression de la valeur à l'indice n° 5 : {ma_liste}")
ma_liste.pop(2)
print(f"Supression de la valeur à l'indice n° 2 : {ma_liste}")
ma_liste.pop()
print(f"Suppression de la dernière valeur de la liste : {ma_liste}")
ma_liste.reverse()
print(f"Affichage inversé de la liste : {ma_liste}")
ma_liste.sort() 
print(f"Trie par ordre croissant : {ma_liste}")
ma_liste.clear() 
print(f"Suppression de tous les éléments dans la liste : {ma_liste}")

"""Accès aux données et découpage en tranches (slicing) 
Cours complémentaire sur les slices : 
https://zestedesavoir.com/tutoriels/582/les-slices-en-python/"""
print("\n\nLES SLICES\n")
ma_liste = [325, 2, 32.7565, 5, 329, 330, 17, 152, 895, 2.16, "ça va ?"]
print(f"Affichage de tous les composants : {ma_liste[:]}")
print(f"Affichage du 1er composant : {ma_liste[0]}")
print(f"Affichage du composant n° 1 au n° 2 (composant n° 3 exclu):{ma_liste[1:3]}")
print(f"Affichage des 3 premiers composants : {ma_liste[:3]}")
print(f"Affichage de tous les composants sauf les 3 premiers : {ma_liste[3:]}")
print(f"Affichage des 3 derniers composants : {ma_liste[-3:]}")
print(f"Affichage de tous les composants sauf les 3 derniers : {ma_liste[:-3]}")
print(f"Affichage des composants par pas de deux : {ma_liste[::2]}")
print(f"Affichage entre le 3ème composant et le 3ème en partant de la fin, par pas de 2 : {ma_liste[3:-3:2]}")
print(f"Affichage entre le 3ème en partant de la fin et le 3ème composant, par pas de 2 : {ma_liste[-3:3:-2]}")
print(f"Affichage des composants à l'envers : {ma_liste[::-1]}")

""" Modifications """
print("\n\nLES MODIFICATIONS\n")
ma_liste = [325, 2, 32.7565, 5, 329, 330, 17, 152, 895, 2.16, "ça va ?"]
print(ma_liste)
ma_liste[2] = 69
print(f"Modification de la valeur à l'indice 2 : {ma_liste}")
ma_liste[3:5] = 5.1561, 59591
print(f"Modification des valeurs à l'indice 3 et 4 : {ma_liste}")
ma_liste[len(ma_liste):len(ma_liste)] = [7, 99999]
print(f"Ajout de plusieurs valeurs en fin de liste : {ma_liste}")

""" Les boucles """
print("\n\nLES BOUCLES\n")
print(f"{ma_liste}\n")
print("\nAvec la boucle 'while'")
i = 0
while i < len(ma_liste):
    print(ma_liste[i])
    i += 1

print("\nAvec la boucle 'for'")
for elements in ma_liste:
    print(elements)

print("\nAvec la boucle 'for in range'")
for i in range(len(ma_liste)):
    print("Caractère d'indice", (i + 1), ":", ma_liste[i])

""" Les compréhensions de liste """
print("\n\nLES COMPREHENSIONS DE LISTE\n")
liste = [1, 2, 3, 4, 5, 6, 7]
print(f"{liste}\n")
print("Affichage des éléments de la liste au carré")
print([elements ** 2 for elements in liste])
print("Affichage des nombres pairs")
print([elements for elements in liste if elements % 2 == 0])

"""Recours au module 'collections'"""
from collections import deque
print("\n\nMODULE COLLECTIONS\n")

"""L'intérêt de l'objet deque est qu'on peut intervenir sur une liste sur ses extrêmités : aussi bien à droite des 
éléments de la liste (comme pour une liste classique) que sur les éléments à gauche de la liste.
L'objet deque est une liste d'un tuple mais modifiable"""

deque_list = [1, 2, 3]
print(deque_list)
d = deque(deque_list)
print(d)
d.appendleft(4)
print(f"Ajout de la valeur 4 à l'indice 0 : {d}")
d.popleft()
print(f"Suppression de la valeur à l'indice 0 : {d}")
d.extendleft([4, 3, 2])
print(f"Ajout de valeurs à gauche du deque mais par odre inversée : {d}")

""" Conversion d'une str, d'un tuple ou d'un ensemble en une liste """
print("\n\nLES CONVERSIONS\n")

print("Conversion d'une str en une liste")
ma_str = "coucou"
print(ma_str)
ma_liste = ma_str.split()
print(ma_liste)

print("\nConversion d'un tuple en une liste")
mon_tuple = ("essai", "salut", 3.141592, 17)
print(mon_tuple)
ma_liste = list(mon_tuple)
print(ma_liste)

print("\nConversion d'un ensemble en une liste")
mon_ensemble = {"essai2", "salut2", 15.1515, 22}
print(mon_ensemble)
ma_liste = list(mon_ensemble)
print(ma_liste)
