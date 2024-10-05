class ChaineUtils:

    @staticmethod
    def est_anagramme(chaine1, chaine2):
        chaine1_triee = sorted(chaine1)
        chaine2_triee = sorted(chaine2)
        return chaine1_triee == chaine2_triee

    @staticmethod
    def comptage_chaine(chaine, sous_chaine):
        compteur = 0
        for i in range(len(chaine)):
            position = chaine.find(sous_chaine, i)
            if position != -1:
                compteur += 1
                i = position + len(sous_chaine)
        return compteur
