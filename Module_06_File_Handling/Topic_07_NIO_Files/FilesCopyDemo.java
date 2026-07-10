import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.IOException;

public class FilesCopyDemo {
    public static void main(String[] args) {
        Path source = Paths.get("output.txt");
        Path target = Paths.get("copy2.txt");
        try {
            Files.copy(source, target);
            System.out.println("File copied successfully.");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
