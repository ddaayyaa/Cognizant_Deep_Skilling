import java.util.HashMap;
import java.util.Map;

public class BankManagement {
    public static void main(String[] args) {
        Map<String, Double> accounts = new HashMap<>();
        accounts.put("A101", 2000.0);
        System.out.println(accounts);
    }
}
