public class NestedTryDemo {
    public static void main(String[] args) {
        try {
            try {
                int[] data = {1, 2, 3};
                System.out.println(data[5]);
            } catch (ArrayIndexOutOfBoundsException ex) {
                System.out.println("Inner catch: " + ex.getMessage());
            }
        } catch (Exception ex) {
            System.out.println("Outer catch: " + ex.getMessage());
        }
    }
}
