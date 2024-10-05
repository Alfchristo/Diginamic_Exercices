package entites;

public class TestAdressePostale {
    public static void main(String[] args) {
       /* AdressePostale adr1 = new AdressePostale();
        adr1.numRue = 123;
        adr1.libelleRue = "Rue de LeTest";
        adr1.codePostal = 12345;
        adr1.ville = "Aix-Test";

        AdressePostale adr2 = new AdressePostale();
        adr2.numRue = 345;
        adr2.libelleRue = "Rue de LeTest";
        adr2.codePostal = 12345;
        adr2.ville = "Aix-Test"; */ // Méthode TP 1

        AdressePostale adr1 = new AdressePostale(123, "Rue de LeTest", 12345, "Aix-Test");
        AdressePostale adr2 = new AdressePostale(345, "Rue de LeTest", 12345, "Aix-Test");
        }
    }

