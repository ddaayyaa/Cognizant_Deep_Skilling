public class TrafficSignalSimulation {
    public static void main(String[] args) {
        Thread northSouth = new Thread(() -> System.out.println("North-South green"));
        Thread eastWest = new Thread(() -> System.out.println("East-West green"));
        northSouth.start();
        eastWest.start();
    }
}
