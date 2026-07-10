import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class SortingDemo {
    public static void main(String[] args) {
        List<String> items = new ArrayList<>();
        items.add("Banana");
        items.add("Apple");
        Collections.sort(items);
        System.out.println(items);
    }
}
