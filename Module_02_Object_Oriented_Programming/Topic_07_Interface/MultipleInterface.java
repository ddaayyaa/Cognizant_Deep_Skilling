interface Printer {
    void print(String message);
}

interface Scanner {
    void scan();
}

public class MultipleInterface implements Printer, Scanner {
    @Override
    public void print(String message) {
        System.out.println("Printing: " + message);
    }

    @Override
    public void scan() {
        System.out.println("Scanning a document.");
    }

    public static void main(String[] args) {
        MultipleInterface device = new MultipleInterface();
        device.print("Hello Interface");
        device.scan();
    }
}
