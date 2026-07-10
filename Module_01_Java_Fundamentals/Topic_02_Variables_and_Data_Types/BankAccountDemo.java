import java.util.Scanner;

public class BankAccountDemo {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Account Holder Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Balance: ");
        double balance = sc.nextDouble();

        System.out.println("\nAccount Holder : " + name);
        System.out.println("Available Balance : ₹" + balance);

        sc.close();

    }
}