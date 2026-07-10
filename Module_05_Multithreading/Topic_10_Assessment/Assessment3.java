public class Assessment3 {
    public static void main(String[] args) {
        try {
            throw new Exception("Assessment exception");
        } catch (Exception ex) {
            System.out.println("Handled: " + ex.getMessage());
        }
    }
}
