"""
Les listes [valeur1, valeur2...]
À la différence des tuples, on peut ajouter, modifier, supprimer des valeurs de la liste : chaque valeur aura un indice
dont on commencera à compter à partir de 0.
Les listes sont plus utilisées que les tuples car on souhaite généralement changer facilement les valeurs des éléments
de la liste.

Éditeur : Laurent REYNAUD
Date : 28-08-2020
"""

""" Création de listes qui sont encadrées par des '[]' et qui comprennent n'importe quel type d'objet """
ma_liste = [325, 2, 32.7565, 5, 329, 330]
ma_liste_bis = ["test", "essai"]

""" Méthodes pour les listes """
print(type(ma_liste))  # type de la variable
print(len(ma_liste))  # longueur de la liste
print(min(ma_liste))  # plus petite valeur de la liste (ne marche pas s'il y a des str et des chiffres dans la liste)
print(min(ma_liste_bis))  # composant minimum de la str de la liste
print(max(ma_liste))  # plus grande valeur de la liste (ne marche pas s'il y a des str et des chiffres dans la liste)
print(max(ma_liste_bis))  # composant maximum de la str de la liste
print(sum(ma_liste))  # somme de tous les éléments (cette fonction ne marche que pour les chiffres)
print(ma_liste.index(5))  # position (n° d'indice) de la valeur 5 dans la liste
print(ma_liste.count(5))  # nombre d'indices comprenant la valeur saisie et comprise dans la liste (à défaut : 0)
for i, element in enumerate(ma_liste):  # énumération des éléments de la liste
    print("Pour l'indice n°", (i + 1), "l'élément est :", element)
ma_liste.insert(3, 22)  # insertion de la valeur 22 à la position 3
print(ma_liste)
ma_liste.append(17)  # ajout d'une seule valeur au dernier élément de la liste
print(ma_liste)
ma_liste.extend([3.141592657, 59599, 566.5165])  # ajout de plusieurs valeurs à la fin de la liste
print(ma_liste)
ma_liste.remove(330)  # suppression de la valeur 330 dans la liste (à défaut affichage d'une erreur)
print(ma_liste)
del ma_liste[5]  # suppression de la valeur à l'indice 5
print(ma_liste)
ma_liste.pop(2)  # suppression de la valeur à l'indice 2
print(ma_liste)
ma_liste.pop()  # suppression de la dernière valeur de la liste
print(ma_liste)
ma_liste.reverse()  # affichage inversé de la liste
print(ma_liste)
ma_liste.sort()  # trie par ordre croissant
print(ma_liste)
ma_liste.clear()  # suppression de tous les éléments dans la liste
print(ma_liste)
# concernant les copies des listes (dont les sous-listes) voir cours
# C:\Users\LRCOM\Documents\Laurent\Python\Tuto@\MOOC\Module5_Sequences : Cours17_Listes&Comprehension&Copie

""" Accès aux données et découpage en tranches (slicing) """
ma_liste = [325, 2, 32.7565, 5, 329, 330]
print(ma_liste[:])  # affichage de toutes les composantes
print(ma_liste[0])  # accès du 1er composant du tuple
print(ma_liste[1:3])  # la composante d'indice 3 est exclue ce qui revient à ma_liste[1:3[
print(ma_liste[:3])  # affichage des 3 premières composantes (indice 0 à indice 2)
print(ma_liste[3:])  # affichage de toutes les composantes sauf les 3 premières
print(ma_liste[-3:])  # affichage des 3 dernières composantes
print(ma_liste[:-3])  # affichage de toutes les composantes sauf les 3 dernières
print(ma_liste[::2])  # affichage des composantes par pas de 2
print(ma_liste[::-1])  # affichage à l'envers des composantes de la liste

""" Modifications """
ma_liste[2] = 69  # modification de la valeur à l'indice 2
print(ma_liste)
ma_liste[3:5] = 5.1561, 59591  # modification des valeurs à l'indice 3 et 4 (indice 5 exclu)
print(ma_liste)
ma_liste[len(ma_liste):len(ma_liste)] = [7, 99999]  # ajout de ces deux valeurs 7 et 99999 en fin de liste
print(ma_liste)

""" Fixation du nombre d'éléments dans la liste """
notes = []
nbre_notes = int(input("Nombre de notes : "))
for nbre_notes in range(nbre_notes):
    print('Note n°', (nbre_notes + 1), 'obtenue :')
    i = float(input())
    notes.append(i)
print(notes)
moyenne = sum(notes) / nbre_notes
print('Moyenne obtenue :', moyenne, '/20')

""" Les boucles """
# Avec la boucle 'while'
i = 0
while i < len(ma_liste):
    print(ma_liste[i])
    i += 1

# Avec la boucle 'for'
for elements in ma_liste:
    print(elements)

# Avec la boucle 'for in range'
for i in range(len(ma_liste)):
    print("Caractère d'indice", (i + 1), ":", ma_liste[i])

""" Les compréhensions de liste """
# Affichage des éléments de la liste au carré
liste = [1, 2, 3, 4, 5, 6, 7]
print([elements ** 2 for elements in liste])
# Affichage des nombres pairs
print([elements for elements in liste if elements % 2 == 0])

""" Conversion d'une str, d'un tuple ou d'un ensemble en une liste """
# Conversion d'une str en une liste
ma_str = "coucou"
ma_liste = ma_str.split()
print(ma_liste)

# Conversion d'un tuple en une liste
mon_tuple = ("essai", "salut", 3.141592, 17)
ma_liste = list(mon_tuple)
print(ma_liste)

# Conversion d'un ensemble en une liste
mon_ensemble = {"essai2", "salut2", 15.1515, 22}
ma_liste = list(mon_ensemble)
print(ma_liste)
