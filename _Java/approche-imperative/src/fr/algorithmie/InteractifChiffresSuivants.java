package fr.algorithmie;

import java.util.Scanner;

public class InteractifChiffresSuivants {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int nombre;
        System.out.println("Entrez un nombre entre 1 et 10 ");
        nombre = scanner.nextInt();
        for (int i = 1; i <= 10; i++) {
            System.out.println(i + nombre);
        }
    }
}