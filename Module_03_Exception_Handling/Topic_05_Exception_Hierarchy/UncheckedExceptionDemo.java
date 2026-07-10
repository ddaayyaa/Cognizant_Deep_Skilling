public class UncheckedExceptionDemo {
    public static void main(String[] args) {
        try {
            String text = null;
            text.length();
        } catch (NullPointerException ex) {
            System.out.println("Unchecked exception caught: " + ex.getMessage());
        }
    }
}
