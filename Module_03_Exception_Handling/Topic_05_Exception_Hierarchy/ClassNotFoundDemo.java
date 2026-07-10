public class ClassNotFoundDemo {
    public static void main(String[] args) {
        try {
            Class.forName("com.example.DoesNotExist");
        } catch (ClassNotFoundException ex) {
            System.out.println("ClassNotFoundException: " + ex.getMessage());
        }
    }
}
