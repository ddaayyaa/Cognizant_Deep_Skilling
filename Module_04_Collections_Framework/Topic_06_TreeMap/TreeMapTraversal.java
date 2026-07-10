import java.util.TreeMap;

public class TreeMapTraversal {
    public static void main(String[] args) {
        TreeMap<String, Integer> map = new TreeMap<>();
        map.put("C", 3);
        map.put("A", 1);
        for (String key : map.keySet()) {
            System.out.println(key + " -> " + map.get(key));
        }
    }
}
