# Definition d'un programme permettant l'affichage de 10 chiffres suivants:
def interactifs_chiffres_suivants(nombre):
    for i in range(1, 11):
        print(nombre + i)

# Demande à l'utilisateur de choisir un nombre:
nombre = int(input("Veuillez entrer un nombre:"))
interactifs_chiffres_suivants(nombre)
