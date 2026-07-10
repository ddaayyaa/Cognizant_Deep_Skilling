public class SetterInjection {
    private String value;

    public void setValue(String value) {
        this.value = value;
    }

    public static void main(String[] args) {
        SetterInjection demo = new SetterInjection();
        demo.setValue("Injected value");
        System.out.println(demo.value);
    }
}
