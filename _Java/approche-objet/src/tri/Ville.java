package tri;

import java.util.ArrayList;
import java.util.Collections;

public class Ville implements Comparable<Ville> {
    private String nom;
    private int nbHabitants;
    public Ville(String nom, int nbHabitants)
    {
        this.nom = nom;
        this.nbHabitants = nbHabitants;
    }
    public String getNom()
    {
        return nom;
    }

    public void setNom(String nom)
    {
        this.nom = nom;
    }
    public int getNbHabitants()
    {
        return nbHabitants;
    }
    public void setNbHabitants(int nbHabitants)
    {
        this.nbHabitants = nbHabitants;
    }
    @Override
    public int compareTo(Ville ville) {
        return this.nom.compareTo(String.valueOf(ville.nbHabitants));
    }
    @Override
    public String toString() {
        return "Ville{" +
                "nom='" + nom + '\'' +
                ", nbHabitants=" + nbHabitants +
                '}';
    }
    public static void main(String[] args) {
        // Créez une liste de villes
        ArrayList<Ville> villes = new ArrayList<>();
        villes.add(new Ville("Nice", 343_000));
        villes.add(new Ville("Carcassonne", 47_800));
        villes.add(new Ville("Narbonne", 53_400));
        villes.add(new Ville("Lyon", 484_000));
        villes.add(new Ville("Foix", 9_700));
        villes.add(new Ville("Pau", 77_200));
        villes.add(new Ville("Marseille", 850_700));
        villes.add(new Ville("Tarbes", 40_600));

        // Triez la liste
        Collections.sort(villes);

        // Affichez le résultat
        System.out.println("La liste triée est : ");
        for (Ville ville : villes) {
            System.out.println(ville);
        }
    }
}