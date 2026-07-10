import java.nio.file.Path;
import java.nio.file.Paths;

public class PathDemo {
    public static void main(String[] args) {
        Path path = Paths.get("sample.txt");
        System.out.println("Path: " + path);
        System.out.println("File name: " + path.getFileName());
    }
}
