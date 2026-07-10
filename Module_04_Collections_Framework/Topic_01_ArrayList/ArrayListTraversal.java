import java.util.ArrayList;

public class ArrayListTraversal {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("A");
        list.add("B");
        for (String item : list) {
            System.out.println(item);
        }
    }
}
