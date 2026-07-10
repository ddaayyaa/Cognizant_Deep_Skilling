public class CustomThrowDemo {
    public static void main(String[] args) {
        try {
            throw new Exception("Custom exception thrown explicitly.");
        } catch (Exception ex) {
            System.out.println("Exception caught: " + ex.getMessage());
        }
    }
}
