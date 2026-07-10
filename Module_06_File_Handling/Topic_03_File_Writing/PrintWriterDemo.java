import java.io.PrintWriter;
import java.io.IOException;

public class PrintWriterDemo {
    public static void main(String[] args) {
        try (PrintWriter writer = new PrintWriter("printwriter.txt")) {
            writer.println("PrintWriter example");
            System.out.println("Data written to printwriter.txt");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
