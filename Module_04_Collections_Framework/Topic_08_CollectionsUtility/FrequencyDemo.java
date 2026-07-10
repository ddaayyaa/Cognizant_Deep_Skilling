import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class FrequencyDemo {
    public static void main(String[] args) {
        List<String> items = new ArrayList<>();
        items.add("apple");
        items.add("banana");
        items.add("apple");
        System.out.println("Frequency of apple: " + Collections.frequency(items, "apple"));
    }
}
