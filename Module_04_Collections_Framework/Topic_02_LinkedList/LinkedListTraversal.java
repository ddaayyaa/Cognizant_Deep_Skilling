import java.util.LinkedList;

public class LinkedListTraversal {
    public static void main(String[] args) {
        LinkedList<String> list = new LinkedList<>();
        list.add("X");
        list.add("Y");
        for (String item : list) {
            System.out.println(item);
        }
    }
}
