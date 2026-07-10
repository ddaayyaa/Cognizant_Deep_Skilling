import java.util.HashMap;

public class HashMapRemove {
    public static void main(String[] args) {
        HashMap<Integer, String> map = new HashMap<>();
        map.put(1, "One");
        map.remove(1);
        System.out.println(map);
    }
}
