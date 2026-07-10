public class BankManagementSystem {

    public static void main(String[] args) {
        BankAccount account = new BankAccount("A123", 1000.0);
        account.deposit(250.0);
        account.withdraw(150.0);
        System.out.println("Final balance: " + account.getBalance());
    }
}

class BankAccount {
    private String id;
    private double balance;

    public BankAccount(String id, double balance) {
        this.id = id;
        this.balance = balance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
        }
    }

    public double getBalance() {
        return balance;
    }
}
