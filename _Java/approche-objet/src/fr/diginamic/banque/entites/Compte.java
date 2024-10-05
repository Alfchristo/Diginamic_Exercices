package fr.diginamic.banque.entites;

public class Compte {
    private int numCompte;
    private double soldeCompte;

    public Compte(int nvNumCompte, double nvSoldeCompte){
        this.numCompte = nvNumCompte;
        this.soldeCompte = nvSoldeCompte;
    }
    public int getNumCompte() {
        return numCompte;
    }
    public void setNumCompte(int numCompte) {
        this.numCompte = numCompte;
    }
    public double getSoldeCompte() {
        return soldeCompte;
    }
    public void setSoldeCompte(double soldeCompte) {
        this.soldeCompte = soldeCompte;
    }
    @Override
    public String toString(){
        return "Numero de Compte:"+ " " + this.numCompte +
                ",Votre Solde" + " " + this.soldeCompte;
    } // TP 6
}
