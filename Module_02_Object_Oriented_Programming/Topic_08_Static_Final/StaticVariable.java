public class StaticVariable {
    private static int count = 0;

    public StaticVariable() {
        count++;
    }

    public static int getCount() {
        return count;
    }

    public static void main(String[] args) {
        new StaticVariable();
        new StaticVariable();
        new StaticVariable();
        System.out.println("Instances created: " + StaticVariable.getCount());
    }
}
