public class Assessment4 {
    public static void main(String[] args) {
        try {
            int[] values = {1, 2, 3};
            System.out.println(values[2]);
        } catch (ArrayIndexOutOfBoundsException ex) {
            System.out.println("Index error: " + ex.getMessage());
        }
    }
}
