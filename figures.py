"""
Les chiffres : les entiers (int) et les réels (float)

Pour connaître toutes les méthodes rattachées aux chiffres, il suffit d'exécuter l'instruction suivante :
-> pour les entiers : print(help(int))
-> pour les réels : print(help(float)

Éditeur : Laurent REYNAUD
Date : 02-09-2020
"""

x = 5
y = 3.1568591981

print(type(x))
print(type(y))

# Instructions ci-après pour une mise en format des chiffres :
# y est arrondi au centième et z est arrondi à l'unité
z = x / y
print("Le résultat de 'x/y' avec x =", x, 'et y =', round(y, 3), 'donne pour résultat ', round(z))
