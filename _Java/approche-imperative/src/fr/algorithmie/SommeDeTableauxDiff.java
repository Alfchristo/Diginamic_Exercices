package fr.algorithmie;

import java.util.Arrays;

public class SommeDeTableauxDiff {
    public static void main(String[] args) {
        int[] tableaux1 =  {1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4} ;
        int[] tableaux2 =  {-1, 12, 17, 14, 5, -9, 0, 18 } ;
        int[] sommeTableauxDiff = new int[Math.max(tableaux1.length, tableaux2.length)];
        System.out.println("Somme des 2 tableaux diff:");
        for (int i = 0; i < sommeTableauxDiff.length; i++){
            int num1 = (i < tableaux1.length) ? tableaux1[i] : 0;
            int num2 = (i < tableaux2.length) ? tableaux2[i] : 0;
            sommeTableauxDiff[i] = num1 + num2;
            System.out.println(Arrays.toString(sommeTableauxDiff));
        }
    }
}
