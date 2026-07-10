import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class BatchProcessing {
    public static void main(String[] args) {
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             Statement stmt = conn.createStatement()) {
            conn.setAutoCommit(false);
            stmt.addBatch("INSERT INTO student (id, name) VALUES (5, 'Ina')");
            stmt.addBatch("INSERT INTO student (id, name) VALUES (6, 'Neil')");
            stmt.executeBatch();
            conn.commit();
            System.out.println("Batch executed.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
