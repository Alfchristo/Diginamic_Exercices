package fr.diginamic.chaines;

public class TestStringBuilder {

    public static void main(String[] args) {

        // Methode StringBuilder
        long debut = System.currentTimeMillis();   // Début chrono
        // Ajoutez tous les nombres de 1 à 100 000
        StringBuilder builder = new StringBuilder();
        for (int i = 1; i <= 100000; i++) {
            builder.append(i);
        }
        long fin = System.currentTimeMillis();   // Fin chrono
        // Affiche le temps en millisecondes
        System.out.println("Le temps mis est de " + (fin - debut) + " millisecondes");  // 8ms

        // Methode Concat
        long debut2 = System.currentTimeMillis();
        String chaine = "";
        for (int i = 1; i <= 100000; i++) {
            chaine = chaine+i;
        }
        long fin2 = System.currentTimeMillis();
        System.out.println("Le temps mis est de " + (fin2 - debut2) + " millisecondes");  //2378ms
    }
}
