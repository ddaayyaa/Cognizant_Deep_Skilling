$base = "Module_01_Java_Fundamentals"

New-Item -ItemType Directory -Force "$base\Topic_04_Scanner_User_Input" | Out-Null

@"
import java.util.Scanner;

public class StudentInput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Name: ");
        String name = sc.nextLine();
        System.out.print("Enter Age: ");
        int age = sc.nextInt();
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        sc.close();
    }
}
"@ | Set-Content "$base\Topic_04_Scanner_User_Input\StudentInput.java"

@"
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
"@ | Set-Content "$base\Topic_04_Scanner_User_Input\EmployeeInput.java"

@"
import java.util.Scanner;

public class BankAccountInput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Account Number: ");
        long account = sc.nextLong();
        System.out.print("Balance: ");
        double balance = sc.nextDouble();
        System.out.println("Account: " + account);
        System.out.println("Balance: " + balance);
        sc.close();
    }
}
"@ | Set-Content "$base\Topic_04_Scanner_User_Input\BankAccountInput.java"

@"
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
"@ | Set-Content "$base\Topic_04_Scanner_User_Input\ProductInput.java"

Write-Host "Topic 04 Created Successfully!"