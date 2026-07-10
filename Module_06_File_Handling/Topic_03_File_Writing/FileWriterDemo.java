import java.io.FileWriter;
import java.io.IOException;

public class FileWriterDemo {
    public static void main(String[] args) {
        try (FileWriter writer = new FileWriter("output.txt")) {
            writer.write("Hello, FileWriter!
");
            System.out.println("Data written to output.txt");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
