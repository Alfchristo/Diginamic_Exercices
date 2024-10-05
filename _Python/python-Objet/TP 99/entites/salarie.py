class Salarie:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

    def __repr__(self):
        return f"Salarie(nom='{self.nom}', prenom='{self.prenom}', salaire={self.salaire})"
