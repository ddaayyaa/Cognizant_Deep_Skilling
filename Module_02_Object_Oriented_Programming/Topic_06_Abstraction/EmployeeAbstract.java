public abstract class EmployeeAbstract {
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
