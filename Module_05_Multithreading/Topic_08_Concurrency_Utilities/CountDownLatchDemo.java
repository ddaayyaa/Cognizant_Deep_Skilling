import java.util.concurrent.CountDownLatch;

public class CountDownLatchDemo {
    public static void main(String[] args) throws InterruptedException {
        CountDownLatch latch = new CountDownLatch(2);
        Runnable worker = () -> {
            System.out.println(Thread.currentThread().getName() + " done");
            latch.countDown();
        };
        new Thread(worker).start();
        new Thread(worker).start();
        latch.await();
        System.out.println("All workers finished");
    }
}
