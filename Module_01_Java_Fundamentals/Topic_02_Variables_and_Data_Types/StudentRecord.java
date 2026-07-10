import java.util.Scanner;

public class StudentRecord {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Student Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Roll Number: ");
        int roll = sc.nextInt();

        System.out.print("Enter Percentage: ");
        double percentage = sc.nextDouble();

        System.out.println("\n----- Student Record -----");
        System.out.println("Name : " + name);
        System.out.println("Roll Number : " + roll);
        System.out.println("Percentage : " + percentage);

        sc.close();

    }
}