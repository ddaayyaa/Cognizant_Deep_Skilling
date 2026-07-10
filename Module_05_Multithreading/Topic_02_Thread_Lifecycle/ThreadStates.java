public class ThreadStates {
    public static void main(String[] args) throws InterruptedException {
        Thread thread = new Thread(() -> {
            try {
                Thread.sleep(100);
            } catch (InterruptedException ex) {
                Thread.currentThread().interrupt();
            }
        });
        System.out.println("State before start: " + thread.getState());
        thread.start();
        System.out.println("State after start: " + thread.getState());
        thread.join();
        System.out.println("State after join: " + thread.getState());
    }
}
