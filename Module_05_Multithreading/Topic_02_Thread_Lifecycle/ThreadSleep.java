public class ThreadSleep {
    public static void main(String[] args) {
        try {
            System.out.println("Sleeping...");
            Thread.sleep(500);
            System.out.println("Woke up");
        } catch (InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
    }
}
