public class NestedCatchDemo {
    public static void main(String[] args) {
        try {
            int[] values = {1, 2, 3};
            try {
                System.out.println(values[5]);
            } catch (ArrayIndexOutOfBoundsException ex) {
                System.out.println("Inner catch: " + ex.getMessage());
            }
        } catch (Exception ex) {
            System.out.println("Outer catch: " + ex.getMessage());
        }
    }
}
