public class SynchronizedBlock {
    private final Object lock = new Object();
    private int count;

    public void increment() {
        synchronized (lock) {
            count++;
        }
    }

    public static void main(String[] args) throws InterruptedException {
        SynchronizedBlock demo = new SynchronizedBlock();
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) demo.increment();
        });
        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) demo.increment();
        });
        t1.start();
        t2.start();
        t1.join();
        t2.join();
        System.out.println("Count: " + demo.count);
    }
}
