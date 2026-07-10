public class RunnableInterfaceDemo {
    public static void main(String[] args) {
        Runnable task = () -> System.out.println("Runnable task executed");
        Thread thread = new Thread(task);
        thread.start();
    }
}
