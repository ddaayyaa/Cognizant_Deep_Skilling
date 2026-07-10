public class ThrowsDemo {
    public static void riskyMethod() throws Exception {
        throw new Exception("This method throws an exception.");
    }

    public static void main(String[] args) {
        try {
            riskyMethod();
        } catch (Exception ex) {
            System.out.println("Handled exception: " + ex.getMessage());
        }
    }
}
