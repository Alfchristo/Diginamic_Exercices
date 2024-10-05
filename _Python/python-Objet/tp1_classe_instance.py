class Adresse_Postale:

    def __init__(self, num_rue, lib_rue, code_postal, ville):
        self.num_rue = num_rue
        self.lib_rue = lib_rue
        self.code_postal = code_postal
        self.ville = ville

adr1 = Adresse_Postale(num_rue=12, lib_rue="Rue de 1ere Adresse", code_postal=34070, ville="Montpellier")
adr2 = Adresse_Postale(num_rue=34, lib_rue="Rue de 2eme Adresse", code_postal=34000, ville="Montpellier")

class Personne:
    def __init__(self, nom, prenom, adresse):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse

personne1 = Personne(nom="Dupont", prenom="Jean", adresse=adr1)
personne2 = Personne(nom="Martin", prenom="Pierre", adresse=adr2)
