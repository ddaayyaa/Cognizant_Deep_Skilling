import java.util.HashSet;

public class HashSetRemove {
    public static void main(String[] args) {
        HashSet<String> set = new HashSet<>();
        set.add("One");
        set.add("Two");
        set.remove("One");
        System.out.println(set);
    }
}
