public class FactorialMethod {

    public static void main(String[] args) {
        int number = 7;
        System.out.println("Factorial of " + number + " is " + factorial(number));
    }

    private static long factorial(int n) {
        long result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}
