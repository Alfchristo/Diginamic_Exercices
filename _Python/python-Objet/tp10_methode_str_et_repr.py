class Personne:

    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def __str__(self):
        return f"{self.nom} {self.prenom} {self.age}"

    def __repr__(self):
        return f"Personne({self.nom}, {self.prenom}, {self.age})"


# Instanciation d'une personne
personne = Personne("Dupont", "Marcel", 42)

# Affichage de la personne
print(personne)

# Instanciation d'une liste de personnes
personnes = [
    Personne("Dupont", "Marcel", 42),
    Personne("Martin", "Pierre", 41),
]

# Affichage de la liste
print(personnes)
# Sortie : [Personne('Marcel', 'Dupont', 42), Person('Pierre', 'Martin', 41)]
