import java.util.Scanner;

public class StudentInformationSystem {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Student Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Roll Number: ");
        int roll = sc.nextInt();

        System.out.print("Enter CGPA: ");
        double cgpa = sc.nextDouble();

        System.out.println("\n------ STUDENT DETAILS ------");
        System.out.println("Name : " + name);
        System.out.println("Roll Number : " + roll);
        System.out.println("CGPA : " + cgpa);

        if(cgpa >= 8.5){

            System.out.println("Grade : A");

        }else if(cgpa >= 7.0){

            System.out.println("Grade : B");

        }else{

            System.out.println("Grade : C");

        }

        sc.close();

    }
}