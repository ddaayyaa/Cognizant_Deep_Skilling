import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class PreparedUpdate {
    public static void main(String[] args) {
        String sql = "UPDATE student SET name = ? WHERE id = ?";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, "Neha Sharma");
            pstmt.setInt(2, 2);
            pstmt.executeUpdate();
            System.out.println("Prepared update completed.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
