import java.util.TreeSet;

public class TreeSetRemove {
    public static void main(String[] args) {
        TreeSet<String> set = new TreeSet<>();
        set.add("A");
        set.add("B");
        set.remove("A");
        System.out.println(set);
    }
}
