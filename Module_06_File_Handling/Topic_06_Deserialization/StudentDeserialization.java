import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;

public class StudentDeserialization {
    public static void main(String[] args) {
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("student.ser"))) {
            Object obj = in.readObject();
            System.out.println("Student deserialized: " + obj);
        } catch (IOException | ClassNotFoundException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
