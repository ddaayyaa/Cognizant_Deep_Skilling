import java.util.concurrent.FutureTask;

public class FutureTaskDemo {
    public static void main(String[] args) throws Exception {
        FutureTask<Integer> task = new FutureTask<>(() -> 20);
        new Thread(task).start();
        System.out.println("FutureTask result: " + task.get());
    }
}
