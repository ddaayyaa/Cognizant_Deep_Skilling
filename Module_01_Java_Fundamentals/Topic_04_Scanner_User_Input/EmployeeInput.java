import java.util.Scanner;

public class EmployeeInput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Employee Name: ");
        String name = sc.nextLine();
        System.out.print("Salary: ");
        double salary = sc.nextDouble();
        System.out.println("Employee: " + name);
        System.out.println("Salary: " + salary);
        sc.close();
    }
}
