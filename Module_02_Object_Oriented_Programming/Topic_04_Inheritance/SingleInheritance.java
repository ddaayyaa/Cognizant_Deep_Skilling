class Animal {
    public void eat() {
        System.out.println("Animal is eating.");
    }
}

public class SingleInheritance extends Animal {
    public void bark() {
        System.out.println("Dog is barking.");
    }

    public static void main(String[] args) {
        SingleInheritance dog = new SingleInheritance();
        dog.eat();
        dog.bark();
    }
}
