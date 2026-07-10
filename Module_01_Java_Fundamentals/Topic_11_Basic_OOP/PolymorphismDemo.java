public class PolymorphismDemo {

    public static void main(String[] args) {
        Creature creature = new DogCreature("Rex");
        creature.makeSound();

        creature = new CatCreature("Whiskers");
        creature.makeSound();

        creature = new BirdCreature("Tweety");
        creature.makeSound();

        printSound(new DogCreature("Max"));
    }

    private static void printSound(Creature creature) {
        creature.makeSound();
    }
}

abstract class Creature {
    private String name;

    public Creature(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public abstract void makeSound();
}

class DogCreature extends Creature {
    public DogCreature(String name) {
        super(name);
    }

    @Override
    public void makeSound() {
        System.out.println(getName() + " says: Woof!");
    }
}

class CatCreature extends Creature {
    public CatCreature(String name) {
        super(name);
    }

    @Override
    public void makeSound() {
        System.out.println(getName() + " says: Meow!");
    }
}

class BirdCreature extends Creature {
    public BirdCreature(String name) {
        super(name);
    }

    @Override
    public void makeSound() {
        System.out.println(getName() + " says: Tweet!");
    }
}
