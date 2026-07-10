import java.io.File;

public class MoveFileDemo {
    public static void main(String[] args) {
        File source = new File("copy.txt");
        File destination = new File("moved.txt");
        if (source.renameTo(destination)) {
            System.out.println("File moved successfully.");
        } else {
            System.out.println("Failed to move file.");
        }
    }
}
