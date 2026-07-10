import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.SQLException;

public class ScrollableResultSet {
    public static void main(String[] args) throws SQLException {
        String sql = "SELECT id, name FROM student";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             Statement stmt = conn.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY);
             ResultSet rs = stmt.executeQuery(sql)) {
            rs.afterLast();
            while (rs.previous()) {
                System.out.println(rs.getInt("id") + ": " + rs.getString("name"));
            }
        }
    }
}
