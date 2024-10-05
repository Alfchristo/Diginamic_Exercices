package fr.algorithmie;

public class SommeDeTableaux {
    public static void main(String[] args) {
        int[] tableaux1 = {1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4};
        int[] tableaux2 = {-1, 12, 17, 14, 5, -9, 0, 18, -6, 0, 4, -13, 5, 7, -2, 8, -1};
        int[] sommeTableaux = new int[tableaux1.length];
        for (int i = 0; i < tableaux1.length; i++) {
            sommeTableaux[i] = tableaux1[i] + tableaux2[i];
            System.out.println(sommeTableaux[i]);
        }
        System.out.println("Somme des 2 tableaux:");
        for (int i = 0; i < sommeTableaux.length; i++) {
            System.out.println(sommeTableaux[i]);
        }
    }
}