package fr.algorithmie;

public class Rotation {
    private int[] tableau;
    public Rotation(int[] tableau) {
        this.tableau = tableau;
    }
    public void changeRotation(){
        int elementRotation = tableau[tableau.length - 1];
        for (int i = tableau.length-1; i>0; i--){
            tableau[i] = tableau[i -1];
        }
        tableau[0] = elementRotation;
    }
    public static void main(String[] args) {
        int[] tableau = {0,1,2,3};
        Rotation rot1 = new Rotation(tableau);
        rot1.changeRotation();
        System.out.println(rot1);
    }
}
