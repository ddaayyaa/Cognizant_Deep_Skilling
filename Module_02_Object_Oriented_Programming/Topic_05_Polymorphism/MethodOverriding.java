class ParentClass {
    public void show() {
        System.out.println("Parent show method.");
    }
}

public class MethodOverriding extends ParentClass {
    @Override
    public void show() {
        System.out.println("Child show method.");
    }

    public static void main(String[] args) {
        ParentClass object = new MethodOverriding();
        object.show();
    }
}
