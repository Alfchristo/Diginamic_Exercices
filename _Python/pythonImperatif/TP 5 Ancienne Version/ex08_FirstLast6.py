# Notre fichier
tab1 = []
tab2 = [2]
tab3 = [6]
tab4 = [1, 6]
tab5 = [6, 1]
tab6 = [0, 6, 1, 2]

# On crée une fonction pour trier notre liste selon notre critere:
def first_last_6(tab):
    if len(tab) >= 1 and (tab[0] == 6 or tab[-1] == 6):
        return True
    else:
        return False

print("Tab 1 Critère Rempli: ", first_last_6(tab1))
print("Tab 2 Critère Rempli: ", first_last_6(tab2))
print("Tab 3 Critère Rempli: ", first_last_6(tab3))
print("Tab 4 Critère Rempli: ", first_last_6(tab4))
print("Tab 5 Critère Rempli: ", first_last_6(tab5))
print("Tab 6 Critère Rempli: ", first_last_6(tab6))


