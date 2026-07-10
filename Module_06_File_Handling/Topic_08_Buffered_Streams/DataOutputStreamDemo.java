import java.io.DataOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class DataOutputStreamDemo {
    public static void main(String[] args) {
        try (DataOutputStream out = new DataOutputStream(new FileOutputStream("data.bin"))) {
            out.writeInt(2024);
            System.out.println("Written integer to data.bin");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
