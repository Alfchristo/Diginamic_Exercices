chaine = "Durand;Marcel;2 523.5"

# Tache 1:
premier_caractere = chaine[0]
print("Premier caractère: ", premier_caractere)

# Tache 2:
print("Longuer chaine de caractère :", len(chaine))

#Tache 3:
print("Index du premier element :", chaine.index("Durand"))

#Tache 4:
nom_famille = chaine[0:chaine.index(";")]
print("Nom de famille: ", nom_famille)

#Tache 5:
print("Nom de famille en majuscule :", nom_famille.upper())

#Tache 6:
print("Nom de famille en minuscle :", nom_famille.lower())

#Tache 7:
print("Chaine en morceaux :", chaine.split(";"))

#Tache 9:
from entites.salarie import Salarie
salaire = Salarie(nom_famille, "Marcel", "2523.5")
print(salaire)

