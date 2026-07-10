import java.util.Scanner;

public class MiniCalculator {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter First Number: ");
        double a = sc.nextDouble();

        System.out.print("Enter Second Number: ");
        double b = sc.nextDouble();

        System.out.println("Addition = " + (a + b));
        System.out.println("Subtraction = " + (a - b));
        System.out.println("Multiplication = " + (a * b));

        if (b != 0) {

            System.out.println("Division = " + (a / b));

        } else {

            System.out.println("Division by zero is not allowed.");

        }

        sc.close();

    }
}