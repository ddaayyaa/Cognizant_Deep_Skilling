import java.io.FileWriter;
import java.io.IOException;

public class Assessment2 {
    public static void main(String[] args) {
        try (FileWriter writer = new FileWriter("assessment2.txt")) {
            writer.write("Assessment2 data
");
            System.out.println("Assessment2 file created.");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
