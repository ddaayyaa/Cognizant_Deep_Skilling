import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class DeleteEmployee {
    public static void main(String[] args) {
        String sql = "DELETE FROM employee WHERE id = ?";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, 101);
            stmt.executeUpdate();
            System.out.println("Employee deleted.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
