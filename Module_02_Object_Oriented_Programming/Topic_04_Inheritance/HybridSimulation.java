interface Runner {
    void run();
}

class Animal {
    public void sleep() {
        System.out.println("Animal is sleeping.");
    }
}

public class HybridSimulation extends Animal implements Runner {
    @Override
    public void run() {
        System.out.println("HybridSimulation is running.");
    }

    public static void main(String[] args) {
        HybridSimulation simulation = new HybridSimulation();
        simulation.sleep();
        simulation.run();
    }
}
