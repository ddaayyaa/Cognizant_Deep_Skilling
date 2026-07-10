import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

public class Assessment3 {
    public static void main(String[] args) {
        try (BufferedReader reader = new BufferedReader(new FileReader("assessment2.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
