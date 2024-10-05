class Personne:

    def __init__(self, nom, prenom, adresse):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse

    def __str__(self):
        return f"{self.nom} {self.prenom} {self.adresse}"



class PersonneException(Exception):
    def __init__(self, message):
        super().__init__(message)

class PersonneService:

    def valider(self, personne):
        if not personne.nom:
            raise PersonneException("Le nom est obligatoire")
        if len(personne.nom.strip()) < 2:
            raise PersonneException("Le nom doit contenir au moins 2 caractères")
        if not personne.prenom:
            raise PersonneException("Le prenom est obligatoire")
        if len(personne.prenom.strip()) < 2:
            raise PersonneException("Le prenom doit contenir au moins 2 caractères")
        if not personne.adresse:
            raise PersonneException("L'adresse est obligatoire")

# Instanciation de personnes avec des erreurs
erreur_nom = Personne("", "Marcel", "42")
erreur_prenom = Personne("", "Marcel", "42")
erreur_prenom_court = Personne("D", "Marce", "42")
erreur_adresse = Personne("Dupont", "Marcel", "")

# Instanciation de personnes sans erreurs
correct_personne = Personne("Dupont", "Marcel", "42")

personne = PersonneService()
try:
    personne.valider(erreur_nom)
except PersonneException as e:
    print(e)
try:
    personne.valider(erreur_prenom)
except PersonneException as e:
    print(e)
try:
    personne.valider(erreur_prenom_court)
except PersonneException as e:
    print(e)
try:
    personne.valider(erreur_adresse)
except PersonneException as e:
    print(e)
try:
    personne.valider(correct_personne)
except PersonneException as e:
    print(e)
else:
    print("Tout s'est bien déroulé")
