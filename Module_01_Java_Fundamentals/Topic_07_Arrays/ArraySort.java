import java.util.Arrays;

public class ArraySort {

    public static void main(String[] args) {
        int[] numbers = {9, 3, 7, 1, 5};
        System.out.println("Before sort: " + Arrays.toString(numbers));
        Arrays.sort(numbers);
        System.out.println("After sort: " + Arrays.toString(numbers));
    }
}
