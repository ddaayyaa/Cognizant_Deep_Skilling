import java.util.Scanner;

public class VolumeCalculator {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Length: ");
        double length = sc.nextDouble();

        System.out.print("Enter Width: ");
        double width = sc.nextDouble();

        System.out.print("Enter Height: ");
        double height = sc.nextDouble();

        double volume = length * width * height;

        System.out.println("Volume = " + volume);

        sc.close();

    }
}