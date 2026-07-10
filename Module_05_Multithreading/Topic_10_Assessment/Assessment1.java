public class Assessment1 {
    public static int safeDivide(int a, int b) {
        try {
            return a / b;
        } catch (ArithmeticException ex) {
            return 0;
        }
    }

    public static void main(String[] args) {
        System.out.println(safeDivide(10, 0));
    }
}
