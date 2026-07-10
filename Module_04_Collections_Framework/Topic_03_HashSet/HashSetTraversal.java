import java.util.HashSet;

public class HashSetTraversal {
    public static void main(String[] args) {
        HashSet<String> set = new HashSet<>();
        set.add("Alpha");
        set.add("Beta");
        for (String item : set) {
            System.out.println(item);
        }
    }
}
