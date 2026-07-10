$base = "Module_01_Java_Fundamentals"

New-Item -ItemType Directory -Force "$base\Topic_03_Operators" | Out-Null

@"
public class ArithmeticOperators {
    public static void main(String[] args) {
        int a = 10, b = 5;
        System.out.println("Addition = " + (a + b));
        System.out.println("Subtraction = " + (a - b));
        System.out.println("Multiplication = " + (a * b));
        System.out.println("Division = " + (a / b));
    }
}
"@ | Set-Content "$base\Topic_03_Operators\ArithmeticOperators.java"

@"
public class RelationalOperators {
    public static void main(String[] args) {
        int a = 10, b = 20;
        System.out.println(a > b);
        System.out.println(a < b);
        System.out.println(a == b);
        System.out.println(a != b);
    }
}
"@ | Set-Content "$base\Topic_03_Operators\RelationalOperators.java"

@"
public class LogicalOperators {
    public static void main(String[] args) {
        boolean x = true;
        boolean y = false;
        System.out.println(x && y);
        System.out.println(x || y);
        System.out.println(!x);
    }
}
"@ | Set-Content "$base\Topic_03_Operators\LogicalOperators.java"

@"
public class TernaryOperator {
    public static void main(String[] args) {
        int a = 15, b = 20;
        int max = (a > b) ? a : b;
        System.out.println("Largest = " + max);
    }
}
"@ | Set-Content "$base\Topic_03_Operators\TernaryOperator.java"

Write-Host "Topic 03 Created Successfully!"