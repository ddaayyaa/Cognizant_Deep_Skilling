import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.IOException;

public class FilesMoveDemo {
    public static void main(String[] args) {
        Path source = Paths.get("copy2.txt");
        Path target = Paths.get("moved2.txt");
        try {
            Files.move(source, target);
            System.out.println("File moved successfully.");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
