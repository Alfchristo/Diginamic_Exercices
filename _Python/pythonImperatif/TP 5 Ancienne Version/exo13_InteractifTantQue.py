#Demande à l'utilisateur de renseigner un nombre compris entre 1 et 10:
def interactif_tant_que(min, max):
    while True:
        nombre = int(input("Choisir un nombre entre {} et {} :".format(min, max)))
        if nombre >= min and nombre <= max:
            return nombre

# Je vais définir ici la valeur que l'utilisateur peut choisir
nombre = interactif_tant_que(1, 10)

# Affichage du nombre choisie:
print("Vous avez choisie:", nombre)

"""
                        Autre méthode trouver mais possible:
nombre = None
while nombre is None or not (nombre >= 1 and nombre <= 10):
    nombre = int(input("Entrez un nombre compris entre 1 et 10 : "))
"""
