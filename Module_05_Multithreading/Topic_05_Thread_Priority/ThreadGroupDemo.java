public class ThreadGroupDemo {
    public static void main(String[] args) {
        ThreadGroup group = new ThreadGroup("MyGroup");
        Thread t1 = new Thread(group, () -> System.out.println("Thread in group"));
        t1.start();
        System.out.println("Group name: " + group.getName());
    }
}
