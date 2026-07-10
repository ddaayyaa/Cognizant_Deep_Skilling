public class StringReverse {

    public static void main(String[] args) {
        String text = "Hello World";
        String reversed = new StringBuilder(text).reverse().toString();
        System.out.println("Original: " + text);
        System.out.println("Reversed: " + reversed);
    }
}
