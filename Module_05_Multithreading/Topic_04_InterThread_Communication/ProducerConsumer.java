import java.util.LinkedList;
import java.util.Queue;

public class ProducerConsumer {
    public static void main(String[] args) {
        Queue<Integer> buffer = new LinkedList<>();
        int capacity = 5;

        Runnable producer = () -> {
            int value = 0;
            while (value < 5) {
                synchronized (buffer) {
                    while (buffer.size() == capacity) {
                        try {
                            buffer.wait();
                        } catch (InterruptedException ex) {
                            Thread.currentThread().interrupt();
                        }
                    }
                    buffer.add(value);
                    System.out.println("Produced " + value);
                    buffer.notify();
                }
                value++;
            }
        };
        Runnable consumer = () -> {
            while (true) {
                synchronized (buffer) {
                    while (buffer.isEmpty()) {
                        try {
                            buffer.wait();
                        } catch (InterruptedException ex) {
                            Thread.currentThread().interrupt();
                        }
                    }
                    int removed = buffer.poll();
                    System.out.println("Consumed " + removed);
                    buffer.notify();
                    if (removed == 4) {
                        break;
                    }
                }
            }
        };
        new Thread(producer).start();
        new Thread(consumer).start();
    }
}
