package org.CA;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.ResourceBundle;

public class TestConnexionJdbc {
    private static final String DB_URL;
    private static final String DB_USER;
    private static final String DB_PWD;

    static {
        System.out.println("Bloc static");
        ResourceBundle bundle = ResourceBundle.getBundle(
                "database");
        DB_URL= bundle.getString("db.url");
        DB_USER = bundle.getString( "db.user");
        DB_PWD = bundle.getString ("db.password");
    }
    {
        System.out.println("hello bloc");}

    public static void main(String[] args) {
        try (Connection cnx = DriverManager.getConnection(DB_URL, DB_USER, DB_PWD)){
            System.out.println("réussi :" + cnx);
        } catch (SQLException e){
            System.out.println("Attention :" + e.getMessage());
        }}
}
