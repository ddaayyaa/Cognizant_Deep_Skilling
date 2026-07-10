public class StudentEncapsulation {
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
