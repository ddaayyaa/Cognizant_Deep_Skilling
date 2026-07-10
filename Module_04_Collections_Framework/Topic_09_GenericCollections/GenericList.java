import java.util.ArrayList;
import java.util.List;

public class GenericList {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("One");
        System.out.println(list.get(0));
    }
}
