import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class ObjectOutputDemo {
    public static void main(String[] args) {
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("object.bin"))) {
            out.writeObject("Hello ObjectOutputStream");
            System.out.println("Object written to object.bin");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
