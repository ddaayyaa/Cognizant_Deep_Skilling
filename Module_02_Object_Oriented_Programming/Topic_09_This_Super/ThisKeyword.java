public class ThisKeyword {
    private String name;
    private int age;

    public ThisKeyword(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void display() {
        System.out.println("Name: " + this.name);
        System.out.println("Age : " + this.age);
    }

    public static void main(String[] args) {
        ThisKeyword student = new ThisKeyword("Ananya", 19);
        student.display();
    }
}
