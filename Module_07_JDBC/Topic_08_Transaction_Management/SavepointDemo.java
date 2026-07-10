import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Savepoint;
import java.sql.Statement;

public class SavepointDemo {
    public static void main(String[] args) {
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             Statement stmt = conn.createStatement()) {
            conn.setAutoCommit(false);
            stmt.executeUpdate("INSERT INTO student (id, name) VALUES (7, 'John')");
            Savepoint savepoint = conn.setSavepoint();
            stmt.executeUpdate("INSERT INTO student (id, name) VALUES (8, 'Lisa')");
            conn.rollback(savepoint);
            conn.commit();
            System.out.println("Rolled back to savepoint and committed.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
