class Parent {
    public void parentMethod() {
        System.out.println("Parent method called.");
    }
}

class ChildOne extends Parent {
    public void childOneMethod() {
        System.out.println("ChildOne method called.");
    }
}

class ChildTwo extends Parent {
    public void childTwoMethod() {
        System.out.println("ChildTwo method called.");
    }
}

public class HierarchicalInheritance {
    public static void main(String[] args) {
        ChildOne first = new ChildOne();
        ChildTwo second = new ChildTwo();

        first.parentMethod();
        first.childOneMethod();
        second.parentMethod();
        second.childTwoMethod();
    }
}
