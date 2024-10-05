package listes;

import java.util.ArrayList;
import java.util.Iterator;

public class TestVille {
    public static void main(String[] args) {
        ArrayList<Ville> villes = new ArrayList<>();
        villes.add(new Ville("Nice", 340000));
        villes.add(new Ville("Lyon", 484000));
        villes.add(new Ville("Narbonne", 53400));
        villes.add(new Ville("Lyon", 484000));
        villes.add(new Ville("Foix", 9700));
        villes.add(new Ville("Pau", 77200));
        villes.add(new Ville("Marseille", 850700));
        villes.add(new Ville("Tarbes", 40600));

        // Recherche de ville la plus peuplée
        Iterator<Ville> iterPlus = villes.iterator();
        Ville plusPeuplee = iterPlus.next();
        while (iterPlus.hasNext()) {
            Ville villesIter = iterPlus.next();
            if (villesIter.getNbHabitants() > plusPeuplee.getNbHabitants()) {
                plusPeuplee = villesIter;
            }
        }
        System.out.println("Ville la plus peuplée:" + plusPeuplee);

        // Suppression de ville la moins peuplée
        Iterator<Ville> iterMoins = villes.iterator();
        Ville moinsPeuplee = iterMoins.next();
        while (iterMoins.hasNext()) {
            Ville villesIter = iterMoins.next();
            if (villesIter.getNbHabitants() < moinsPeuplee.getNbHabitants()) {
                moinsPeuplee = villesIter;
            }
        }
        villes.remove(moinsPeuplee);
        System.out.println("nombre de villes restantes: " + villes.size());// 7 villes

        // Modification de villes avec pop sup. à 100k en MAJ
        for (Ville ville : villes) {
            if (ville.getNbHabitants() > 100000) {
                ville.setNom(ville.getNom().toUpperCase());
            }
        }
        //Affichage résultat:
        System.out.println(villes);
    }
}