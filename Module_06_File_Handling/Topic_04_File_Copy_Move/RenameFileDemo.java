import java.io.File;

public class RenameFileDemo {
    public static void main(String[] args) {
        File file = new File("moved.txt");
        File renamed = new File("renamed.txt");
        if (file.renameTo(renamed)) {
            System.out.println("File renamed successfully.");
        } else {
            System.out.println("Failed to rename file.");
        }
    }
}
