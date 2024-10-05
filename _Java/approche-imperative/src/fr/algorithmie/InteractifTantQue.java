package fr.algorithmie;

import java.util.Scanner;
public class InteractifTantQue {
    public static void main(String[] args) {
        int nombre = 3;
        Scanner scanner = new Scanner(System.in);
        while ( nombre < 1 || nombre > 10){
            System.out.println("entrer un nombre entre 1 et 10");
            nombre = scanner.nextInt();
            System.out.println(nombre);
        }
        System.out.println(nombre);
    }
}
