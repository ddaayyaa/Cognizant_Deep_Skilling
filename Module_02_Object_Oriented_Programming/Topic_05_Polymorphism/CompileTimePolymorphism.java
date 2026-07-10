public class CompileTimePolymorphism {
    public int add(int a, int b) {
        return a + b;
    }

    public double add(double a, double b) {
        return a + b;
    }

    public int add(int a, int b, int c) {
        return a + b + c;
    }

    public static void main(String[] args) {
        CompileTimePolymorphism calculator = new CompileTimePolymorphism();
        System.out.println("Sum of two ints: " + calculator.add(5, 10));
        System.out.println("Sum of two doubles: " + calculator.add(3.5, 4.7));
        System.out.println("Sum of three ints: " + calculator.add(1, 2, 3));
    }
}
