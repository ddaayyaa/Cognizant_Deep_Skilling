public class Assessment2 {
    public static String getSafeLength(String input) {
        try {
            return String.valueOf(input.length());
        } catch (NullPointerException ex) {
            return "0";
        }
    }

    public static void main(String[] args) {
        System.out.println(getSafeLength(null));
    }
}
