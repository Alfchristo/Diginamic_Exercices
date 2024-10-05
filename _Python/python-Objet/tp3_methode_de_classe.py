class Zoo:

    # Attributs de classe

    liste_animaux = []
    nombre_animaux = 0

    # Méthode de classe ajouter_animaux

    @classmethod
    def ajouter_animaux(cls, espece, nombre):
        # Si l'espèce n'existe pas dans la liste
        if espece not in cls.liste_animaux:
            # Ajoute l'animal à la liste des animaux du zoo
            cls.liste_animaux.append(espece)
        # Augmente le nombre d'animaux du zoo du nombre indiqué
        cls.nombre_animaux += nombre

    # Méthode de classe afficher_animaux

    @classmethod
    def afficher_animaux(cls):
        # Affiche toutes les espèces du Zoo
        print("Les espèces du zoo sont :")
        for espece in cls.liste_animaux:
            print(espece)
        # Affiche le nombre total d'animaux dans le Zoo
        print(f"Le nombre total d'animaux dans le zoo est de {cls.nombre_animaux}")
