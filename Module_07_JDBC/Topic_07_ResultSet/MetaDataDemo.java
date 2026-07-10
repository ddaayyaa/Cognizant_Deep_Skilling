import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.SQLException;

public class MetaDataDemo {
    public static void main(String[] args) {
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password")) {
            DatabaseMetaData meta = conn.getMetaData();
            System.out.println("Database product name: " + meta.getDatabaseProductName());
            System.out.println("Driver name: " + meta.getDriverName());
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
