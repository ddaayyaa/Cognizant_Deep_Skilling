import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class LibraryManagementJDBC {
    public static void main(String[] args) {
        String sql = "INSERT INTO library_book (id, title, author) VALUES (?, ?, ?)";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, 301);
            stmt.setString(2, "1984");
            stmt.setString(3, "George Orwell");
            stmt.executeUpdate();
            System.out.println("Book inserted.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
