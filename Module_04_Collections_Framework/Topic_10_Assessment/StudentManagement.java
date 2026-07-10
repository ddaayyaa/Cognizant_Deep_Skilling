import java.util.HashMap;
import java.util.Map;

public class StudentManagement {
    public static void main(String[] args) {
        Map<Integer, String> students = new HashMap<>();
        students.put(1, "Ravi");
        students.put(2, "Pooja");
        System.out.println(students);
    }
}
