public class ReturnFinallyDemo {
    public static void main(String[] args) {
        System.out.println(showMessage());
    }

    public static String showMessage() {
        try {
            return "Try Block";
        } finally {
            System.out.println("Finally block executed before return.");
        }
    }
}
