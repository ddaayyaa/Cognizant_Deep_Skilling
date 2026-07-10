public class ConstructorInjection {
    private final String value;

    public ConstructorInjection(String value) {
        this.value = value;
    }

    public static void main(String[] args) {
        ConstructorInjection demo = new ConstructorInjection("Injected value");
        System.out.println(demo.value);
    }
}
