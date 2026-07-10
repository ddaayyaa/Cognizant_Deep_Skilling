class Base {
    public Base(String message) {
        System.out.println("Base constructor: " + message);
    }
}

public class SuperConstructor extends Base {
    public SuperConstructor() {
        super("Hello from the base class");
        System.out.println("Derived constructor called.");
    }

    public static void main(String[] args) {
        new SuperConstructor();
    }
}
