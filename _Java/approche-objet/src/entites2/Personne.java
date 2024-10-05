package entites2;

import entites.AdressePostale;

public class Personne {
    public String nom;
    public String prénom;
    public AdressePostale adresse;

    public Personne(String nvNom, String nvPrénom) {
        nom = nvNom;
        prénom = nvPrénom;
    }  // a 2 paramètres
    // TP 2
    public Personne(String nvNom, String nvPrénom, AdressePostale adresse) {
        nom = nvNom;
        prénom = nvPrénom;
        this.adresse = adresse;
    }
    // TP 3
    public void afficherIdentite() {
        System.out.println(nom.toUpperCase() + " " + prénom);
    }
    public void changerNom(String nvNom){
        this.nom = nvNom;
        System.out.println(nom);
    }
    public void changerPrenom(String nvPrenom){
        this.prénom = nvPrenom;
        System.out.println(prénom);
    }
    public void changerAdresse(AdressePostale adresse) {
        this.adresse = adresse;
        System.out.println(adresse);
    }
    public String retourNom() {
        return nom;
    }
    public String retourPrénom(){
        return prénom;
    }
    public AdressePostale retourAdresse(){
        return adresse;
    }
}
