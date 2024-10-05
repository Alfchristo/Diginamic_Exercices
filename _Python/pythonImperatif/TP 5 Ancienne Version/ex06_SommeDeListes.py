liste1 = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
liste2 = [-1, 12, 17, 14, 5, -9, 0, 18, -6, 0, 4, -13, 5, 7, -2, 8, -1]

# Calcul de somme de listes
resultat = []
for i in range(len(liste1)):
    resultat.append(liste1[i] + liste2[i])
print(resultat)
