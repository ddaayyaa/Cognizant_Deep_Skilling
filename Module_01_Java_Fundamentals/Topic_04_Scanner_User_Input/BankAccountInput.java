import java.util.Scanner;

public class BankAccountInput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Account Number: ");
        long account = sc.nextLong();
        System.out.print("Balance: ");
        double balance = sc.nextDouble();
        System.out.println("Account: " + account);
        System.out.println("Balance: " + balance);
        sc.close();
    }
}
