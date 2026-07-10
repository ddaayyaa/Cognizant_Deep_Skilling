import java.util.TreeSet;

public class TreeSetTraversal {
    public static void main(String[] args) {
        TreeSet<Integer> set = new TreeSet<>();
        set.add(10);
        set.add(20);
        for (Integer value : set) {
            System.out.println(value);
        }
    }
}
