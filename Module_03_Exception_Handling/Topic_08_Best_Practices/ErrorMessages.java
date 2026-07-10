public class ErrorMessages {
    public static void main(String[] args) {
        try {
            String value = null;
            value.length();
        } catch (NullPointerException ex) {
            System.out.println("User-friendly error: input value is missing.");
            System.out.println("Technical detail: " + ex.getMessage());
        }
    }
}
