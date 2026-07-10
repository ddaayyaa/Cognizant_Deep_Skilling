import java.util.ArrayList;

public class ArrayListRemove {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(10);
        list.add(20);
        list.remove(Integer.valueOf(10));
        System.out.println(list);
    }
}
