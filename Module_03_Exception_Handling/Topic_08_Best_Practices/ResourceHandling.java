import java.io.BufferedReader;
import java.io.IOException;
import java.io.StringReader;

public class ResourceHandling {
    public static void main(String[] args) {
        try (BufferedReader reader = new BufferedReader(new StringReader("Hello"))) {
            System.out.println(reader.readLine());
        } catch (IOException ex) {
            System.out.println("IOException: " + ex.getMessage());
        }
    }
}
