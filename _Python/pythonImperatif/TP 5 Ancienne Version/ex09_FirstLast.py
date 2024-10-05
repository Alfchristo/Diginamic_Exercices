# Notre fichier
tab1 = []
tab2 = [ 2 ]
tab3 = [ 1, 6 ]
tab4 = [ 1, 6, 1 ]

# On crée une fonction pour trier notre liste selon notre critere:
def first_last(tab):
    if len(tab) >= 1 and (tab[0] == tab[-1]):
        return True
    else:
        return False

print("Tab 1 Critère Rempli: ", first_last(tab1))
print("Tab 2 Critère Rempli: ", first_last(tab2))
print("Tab 3 Critère Rempli: ", first_last(tab3))
print("Tab 4 Critère Rempli: ", first_last(tab4))


