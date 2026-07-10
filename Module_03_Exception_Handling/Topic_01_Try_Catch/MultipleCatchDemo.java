public class MultipleCatchDemo {
    public static void main(String[] args) {
        try {
            int[] values = new int[2];
            values[5] = 10;
        } catch (ArrayIndexOutOfBoundsException ex) {
            System.out.println("Array error: " + ex.getMessage());
        } catch (Exception ex) {
            System.out.println("General exception: " + ex.getMessage());
        }
    }
}
