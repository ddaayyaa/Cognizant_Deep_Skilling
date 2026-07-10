public class InheritanceDemo {

    public static void main(String[] args) {
        AnimalBase animal = new AnimalBase("Generic Animal");
        animal.eat();

        Dog dog = new Dog("Buddy");
        dog.eat();
        dog.bark();
    }
}

class AnimalBase {
    private String name;

    public AnimalBase(String name) {
        this.name = name;
    }

    public void eat() {
        System.out.println(name + " is eating.");
    }
}

class Dog extends AnimalBase {
    public Dog(String name) {
        super(name);
    }

    public void bark() {
        System.out.println("Dog is barking.");
    }
}
