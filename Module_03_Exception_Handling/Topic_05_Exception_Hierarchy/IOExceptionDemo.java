import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

public class IOExceptionDemo {
    public static void main(String[] args) {
        try (FileInputStream stream = new FileInputStream(new File("missing.txt"))) {
            System.out.println(stream.read());
        } catch (IOException ex) {
            System.out.println("IOException caught: " + ex.getMessage());
        }
    }
}
