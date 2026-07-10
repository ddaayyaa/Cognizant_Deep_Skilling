public class AbstractClassDemo extends EmployeeAbstract {
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
