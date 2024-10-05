class Livre:
    def __init__(self, titre, auteur, achetable):
        self.titre = titre
        self.auteur = auteur
        self.achetable = achetable

    def afficher_infos(self):
        print(f"Titre : {self.titre}")
        print(f"Auteur : {self.auteur}")
        print(f"Achetable : {self.achetable}")


class LivrePapier(Livre):
    def __init__(self, titre, auteur, achetable, etat="moyen"):
        super().__init__(titre, auteur, achetable)
        self.etat = etat

    def afficher_infos(self):
        super().afficher_infos()
        print(f"Etat : {self.etat}")


class LivreNumerique(Livre):
    def __init__(self, titre, auteur, achetable, format):
        super().__init__(titre, auteur, achetable)
        self.format = format

    def afficher_infos(self):
        super().afficher_infos()
        print(f"Format : {self.format}")


# Création d'une liste de livres
livres = [
    LivrePapier("Le Seigneur des anneaux", "J.R.R. Tolkien", True, "neuf"),
    LivrePapier("Harry Potter et la pierre philosophale", "J.K. Rowling", True, "moyen"),
    LivreNumerique("Voyages a Antares", "A. Wolff", True, "PDF"),
    LivreNumerique("La Peste", "A. Camus", True, "Kindle"),
]

# Affichage des informations des livres
for livre in livres:
    livre.afficher_infos()
