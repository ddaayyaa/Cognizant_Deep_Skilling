public class CountVowels {

    public static void main(String[] args) {
        String text = "Java programming";
        int count = 0;
        for (char ch : text.toLowerCase().toCharArray()) {
            if ("aeiou".indexOf(ch) >= 0) {
                count++;
            }
        }
        System.out.println("Number of vowels in '" + text + "' is " + count);
    }
}
