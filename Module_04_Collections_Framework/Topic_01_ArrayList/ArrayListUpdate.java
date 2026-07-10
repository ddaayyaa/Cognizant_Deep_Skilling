import java.util.ArrayList;

public class ArrayListUpdate {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("Old");
        list.set(0, "New");
        System.out.println(list);
    }
}
