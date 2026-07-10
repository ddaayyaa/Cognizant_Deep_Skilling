public class SynchronizedMethod {
    private int count;

    public synchronized void increment() {
        count++;
    }

    public static void main(String[] args) throws InterruptedException {
        SynchronizedMethod demo = new SynchronizedMethod();
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
