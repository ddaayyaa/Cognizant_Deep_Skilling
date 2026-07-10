import java.util.ArrayList;
import java.util.List;

class StudentRecord {
    private String name;
    private int rollNumber;
    private String course;

    public StudentRecord(String name, int rollNumber, String course) {
        this.name = name;
        this.rollNumber = rollNumber;
        this.course = course;
    }

    public String getSummary() {
        return "Roll: " + rollNumber + ", Name: " + name + ", Course: " + course;
    }
}

public class StudentManagementSystem {
    public static void main(String[] args) {
        List<StudentRecord> students = new ArrayList<>();
        students.add(new StudentRecord("Riya", 10, "Computer Science"));
        students.add(new StudentRecord("Arjun", 11, "Mathematics"));

        for (StudentRecord student : students) {
            System.out.println(student.getSummary());
        }
    }
}
