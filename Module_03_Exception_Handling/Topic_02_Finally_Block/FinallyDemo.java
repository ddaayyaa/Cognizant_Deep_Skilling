public class FinallyDemo {
    public static void main(String[] args) {
        try {
            System.out.println("Inside try block.");
        } finally {
            System.out.println("Finally block always executes.");
        }
    }
}
