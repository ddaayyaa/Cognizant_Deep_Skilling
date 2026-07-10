public class StaticMethod {
    private static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        int result = StaticMethod.add(15, 20);
        System.out.println("Result: " + result);
    }
}
