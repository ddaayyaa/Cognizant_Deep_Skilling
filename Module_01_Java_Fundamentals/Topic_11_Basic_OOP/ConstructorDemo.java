public class ConstructorDemo {

    public static void main(String[] args) {
        ConstructorExample example1 = new ConstructorExample("Alice", 20);
        ConstructorExample example2 = new ConstructorExample("Bob");

        example1.printInfo();
        example2.printInfo();
    }
}

class ConstructorExample {
    private String name;
    private int age;

    public ConstructorExample(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public ConstructorExample(String name) {
        this(name, 18); // default age
    }

    public void printInfo() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}
