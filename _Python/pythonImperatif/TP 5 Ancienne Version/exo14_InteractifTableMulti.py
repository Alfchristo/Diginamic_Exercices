#Demande à l'utilisateur de renseigner un nombre pour faire une multiplication:
def interactif_table_multi(min, max):
    while True:
        nombre = int(input("Choix de nombre {} et {}:".format(min, max)))
        if nombre >= min and nombre <= max:
            return nombre

# Definition de notre intervalle de valeur:
nombre = interactif_table_multi(1, 10)

# Code pour faire la multiplication de la valeur renseigner:
for i in range(1, 11):
    print(f"{nombre} * {i} = {nombre * i}")

