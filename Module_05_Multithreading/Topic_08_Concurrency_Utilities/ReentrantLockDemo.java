import java.util.concurrent.locks.ReentrantLock;

public class ReentrantLockDemo {
    public static void main(String[] args) {
        ReentrantLock lock = new ReentrantLock();
        Runnable task = () -> {
            lock.lock();
            try {
                System.out.println(Thread.currentThread().getName() + " acquired lock");
            } finally {
                lock.unlock();
            }
        };
        new Thread(task).start();
        new Thread(task).start();
    }
}
