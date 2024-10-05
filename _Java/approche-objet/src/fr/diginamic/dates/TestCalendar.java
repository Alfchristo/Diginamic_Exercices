package fr.diginamic.dates;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Locale;

public class TestCalendar {
    public static void main(String[] args) {
        // Créez une instance de Calendar à la date du 19/05/2016 à 23h59 et 30 secondes
        Calendar calendar2016 = Calendar.getInstance();
        calendar2016.set(2016, Calendar.MAY, 19, 23, 59, 30);

        // Formatez la date au format jour/mois/année
        SimpleDateFormat formatDate = new SimpleDateFormat("dd/MM/yyyy");
        String dateFormatee = formatDate.format(calendar2016.getTime());

        // Affiche la date formatée
        System.out.println("La date de 2016 en question est: : " + dateFormatee);

        // Instance de Calendar à la date du jour
        Calendar calendarAujourdhui = Calendar.getInstance();
        // Date au format année/mois/jour heure:minute:seconde
        SimpleDateFormat formatDateHeure = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
        String dateFormateeHeure = formatDateHeure.format(calendarAujourdhui.getTime());

        // Affiche la date formatée
        System.out.println("La date du jour est : " + dateFormateeHeure);

        // Affichez la même instance avec le nom des jours et des mois en français, russe, chinois et allemand
        DateFormat[] formats = {
                new SimpleDateFormat("EEEE yyyy/MM/dd HH:mm:ss", Locale.FRENCH),
                new SimpleDateFormat("EEEE yyyy/MM/dd HH:mm:ss", new Locale("ru", "RU")),
                new SimpleDateFormat("EEEE yyyy/MM/dd HH:mm:ss", Locale.CHINESE),
                new SimpleDateFormat("EEEE yyyy/MM/dd HH:mm:ss", Locale.GERMAN),
        };

        for (DateFormat format : formats) {
            System.out.println(format.format(calendarAujourdhui.getTime()));
        }
    }
}
