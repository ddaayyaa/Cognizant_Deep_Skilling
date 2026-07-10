public class ExceptionLogging {
    public static void main(String[] args) {
        try {
            String result = "";
            int value = Integer.parseInt(result);
            System.out.println(value);
        } catch (NumberFormatException ex) {
            System.err.println("LOG: NumberFormatException occurred: " + ex.getMessage());
        }
    }
}
