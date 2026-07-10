import java.util.*;

public class HashMapExample {

    public static void main(String[] args) {

        HashMap<Integer,String> map = new HashMap<>();

        map.put(101,"Daya");
        map.put(102,"Rahul");
        map.put(103,"Anil");

        for(Map.Entry<Integer,String> entry : map.entrySet()){

            System.out.println(entry.getKey()+" "+entry.getValue());

        }

    }

}