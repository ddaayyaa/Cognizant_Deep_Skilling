public class BankSynchronization {
    private static class Account {
        private double balance = 1000.0;

        public synchronized void withdraw(double amount) {
            if (amount <= balance) {
                balance -= amount;
                System.out.println("Withdrawn: " + amount + ", remaining: " + balance);
            }
        }
    }

    public static void main(String[] args) {
        Account account = new Account();
        Runnable task = () -> account.withdraw(500);
        new Thread(task).start();
        new Thread(task).start();
    }
}
