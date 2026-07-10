import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ShuffleDemo {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
        Collections.shuffle(numbers);
        System.out.println(numbers);
    }
}
