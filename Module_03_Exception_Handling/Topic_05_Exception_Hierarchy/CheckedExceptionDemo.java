import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class CheckedExceptionDemo {
    public static void main(String[] args) {
        try {
            File file = new File("missing.txt");
            new FileInputStream(file);
        } catch (FileNotFoundException ex) {
            System.out.println("Checked exception: " + ex.getMessage());
        }
    }
}
