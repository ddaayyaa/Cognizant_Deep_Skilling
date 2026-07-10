public class ChatApplication {
    public static void main(String[] args) {
        Thread user1 = new Thread(() -> System.out.println("User1: Hello"));
        Thread user2 = new Thread(() -> System.out.println("User2: Hi"));
        user1.start();
        user2.start();
    }
}
