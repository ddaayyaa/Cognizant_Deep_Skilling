import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class EmployeeManagementJDBC {
    public static void main(String[] args) {
        String sql = "INSERT INTO employee (id, name, department) VALUES (?, ?, ?)";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, 201);
            stmt.setString(2, "Rina");
            stmt.setString(3, "Sales");
            stmt.executeUpdate();
            System.out.println("Employee inserted.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
