package fr.algorithmie;

import java.util.Scanner;

public class InteractifPlusGrand {
    public static void main(String[] args) {
        int[] nombres = new int[10];
        int grandNombre = 0;
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < nombres.length; i++) {
            System.out.println("Entrez un nombre :");
            nombres[i] = scanner.nextInt();
            if(grandNombre < nombres[i]) {
                grandNombre = nombres[i];
            }
        }
        System.out.println(" le plus grand nombre entrée est  :" + grandNombre);
    }
    }
