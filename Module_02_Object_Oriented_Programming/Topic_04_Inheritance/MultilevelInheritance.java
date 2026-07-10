class Vehicle {
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
