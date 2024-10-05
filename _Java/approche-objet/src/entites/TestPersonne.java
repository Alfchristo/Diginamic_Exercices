package entites;

import entites2.Personne;

public class TestPersonne {
    /* public static void main(String[] args) {
        AdressePostale adr = new AdressePostale();
        adr.numRue = 123;
        adr.libelleRue = "Rue de LeTest";
        adr.codePostal = 12345;
        adr.ville = "Aix-Test";

        Personne pers1 = new Personne();
        pers1.nom = "Dupont";
        pers1.prénom = "Patrick";

        Personne pers2 = new Personne();
        pers2.nom = "DuJardin";
        pers2.prénom = "Mathilde";
    }*/ //Méthode TP 1

        public static void main (String[]args){
            Personne pers2 = new Personne("Dupont", "Patrick");
            AdressePostale adr1 = new AdressePostale(123, "Rue de LeTest", 12345, "Aix-Test");
            Personne pers1 = new Personne("Dupont", "Patrick", adr1); // TP 2

            pers1.afficherIdentite(); // TP 3
            pers2.afficherIdentite();
            pers2.changerAdresse(new AdressePostale(321, "Nouvelle Test", 54321, "Test-Aix"));
            pers2.toString();
    }
}