import java.util.TreeMap;

public class TreeMapRemove {
    public static void main(String[] args) {
        TreeMap<String, Integer> map = new TreeMap<>();
        map.put("A", 1);
        map.remove("A");
        System.out.println(map);
    }
}
