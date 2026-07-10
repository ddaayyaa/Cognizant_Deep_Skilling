import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;

public class DataInputStreamDemo {
    public static void main(String[] args) {
        try (DataInputStream in = new DataInputStream(new FileInputStream("data.bin"))) {
            int value = in.readInt();
            System.out.println("Read integer: " + value);
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
