public class GenericClass<T> {
    private T value;

    public GenericClass(T value) {
        this.value = value;
    }

    public T getValue() {
        return value;
    }

    public static void main(String[] args) {
        GenericClass<String> generic = new GenericClass<>("Test");
        System.out.println(generic.getValue());
    }
}
