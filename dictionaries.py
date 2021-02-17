"""
Les dictionnaires {clé1 : valeur1, clé2 : valeur2...}

Les dictionnaires sont assimilables aux Hashmap dans Java : les éléments ne sont pas ordonnés (il n'y a donc pas
d'indice).
Chaque clé du dictionnaire est unique. Lorsque au moins deux valeurs d'un dictionnaire sont identiques, seule la
dernière valeur sera affichée. Les valeurs d'un dictionnaire ne sont pas numérotées comme c'est le cas d'une liste ou
d'un tuple.

Pour connaître toutes les méthodes rattachées à un ensemble, il suffit d'exécuter l'instruction suivante :
print(help(dict))

Éditeur : Laurent REYNAUD
Date : 02/09/2020
"""

""" Création de dictionnaires qui sont encadrées par des '{}' et qui comprennent n'importe quel type d'objet """
mon_dico_vide = {}  # dictionnaire vide : attention ce n'est pas un ensemble vide !
mon_dico = {"ma_cle1": 17, "ma_cle2": 3.141592, "ma_cle3": 22}

""" Méthodes pour les dictionnaires """
print(type(mon_dico))  # type de la variable
print(len(mon_dico))  # longueur du dictionnaire
print(min(mon_dico))  # plus petite clé du dictionnaire
print(min(mon_dico.values()))  # plus petite valeur du dictionnaire
print(max(mon_dico))  # plus grande clé du dictionnaire
print(max(mon_dico.values()))  # plus grande valeur du dictionnaire
print(sum(mon_dico.values()))  # somme de tous les valeurs (cette fonction ne marche que pour les chiffres)
for i, element in enumerate(mon_dico.values()):  # énumération des valeurs du dictionnaire
    print("Pour l'indice n°", (i + 1), "la valeur est :", element)
print(mon_dico.pop("ma_cle5", "Clé inconnue"))  # suppression de la clé saisie et de la valeur rattachée : le
# deuxième paramètre de la méthode "pop" permet de signaler si la clé que l'on souhaite supprimer n'existe. A défaut,
# un message d'erreur s'affiche.
del (mon_dico["ma_cle3"])  # autre méthode pour supprimer une clé saisie avec la valeur rattachée
print(mon_dico)
mon_dico.clear()  # suppression de tous les éléments dans la liste
print(mon_dico)
mon_dico = {"ma_cle1": 17, "ma_cle2": 3.141592, "ma_cle3": 22}
mon_dico = {}.fromkeys("adse", 22)  # toutes les clés ont la même valeur (chaque lettre "adse" est une clé)
print(mon_dico)
# Concernant les méthodes sur les copies, voir :
# C:\Users\LRCOM\Documents\Laurent\Python\Tuto@\MOOC\Module6_Ensembles&Dictionnaires\Cours3_Dictionnaires&Methodes

""" Accès aux données """
mon_dico = {"ma_cle1": 17, "ma_cle2": 3.141592, "ma_cle3": 22}
print(mon_dico.get("ma_cle4", "Cette clé n'existe pas"))  # recherche de la valeur à la clé saisie sinon possibilité
# de mettre un commentaire (ici : "Cette clé n'existe pas")
print(mon_dico.keys())  # affichage de toutes les clés
print(mon_dico.values())  # affichage de toutes les valeurs
print(mon_dico.items())  # affichage de toutes les clés et les valeurs

""" Modifications et ajouts """
mon_dico["ma_cle4"] = 69  # ajout d'une donnée (clé + valeur)
print(mon_dico)
mon_dico.setdefault("ma_cle5", 519.1989)  # ajoute la clé si elle n'exite pas à défaut il n'y a pas d'erreur
print(mon_dico)
mon_dico.update({"ma_cle1": 5959, "ma_cle3": 1717, "ma_cle6": 1.5})  # modification et ajout de données (clé + valeur)
print(mon_dico)

""" Les boucles """
# Avec la boucle 'for'
for cle in mon_dico:  # affichage des clés
    print(cle)
for valeur in mon_dico.values():  # affichage des valeurs
    print(valeur)
for cle, valeur in mon_dico.items():
    print(cle, ":", valeur)  # affichage des clés et des valeurs

""" Conversion d'une liste, d'un tuple en un dictionnaire """
# Conversion d'une liste de couple (tuple)
ma_liste = [("elt1", 5.156), ("elt2", 22), ("elt3", 756.159)]
mon_dico = dict(ma_liste)
print(mon_dico)

# Conversion d'un tuple de couple
mon_tuple = (("elt1", 5.156), ("elt2", 22), ("elt3", 756.159))
mon_dico = dict(mon_tuple)
print(mon_dico)
