from pathlib import Path

base = Path(r'c:\Users\ydaya\Desktop\Cognizant Deep Skilling\Module_02_Object_Oriented_Programming')
files = {
    'Topic_01_Classes_Objects/Book.java': '''public class Book {
    private String title;
    private String author;
    private String isbn;

    public Book() {
        this("Unknown", "Unknown", "0000000000");
    }

    public Book(String title, String author, String isbn) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
    }

    public void displayDetails() {
        System.out.println("Book Details:");
        System.out.println("Title : " + title);
        System.out.println("Author: " + author);
        System.out.println("ISBN  : " + isbn);
    }

    public static void main(String[] args) {
        Book defaultBook = new Book();
        Book javaBook = new Book("Effective Java", "Joshua Bloch", "9780134685991");

        defaultBook.displayDetails();
        System.out.println();
        javaBook.displayDetails();
    }
}
''',
    'Topic_01_Classes_Objects/Car.java': '''public class Car {
    private String model;
    private int year;
    private int speed;

    public Car(String model, int year) {
        this.model = model;
        this.year = year;
        this.speed = 0;
    }

    public void accelerate(int amount) {
        speed += amount;
        System.out.println(model + " accelerated to " + speed + " km/h");
    }

    public void brake(int amount) {
        speed = Math.max(0, speed - amount);
        System.out.println(model + " slowed down to " + speed + " km/h");
    }

    public void display() {
        System.out.println("Model: " + model);
        System.out.println("Year : " + year);
        System.out.println("Speed: " + speed + " km/h");
    }

    public static void main(String[] args) {
        Car car = new Car("Honda Civic", 2024);
        car.display();
        car.accelerate(40);
        car.brake(10);
    }
}
''',
    'Topic_01_Classes_Objects/Employee.java': '''public class Employee {
    private int id;
    private String name;
    private double salary;

    public Employee(int id, String name, double salary) {
        this.id = id;
        this.name = name;
        this.salary = salary;
    }

    public void displayEmployee() {
        System.out.println("Employee ID   : " + id);
        System.out.println("Employee Name : " + name);
        System.out.println("Salary        : " + salary);
    }

    public static void main(String[] args) {
        Employee employee = new Employee(101, "Rohit Sharma", 75000.0);
        employee.displayEmployee();
    }
}
''',
    'Topic_01_Classes_Objects/Student.java': '''public class Student {
    private String name;
    private int rollNumber;
    private String grade;

    public Student(String name, int rollNumber, String grade) {
        this.name = name;
        this.rollNumber = rollNumber;
        this.grade = grade;
    }

    public void showStudentInfo() {
        System.out.println("Student Name : " + name);
        System.out.println("Roll Number  : " + rollNumber);
        System.out.println("Grade        : " + grade);
    }

    public static void main(String[] args) {
        Student student = new Student("Simran", 12, "A");
        student.showStudentInfo();
    }
}
''',
    'Topic_02_Constructors/DefaultConstructor.java': '''public class DefaultConstructor {
    private String name;
    private int age;

    public DefaultConstructor() {
        this.name = "Default Student";
        this.age = 18;
    }

    public void showInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age : " + age);
    }

    public static void main(String[] args) {
        DefaultConstructor student = new DefaultConstructor();
        student.showInfo();
    }
}
''',
    'Topic_02_Constructors/ParameterizedConstructor.java': '''public class ParameterizedConstructor {
    private String name;
    private int age;

    public ParameterizedConstructor(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void display() {
        System.out.println("Name: " + name);
        System.out.println("Age : " + age);
    }

    public static void main(String[] args) {
        ParameterizedConstructor student = new ParameterizedConstructor("Priya", 21);
        student.display();
    }
}
''',
    'Topic_02_Constructors/CopyConstructor.java': '''public class CopyConstructor {
    private String title;
    private String author;

    public CopyConstructor(String title, String author) {
        this.title = title;
        this.author = author;
    }

    public CopyConstructor(CopyConstructor original) {
        this.title = original.title;
        this.author = original.author;
    }

    public void printDetails() {
        System.out.println("Title : " + title);
        System.out.println("Author: " + author);
    }

    public static void main(String[] args) {
        CopyConstructor firstBook = new CopyConstructor("Clean Code", "Robert C. Martin");
        CopyConstructor copiedBook = new CopyConstructor(firstBook);
        firstBook.printDetails();
        System.out.println();
        copiedBook.printDetails();
    }
}
''',
    'Topic_02_Constructors/ConstructorOverloading.java': '''public class ConstructorOverloading {
    private String name;
    private int age;
    private double salary;

    public ConstructorOverloading(String name) {
        this(name, 25, 45000.0);
    }

    public ConstructorOverloading(String name, int age) {
        this(name, age, 45000.0);
    }

    public ConstructorOverloading(String name, int age, double salary) {
        this.name = name;
        this.age = age;
        this.salary = salary;
    }

    public void showInfo() {
        System.out.println("Name  : " + name);
        System.out.println("Age   : " + age);
        System.out.println("Salary: " + salary);
    }

    public static void main(String[] args) {
        ConstructorOverloading employee1 = new ConstructorOverloading("Asha");
        ConstructorOverloading employee2 = new ConstructorOverloading("Vikram", 29);
        ConstructorOverloading employee3 = new ConstructorOverloading("Neel", 32, 82000.0);

        employee1.showInfo();
        System.out.println();
        employee2.showInfo();
        System.out.println();
        employee3.showInfo();
    }
}
''',
    'Topic_03_Encapsulation/BankAccount.java': '''public class BankAccount {
    private String accountNumber;
    private String accountHolder;
    private double balance;

    public BankAccount(String accountNumber, String accountHolder, double initialBalance) {
        this.accountNumber = accountNumber;
        this.accountHolder = accountHolder;
        this.balance = initialBalance;
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public String getAccountHolder() {
        return accountHolder;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println(amount + " deposited. New balance: " + balance);
        } else {
            System.out.println("Deposit amount must be positive.");
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println(amount + " withdrawn. Remaining balance: " + balance);
        } else {
            System.out.println("Invalid withdraw amount or insufficient funds.");
        }
    }

    public static void main(String[] args) {
        BankAccount account = new BankAccount("ACC12345", "Neha Patel", 1000.0);
        System.out.println("Account Holder: " + account.getAccountHolder());
        account.deposit(500.0);
        account.withdraw(200.0);
    }
}
''',
    'Topic_03_Encapsulation/EmployeeEncapsulation.java': '''public class EmployeeEncapsulation {
    private int id;
    private String name;
    private double salary;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        if (salary >= 0) {
            this.salary = salary;
        }
    }

    public void displayDetails() {
        System.out.println("Employee ID  : " + id);
        System.out.println("Employee Name: " + name);
        System.out.println("Salary       : " + salary);
    }

    public static void main(String[] args) {
        EmployeeEncapsulation emp = new EmployeeEncapsulation();
        emp.setId(301);
        emp.setName("Kavita Sharma");
        emp.setSalary(68000.0);
        emp.displayDetails();
    }
}
''',
    'Topic_03_Encapsulation/Person.java': '''public class Person {
    private String name;
    private int age;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if (age > 0) {
            this.age = age;
        }
    }

    public void display() {
        System.out.println("Name: " + name);
        System.out.println("Age : " + age);
    }

    public static void main(String[] args) {
        Person person = new Person();
        person.setName("Rahul");
        person.setAge(34);
        person.display();
    }
}
''',
    'Topic_03_Encapsulation/StudentEncapsulation.java': '''public class StudentEncapsulation {
    private int rollNumber;
    private String name;
    private double percentage;

    public int getRollNumber() {
        return rollNumber;
    }

    public void setRollNumber(int rollNumber) {
        this.rollNumber = rollNumber;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPercentage() {
        return percentage;
    }

    public void setPercentage(double percentage) {
        if (percentage >= 0 && percentage <= 100) {
            this.percentage = percentage;
        }
    }

    public void display() {
        System.out.println("Roll No   : " + rollNumber);
        System.out.println("Name      : " + name);
        System.out.println("Percentage: " + percentage);
    }

    public static void main(String[] args) {
        StudentEncapsulation student = new StudentEncapsulation();
        student.setRollNumber(23);
        student.setName("Priya");
        student.setPercentage(92.75);
        student.display();
    }
}
''',
    'Topic_04_Inheritance/SingleInheritance.java': '''class Animal {
    public void eat() {
        System.out.println("Animal is eating.");
    }
}

public class SingleInheritance extends Animal {
    public void bark() {
        System.out.println("Dog is barking.");
    }

    public static void main(String[] args) {
        SingleInheritance dog = new SingleInheritance();
        dog.eat();
        dog.bark();
    }
}
''',
    'Topic_04_Inheritance/MultilevelInheritance.java': '''class Vehicle {
    public void start() {
        System.out.println("Vehicle started.");
    }
}

class Car extends Vehicle {
    public void drive() {
        System.out.println("Car is driving.");
    }
}

public class MultilevelInheritance extends Car {
    public void display() {
        System.out.println("Multilevel inheritance example.");
    }

    public static void main(String[] args) {
        MultilevelInheritance demo = new MultilevelInheritance();
        demo.start();
        demo.drive();
        demo.display();
    }
}
''',
    'Topic_04_Inheritance/HierarchicalInheritance.java': '''class Parent {
    public void parentMethod() {
        System.out.println("Parent method called.");
    }
}

class ChildOne extends Parent {
    public void childOneMethod() {
        System.out.println("ChildOne method called.");
    }
}

class ChildTwo extends Parent {
    public void childTwoMethod() {
        System.out.println("ChildTwo method called.");
    }
}

public class HierarchicalInheritance {
    public static void main(String[] args) {
        ChildOne first = new ChildOne();
        ChildTwo second = new ChildTwo();

        first.parentMethod();
        first.childOneMethod();
        second.parentMethod();
        second.childTwoMethod();
    }
}
''',
    'Topic_04_Inheritance/HybridSimulation.java': '''interface Runner {
    void run();
}

class Animal {
    public void sleep() {
        System.out.println("Animal is sleeping.");
    }
}

public class HybridSimulation extends Animal implements Runner {
    @Override
    public void run() {
        System.out.println("HybridSimulation is running.");
    }

    public static void main(String[] args) {
        HybridSimulation simulation = new HybridSimulation();
        simulation.sleep();
        simulation.run();
    }
}
''',
    'Topic_05_Polymorphism/CompileTimePolymorphism.java': '''public class CompileTimePolymorphism {
    public int add(int a, int b) {
        return a + b;
    }

    public double add(double a, double b) {
        return a + b;
    }

    public int add(int a, int b, int c) {
        return a + b + c;
    }

    public static void main(String[] args) {
        CompileTimePolymorphism calculator = new CompileTimePolymorphism();
        System.out.println("Sum of two ints: " + calculator.add(5, 10));
        System.out.println("Sum of two doubles: " + calculator.add(3.5, 4.7));
        System.out.println("Sum of three ints: " + calculator.add(1, 2, 3));
    }
}
''',
    'Topic_05_Polymorphism/MethodOverloading.java': '''public class MethodOverloading {
    public void display(String message) {
        System.out.println("Message: " + message);
    }

    public void display(String message, int count) {
        System.out.println("Message: " + message + " (count = " + count + ")");
    }

    public void display(int number) {
        System.out.println("Number: " + number);
    }

    public static void main(String[] args) {
        MethodOverloading overloading = new MethodOverloading();
        overloading.display("Hello World");
        overloading.display("Hello World", 3);
        overloading.display(42);
    }
}
''',
    'Topic_05_Polymorphism/MethodOverriding.java': '''class ParentClass {
    public void show() {
        System.out.println("Parent show method.");
    }
}

public class MethodOverriding extends ParentClass {
    @Override
    public void show() {
        System.out.println("Child show method.");
    }

    public static void main(String[] args) {
        ParentClass object = new MethodOverriding();
        object.show();
    }
}
''',
    'Topic_05_Polymorphism/RuntimePolymorphism.java': '''class Animal {
    public void sound() {
        System.out.println("Some generic animal sound.");
    }
}

class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("Dog barks.");
    }
}

class Cat extends Animal {
    @Override
    public void sound() {
        System.out.println("Cat meows.");
    }
}

public class RuntimePolymorphism {
    public static void main(String[] args) {
        Animal animal1 = new Dog();
        Animal animal2 = new Cat();

        animal1.sound();
        animal2.sound();
    }
}
''',
    'Topic_06_Abstraction/Shape.java': '''public abstract class Shape {
    public abstract double area();

    public void displayArea() {
        System.out.println("Area: " + area());
    }
}
''',
    'Topic_06_Abstraction/Vehicle.java': '''public abstract class Vehicle {
    public abstract void start();

    public void fuelType() {
        System.out.println("Fuel type: Petrol or Diesel.");
    }
}
''',
    'Topic_06_Abstraction/EmployeeAbstract.java': '''public abstract class EmployeeAbstract {
    private String name;
    private int id;

    public EmployeeAbstract(String name, int id) {
        this.name = name;
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public int getId() {
        return id;
    }

    public abstract void displayRole();
}
''',
    'Topic_06_Abstraction/AbstractClassDemo.java': '''public class AbstractClassDemo extends EmployeeAbstract {
    private String role;

    public AbstractClassDemo(String name, int id, String role) {
        super(name, id);
        this.role = role;
    }

    @Override
    public void displayRole() {
        System.out.println("Employee Name: " + getName());
        System.out.println("Employee ID  : " + getId());
        System.out.println("Role         : " + role);
    }

    public static void main(String[] args) {
        AbstractClassDemo developer = new AbstractClassDemo("Rahul", 502, "Software Engineer");
        developer.displayRole();
    }
}
''',
    'Topic_07_Interface/BankInterface.java': '''public interface BankInterface {
    void withdraw(double amount);
    void deposit(double amount);
    double getBalance();
}
''',
    'Topic_07_Interface/CalculatorInterface.java': '''public interface CalculatorInterface {
    int add(int a, int b);
    int subtract(int a, int b);
    int multiply(int a, int b);
    double divide(int a, int b);
}
''',
    'Topic_07_Interface/InterfaceDemo.java': '''public class InterfaceDemo implements BankInterface {
    private double balance;

    @Override
    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println(amount + " withdrawn. Remaining balance: " + balance);
        } else {
            System.out.println("Invalid withdrawal.");
        }
    }

    @Override
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println(amount + " deposited. New balance: " + balance);
        } else {
            System.out.println("Invalid deposit.");
        }
    }

    @Override
    public double getBalance() {
        return balance;
    }

    public static void main(String[] args) {
        InterfaceDemo account = new InterfaceDemo();
        account.deposit(1200.0);
        account.withdraw(450.0);
        System.out.println("Final Balance: " + account.getBalance());
    }
}
''',
    'Topic_07_Interface/MultipleInterface.java': '''interface Printer {
    void print(String message);
}

interface Scanner {
    void scan();
}

public class MultipleInterface implements Printer, Scanner {
    @Override
    public void print(String message) {
        System.out.println("Printing: " + message);
    }

    @Override
    public void scan() {
        System.out.println("Scanning a document.");
    }

    public static void main(String[] args) {
        MultipleInterface device = new MultipleInterface();
        device.print("Hello Interface");
        device.scan();
    }
}
''',
    'Topic_08_Static_Final/StaticVariable.java': '''public class StaticVariable {
    private static int count = 0;

    public StaticVariable() {
        count++;
    }

    public static int getCount() {
        return count;
    }

    public static void main(String[] args) {
        new StaticVariable();
        new StaticVariable();
        new StaticVariable();
        System.out.println("Instances created: " + StaticVariable.getCount());
    }
}
''',
    'Topic_08_Static_Final/StaticMethod.java': '''public class StaticMethod {
    private static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        int result = StaticMethod.add(15, 20);
        System.out.println("Result: " + result);
    }
}
''',
    'Topic_08_Static_Final/FinalKeyword.java': '''public class FinalKeyword {
    private final String companyName = "ABC Technologies";

    public void displayCompany() {
        System.out.println("Company: " + companyName);
    }

    public static void main(String[] args) {
        FinalKeyword example = new FinalKeyword();
        example.displayCompany();
    }
}
''',
    'Topic_08_Static_Final/FinalMethod.java': '''public class FinalMethod {
    public final void showMessage() {
        System.out.println("This is a final method.");
    }
}
''',
    'Topic_09_This_Super/ThisKeyword.java': '''public class ThisKeyword {
    private String name;
    private int age;

    public ThisKeyword(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void display() {
        System.out.println("Name: " + this.name);
        System.out.println("Age : " + this.age);
    }

    public static void main(String[] args) {
        ThisKeyword student = new ThisKeyword("Ananya", 19);
        student.display();
    }
}
''',
    'Topic_09_This_Super/ThisConstructor.java': '''public class ThisConstructor {
    private String title;
    private String author;

    public ThisConstructor() {
        this("Unknown", "Unknown");
    }

    public ThisConstructor(String title, String author) {
        this.title = title;
        this.author = author;
    }

    public void display() {
        System.out.println("Title : " + title);
        System.out.println("Author: " + author);
    }

    public static void main(String[] args) {
        ThisConstructor book = new ThisConstructor("Java Basics", "Ravi");
        book.display();
    }
}
''',
    'Topic_09_This_Super/SuperKeyword.java': '''class ParentClass {
    protected String name = "Parent";

    public void showName() {
        System.out.println("Name from Parent: " + name);
    }
}

public class SuperKeyword extends ParentClass {
    protected String name = "Child";

    public void displayNames() {
        System.out.println("Name from Child: " + name);
        System.out.println("Name from Parent using super: " + super.name);
    }

    public static void main(String[] args) {
        SuperKeyword example = new SuperKeyword();
        example.displayNames();
    }
}
''',
    'Topic_09_This_Super/SuperConstructor.java': '''class Base {
    public Base(String message) {
        System.out.println("Base constructor: " + message);
    }
}

public class SuperConstructor extends Base {
    public SuperConstructor() {
        super("Hello from the base class");
        System.out.println("Derived constructor called.");
    }

    public static void main(String[] args) {
        new SuperConstructor();
    }
}
''',
    'Topic_10_OOP_Mini_Project/BankManagementSystem.java': '''import java.util.ArrayList;
import java.util.List;

class BankAccount {
    private String accountNumber;
    private String owner;
    private double balance;

    public BankAccount(String accountNumber, String owner, double balance) {
        this.accountNumber = accountNumber;
        this.owner = owner;
        this.balance = balance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
        }
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public String getOwner() {
        return owner;
    }

    public double getBalance() {
        return balance;
    }
}

public class BankManagementSystem {
    public static void main(String[] args) {
        List<BankAccount> accounts = new ArrayList<>();
        accounts.add(new BankAccount("B001", "Amit", 1500.0));
        accounts.add(new BankAccount("B002", "Rina", 2800.0));

        for (BankAccount account : accounts) {
            System.out.println("Account: " + account.getAccountNumber() + ", Owner: " + account.getOwner() + ", Balance: " + account.getBalance());
        }
    }
}
''',
    'Topic_10_OOP_Mini_Project/EmployeeManagementSystem.java': '''import java.util.ArrayList;
import java.util.List;

class EmployeeRecord {
    private int id;
    private String name;
    private String department;

    public EmployeeRecord(int id, String name, String department) {
        this.id = id;
        this.name = name;
        this.department = department;
    }

    public String getSummary() {
        return "ID: " + id + ", Name: " + name + ", Department: " + department;
    }
}

public class EmployeeManagementSystem {
    public static void main(String[] args) {
        List<EmployeeRecord> employees = new ArrayList<>();
        employees.add(new EmployeeRecord(101, "Priya", "HR"));
        employees.add(new EmployeeRecord(102, "Aman", "IT"));

        for (EmployeeRecord employee : employees) {
            System.out.println(employee.getSummary());
        }
    }
}
''',
    'Topic_10_OOP_Mini_Project/LibraryManagementSystem.java': '''import java.util.ArrayList;
import java.util.List;

class LibraryBook {
    private String title;
    private String author;
    private boolean available;

    public LibraryBook(String title, String author) {
        this.title = title;
        this.author = author;
        this.available = true;
    }

    public String getDetails() {
        return title + " by " + author + " (" + (available ? "Available" : "Not Available") + ")";
    }
}

public class LibraryManagementSystem {
    public static void main(String[] args) {
        List<LibraryBook> books = new ArrayList<>();
        books.add(new LibraryBook("The Alchemist", "Paulo Coelho"));
        books.add(new LibraryBook("To Kill a Mockingbird", "Harper Lee"));

        for (LibraryBook book : books) {
            System.out.println(book.getDetails());
        }
    }
}
''',
    'Topic_10_OOP_Mini_Project/StudentManagementSystem.java': '''import java.util.ArrayList;
import java.util.List;

class StudentRecord {
    private String name;
    private int rollNumber;
    private String course;

    public StudentRecord(String name, int rollNumber, String course) {
        this.name = name;
        this.rollNumber = rollNumber;
        this.course = course;
    }

    public String getSummary() {
        return "Roll: " + rollNumber + ", Name: " + name + ", Course: " + course;
    }
}

public class StudentManagementSystem {
    public static void main(String[] args) {
        List<StudentRecord> students = new ArrayList<>();
        students.add(new StudentRecord("Riya", 10, "Computer Science"));
        students.add(new StudentRecord("Arjun", 11, "Mathematics"));

        for (StudentRecord student : students) {
            System.out.println(student.getSummary());
        }
    }
}
'''
}

for relative_path, content in files.items():
    path = base / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')
print(f"Wrote {len(files)} Module_02 Java files.")
