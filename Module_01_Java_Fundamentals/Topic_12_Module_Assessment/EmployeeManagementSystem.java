public class EmployeeManagementSystem {

    public static void main(String[] args) {
        Employee employee = new Employee("E001", "Alice", 50000);
        employee.displayDetails();
    }
}

class Employee {
    private String id;
    private String name;
    private double salary;

    public Employee(String id, String name, double salary) {
        this.id = id;
        this.name = name;
        this.salary = salary;
    }

    public void displayDetails() {
        System.out.println("ID: " + id);
        System.out.println("Name: " + name);
        System.out.println("Salary: " + salary);
    }
}
