import java.util.Scanner;

public class BMI_Calculator {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Weight (kg): ");
        double weight = sc.nextDouble();

        System.out.print("Enter Height (m): ");
        double height = sc.nextDouble();

        double bmi = weight / (height * height);

        System.out.println("BMI = " + bmi);

        sc.close();

    }
}