"""
Les tuples (valeur1, valeur2...)

Les tuples sont non modifiables : on ne peut pas changer les valeurs une fois que la tuple a été initialisée
(équivalent aux tableaux de taille fixe sur Java), à la différence des listes pour lesquelles on peut ajouter, modifier,
supprimer les valeurs.
Cependant, ils sont préférables aux listes partout où l'on veut être certain que les donnéestransmises ne soient pas
modifiées par erreur au sein d'un programme. De plus, les tuples occupent moins de place en mémoire et peuvent être
traîtées plus rapidemen à l'interpréteur.

Pour connaître toutes les méthodes rattachées à un tuple, il suffit d'exécuter l'instruction suivante :
print(help(tuple))

Éditeur : Laurent REYNAUD
Date : 27-08-2020
"""

""" Création de tuples qui sont encadrés par des '()' et qui comprend n'importe quel type d'objet """
mon_tup = (325, 2, 32.7565, 5, 329, 330)
mon_tup_bis = ("test", "essai")

""" Méthodes pour les tuples"""
print(type(mon_tup))  # type de la variable
print(len(mon_tup))  # longueur du tuple
print(min(mon_tup))  # composant minimum (cette fonction ne marche pas s'il y a des str ET des chiffres dans le tuple)
print(min(mon_tup_bis))  # composant minimum de la str
print(max(mon_tup))  # composant maximum (cette fonction ne marche pas s'il y a des str ET des chiffres dans le tuple)
print(max(mon_tup_bis))  # composant maximum de la str
print(sum(mon_tup))  # somme de tous les éléments (cette fonction ne marche que pour les chiffres)
print(mon_tup.index(329))  # affichage du n° d'indice de la valeur comprise dans le tuple (à défaut affichage erreur)
print(mon_tup.count(330))  # nombre d'indices comprenant la valeur saisie et comprise dans le tuple (à défaut : 0)
for i, element in enumerate(mon_tup):  # énumération des éléments du tuples
    print("Pour l'indice n°", (i + 1), "l'élément est :", element)
for element_mon_tup, element_mon_tup_bis in zip(mon_tup, mon_tup_bis):  # regroupage de différents tuples
    print(element_mon_tup_bis, ": ", element_mon_tup)

""" Accès aux données et découpage en tranches (slicing) """
print(mon_tup[:])  # affichage de toutes les composantes
print(mon_tup[0])  # accès du 1er composant du tuple
print(mon_tup[1:3])  # la composante d'indice 3 est exclue ce qui revient à mon_tup[1:3[
print(mon_tup[:3])  # affichage des 3 premières composantes (indice 0 à indice 2)
print(mon_tup[3:])  # affichage des 3 dernières composantes
print(mon_tup[-3:])  # affichage des 3 dernières composantes également
print(mon_tup[:-3])  # affichage de toutes les composantes sauf les 3 dernières
print(mon_tup[::2])  # affichage des composantes par pas de 2

""" Les boucles """
# Avec la boucle 'while'
i = 0
while i < len(mon_tup):
    print(mon_tup[i])
    i += 1

# Avec la boucle 'for'
for element in mon_tup:
    print(element)

# Avec la boucle 'for in range'
for i in range(len(mon_tup)):
    print(mon_tup[i])

""" Conversion d'une str, d'une liste ou d'un ensemble en un tuple """
# Conversion d'une liste en un tuple
ma_liste = ["essai", "test", "salut"]
mon_tup = tuple(ma_liste)
print(type(mon_tup))

# Conversion d'une chaîne de caractères en un tuple
ma_str = "coucou"
mon_tup = tuple(ma_str)
print(type(mon_tup))

# Conversion d'un ensemble en un tuple
mon_ensemble = {"essai2", "test2", "salut2"}
mon_tup = tuple(mon_ensemble)
print(type(mon_tup))
