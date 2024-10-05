class Personne:

    def __init__(self, nom, prenom, adresse):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse

    def __str__(self):
        return f"{self.nom} {self.prenom} {self.adresse}"

    def __lt__(self, tri_personnes):
        return self.nom < tri_personnes.nom

# Instanciation d'une liste de personnes
personnes = [
    Personne("Untel", "Alex", "Montpellier"),
    Personne("Anatole", "Jean", "Lyon"),
    Personne("Lyon", "Pierre", "Montpellier"),
]

# Tentative de tri de la liste
# personnes.sort()
# Erreur : TypeError: '<' not supported between instances of 'Personne' and 'Personne'

# Redefinition de la méthode __lt__



# Tri de la liste
personnes.sort()

# Affichage de la liste triée
for personne in personnes:
    print(personne)

# Redefinition de la méthode __lt__
def __lt__(self, tri_personnes):
    return self.prenom < tri_personnes.prenom

# Tri de la liste
personnes.sort()

# Affichage de la liste triée
for personne in personnes:
    print(personne)
