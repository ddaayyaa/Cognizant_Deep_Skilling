public class EncapsulationDemo {

    public static void main(String[] args) {
        BankAccount account = new BankAccount("A1001", 500.0);
        System.out.println("Account ID: " + account.getAccountId());
        System.out.println("Initial Balance: " + account.getBalance());

        account.deposit(150.0);
        account.withdraw(200.0);

        System.out.println("Final Balance: " + account.getBalance());
    }
}

class BankAccount {
    private String accountId;
    private double balance;

    public BankAccount(String accountId, double balance) {
        this.accountId = accountId;
        this.balance = balance;
    }

    public String getAccountId() {
        return accountId;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposited: " + amount);
        } else {
            System.out.println("Deposit amount must be positive.");
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println("Withdrew: " + amount);
        } else {
            System.out.println("Invalid withdrawal amount.");
        }
    }
}
