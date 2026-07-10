public class NestedExceptionExample {
    public static void main(String[] args) {
        try {
            try {
                int result = 10 / 0;
                System.out.println(result);
            } catch (ArithmeticException ex) {
                System.out.println("Inner catch: " + ex.getMessage());
                throw ex;
            }
        } catch (ArithmeticException ex) {
            System.out.println("Outer catch: " + ex.getMessage());
        }
    }
}
