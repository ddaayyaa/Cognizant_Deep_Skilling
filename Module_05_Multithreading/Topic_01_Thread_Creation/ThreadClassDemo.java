public class ThreadClassDemo extends Thread {
    @Override
    public void run() {
        System.out.println("ThreadClassDemo is running");
    }

    public static void main(String[] args) {
        new ThreadClassDemo().start();
    }
}
