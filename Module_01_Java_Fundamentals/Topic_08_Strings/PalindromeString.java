public class PalindromeString {

    public static void main(String[] args) {
        String original = "radar";
        String reversed = new StringBuilder(original).reverse().toString();
        System.out.println(original + " is " + (original.equals(reversed) ? "a palindrome." : "not a palindrome."));
    }
}
