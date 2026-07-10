public class Factorial {

    public static void main(String[] args) {
        int number = 6;
        long result = 1;
        for (int i = 1; i <= number; i++) {
            result *= i;
        }
        System.out.println("Factorial of " + number + " is " + result);
    }
}
