import java.util.Scanner;

public class CurrencyConverter {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        double exchangeRate = 83.50;

        System.out.print("Enter Amount in USD: ");

        double usd = sc.nextDouble();

        double inr = usd * exchangeRate;

        System.out.println("INR = " + inr);

        sc.close();

    }
}