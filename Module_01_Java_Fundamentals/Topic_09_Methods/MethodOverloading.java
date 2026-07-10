public class MethodOverloading {

    public static void main(String[] args) {
        System.out.println("Sum of two ints: " + add(5, 10));
        System.out.println("Sum of three ints: " + add(4, 7, 2));
        System.out.println("Sum of two doubles: " + add(3.5, 2.4));
    }

    private static int add(int a, int b) {
        return a + b;
    }

    private static int add(int a, int b, int c) {
        return a + b + c;
    }

    private static double add(double a, double b) {
        return a + b;
    }
}
