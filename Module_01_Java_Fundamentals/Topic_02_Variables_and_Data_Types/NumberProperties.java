import java.util.Scanner;

public class NumberProperties {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Number: ");

        int number = sc.nextInt();

        System.out.println("Square = " + (number * number));
        System.out.println("Cube = " + (number * number * number));

        sc.close();

    }
}