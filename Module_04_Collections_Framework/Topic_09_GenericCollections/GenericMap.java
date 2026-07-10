import java.util.HashMap;
import java.util.Map;

public class GenericMap {
    public static void main(String[] args) {
        Map<String, Integer> map = new HashMap<>();
        map.put("A", 1);
        System.out.println(map.get("A"));
    }
}
