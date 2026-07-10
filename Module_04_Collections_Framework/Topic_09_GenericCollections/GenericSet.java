import java.util.HashSet;
import java.util.Set;

public class GenericSet {
    public static void main(String[] args) {
        Set<String> set = new HashSet<>();
        set.add("Hello");
        System.out.println(set.contains("Hello"));
    }
}
