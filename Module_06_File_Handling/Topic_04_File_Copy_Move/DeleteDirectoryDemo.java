import java.io.File;

public class DeleteDirectoryDemo {
    public static void main(String[] args) {
        File dir = new File("sampleDir");
        if (dir.exists() && dir.isDirectory()) {
            if (dir.delete()) {
                System.out.println("Directory deleted.");
            } else {
                System.out.println("Directory not empty or could not be deleted.");
            }
        }
    }
}
