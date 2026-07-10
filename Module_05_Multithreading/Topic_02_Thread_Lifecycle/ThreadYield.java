public class ThreadYield {
    public static void main(String[] args) {
        Runnable task = () -> {
            System.out.println(Thread.currentThread().getName() + " before yield");
            Thread.yield();
            System.out.println(Thread.currentThread().getName() + " after yield");
        };
        new Thread(task, "Thread-A").start();
        new Thread(task, "Thread-B").start();
    }
}
