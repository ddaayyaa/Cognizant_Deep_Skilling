public class InterfaceDemo implements BankInterface {
    private double balance;

    @Override
    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println(amount + " withdrawn. Remaining balance: " + balance);
        } else {
            System.out.println("Invalid withdrawal.");
        }
    }

    @Override
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println(amount + " deposited. New balance: " + balance);
        } else {
            System.out.println("Invalid deposit.");
        }
    }

    @Override
    public double getBalance() {
        return balance;
    }

    public static void main(String[] args) {
        InterfaceDemo account = new InterfaceDemo();
        account.deposit(1200.0);
        account.withdraw(450.0);
        System.out.println("Final Balance: " + account.getBalance());
    }
}
