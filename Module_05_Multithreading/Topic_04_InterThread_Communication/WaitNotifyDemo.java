public class WaitNotifyDemo {
    private static class Signal {
        public synchronized void doWait() {
            try {
                wait();
                System.out.println("Notified");
            } catch (InterruptedException ex) {
                Thread.currentThread().interrupt();
            }
        }

        public synchronized void doNotify() {
            notify();
        }
    }

    public static void main(String[] args) throws InterruptedException {
        Signal signal = new Signal();
        Thread waiter = new Thread(signal::doWait);
        waiter.start();
        Thread.sleep(100);
        synchronized (signal) {
            signal.doNotify();
        }
    }
}
