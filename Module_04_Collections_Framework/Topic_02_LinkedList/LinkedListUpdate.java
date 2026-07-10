import java.util.LinkedList;

public class LinkedListUpdate {
    public static void main(String[] args) {
        LinkedList<String> list = new LinkedList<>();
        list.add("Old");
        list.set(0, "Updated");
        System.out.println(list);
    }
}
