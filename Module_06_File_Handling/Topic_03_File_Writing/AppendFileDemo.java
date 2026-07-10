import java.io.FileWriter;
import java.io.IOException;

public class AppendFileDemo {
    public static void main(String[] args) {
        try (FileWriter writer = new FileWriter("append.txt", true)) {
            writer.write("Appended line
");
            System.out.println("Data appended to append.txt");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
