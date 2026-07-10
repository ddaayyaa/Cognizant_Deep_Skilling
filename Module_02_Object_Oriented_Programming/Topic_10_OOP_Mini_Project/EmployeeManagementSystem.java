import java.util.ArrayList;
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
