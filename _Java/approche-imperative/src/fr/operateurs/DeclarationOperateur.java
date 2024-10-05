package fr.operateurs;
import javax.swing.plaf.basic.BasicInternalFrameTitlePane;

public class DeclarationOperateur {public static void main(String[] args) {
    int a = 10;
    int b = 20;
    boolean testET = a>10 && b<10;
    System.out.println(testET);
    boolean testOu = a>10 || b<10;
    System.out.println(testOu);
    a=a+1;
    System.out.println(a);
    a++;
    System.out.println(a);
    a+=1;
    System.out.println(a);
    String c = a>0 ? "a est plus grand que 0" : "a est inférieur à 0";
    System.out.println(c);
}
}
