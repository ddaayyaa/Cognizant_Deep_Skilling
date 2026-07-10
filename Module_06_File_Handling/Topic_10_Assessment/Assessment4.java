import java.io.File;

public class Assessment4 {
    public static void main(String[] args) {
        File dir = new File("assessmentDir");
        if (!dir.exists()) {
            dir.mkdir();
        }
        System.out.println("Directory path: " + dir.getAbsolutePath());
    }
}
