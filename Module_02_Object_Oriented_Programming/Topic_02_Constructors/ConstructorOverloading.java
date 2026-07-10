public class ConstructorOverloading {
    private String name;
    private int age;
    private double salary;

    public ConstructorOverloading(String name) {
        this(name, 25, 45000.0);
    }

    public ConstructorOverloading(String name, int age) {
        this(name, age, 45000.0);
    }

    public ConstructorOverloading(String name, int age, double salary) {
        this.name = name;
        this.age = age;
        this.salary = salary;
    }

    public void showInfo() {
        System.out.println("Name  : " + name);
        System.out.println("Age   : " + age);
        System.out.println("Salary: " + salary);
    }

    public static void main(String[] args) {
        ConstructorOverloading employee1 = new ConstructorOverloading("Asha");
        ConstructorOverloading employee2 = new ConstructorOverloading("Vikram", 29);
        ConstructorOverloading employee3 = new ConstructorOverloading("Neel", 32, 82000.0);

        employee1.showInfo();
        System.out.println();
        employee2.showInfo();
        System.out.println();
        employee3.showInfo();
    }
}
