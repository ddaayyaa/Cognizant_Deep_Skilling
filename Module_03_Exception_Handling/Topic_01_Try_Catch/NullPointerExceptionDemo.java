public class NullPointerExceptionDemo {
    public static void main(String[] args) {
        try {
            String text = null;
            System.out.println(text.length());
        } catch (NullPointerException ex) {
            System.out.println("NullPointerException caught: " + ex.getMessage());
        }
    }
}
