import java.util.Scanner;

public class ElectricityBill {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Units Consumed: ");

        int units = sc.nextInt();

        double bill = units * 7.5;

        System.out.println("Electricity Bill = ₹" + bill);

        sc.close();

    }
}