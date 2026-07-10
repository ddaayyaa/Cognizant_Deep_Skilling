public class CalculatorExceptionDemo {
    public static void main(String[] args) {
        try {
            int result = divide(10, 0);
            System.out.println("Result: " + result);
        } catch (ArithmeticException ex) {
            System.out.println("Cannot divide by zero: " + ex.getMessage());
        }
    }

    private static int divide(int a, int b) {
        return a / b;
    }
}
