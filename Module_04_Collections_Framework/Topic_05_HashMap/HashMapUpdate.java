import java.util.HashMap;

public class HashMapUpdate {
    public static void main(String[] args) {
        HashMap<Integer, String> map = new HashMap<>();
        map.put(1, "One");
        map.put(1, "Uno");
        System.out.println(map);
    }
}
