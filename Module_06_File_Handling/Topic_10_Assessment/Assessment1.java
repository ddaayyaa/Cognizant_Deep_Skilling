import java.io.File;

public class Assessment1 {
    public static void main(String[] args) {
        File file = new File("assessment1.txt");
        System.out.println("Can read: " + file.canRead());
    }
}
