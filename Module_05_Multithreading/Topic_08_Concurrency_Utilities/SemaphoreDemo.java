import java.util.concurrent.Semaphore;

public class SemaphoreDemo {
    public static void main(String[] args) {
        Semaphore semaphore = new Semaphore(1);
        Runnable task = () -> {
            try {
                semaphore.acquire();
                System.out.println(Thread.currentThread().getName() + " acquired permit");
            } catch (InterruptedException ex) {
                Thread.currentThread().interrupt();
            } finally {
                semaphore.release();
            }
        };
        new Thread(task).start();
        new Thread(task).start();
    }
}
