public class LargestElement {

    public static void main(String[] args) {
        int[] numbers = {6, 12, 3, 19, 8};
        int max = numbers[0];
        for (int number : numbers) {
            if (number > max) {
                max = number;
            }
        }
        System.out.println("Largest element: " + max);
    }
}
