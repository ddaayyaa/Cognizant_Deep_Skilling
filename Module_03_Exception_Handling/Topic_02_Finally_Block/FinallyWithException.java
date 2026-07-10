public class FinallyWithException {
    public static void main(String[] args) {
        try {
            int value = Integer.parseInt("abc");
            System.out.println(value);
        } catch (NumberFormatException ex) {
            System.out.println("Caught NumberFormatException: " + ex.getMessage());
        } finally {
            System.out.println("Finally block execution completed.");
        }
    }
}
