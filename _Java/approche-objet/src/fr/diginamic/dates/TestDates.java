package fr.diginamic.dates;

import java.text.SimpleDateFormat;
import java.util.Date;

public class TestDates {
    public static void main(String[] args) {

        // Instance date du jour
        Date auj = new Date(123, 10, 22);
        SimpleDateFormat formatAuj = new SimpleDateFormat("dd/MM/yyyy");
        String aujFormatee = formatAuj.format(auj);
        System.out.println("La date du jour: " + aujFormatee);

        // Instance date du 19/05/2016
        Date date2016 = new Date(116, 06, 19, 23, 59,30);
        SimpleDateFormat formatD2016 = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
        String date2016Formatee = formatD2016.format(date2016);
        System.out.println("La date cible en 2016: " + date2016Formatee);

        // Instance Date/Heure du systeme
        Date dateSysteme = new Date();
        String dateSystemeFormatee = formatD2016.format(dateSysteme);
        System.out.println("La Date/Heure système est : " + dateSystemeFormatee);

    }
}
