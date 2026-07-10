public class ThreadJoin {
    public static void main(String[] args) {
        Thread thread = new Thread(() -> {
            try {
                Thread.sleep(500);
                System.out.println("Joined thread finished");
            } catch (InterruptedException ex) {
                Thread.currentThread().interrupt();
            }
        });
        thread.start();
        try {
            thread.join();
            System.out.println("Main thread resumed after join");
        } catch (InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
    }
}
