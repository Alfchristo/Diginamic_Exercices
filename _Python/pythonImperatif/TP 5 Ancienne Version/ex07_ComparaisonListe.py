liste1 = [1, 15, -3, 8, 7, 4, -2, 28, -1, 17, 2, 3, 0, 14, -4]
liste2 = [3, -8, 17, 5, -1, 4, 0, 6, 2, 11, -5, -4, 8]

#Comparaison des valeurs de la liste
comparateur = 0
for i in liste1:
    for j in liste2:
        if i == j:
            comparateur += 1
print("Nombre de valeurs similaire :", comparateur)
