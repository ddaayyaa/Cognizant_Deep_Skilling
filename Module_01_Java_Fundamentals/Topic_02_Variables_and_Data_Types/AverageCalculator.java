import java.util.Scanner;

public class AverageCalculator {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter First Number : ");
        int a = sc.nextInt();

        System.out.print("Enter Second Number : ");
        int b = sc.nextInt();

        System.out.print("Enter Third Number : ");
        int c = sc.nextInt();

        double average = (a + b + c) / 3.0;

        System.out.println("Average = " + average);

        sc.close();

    }
}