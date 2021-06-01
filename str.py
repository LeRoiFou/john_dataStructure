"""
Les chaînes de caractères (str) "texte" ne sont rien d'autres que des séquences de caractères.
On ne peut pas modifier les éléments d'une str, elle est donc immuable.

Pour connaître toutes les méthodes rattachées à une str, il suffit d'exécuter l'instruction suivante :
print(help(str))

Éditeur : Laurent REYNAUD
Date : 01-09-2020
"""

""" Création de str qui sont encadrées par des 'texte' """
ma_str = "   salut ! la forme 17 ?   "
print(f"ma_str : {ma_str}")

# Fonctions natives pour les str 
print("\n\nLES FONCTIONS NATIVES\n")
print(f"Type d'objet : {type(ma_str)}")
print(f"Longueur de la str : {len(ma_str)}")
print(f"Plus petite valeur : {min(ma_str)}")
print(f"Plus grande valeur : {max(ma_str)}")
print(f"N° indice de la valeur recherchée 'a' : {ma_str.index('a')}")
print(f"Str en minuscules : {ma_str.lower()}")
print(f"Str en majuscules : {ma_str.upper()}")
print(f"N° d'indice de la valeur recherchée '?' : {ma_str.find('?')}")
print(f"Recherche du caractère 'a' à partir de l'indice n° 3 : indice n° {ma_str.find('a', 3)}")
print("Est-ce que ma chaîne de caractères se termine par '17 ?'")
if ma_str.endswith('17 ?'): 
    print("oui oui ça finit bien par '17 ?'")
else:
    print('euh... non... il doit y avoir quelque chose à la fin de la str...')
ma_str = ma_str.replace("la forme 17 ?", "John Gerald !")
print(f"Remplacement d'une str : {ma_str}")
print(f"Suppression des espaces en début et fin de la str : {ma_str.strip()}")
ma_str = ma_str.strip()
print(f"Majuscule pour la 1ère lettre de la chaîne de caractères : {ma_str.capitalize()}")
print(f"Inversion des majuscules et des minuscules : {ma_str.swapcase()}")
print(f"Le premier caractère de chaque mot est une majuscule : {ma_str.title()}")
print(f"Boléen -> True si la str est en minuscule : {ma_str.islower()}")
print(f"Boléen -> True si la str est en majuscule : {ma_str.isupper()}")
print(f"Boléen -> True si la str n'a que des chiffres : {ma_str.isdigit()}")
print(f"Boléen -> True si la str n'a que des caractères alphanumériques : {ma_str.isalnum()}")
print(f"Boléen -> True si la str n'a que des caractères alphabétiques{ma_str.isalpha()}")
for i, element in enumerate(ma_str):
    print("Pour le caractère n°", (i + 1), "l'élément est :", element)
my_str = "Ceci/est/un/test"
print(my_str)
my_split = (my_str.split("/"))
print(f"Affichage en liste avec suppression du '/' : {my_split}")
my_new_str = "_".join(my_split)
print(f"Concaténation de la liste ci-avant avec le '_' : {my_new_str}")

""" Mise en forme """
print("\n\nMISE EN FORME\n")
long_t = "******************" \
         "* Bon anniversaire ! *" \
         "********************"
print(f"Str sur plusieurs lignes : {long_t}")
print("Saut de page :\nEssai 1 \nEssai 2 \nEssai 3")
print("Tabulation :\nEssai 11 \tEssai 12 \tEssai 13")
print("Concatenation :\nCeci est un test :" + " 1, 2, 3 !")
print("Répétition :\nEssai !" * 5)
print("Séparateur :\n", "x" * 10, "+" * 10, "x" * 10, sep="|")
print("Guillemets dans un texte :\nC'est vraiment \"dommage !\"")
print("Largeurs fixes :")
comptes = [
 ('Apollin', 'Dupont', 127),
 ('Myrtille', 'Lamartine', 25432),
 ('Prune', 'Soc', 827465),
]
for prenom, nom, solde in comptes:
    # < : affichage à gauche de la console
    # ^ : affichage centré de la console
    # > : affichage à droite de la console
    print(f"{prenom:<10} -- {nom:^12} -- {solde:>8} €")

""" Accès aux données et découpage en tranches (slicing) 
Cours complémentaire sur les slices : https://zestedesavoir.com/tutoriels/582/les-slices-en-python/"""
print("\n\nLES SLICES\n")
print(f"Affichage de tous les composants : {ma_str[:]}")
print(f"Affichage du 1er composant : {ma_str[0]}")
print(f"Affichange du composant n° 1 au n° 2 (composant n° 3 exclu):{ma_str[1:3]}")
print(f"Affichage des 3 premiers composants : {ma_str[:3]}")
print(f"Affichage de tous les composants sauf les 3 premiers : {ma_str[3:]}")
print(f"Méme résultat que précédemment : {ma_str[3:-3]}")
print(f"Affichage des 3 derniers composants : {ma_str[-3:]}")
print(f"Affichage de tous les composants sauf les 3 derniers : {ma_str[:-3]}")
print(f"Affichage des composants par pas de deux : {ma_str[::2]}")
print(f"Affichage entre le 3ème composant et le 3ème en partant de la fin, par pas de 2 : {ma_str[3:-3:2]}")
print(f"Affichage entre le 3ème en partant de la fin et le 3ème composant, par pas de 2 : {ma_str[-3:3:-2]}")
print(f"Affichage des composants à l'envers : {ma_str[::-1]}")

""" Les boucles """
print("\n\nLES BOUCLES\n")
print(f"{ma_str}\n")
print("Avec la boucle 'while' :")
i = 0
while i < len(ma_str):
    print(ma_str[i])
    i += 1

print("Avec la boucle 'for' :")
for elements in ma_str:
    print(elements)

print("Avec la boucle 'for in range' :")
for i in range(len(ma_str)):
    print("Caractère n°", (i + 1), ":", ma_str[i])

""" Conversion d'une liste, ..., en une str """
print("\n\nLES CONVERSIONS\n")
print(f"{ma_str}\n")

print("Conversion d'une liste de str")
ma_liste_bis = [2, 3.141592, 51, 561.121321, "essai"]
print(ma_liste_bis)
ma_str = "/".join(map(str, ma_liste_bis))
print(ma_str)

print("Conversion d'un tuple en str")
mon_tuple = ("test", "coucou", "hello !", 3.1561516, 56)
print(mon_tuple)
ma_str = "/".join(map(str, mon_tuple))
print(ma_str)

print("Conversion d'un ensemble en str (affichage dans le désordre)")
mon_ensemble = {"test", "coucou", "hello !", 3.1561516, 56}
print(mon_ensemble)
ma_str = "/".join(map(str, mon_ensemble))
print(ma_str)
