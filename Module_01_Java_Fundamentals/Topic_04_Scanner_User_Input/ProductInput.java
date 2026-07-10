import java.util.Scanner;

public class ProductInput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Product Name: ");
        String product = sc.nextLine();
        System.out.print("Price: ");
        double price = sc.nextDouble();
        System.out.println("Product: " + product);
        System.out.println("Price: " + price);
        sc.close();
    }
}
