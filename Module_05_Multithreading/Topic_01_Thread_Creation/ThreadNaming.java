public class ThreadNaming {
    public static void main(String[] args) {
        Thread thread = new Thread(() -> System.out.println("Named thread running"));
        thread.setName("WorkerThread");
        thread.start();
        System.out.println("Thread name: " + thread.getName());
    }
}
