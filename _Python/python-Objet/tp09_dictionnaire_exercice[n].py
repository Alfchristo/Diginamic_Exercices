# Exercice 1:
print("Exercice 1:")
dicoVilles = {13: "Marseille", 34: "Montpellier", 44: "Nantes", 75: "Paris", 31: "Toulouse"}

# Boucle pour afficher l'ensemble des clés contenues dans le dictionnaire
print("Clés contenues dans dictionnaire :")
for dicoVilles_key in dicoVilles.keys():
    print(dicoVilles_key)

# Boucle pour afficher l'ensemble des valeurs contenues dans le dictionnaire
print("Valeurs contenues dans dictionnaire :")
for dicoVilles_value in dicoVilles.values():
    print(dicoVilles_value)

# Boucle pour afficher la taille du dictionnaire
print("Taille du dictionnaire:", len(dicoVilles))

# Exercice 2:
print("Exercice 2:")
# Définition d'une liste à tester
liste_keys = ("Coucou", "Hi")


# Fonction pour convertir liste à dictionnaire en incluant les clés à partir de la longuer des chaines characteres
def parametre_liste_keys(liste_keys):
    dict = {}
    for key in liste_keys:
        dict[key] = len(key)
    return dict


# Execution de la fonction et affichage de résultat
dict = parametre_liste_keys(liste_keys)
print("Nouvelle clés du dictionnaire :", dict)

# Exercice 3:
print("Exercice 3:")
liste_keys = ("Ananas", "Banane", "Orange", "Ananas", "Banane")


def parametre_liste_keys_count(liste_keys):
    dict = {}
    for key in liste_keys:
        dict[key] = liste_keys.count(key)
    return dict


dict = parametre_liste_keys_count(liste_keys)
print("Nombre d'occurence dans le dictionnaire :", dict)


# Exercice 4:
print("Exercice 4:")
class Salarier:
    # Constructeur de la classe Salarié
    def __init__(self, nom, matricule, service):
        self.nom = nom
        self.matricule = matricule
        self.service = service

    # Représentation chaine charactère:
    def __repr__(self):
        return f"{self.nom} ({self.matricule}) ({self.service})"

# Création d'une liste de Salariés
liste_salarie = [Salarier("Antoine Dupont", 127, "DSI/JAVA"),
            Salarier("Berthe Casa", 238, "DSI/PHP"),
            Salarier('Fatima Ouassa', 478, "DSI/JAVA"),
            Salarier("Cassian Andor", 156, "DSI/PYTHON"),
            Salarier("Lee Wu", 559, "DSI/PHP"),
            Salarier("Hassan Missen", 96, "DSI/PYTHON"),
            Salarier("Aurélien PIC", 889, "DSI/JAVA")]

# Défintion de dictionnaire
dict_salarie = {}
for salarier in liste_salarie:
    service = salarier.service
    if service not in dict_salarie:
        dict_salarie[service] = 0
    dict_salarie[service] += 1

print("Nombres de salarié par service: ", dict_salarie)


