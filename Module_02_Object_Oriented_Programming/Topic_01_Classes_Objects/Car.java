public class Car {
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
