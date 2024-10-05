liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]

# Calcul de la moyennne:
somme = 0
for x in liste:
    somme += x
moyenne = somme / len(liste)
print("Moyenne de la liste:", moyenne)

# Calcul de la moyenne des valeurs positives de la liste:
somme_des_positive = 0
for x_positive in liste:
    if x_positive > 0:
        somme_des_positive += x_positive
moyenne = somme_des_positive / len(liste)
print("Moyenne des valeurs positifs :", moyenne)
