import java.util.ArrayList;
import java.util.List;

class BankAccount {
    private String accountNumber;
    private String owner;
    private double balance;

    public BankAccount(String accountNumber, String owner, double balance) {
        this.accountNumber = accountNumber;
        this.owner = owner;
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

    public String getAccountNumber() {
        return accountNumber;
    }

    public String getOwner() {
        return owner;
    }

    public double getBalance() {
        return balance;
    }
}

public class BankManagementSystem {
    public static void main(String[] args) {
        List<BankAccount> accounts = new ArrayList<>();
        accounts.add(new BankAccount("B001", "Amit", 1500.0));
        accounts.add(new BankAccount("B002", "Rina", 2800.0));

        for (BankAccount account : accounts) {
            System.out.println("Account: " + account.getAccountNumber() + ", Owner: " + account.getOwner() + ", Balance: " + account.getBalance());
        }
    }
}
