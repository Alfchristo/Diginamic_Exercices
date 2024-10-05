# Définition d'un programme calculant la somme de 10 chiffres suivants:
def interactifs_chiffres_suivants(nombre):
    somme = 0
    for i in range(1, nombre+1):
        somme += i
    return somme

# Demande à l'utilisateur de choisir un nombre:
nombre = int(input("Veuillez entrer un nombre:"))

# Affichage du nombre choisie:
print("Nombre choisie:", nombre)

# Resultat:
somme = interactifs_chiffres_suivants(nombre)
print("Votre résultat:", somme)
