public class SharedResource {
    private int value;

    public synchronized void setValue(int value) {
        this.value = value;
    }

    public synchronized int getValue() {
        return value;
    }

    public static void main(String[] args) {
        SharedResource resource = new SharedResource();
        Thread writer = new Thread(() -> resource.setValue(10));
        Thread reader = new Thread(() -> System.out.println(resource.getValue()));
        writer.start();
        reader.start();
    }
}
