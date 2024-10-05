class Theatre:

    def __init__(self, nom, capaciter_max):
        self.nom = nom
        self.capaciter_max = capaciter_max
        self.inscrits_totale = 0
        self.recette_totale = 0

    def inscrire(self, nb_clients, prix_place):
        if self.inscrits_totale + nb_clients <= self.capaciter_max:
            self.inscrits_totale += nb_clients
            self.recette_totale += nb_clients * prix_place
        else:
            print("Attention, capacité maximale atteinte")


# Mise en Oeuvre:
theatre = Theatre("Opéra Comédie", 1200)

# Appel de la méthode inscrire jusqu'à capacité maximale
theatre.inscrire(500, 1)
theatre.inscrire(500, 2)
theatre.inscrire(199, 3)
theatre.inscrire(2, 25000000)
print("Situation actuel :", theatre.inscrits_totale)



# Affichage du total de clients inscrits
print(f"Total de clients inscrits : {theatre.inscrits_totale}")

# Affichage de la recette totale de l'établissement
print(f"Recette totale de l'établissement : {theatre.recette_totale}")


