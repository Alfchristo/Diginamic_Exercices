from abc import abstractmethod

from tp6_redefinition_methode import LivrePapier, LivreNumerique


class Sortie:

    def __init__(self, date, livre):
        self.date = date
        self.livre = livre

    @abstractmethod
    def get_montant(self):
        pass


class Emprunt(Sortie):

    def __init__(self, date, livre, duree):
        super().__init__(date, livre)
        self.duree = duree

    def get_montant(self):
        if isinstance(self.livre, LivrePapier):
            return self.duree * 0.5
        else:
            return self.duree * 0.25


class Achat(Sortie):

    def __init__(self, date, livre, montant):
        super().__init__(date, livre)
        self.montant = montant

    def get_montant(self):
        return self.montant


# Création d'une liste de sorties
sorties = [
    Achat("2023-07-20", LivrePapier("Le Seigneur des anneaux", "J.R.R. Tolkien", True, "neuf"), 20),
    Achat("2023-07-21", LivreNumerique("Les Fleurs du mal", "Charles Baudelaire", True, "EPUB"), 10),
    Emprunt("2023-07-22", LivrePapier("Harry Potter et la pierre philosophale", "J.K. Rowling", True, "moyen"), 5),
    Emprunt("2023-07-23", LivreNumerique("Le Petit Prince", "Antoine de Saint-Exupéry", True, "Kindle"), 3),
]


# Fonction retournant le montant global pour une liste de sorties
def get_montant_global(sorties):
    montant_global = 0
    for sortie in sorties:
        montant_global += sortie.get_montant()
    return montant_global


# Fonction retournant un dictionnaire avec en clé : le type de sortie (achat ou emprunt) et en valeur le montant total des sorties de ce type.

