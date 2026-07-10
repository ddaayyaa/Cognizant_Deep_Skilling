public class Student {
    private String name;
    private int rollNumber;
    private String grade;

    public Student(String name, int rollNumber, String grade) {
        this.name = name;
        this.rollNumber = rollNumber;
        this.grade = grade;
    }

    public void showStudentInfo() {
        System.out.println("Student Name : " + name);
        System.out.println("Roll Number  : " + rollNumber);
        System.out.println("Grade        : " + grade);
    }

    public static void main(String[] args) {
        Student student = new Student("Simran", 12, "A");
        student.showStudentInfo();
    }
}
