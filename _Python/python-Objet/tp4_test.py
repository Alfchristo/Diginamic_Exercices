# Importer le module
import tp4_methode_static

# Tester si une chaine est un palindrome
chaine = "kayak"
print(tp4_methode_static.ChaineUtils.est_anagramme(chaine))

# Compter le nombre de fois où une sous-chaine est présente dans une chaine
chaine = "bonjour, comment allez-vous ?"
sous_chaine = "allez"
print(tp4_methode_static.ChaineUtils.comptage_chaine(chaine, sous_chaine))
