public class NestedFinallyDemo {
    public static void main(String[] args) {
        try {
            try {
                System.out.println("Inner try block.");
                int result = 10 / 0;
            } finally {
                System.out.println("Inner finally block.");
            }
        } catch (ArithmeticException ex) {
            System.out.println("Outer catch: " + ex.getMessage());
        } finally {
            System.out.println("Outer finally block.");
        }
    }
}
