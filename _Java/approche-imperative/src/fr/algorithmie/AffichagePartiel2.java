package fr.algorithmie;

public class AffichagePartiel {
    public static void main(String[] args) {
        int[] array = {1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4};
        System.out.println("Affichage Nb sup à 3");
        for (int i = 0; i < array.length; ++i) {
            if (array[i] > 3) {
                System.out.println(array[i]);
            }
        }
        System.out.println("Affichage Nb pair:");
        for (int i = 0; i < array.length; ++i) {
            if (array[i] % 2 == 0) {
                System.out.println(array[i]);
            }
        }
        System.out.println("Affichage index pair:");
        for (int i =0; i < array.length; ++i) {
            if (i % 2 ==0) {
                System.out.println(array[i]);
            }
        }
        System.out.println("Affichage Nb impair:");
        for (int i = 0; i < array.length; ++i){
            if (array[i] % 2 != 0){
                System.out.println(array[i]);
            }
        }
    }
}