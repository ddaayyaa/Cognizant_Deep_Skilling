import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.IOException;

public class FilesDeleteDemo {
    public static void main(String[] args) {
        Path path = Paths.get("moved2.txt");
        try {
            Files.deleteIfExists(path);
            System.out.println("File deleted if it existed.");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
