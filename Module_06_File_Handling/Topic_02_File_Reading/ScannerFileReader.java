import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ScannerFileReader {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(new File("output.txt"))) {
            while (scanner.hasNextLine()) {
                System.out.println(scanner.nextLine());
            }
        } catch (FileNotFoundException ex) {
            System.out.println("File not found: " + ex.getMessage());
        }
    }
}
