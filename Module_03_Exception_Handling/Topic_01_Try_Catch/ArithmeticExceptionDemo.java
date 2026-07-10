public class ArithmeticExceptionDemo {
    public static void main(String[] args) {
        try {
            int result = 10 / 0;
            System.out.println("Result: " + result);
        } catch (ArithmeticException ex) {
            System.out.println("ArithmeticException caught: " + ex.getMessage());
        }
    }
}
