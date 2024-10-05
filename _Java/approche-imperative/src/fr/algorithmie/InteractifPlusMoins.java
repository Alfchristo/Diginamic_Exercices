package fr.algorithmie;

import java.util.Scanner;

public class InteractifPlusMoins {
    public static void main(String[] args) {
        int nombreRand = (int) (Math.random()*100);
        boolean trouve =true;
        Scanner scanner = new Scanner(System.in);
        int nb;
        int nbEssai = 0;
        System.out.println("trouvez le bon chiffre entre 1 et 100");
        System.out.println("entrez un nombre:");
        do {
            nb = scanner.nextInt();
            nbEssai++;
            if(nb == nombreRand) {
                trouve = false;
                System.out.println("Correct");
            }
            else if(nb> nombreRand) {
                System.out.println("c'est moins");
            }
            else if(nb < nombreRand) {
                System.out.println("C'est plus");
            }
            System.out.println("Bravo!, il vous a pris" + nbEssai + "tentative");
        } while (trouve);
    }
}
