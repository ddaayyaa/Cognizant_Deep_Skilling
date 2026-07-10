public class BankTransaction {
    private static class Account {
        private double balance = 1000.0;

        public synchronized void deposit(double amount) {
            balance += amount;
            System.out.println("Deposited: " + amount);
        }

        public synchronized void withdraw(double amount) {
            if (amount <= balance) {
                balance -= amount;
                System.out.println("Withdrawn: " + amount);
            }
        }
    }

    public static void main(String[] args) {
        Account account = new Account();
        Thread t1 = new Thread(() -> account.deposit(200));
        Thread t2 = new Thread(() -> account.withdraw(150));
        t1.start();
        t2.start();
    }
}
