class Livre:
    def __init__(self, titre, auteur):
        self._titre = titre
        self._auteur = auteur
        self._achetable = False

    @property
    def titre(self):
        return self._titre

    @titre.setter
    def titre(self, titre):
        self._titre = titre

    @property
    def auteur(self):
        return self._auteur

    @auteur.setter
    def auteur(self, auteur):
        self._auteur = auteur

    @property
    def achetable(self):
        return self._achetable

    @achetable.setter
    def achetable(self, achetable):
        self._achetable = achetable


# Instance de livre
livre = Livre("Le Seigneur des anneaux", "J.R.R. Tolkien")

# Modification des informations du livre
livre.titre = "Harry Potter"
livre.auteur = "J.K Rowling"
livre.achetable = True

# Affichage des informations du livre
print(f"Titre : {livre.titre}")
print(f"Auteur : {livre.auteur}")
print(f"Achetable : {livre.achetable}")
