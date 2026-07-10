import java.util.Scanner;

public class DiscountCalculator {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Product Price: ");

        double price = sc.nextDouble();

        double discount = price * 0.15;
        double finalPrice = price - discount;

        System.out.println("Discount = " + discount);
        System.out.println("Final Price = " + finalPrice);

        sc.close();

    }
}