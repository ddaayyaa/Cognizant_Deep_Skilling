import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class PreparedInsert {
    public static void main(String[] args) {
        String sql = "INSERT INTO student (id, name) VALUES (?, ?)";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, 2);
            pstmt.setString(2, "Neha");
            pstmt.executeUpdate();
            System.out.println("Prepared insert completed.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
