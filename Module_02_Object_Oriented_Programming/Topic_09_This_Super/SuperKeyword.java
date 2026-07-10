class ParentClass {
    protected String name = "Parent";

    public void showName() {
        System.out.println("Name from Parent: " + name);
    }
}

public class SuperKeyword extends ParentClass {
    protected String name = "Child";

    public void displayNames() {
        System.out.println("Name from Child: " + name);
        System.out.println("Name from Parent using super: " + super.name);
    }

    public static void main(String[] args) {
        SuperKeyword example = new SuperKeyword();
        example.displayNames();
    }
}
