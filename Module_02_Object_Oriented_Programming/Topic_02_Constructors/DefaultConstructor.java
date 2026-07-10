public class DefaultConstructor {
    private String name;
    private int age;

    public DefaultConstructor() {
        this.name = "Default Student";
        this.age = 18;
    }

    public void showInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age : " + age);
    }

    public static void main(String[] args) {
        DefaultConstructor student = new DefaultConstructor();
        student.showInfo();
    }
}
