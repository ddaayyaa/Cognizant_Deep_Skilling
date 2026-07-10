import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CyclicBarrier;

public class CyclicBarrierDemo {
    public static void main(String[] args) throws InterruptedException, BrokenBarrierException {
        CyclicBarrier barrier = new CyclicBarrier(2, () -> System.out.println("Barrier reached"));
        Runnable task = () -> {
            try {
                System.out.println(Thread.currentThread().getName() + " waiting");
                barrier.await();
            } catch (Exception ex) {
                Thread.currentThread().interrupt();
            }
        };
        new Thread(task).start();
        new Thread(task).start();
    }
}
