# Exercice 1
for i in range(0, 11):
    if i % 2 ==0:
        print(i)

for i in range(0, 11):
    if i % 2 !=0:
        print(i)

# Exercice 2
liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]

# Affichage des valeurs dans la liste:
for i in range(len(liste)):
    print("Affichage de la liste :", liste[i])

# Affichage de valeurs positifs avec une autre méthode:
for listeValues in liste:
    if listeValues > 0:
        print("Valeurs positifs :", listeValues)

# Calculs du nombre de valeurs positifs dans la liste:
valeursPositifs = 0
for listeValues in liste:
    if listeValues > 0:
        valeursPositifs += 1
print("Compte de valeurs positifs:", valeursPositifs)



