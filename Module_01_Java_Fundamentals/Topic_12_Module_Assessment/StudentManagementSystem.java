import java.util.ArrayList;
import java.util.List;

public class StudentManagementSystem {

    public static void main(String[] args) {
        List<Student> students = new ArrayList<>();
        students.add(new Student("S001", "John", 85));
        students.add(new Student("S002", "Emma", 92));
        for (Student student : students) {
            student.printDetails();
        }
    }
}

class Student {
    private String id;
    private String name;
    private int score;

    public Student(String id, String name, int score) {
        this.id = id;
        this.name = name;
        this.score = score;
    }

    public void printDetails() {
        System.out.println(id + " - " + name + " : " + score);
    }
}
