public class EvenOddChecker {

    public static void main(String[] args) {
        int[] numbers = {2, 5, 8, 11, 14, 17};
        for (int number : numbers) {
            if (number % 2 == 0) {
                System.out.println(number + " is even.");
            } else {
                System.out.println(number + " is odd.");
            }
        }
    }
}
