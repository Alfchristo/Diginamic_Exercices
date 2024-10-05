class AdressePostale:
    def __init__(self, numero_rue, libelle_rue, code_postal, ville):
        self.numero_rue = numero_rue
        self.libelle_rue = libelle_rue
        self.code_postal = code_postal
        self.ville = ville

    def __str__(self):
        return f"AdressePostale(numero_rue={self.numero_rue}, libelle_rue='{self.libelle_rue}', code_postal={self.code_postal}, ville='{self.ville}')"

class Personne:
    def __init__(self, nom, prenom, adresse = None):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse

    def affichage_majuscule(self):
        print("Je m'appelle " + self.nom.upper() + " " + self.prenom.upper())

    def modifier_nom(self, nouveau_nom: str):
        self.nom = nouveau_nom

    def modifier_prenom(self, nouveau_prenom: str):
        self.prenom = nouveau_prenom

    def modifier_adresse(self, nouvelle_adresse):
        self.adresse = nouvelle_adresse

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_adresse(self):
        return self.adresse

    def afficher_attributs(self):
        print(f"Nom : {self.nom}, Prénom : {self.prenom}, Adresse : {self.adresse}")

ut1 = Personne("Jeff", "Condolla")

identite = ut1.affichage_majuscule()
print(identite)
