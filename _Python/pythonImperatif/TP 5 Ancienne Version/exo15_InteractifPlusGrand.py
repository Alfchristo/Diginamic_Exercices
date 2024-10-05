
# création d'une liste vide pour stocker les inputs de l'utilisateur
nombres_stocker = []

# On définit à 10 le nombre de valeurs qui peuvent etre ajouter
for i in range(10):
    nombre_choisie = int(input("Veuillez enter un nombre :"))
    nombres_stocker.append(nombre_choisie)

# Calcul de la plus grand valeur après etre renseigner:
plus_grand = max(nombres_stocker)
print("Plus grande valeur renseigner:", plus_grand)
