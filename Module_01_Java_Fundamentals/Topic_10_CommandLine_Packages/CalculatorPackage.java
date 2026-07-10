public class CalculatorPackage {

    public static void main(String[] args) {
        if (args.length < 3) {
            System.out.println("Usage: java CalculatorPackage <num1> <operator> <num2>");
            return;
        }
        double num1 = Double.parseDouble(args[0]);
        String operator = args[1];
        double num2 = Double.parseDouble(args[2]);
        switch (operator) {
            case "+":
                System.out.println(num1 + num2);
                break;
            case "-":
                System.out.println(num1 - num2);
                break;
            case "*":
                System.out.println(num1 * num2);
                break;
            case "/":
                if (num2 == 0) {
                    System.out.println("Cannot divide by zero.");
                } else {
                    System.out.println(num1 / num2);
                }
                break;
            default:
                System.out.println("Invalid operator.");
        }
    }
}
