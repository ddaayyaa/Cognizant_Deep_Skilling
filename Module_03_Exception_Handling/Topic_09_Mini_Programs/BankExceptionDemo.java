public class BankExceptionDemo {
    public static void main(String[] args) {
        try {
            processTransaction(-50);
        } catch (IllegalArgumentException ex) {
            System.out.println("Transaction failed: " + ex.getMessage());
        }
    }

    private static void processTransaction(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Amount must be greater than zero.");
        }
        System.out.println("Transaction successful: " + amount);
    }
}
