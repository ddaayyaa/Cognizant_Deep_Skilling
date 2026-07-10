public class EmployeeEncapsulation {
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
