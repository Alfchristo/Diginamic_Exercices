class Personne:

    def __init__(self, nom, prenom, adresse):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse

    def __str__(self):
        return f"{self.nom} {self.prenom} {self.adresse}"


# Instanciation de deux personnes avec les mêmes valeurs d'attributs
personne1 = Personne("Untel", "Alex", "Montpellier")
personne2 = Personne("Untel", "Alex", "Montpellier")

# Mise en place dans un set
set_personnes = {personne1, personne2}
print("résultat méthode set :", set_personnes)

# Redefinition de la méthode __hash__
def __hash__(self):
    return hash((self.nom, self.prenom, self.adresse))

print("Résultat après redéfinition méthode __hash__ :")
# Affichage du contenu du set avec une boucle
for personne in set_personnes:
    print(personne)
