public class LinearSearch {

    public static void main(String[] args) {
        int[] numbers = {4, 7, 1, 9, 2};
        int target = 9;
        int index = linearSearch(numbers, target);
        if (index >= 0) {
            System.out.println(target + " found at index " + index);
        } else {
            System.out.println(target + " not found.");
        }
    }

    private static int linearSearch(int[] array, int target) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == target) {
                return i;
            }
        }
        return -1;
    }
}
