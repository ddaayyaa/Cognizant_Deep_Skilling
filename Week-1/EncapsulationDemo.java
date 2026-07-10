class Employee {

    private int id;

    public void setId(int id) {
        this.id = id;
    }

    public int getId() {
        return id;
    }

}

public class EncapsulationDemo {

    public static void main(String[] args) {

        Employee e = new Employee();

        e.setId(5001);

        System.out.println(e.getId());

    }

}