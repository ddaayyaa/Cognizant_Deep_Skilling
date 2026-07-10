public class DaemonThread {
    public static void main(String[] args) {
        Thread daemon = new Thread(() -> {
            while (true) {
                System.out.println("Daemon thread running");
                try {
                    Thread.sleep(200);
                } catch (InterruptedException ex) {
                    Thread.currentThread().interrupt();
                }
            }
        });
        daemon.setDaemon(true);
        daemon.start();
        System.out.println("Main thread ends");
    }
}
