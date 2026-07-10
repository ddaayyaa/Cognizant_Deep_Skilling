import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class StudentManagementJDBC {
    public static void main(String[] args) {
        String sql = "INSERT INTO student (id, name, course) VALUES (?, ?, ?)";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, 401);
            stmt.setString(2, "Nina");
            stmt.setString(3, "Computer Science");
            stmt.executeUpdate();
            System.out.println("Student inserted.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
