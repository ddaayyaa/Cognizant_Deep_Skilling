import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ConnectionDemo {
    public static void main(String[] args) {
        try (Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password")) {
            System.out.println("Connected successfully.");
        } catch (SQLException ex) {
            System.out.println("Connection failed: " + ex.getMessage());
        }
    }
}
