public class InputValidation {
    public static void main(String[] args) {
        String input = "";
        if (input == null || input.isEmpty()) {
            System.out.println("Input validation failed: value cannot be empty.");
        } else {
            System.out.println("Input is valid: " + input);
        }
    }
}
