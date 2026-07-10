public class RecursiveMethod {

    public static void main(String[] args) {
        int number = 5;
        System.out.println("Factorial of " + number + " is " + factorial(number));
    }

    private static long factorial(int n) {
        if (n <= 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }
}
