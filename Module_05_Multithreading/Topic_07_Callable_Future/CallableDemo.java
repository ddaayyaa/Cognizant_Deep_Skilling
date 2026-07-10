import java.util.concurrent.Callable;

public class CallableDemo {
    public static void main(String[] args) throws Exception {
        Callable<String> task = () -> "Callable result";
        System.out.println(task.call());
    }
}
