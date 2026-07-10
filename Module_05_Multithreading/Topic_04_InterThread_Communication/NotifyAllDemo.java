public class NotifyAllDemo {
    private static class MessageQueue {
        public synchronized void produce() throws InterruptedException {
            System.out.println("Producer producing");
            wait();
        }

        public synchronized void consume() {
            System.out.println("Consumer notifying all");
            notifyAll();
        }
    }

    public static void main(String[] args) throws InterruptedException {
        MessageQueue queue = new MessageQueue();
        Thread t1 = new Thread(() -> {
            try {
                queue.produce();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });
        t1.start();
        Thread.sleep(100);
        queue.consume();
    }
}
