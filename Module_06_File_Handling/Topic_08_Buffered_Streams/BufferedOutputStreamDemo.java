import java.io.BufferedOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class BufferedOutputStreamDemo {
    public static void main(String[] args) {
        try (BufferedOutputStream out = new BufferedOutputStream(new FileOutputStream("buffered_out.txt"))) {
            out.write("Buffered output example
".getBytes());
            System.out.println("Written to buffered_out.txt");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
