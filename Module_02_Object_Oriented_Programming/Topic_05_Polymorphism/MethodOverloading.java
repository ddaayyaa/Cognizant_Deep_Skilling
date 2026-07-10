public class MethodOverloading {
    public void display(String message) {
        System.out.println("Message: " + message);
    }

    public void display(String message, int count) {
        System.out.println("Message: " + message + " (count = " + count + ")");
    }

    public void display(int number) {
        System.out.println("Number: " + number);
    }

    public static void main(String[] args) {
        MethodOverloading overloading = new MethodOverloading();
        overloading.display("Hello World");
        overloading.display("Hello World", 3);
        overloading.display(42);
    }
}
