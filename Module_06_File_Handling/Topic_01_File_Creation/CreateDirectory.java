import java.io.File;

public class CreateDirectory {
    public static void main(String[] args) {
        File dir = new File("sampleDir");
        if (dir.mkdir()) {
            System.out.println("Directory created: " + dir.getName());
        } else {
            System.out.println("Failed to create directory.");
        }
    }
}
