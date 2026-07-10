public class ThrowDemo {
    public static void main(String[] args) {
        try {
            throw new RuntimeException("Explicit runtime exception.");
        } catch (RuntimeException ex) {
            System.out.println("Caught: " + ex.getMessage());
        }
    }
}
