import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class BankManagementJDBC {
    public static void main(String[] args) {
        String sql = "INSERT INTO bank_account (id, owner, balance) VALUES (?, ?, ?)";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, 100);
            stmt.setString(2, "Kumar");
            stmt.setDouble(3, 1200.0);
            stmt.executeUpdate();
            System.out.println("Bank account inserted.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
