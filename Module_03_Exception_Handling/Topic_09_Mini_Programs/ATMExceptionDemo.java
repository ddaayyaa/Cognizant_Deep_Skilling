public class ATMExceptionDemo {
    public static void main(String[] args) {
        double balance = 1000.0;
        double withdrawal = 1200.0;
        try {
            if (withdrawal > balance) {
                throw new IllegalArgumentException("Insufficient funds.");
            }
            balance -= withdrawal;
            System.out.println("Remaining balance: " + balance);
        } catch (IllegalArgumentException ex) {
            System.out.println("ATM error: " + ex.getMessage());
        }
    }
}
