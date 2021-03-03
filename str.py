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
long_t = "******************" \
         "* Bon anniversaire ! *" \
         "********************"  # chaîne de caractères sur plusieurs lignes
print(long_t)

""" Méthodes pour les str """
print(type(ma_str))  # type de la variable
print(len(ma_str))  # longueur de la str
print(min(ma_str))  # plus petite valeur de la str
print(max(ma_str))  # plus grande valeur de la str
print(ma_str.index("a"))  # 1er n° d'indice de la valeur recherchée
print(ma_str.lower())  # minuscules
print(ma_str.upper())  # majuscules
print(ma_str.find("?"))  # n° d'indice de la valeur recherchée
print(ma_str.find("a", 3))  # recherche à partir de l'indice 3 le n° d'indice de la valeur recherchée
if ma_str.endswith('17 ?'):  # recherche des derniers caractères de la str
    print("oui oui ça finit bien par '17 ?'")
else:
    print('euh... non... il doit y avoir quelque chose à la fin de la str...')
ma_str = ma_str.replace("la forme 17 ?", "connard 22 !")  # remplacement d'une str
print(ma_str)
ma_str = ma_str.strip()  # suppression des espaces en début et en fin de la str
print(ma_str)
ma_str = ma_str.capitalize()  # majuscule pour la 1ère lettre de la str
print(ma_str)
print(ma_str.swapcase())  # inversion des majuscules et des minuscules de la str
print(ma_str.title())  # le premier caractère de chaque mot est en majuscule
print(ma_str.islower())  # booléen : true si la str est en minuscule
print(ma_str.isupper())  # booléen : true si la str est en majuscule
print(ma_str.isdigit())  # booléen : true si la str ne comprend que des chiffres
print(ma_str.isalnum())  # booléen : true si la str ne contient que des caractères alphanumériques
print(ma_str.isalpha())  # booléen : true si la str ne contient que des caractères alphabétiques
for i, element in enumerate(ma_str):  # énumération des éléments de la str
    print("Pour le caractère n°", (i + 1), "l'élément est :", element)

""" Mise en forme """
print("Essai 1 \nEssai 2 \nEssai 3")  # saut de page
print("Essai 11 \tEssai 12 \tEssai 13")  # tabulation
print("Ceci est un test :" + " 1, 2, 3 !")  # concaténation
print("Essai !" * 5)  # répétition
print("x" * 10, "+" * 10, "x" * 10, sep="|")  # séparateur
print("C'est vraiment \"dommage !\"")  # guillemets dans un texte


def create_message(character, quote):  # fusion de deux chaînes de caractères en recourant à une fonction
    res = "{} a dit : {}".format(character, quote)
    return res


def create_message_bis(character, quote):  # autre solution en recourant cette fois-ci à la fonction "f-strings"
    """La fonction f_strings est préconisée compte tenu de sa simplicité par rapport à la fonction ci-avant.
    Pour afficher un réel avec par exemple 2 décimales, il suffit d'effectuer les instructions suivantes :
    f"{instruction}:.2f" """
    return f"{character} a dit : {quote}"


personnage = "Tyler Joseph"
citation = "They told me I was gone"
print(create_message(personnage, citation))
print(create_message_bis(personnage, citation))

""" Accès aux données et découpage en tranches (slicing) 
Cours complémentaire sur les slices : https://zestedesavoir.com/tutoriels/582/les-slices-en-python/"""
print(ma_str[:])  # affichage de toutes les composantes
print(ma_str[0])  # accès du 1er composant du tuple
print(ma_str[1:3])  # la composante d'indice 3 est exclue ce qui revient à ma_str[1:3[
print(ma_str[:3])  # affichage des 3 premières composantes (indice 0 à indice 2)
print(ma_str[3:])  # affichage de toutes les composantes sauf les 3 premières
print(ma_str[-3:])  # affichage des 3 dernières composantes
print(ma_str[:-3])  # affichage de toutes les composantes sauf les 3 dernières
print(ma_str[::2])  # affichage des composantes par pas de 2
print(ma_str[::-1])  # affichage à l'envers de toutes les composantes de la str

""" Les boucles """
# Avec la boucle 'while'
i = 0
while i < len(ma_str):
    print(ma_str[i])
    i += 1

# Avec la boucle 'for'
for elements in ma_str:
    print(elements)

# Avec la boucle 'for in range'
for i in range(len(ma_str)):
    print("Caractère n°", (i + 1), ":", ma_str[i])

""" Conversion d'une liste, ..., en une str """
# Conversion d'une liste den str
ma_liste_bis = [2, 3.141592, 51, 561.121321, "essai"]
ma_str = "/".join(map(str, ma_liste_bis))
print(ma_str)

# Conversion d'un tuple en str
mon_tuple = ("test", "coucou", "hello !", 3.1561516, 56)
ma_str = "/".join(map(str, mon_tuple))
print(ma_str)

# Conversion d'un ensemble en str (affichage dans le désordre)
mon_ensemble = {"test", "coucou", "hello !", 3.1561516, 56}
ma_str = "/".join(map(str, mon_ensemble))
print(ma_str)
