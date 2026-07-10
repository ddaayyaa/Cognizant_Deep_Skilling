public class PrimeNumber {

    public static void main(String[] args) {
        int number = 29;
        System.out.println(number + " is " + (isPrime(number) ? "a prime number." : "not a prime number."));
    }

    private static boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}
