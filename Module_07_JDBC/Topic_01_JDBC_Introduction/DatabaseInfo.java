import java.sql.DatabaseMetaData;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseInfo {
    public static void main(String[] args) {
        try (Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password")) {
            DatabaseMetaData meta = connection.getMetaData();
            System.out.println("Database product: " + meta.getDatabaseProductName());
            System.out.println("Driver version: " + meta.getDriverVersion());
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
