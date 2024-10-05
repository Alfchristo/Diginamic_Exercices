package fr.diginamic.banque.entites;

public class TauxCompte extends Compte {
    private double tauxRem;
    public TauxCompte(int numCompte, double soldeCompte, double tauxRem) {
        super(numCompte, soldeCompte);
        this.tauxRem = tauxRem;
    }
    public double getTauxRem() {
        return tauxRem;
    }
    public void setTauxRem(double tauxRem) {
        this.tauxRem = tauxRem;
    }
    @Override
    public String toString() {
        return super.toString() + " " + "et votre taux de rémunération est" + " " + tauxRem + "%";
    }
} // TP 7
