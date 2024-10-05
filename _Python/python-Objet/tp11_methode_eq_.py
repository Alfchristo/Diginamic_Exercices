class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def __str__(self):
        return f" {self.nom}, {self.prenom}, {self.age}"

    def __repr__(self):
        return f"Personne({self.nom}, {self.prenom}, {self.age})"

    def __eq__(self, other):
        if isinstance(other, Personne):
            return (
                self.nom == other.nom
                and self.prenom == other.prenom
                and self.age == other.age
            )
        return False


# Instanciation de deux personnes avec les mêmes valeurs d'attributs
personne1 = Personne("Dupont", "Marcel", 42)
personne2 = Personne("Dupont", "Marcel", 42)

# Test de l'égalité avec l'opérateur ==
print(personne1 == personne2)  # Devrait afficher False sans la méthode __eq__

# Redéfinition de la méthode __eq__
Personne.__eq__ = lambda self, other: (
        self.nom == other.nom
        and self.prenom == other.prenom
        and self.age == other.age
    )

# Test de l'égalité avec l'opérateur ==
print(personne1 == personne2)
# Sortie : True
