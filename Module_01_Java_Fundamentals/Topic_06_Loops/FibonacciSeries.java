public class FibonacciSeries {

    public static void main(String[] args) {
        int terms = 10;
        int a = 0;
        int b = 1;
        System.out.print("Fibonacci series for " + terms + " terms: ");
        for (int i = 1; i <= terms; i++) {
            System.out.print(a + (i < terms ? ", " : "\n"));
            int next = a + b;
            a = b;
            b = next;
        }
    }
}
