from pathlib import Path

base = Path(r'c:\Users\ydaya\Desktop\Cognizant Deep Skilling')

files = [
    # Module 03
    'Module_03_Exception_Handling/Topic_01_Try_Catch/ArithmeticExceptionDemo.java',
    'Module_03_Exception_Handling/Topic_01_Try_Catch/ArrayIndexExceptionDemo.java',
    'Module_03_Exception_Handling/Topic_01_Try_Catch/MultipleCatchDemo.java',
    'Module_03_Exception_Handling/Topic_01_Try_Catch/NullPointerExceptionDemo.java',
    'Module_03_Exception_Handling/Topic_02_Finally_Block/FinallyDemo.java',
    'Module_03_Exception_Handling/Topic_02_Finally_Block/FinallyWithException.java',
    'Module_03_Exception_Handling/Topic_02_Finally_Block/NestedFinallyDemo.java',
    'Module_03_Exception_Handling/Topic_02_Finally_Block/ReturnFinallyDemo.java',
    'Module_03_Exception_Handling/Topic_03_Throw_Throws/AgeValidation.java',
    'Module_03_Exception_Handling/Topic_03_Throw_Throws/CustomThrowDemo.java',
    'Module_03_Exception_Handling/Topic_03_Throw_Throws/ThrowDemo.java',
    'Module_03_Exception_Handling/Topic_03_Throw_Throws/ThrowsDemo.java',
    'Module_03_Exception_Handling/Topic_04_Custom_Exception/EmployeeException.java',
    'Module_03_Exception_Handling/Topic_04_Custom_Exception/InsufficientBalanceException.java',
    'Module_03_Exception_Handling/Topic_04_Custom_Exception/InvalidAgeException.java',
    'Module_03_Exception_Handling/Topic_04_Custom_Exception/StudentException.java',
    'Module_03_Exception_Handling/Topic_05_Exception_Hierarchy/CheckedExceptionDemo.java',
    'Module_03_Exception_Handling/Topic_05_Exception_Hierarchy/ClassNotFoundDemo.java',
    'Module_03_Exception_Handling/Topic_05_Exception_Hierarchy/IOExceptionDemo.java',
    'Module_03_Exception_Handling/Topic_05_Exception_Hierarchy/UncheckedExceptionDemo.java',
    'Module_03_Exception_Handling/Topic_06_Nested_Exception/NestedCatchDemo.java',
    'Module_03_Exception_Handling/Topic_06_Nested_Exception/NestedExceptionExample.java',
    'Module_03_Exception_Handling/Topic_06_Nested_Exception/NestedFinallyDemo.java',
    'Module_03_Exception_Handling/Topic_06_Nested_Exception/NestedTryDemo.java',
    'Module_03_Exception_Handling/Topic_07_User_Defined_Exception/BankException.java',
    'Module_03_Exception_Handling/Topic_07_User_Defined_Exception/PasswordException.java',
    'Module_03_Exception_Handling/Topic_07_User_Defined_Exception/SalaryException.java',
    'Module_03_Exception_Handling/Topic_07_User_Defined_Exception/VotingException.java',
    'Module_03_Exception_Handling/Topic_08_Best_Practices/ErrorMessages.java',
    'Module_03_Exception_Handling/Topic_08_Best_Practices/ExceptionLogging.java',
    'Module_03_Exception_Handling/Topic_08_Best_Practices/InputValidation.java',
    'Module_03_Exception_Handling/Topic_08_Best_Practices/ResourceHandling.java',
    'Module_03_Exception_Handling/Topic_09_Mini_Programs/ATMExceptionDemo.java',
    'Module_03_Exception_Handling/Topic_09_Mini_Programs/BankExceptionDemo.java',
    'Module_03_Exception_Handling/Topic_09_Mini_Programs/CalculatorExceptionDemo.java',
    'Module_03_Exception_Handling/Topic_09_Mini_Programs/StudentExceptionDemo.java',
    'Module_03_Exception_Handling/Topic_10_Assessment/Assessment1.java',
    'Module_03_Exception_Handling/Topic_10_Assessment/Assessment2.java',
    'Module_03_Exception_Handling/Topic_10_Assessment/Assessment3.java',
    'Module_03_Exception_Handling/Topic_10_Assessment/Assessment4.java',
    # Module 04
    'Module_04_Collections_Framework/Topic_01_ArrayList/ArrayListAdd.java',
    'Module_04_Collections_Framework/Topic_01_ArrayList/ArrayListRemove.java',
    'Module_04_Collections_Framework/Topic_01_ArrayList/ArrayListTraversal.java',
    'Module_04_Collections_Framework/Topic_01_ArrayList/ArrayListUpdate.java',
    'Module_04_Collections_Framework/Topic_02_LinkedList/LinkedListAdd.java',
    'Module_04_Collections_Framework/Topic_02_LinkedList/LinkedListRemove.java',
    'Module_04_Collections_Framework/Topic_02_LinkedList/LinkedListTraversal.java',
    'Module_04_Collections_Framework/Topic_02_LinkedList/LinkedListUpdate.java',
    'Module_04_Collections_Framework/Topic_03_HashSet/HashSetAdd.java',
    'Module_04_Collections_Framework/Topic_03_HashSet/HashSetDemo.java',
    'Module_04_Collections_Framework/Topic_03_HashSet/HashSetRemove.java',
    'Module_04_Collections_Framework/Topic_03_HashSet/HashSetTraversal.java',
    'Module_04_Collections_Framework/Topic_04_TreeSet/TreeSetDemo.java',
    'Module_04_Collections_Framework/Topic_04_TreeSet/TreeSetRemove.java',
    'Module_04_Collections_Framework/Topic_04_TreeSet/TreeSetSorting.java',
    'Module_04_Collections_Framework/Topic_04_TreeSet/TreeSetTraversal.java',
    'Module_04_Collections_Framework/Topic_05_HashMap/HashMapInsert.java',
    'Module_04_Collections_Framework/Topic_05_HashMap/HashMapRemove.java',
    'Module_04_Collections_Framework/Topic_05_HashMap/HashMapTraversal.java',
    'Module_04_Collections_Framework/Topic_05_HashMap/HashMapUpdate.java',
    'Module_04_Collections_Framework/Topic_06_TreeMap/TreeMapInsert.java',
    'Module_04_Collections_Framework/Topic_06_TreeMap/TreeMapRemove.java',
    'Module_04_Collections_Framework/Topic_06_TreeMap/TreeMapSorting.java',
    'Module_04_Collections_Framework/Topic_06_TreeMap/TreeMapTraversal.java',
    'Module_04_Collections_Framework/Topic_07_Iterator/IteratorDemo.java',
    'Module_04_Collections_Framework/Topic_07_Iterator/ListIteratorDemo.java',
    'Module_04_Collections_Framework/Topic_07_Iterator/MapIteratorDemo.java',
    'Module_04_Collections_Framework/Topic_07_Iterator/SetIteratorDemo.java',
    'Module_04_Collections_Framework/Topic_08_CollectionsUtility/FrequencyDemo.java',
    'Module_04_Collections_Framework/Topic_08_CollectionsUtility/ReverseDemo.java',
    'Module_04_Collections_Framework/Topic_08_CollectionsUtility/ShuffleDemo.java',
    'Module_04_Collections_Framework/Topic_08_CollectionsUtility/SortingDemo.java',
    'Module_04_Collections_Framework/Topic_09_GenericCollections/GenericClass.java',
    'Module_04_Collections_Framework/Topic_09_GenericCollections/GenericList.java',
    'Module_04_Collections_Framework/Topic_09_GenericCollections/GenericMap.java',
    'Module_04_Collections_Framework/Topic_09_GenericCollections/GenericSet.java',
    'Module_04_Collections_Framework/Topic_10_Assessment/BankManagement.java',
    'Module_04_Collections_Framework/Topic_10_Assessment/EmployeeManagement.java',
    'Module_04_Collections_Framework/Topic_10_Assessment/LibraryManagement.java',
    'Module_04_Collections_Framework/Topic_10_Assessment/StudentManagement.java',
    # Module 05
    'Module_05_Multithreading/Topic_01_Thread_Creation/MultipleThreads.java',
    'Module_05_Multithreading/Topic_01_Thread_Creation/RunnableInterfaceDemo.java',
    'Module_05_Multithreading/Topic_01_Thread_Creation/ThreadClassDemo.java',
    'Module_05_Multithreading/Topic_01_Thread_Creation/ThreadNaming.java',
    'Module_05_Multithreading/Topic_02_Thread_Lifecycle/ThreadJoin.java',
    'Module_05_Multithreading/Topic_02_Thread_Lifecycle/ThreadSleep.java',
    'Module_05_Multithreading/Topic_02_Thread_Lifecycle/ThreadStates.java',
    'Module_05_Multithreading/Topic_02_Thread_Lifecycle/ThreadYield.java',
    'Module_05_Multithreading/Topic_03_Synchronization/BankSynchronization.java',
    'Module_05_Multithreading/Topic_03_Synchronization/CounterSynchronization.java',
    'Module_05_Multithreading/Topic_03_Synchronization/SynchronizedBlock.java',
    'Module_05_Multithreading/Topic_03_Synchronization/SynchronizedMethod.java',
    'Module_05_Multithreading/Topic_04_InterThread_Communication/NotifyAllDemo.java',
    'Module_05_Multithreading/Topic_04_InterThread_Communication/ProducerConsumer.java',
    'Module_05_Multithreading/Topic_04_InterThread_Communication/SharedResource.java',
    'Module_05_Multithreading/Topic_04_InterThread_Communication/WaitNotifyDemo.java',
    'Module_05_Multithreading/Topic_05_Thread_Priority/CurrentThreadDemo.java',
    'Module_05_Multithreading/Topic_05_Thread_Priority/DaemonThread.java',
    'Module_05_Multithreading/Topic_05_Thread_Priority/PriorityDemo.java',
    'Module_05_Multithreading/Topic_05_Thread_Priority/ThreadGroupDemo.java',
    'Module_05_Multithreading/Topic_06_Executor_Framework/CachedThreadPool.java',
    'Module_05_Multithreading/Topic_06_Executor_Framework/ExecutorServiceDemo.java',
    'Module_05_Multithreading/Topic_06_Executor_Framework/FixedThreadPool.java',
    'Module_05_Multithreading/Topic_06_Executor_Framework/ScheduledExecutor.java',
    'Module_05_Multithreading/Topic_07_Callable_Future/CallableDemo.java',
    'Module_05_Multithreading/Topic_07_Callable_Future/FutureDemo.java',
    'Module_05_Multithreading/Topic_07_Callable_Future/FutureTaskDemo.java',
    'Module_05_Multithreading/Topic_07_Callable_Future/ResultFromThread.java',
    'Module_05_Multithreading/Topic_08_Concurrency_Utilities/CountDownLatchDemo.java',
    'Module_05_Multithreading/Topic_08_Concurrency_Utilities/CyclicBarrierDemo.java',
    'Module_05_Multithreading/Topic_08_Concurrency_Utilities/ReentrantLockDemo.java',
    'Module_05_Multithreading/Topic_08_Concurrency_Utilities/SemaphoreDemo.java',
    'Module_05_Multithreading/Topic_09_Mini_Programs/BankTransaction.java',
    'Module_05_Multithreading/Topic_09_Mini_Programs/ChatApplication.java',
    'Module_05_Multithreading/Topic_09_Mini_Programs/TicketBooking.java',
    'Module_05_Multithreading/Topic_09_Mini_Programs/TrafficSignalSimulation.java',
    'Module_05_Multithreading/Topic_10_Assessment/Assessment1.java',
    'Module_05_Multithreading/Topic_10_Assessment/Assessment2.java',
    'Module_05_Multithreading/Topic_10_Assessment/Assessment3.java',
    'Module_05_Multithreading/Topic_10_Assessment/Assessment4.java',
]


def generate_content(name: str) -> str:
    if name == 'ArithmeticExceptionDemo':
        return '''public class ArithmeticExceptionDemo {
    public static void main(String[] args) {
        try {
            int result = 10 / 0;
            System.out.println("Result: " + result);
        } catch (ArithmeticException ex) {
            System.out.println("ArithmeticException caught: " + ex.getMessage());
        }
    }
}
'''
    if name == 'ArrayIndexExceptionDemo':
        return '''public class ArrayIndexExceptionDemo {
    public static void main(String[] args) {
        try {
            int[] numbers = {1, 2, 3};
            System.out.println(numbers[5]);
        } catch (ArrayIndexOutOfBoundsException ex) {
            System.out.println("ArrayIndexOutOfBoundsException caught: " + ex.getMessage());
        }
    }
}
'''
    if name == 'MultipleCatchDemo':
        return '''public class MultipleCatchDemo {
    public static void main(String[] args) {
        try {
            int[] values = new int[2];
            values[5] = 10;
        } catch (ArrayIndexOutOfBoundsException ex) {
            System.out.println("Array error: " + ex.getMessage());
        } catch (Exception ex) {
            System.out.println("General exception: " + ex.getMessage());
        }
    }
}
'''
    if name == 'NullPointerExceptionDemo':
        return '''public class NullPointerExceptionDemo {
    public static void main(String[] args) {
        try {
            String text = null;
            System.out.println(text.length());
        } catch (NullPointerException ex) {
            System.out.println("NullPointerException caught: " + ex.getMessage());
        }
    }
}
'''
    if name == 'FinallyDemo':
        return '''public class FinallyDemo {
    public static void main(String[] args) {
        try {
            System.out.println("Inside try block.");
        } finally {
            System.out.println("Finally block always executes.");
        }
    }
}
'''
    if name == 'FinallyWithException':
        return '''public class FinallyWithException {
    public static void main(String[] args) {
        try {
            int value = Integer.parseInt("abc");
            System.out.println(value);
        } catch (NumberFormatException ex) {
            System.out.println("Caught NumberFormatException: " + ex.getMessage());
        } finally {
            System.out.println("Finally block execution completed.");
        }
    }
}
'''
    if name == 'NestedFinallyDemo':
        return '''public class NestedFinallyDemo {
    public static void main(String[] args) {
        try {
            try {
                System.out.println("Inner try block.");
                int result = 10 / 0;
            } finally {
                System.out.println("Inner finally block.");
            }
        } catch (ArithmeticException ex) {
            System.out.println("Outer catch: " + ex.getMessage());
        } finally {
            System.out.println("Outer finally block.");
        }
    }
}
'''
    if name == 'ReturnFinallyDemo':
        return '''public class ReturnFinallyDemo {
    public static void main(String[] args) {
        System.out.println(showMessage());
    }

    public static String showMessage() {
        try {
            return "Try Block";
        } finally {
            System.out.println("Finally block executed before return.");
        }
    }
}
'''
    if name == 'AgeValidation':
        return '''public class AgeValidation {
    public static void validateAge(int age) throws IllegalArgumentException {
        if (age < 18) {
            throw new IllegalArgumentException("Age must be at least 18.");
        }
    }

    public static void main(String[] args) {
        try {
            validateAge(16);
        } catch (IllegalArgumentException ex) {
            System.out.println("Validation failed: " + ex.getMessage());
        }
    }
}
'''
    if name == 'CustomThrowDemo':
        return '''public class CustomThrowDemo {
    public static void main(String[] args) {
        try {
            throw new Exception("Custom exception thrown explicitly.");
        } catch (Exception ex) {
            System.out.println("Exception caught: " + ex.getMessage());
        }
    }
}
'''
    if name == 'ThrowDemo':
        return '''public class ThrowDemo {
    public static void main(String[] args) {
        try {
            throw new RuntimeException("Explicit runtime exception.");
        } catch (RuntimeException ex) {
            System.out.println("Caught: " + ex.getMessage());
        }
    }
}
'''
    if name == 'ThrowsDemo':
        return '''public class ThrowsDemo {
    public static void riskyMethod() throws Exception {
        throw new Exception("This method throws an exception.");
    }

    public static void main(String[] args) {
        try {
            riskyMethod();
        } catch (Exception ex) {
            System.out.println("Handled exception: " + ex.getMessage());
        }
    }
}
'''
    if name == 'EmployeeException':
        return '''public class EmployeeException extends Exception {
    public EmployeeException(String message) {
        super(message);
    }
}
'''
    if name == 'InsufficientBalanceException':
        return '''public class InsufficientBalanceException extends Exception {
    public InsufficientBalanceException(String message) {
        super(message);
    }
}
'''
    if name == 'InvalidAgeException':
        return '''public class InvalidAgeException extends Exception {
    public InvalidAgeException(String message) {
        super(message);
    }
}
'''
    if name == 'StudentException':
        return '''public class StudentException extends Exception {
    public StudentException(String message) {
        super(message);
    }
}
'''
    if name == 'CheckedExceptionDemo':
        return '''import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class CheckedExceptionDemo {
    public static void main(String[] args) {
        try {
            File file = new File("missing.txt");
            new FileInputStream(file);
        } catch (FileNotFoundException ex) {
            System.out.println("Checked exception: " + ex.getMessage());
        }
    }
}
'''
    if name == 'ClassNotFoundDemo':
        return '''public class ClassNotFoundDemo {
    public static void main(String[] args) {
        try {
            Class.forName("com.example.DoesNotExist");
        } catch (ClassNotFoundException ex) {
            System.out.println("ClassNotFoundException: " + ex.getMessage());
        }
    }
}
'''
    if name == 'IOExceptionDemo':
        return '''import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

public class IOExceptionDemo {
    public static void main(String[] args) {
        try (FileInputStream stream = new FileInputStream(new File("missing.txt"))) {
            System.out.println(stream.read());
        } catch (IOException ex) {
            System.out.println("IOException caught: " + ex.getMessage());
        }
    }
}
'''
    if name == 'UncheckedExceptionDemo':
        return '''public class UncheckedExceptionDemo {
    public static void main(String[] args) {
        try {
            String text = null;
            text.length();
        } catch (NullPointerException ex) {
            System.out.println("Unchecked exception caught: " + ex.getMessage());
        }
    }
}
'''
    if name == 'NestedCatchDemo':
        return '''public class NestedCatchDemo {
    public static void main(String[] args) {
        try {
            int[] values = {1, 2, 3};
            try {
                System.out.println(values[5]);
            } catch (ArrayIndexOutOfBoundsException ex) {
                System.out.println("Inner catch: " + ex.getMessage());
            }
        } catch (Exception ex) {
            System.out.println("Outer catch: " + ex.getMessage());
        }
    }
}
'''
    if name == 'NestedExceptionExample':
        return '''public class NestedExceptionExample {
    public static void main(String[] args) {
        try {
            try {
                int result = 10 / 0;
                System.out.println(result);
            } catch (ArithmeticException ex) {
                System.out.println("Inner catch: " + ex.getMessage());
                throw ex;
            }
        } catch (ArithmeticException ex) {
            System.out.println("Outer catch: " + ex.getMessage());
        }
    }
}
'''
    if name == 'NestedFinallyDemo':
        return '''public class NestedFinallyDemo {
    public static void main(String[] args) {
        try {
            try {
                System.out.println("Inner try executing.");
            } finally {
                System.out.println("Inner finally executing.");
            }
        } finally {
            System.out.println("Outer finally executing.");
        }
    }
}
'''
    if name == 'NestedTryDemo':
        return '''public class NestedTryDemo {
    public static void main(String[] args) {
        try {
            try {
                int[] data = {1, 2, 3};
                System.out.println(data[5]);
            } catch (ArrayIndexOutOfBoundsException ex) {
                System.out.println("Inner catch: " + ex.getMessage());
            }
        } catch (Exception ex) {
            System.out.println("Outer catch: " + ex.getMessage());
        }
    }
}
'''
    if name == 'BankException':
        return '''public class BankException extends Exception {
    public BankException(String message) {
        super(message);
    }
}
'''
    if name == 'PasswordException':
        return '''public class PasswordException extends Exception {
    public PasswordException(String message) {
        super(message);
    }
}
'''
    if name == 'SalaryException':
        return '''public class SalaryException extends Exception {
    public SalaryException(String message) {
        super(message);
    }
}
'''
    if name == 'VotingException':
        return '''public class VotingException extends Exception {
    public VotingException(String message) {
        super(message);
    }
}
'''
    if name == 'ErrorMessages':
        return '''public class ErrorMessages {
    public static void main(String[] args) {
        try {
            String value = null;
            value.length();
        } catch (NullPointerException ex) {
            System.out.println("User-friendly error: input value is missing.");
            System.out.println("Technical detail: " + ex.getMessage());
        }
    }
}
'''
    if name == 'ExceptionLogging':
        return '''public class ExceptionLogging {
    public static void main(String[] args) {
        try {
            String result = "";
            int value = Integer.parseInt(result);
            System.out.println(value);
        } catch (NumberFormatException ex) {
            System.err.println("LOG: NumberFormatException occurred: " + ex.getMessage());
        }
    }
}
'''
    if name == 'InputValidation':
        return '''public class InputValidation {
    public static void main(String[] args) {
        String input = "";
        if (input == null || input.isEmpty()) {
            System.out.println("Input validation failed: value cannot be empty.");
        } else {
            System.out.println("Input is valid: " + input);
        }
    }
}
'''
    if name == 'ResourceHandling':
        return '''import java.io.BufferedReader;
import java.io.IOException;
import java.io.StringReader;

public class ResourceHandling {
    public static void main(String[] args) {
        try (BufferedReader reader = new BufferedReader(new StringReader("Hello"))) {
            System.out.println(reader.readLine());
        } catch (IOException ex) {
            System.out.println("IOException: " + ex.getMessage());
        }
    }
}
'''
    if name == 'ATMExceptionDemo':
        return '''public class ATMExceptionDemo {
    public static void main(String[] args) {
        double balance = 1000.0;
        double withdrawal = 1200.0;
        try {
            if (withdrawal > balance) {
                throw new IllegalArgumentException("Insufficient funds.");
            }
            balance -= withdrawal;
            System.out.println("Remaining balance: " + balance);
        } catch (IllegalArgumentException ex) {
            System.out.println("ATM error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'BankExceptionDemo':
        return '''public class BankExceptionDemo {
    public static void main(String[] args) {
        try {
            processTransaction(-50);
        } catch (IllegalArgumentException ex) {
            System.out.println("Transaction failed: " + ex.getMessage());
        }
    }

    private static void processTransaction(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Amount must be greater than zero.");
        }
        System.out.println("Transaction successful: " + amount);
    }
}
'''
    if name == 'CalculatorExceptionDemo':
        return '''public class CalculatorExceptionDemo {
    public static void main(String[] args) {
        try {
            int result = divide(10, 0);
            System.out.println("Result: " + result);
        } catch (ArithmeticException ex) {
            System.out.println("Cannot divide by zero: " + ex.getMessage());
        }
    }

    private static int divide(int a, int b) {
        return a / b;
    }
}
'''
    if name == 'StudentExceptionDemo':
        return '''public class StudentExceptionDemo {
    public static void main(String[] args) {
        try {
            validateGrade(120);
        } catch (IllegalArgumentException ex) {
            System.out.println("Student validation error: " + ex.getMessage());
        }
    }

    private static void validateGrade(int grade) {
        if (grade < 0 || grade > 100) {
            throw new IllegalArgumentException("Grade must be between 0 and 100.");
        }
    }
}
'''
    if name == 'Assessment1':
        return '''public class Assessment1 {
    public static int safeDivide(int a, int b) {
        try {
            return a / b;
        } catch (ArithmeticException ex) {
            return 0;
        }
    }

    public static void main(String[] args) {
        System.out.println(safeDivide(10, 0));
    }
}
'''
    if name == 'Assessment2':
        return '''public class Assessment2 {
    public static String getSafeLength(String input) {
        try {
            return String.valueOf(input.length());
        } catch (NullPointerException ex) {
            return "0";
        }
    }

    public static void main(String[] args) {
        System.out.println(getSafeLength(null));
    }
}
'''
    if name == 'Assessment3':
        return '''public class Assessment3 {
    public static void main(String[] args) {
        try {
            throw new Exception("Assessment exception");
        } catch (Exception ex) {
            System.out.println("Handled: " + ex.getMessage());
        }
    }
}
'''
    if name == 'Assessment4':
        return '''public class Assessment4 {
    public static void main(String[] args) {
        try {
            int[] values = {1, 2, 3};
            System.out.println(values[2]);
        } catch (ArrayIndexOutOfBoundsException ex) {
            System.out.println("Index error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'ArrayListAdd':
        return '''import java.util.ArrayList;

public class ArrayListAdd {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("Java");
        list.add("Python");
        System.out.println(list);
    }
}
'''
    if name == 'ArrayListRemove':
        return '''import java.util.ArrayList;

public class ArrayListRemove {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(10);
        list.add(20);
        list.remove(Integer.valueOf(10));
        System.out.println(list);
    }
}
'''
    if name == 'ArrayListTraversal':
        return '''import java.util.ArrayList;

public class ArrayListTraversal {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("A");
        list.add("B");
        for (String item : list) {
            System.out.println(item);
        }
    }
}
'''
    if name == 'ArrayListUpdate':
        return '''import java.util.ArrayList;

public class ArrayListUpdate {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("Old");
        list.set(0, "New");
        System.out.println(list);
    }
}
'''
    if name == 'LinkedListAdd':
        return '''import java.util.LinkedList;

public class LinkedListAdd {
    public static void main(String[] args) {
        LinkedList<String> list = new LinkedList<>();
        list.add("First");
        list.addLast("Last");
        System.out.println(list);
    }
}
'''
    if name == 'LinkedListRemove':
        return '''import java.util.LinkedList;

public class LinkedListRemove {
    public static void main(String[] args) {
        LinkedList<Integer> list = new LinkedList<>();
        list.add(1);
        list.add(2);
        list.removeFirst();
        System.out.println(list);
    }
}
'''
    if name == 'LinkedListTraversal':
        return '''import java.util.LinkedList;

public class LinkedListTraversal {
    public static void main(String[] args) {
        LinkedList<String> list = new LinkedList<>();
        list.add("X");
        list.add("Y");
        for (String item : list) {
            System.out.println(item);
        }
    }
}
'''
    if name == 'LinkedListUpdate':
        return '''import java.util.LinkedList;

public class LinkedListUpdate {
    public static void main(String[] args) {
        LinkedList<String> list = new LinkedList<>();
        list.add("Old");
        list.set(0, "Updated");
        System.out.println(list);
    }
}
'''
    if name == 'HashSetAdd':
        return '''import java.util.HashSet;

public class HashSetAdd {
    public static void main(String[] args) {
        HashSet<String> set = new HashSet<>();
        set.add("Apple");
        set.add("Banana");
        System.out.println(set);
    }
}
'''
    if name == 'HashSetDemo':
        return '''import java.util.HashSet;

public class HashSetDemo {
    public static void main(String[] args) {
        HashSet<Integer> set = new HashSet<>();
        set.add(1);
        set.add(2);
        set.add(2);
        System.out.println(set);
    }
}
'''
    if name == 'HashSetRemove':
        return '''import java.util.HashSet;

public class HashSetRemove {
    public static void main(String[] args) {
        HashSet<String> set = new HashSet<>();
        set.add("One");
        set.add("Two");
        set.remove("One");
        System.out.println(set);
    }
}
'''
    if name == 'HashSetTraversal':
        return '''import java.util.HashSet;

public class HashSetTraversal {
    public static void main(String[] args) {
        HashSet<String> set = new HashSet<>();
        set.add("Alpha");
        set.add("Beta");
        for (String item : set) {
            System.out.println(item);
        }
    }
}
'''
    if name == 'TreeSetDemo':
        return '''import java.util.TreeSet;

public class TreeSetDemo {
    public static void main(String[] args) {
        TreeSet<Integer> set = new TreeSet<>();
        set.add(5);
        set.add(1);
        set.add(3);
        System.out.println(set);
    }
}
'''
    if name == 'TreeSetRemove':
        return '''import java.util.TreeSet;

public class TreeSetRemove {
    public static void main(String[] args) {
        TreeSet<String> set = new TreeSet<>();
        set.add("A");
        set.add("B");
        set.remove("A");
        System.out.println(set);
    }
}
'''
    if name == 'TreeSetSorting':
        return '''import java.util.TreeSet;

public class TreeSetSorting {
    public static void main(String[] args) {
        TreeSet<String> set = new TreeSet<>();
        set.add("Zebra");
        set.add("Apple");
        set.add("Mango");
        System.out.println(set);
    }
}
'''
    if name == 'TreeSetTraversal':
        return '''import java.util.TreeSet;

public class TreeSetTraversal {
    public static void main(String[] args) {
        TreeSet<Integer> set = new TreeSet<>();
        set.add(10);
        set.add(20);
        for (Integer value : set) {
            System.out.println(value);
        }
    }
}
'''
    if name == 'HashMapInsert':
        return '''import java.util.HashMap;

public class HashMapInsert {
    public static void main(String[] args) {
        HashMap<Integer, String> map = new HashMap<>();
        map.put(1, "One");
        map.put(2, "Two");
        System.out.println(map);
    }
}
'''
    if name == 'HashMapRemove':
        return '''import java.util.HashMap;

public class HashMapRemove {
    public static void main(String[] args) {
        HashMap<Integer, String> map = new HashMap<>();
        map.put(1, "One");
        map.remove(1);
        System.out.println(map);
    }
}
'''
    if name == 'HashMapTraversal':
        return '''import java.util.HashMap;

public class HashMapTraversal {
    public static void main(String[] args) {
        HashMap<String, Integer> map = new HashMap<>();
        map.put("A", 1);
        map.put("B", 2);
        for (String key : map.keySet()) {
            System.out.println(key + " -> " + map.get(key));
        }
    }
}
'''
    if name == 'HashMapUpdate':
        return '''import java.util.HashMap;

public class HashMapUpdate {
    public static void main(String[] args) {
        HashMap<Integer, String> map = new HashMap<>();
        map.put(1, "One");
        map.put(1, "Uno");
        System.out.println(map);
    }
}
'''
    if name == 'TreeMapInsert':
        return '''import java.util.TreeMap;

public class TreeMapInsert {
    public static void main(String[] args) {
        TreeMap<Integer, String> map = new TreeMap<>();
        map.put(3, "Three");
        map.put(1, "One");
        System.out.println(map);
    }
}
'''
    if name == 'TreeMapRemove':
        return '''import java.util.TreeMap;

public class TreeMapRemove {
    public static void main(String[] args) {
        TreeMap<String, Integer> map = new TreeMap<>();
        map.put("A", 1);
        map.remove("A");
        System.out.println(map);
    }
}
'''
    if name == 'TreeMapSorting':
        return '''import java.util.TreeMap;

public class TreeMapSorting {
    public static void main(String[] args) {
        TreeMap<Integer, String> map = new TreeMap<>();
        map.put(5, "Five");
        map.put(2, "Two");
        System.out.println(map);
    }
}
'''
    if name == 'TreeMapTraversal':
        return '''import java.util.TreeMap;

public class TreeMapTraversal {
    public static void main(String[] args) {
        TreeMap<String, Integer> map = new TreeMap<>();
        map.put("C", 3);
        map.put("A", 1);
        for (String key : map.keySet()) {
            System.out.println(key + " -> " + map.get(key));
        }
    }
}
'''
    if name == 'IteratorDemo':
        return '''import java.util.ArrayList;
import java.util.Iterator;

public class IteratorDemo {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("Java");
        list.add("C#");
        Iterator<String> iterator = list.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }
}
'''
    if name == 'ListIteratorDemo':
        return '''import java.util.ArrayList;
import java.util.ListIterator;

public class ListIteratorDemo {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("One");
        list.add("Two");
        ListIterator<String> iterator = list.listIterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }
}
'''
    if name == 'MapIteratorDemo':
        return '''import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class MapIteratorDemo {
    public static void main(String[] args) {
        HashMap<String, Integer> map = new HashMap<>();
        map.put("A", 1);
        map.put("B", 2);
        Iterator<Map.Entry<String, Integer>> iterator = map.entrySet().iterator();
        while (iterator.hasNext()) {
            Map.Entry<String, Integer> entry = iterator.next();
            System.out.println(entry.getKey() + " -> " + entry.getValue());
        }
    }
}
'''
    if name == 'SetIteratorDemo':
        return '''import java.util.HashSet;
import java.util.Iterator;

public class SetIteratorDemo {
    public static void main(String[] args) {
        HashSet<String> set = new HashSet<>();
        set.add("One");
        set.add("Two");
        Iterator<String> iterator = set.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }
}
'''
    if name == 'FrequencyDemo':
        return '''import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class FrequencyDemo {
    public static void main(String[] args) {
        List<String> items = new ArrayList<>();
        items.add("apple");
        items.add("banana");
        items.add("apple");
        System.out.println("Frequency of apple: " + Collections.frequency(items, "apple"));
    }
}
'''
    if name == 'ReverseDemo':
        return '''import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ReverseDemo {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
        Collections.reverse(numbers);
        System.out.println(numbers);
    }
}
'''
    if name == 'ShuffleDemo':
        return '''import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ShuffleDemo {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
        Collections.shuffle(numbers);
        System.out.println(numbers);
    }
}
'''
    if name == 'SortingDemo':
        return '''import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class SortingDemo {
    public static void main(String[] args) {
        List<String> items = new ArrayList<>();
        items.add("Banana");
        items.add("Apple");
        Collections.sort(items);
        System.out.println(items);
    }
}
'''
    if name == 'GenericClass':
        return '''public class GenericClass<T> {
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
'''
    if name == 'GenericList':
        return '''import java.util.ArrayList;
import java.util.List;

public class GenericList {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("One");
        System.out.println(list.get(0));
    }
}
'''
    if name == 'GenericMap':
        return '''import java.util.HashMap;
import java.util.Map;

public class GenericMap {
    public static void main(String[] args) {
        Map<String, Integer> map = new HashMap<>();
        map.put("A", 1);
        System.out.println(map.get("A"));
    }
}
'''
    if name == 'GenericSet':
        return '''import java.util.HashSet;
import java.util.Set;

public class GenericSet {
    public static void main(String[] args) {
        Set<String> set = new HashSet<>();
        set.add("Hello");
        System.out.println(set.contains("Hello"));
    }
}
'''
    if name == 'BankManagement':
        return '''import java.util.HashMap;
import java.util.Map;

public class BankManagement {
    public static void main(String[] args) {
        Map<String, Double> accounts = new HashMap<>();
        accounts.put("A101", 2000.0);
        System.out.println(accounts);
    }
}
'''
    if name == 'EmployeeManagement':
        return '''import java.util.ArrayList;
import java.util.List;

public class EmployeeManagement {
    public static void main(String[] args) {
        List<String> employees = new ArrayList<>();
        employees.add("Amit");
        employees.add("Neha");
        System.out.println(employees);
    }
}
'''
    if name == 'LibraryManagement':
        return '''import java.util.ArrayList;
import java.util.List;

public class LibraryManagement {
    public static void main(String[] args) {
        List<String> books = new ArrayList<>();
        books.add("The Alchemist");
        books.add("1984");
        System.out.println(books);
    }
}
'''
    if name == 'StudentManagement':
        return '''import java.util.HashMap;
import java.util.Map;

public class StudentManagement {
    public static void main(String[] args) {
        Map<Integer, String> students = new HashMap<>();
        students.put(1, "Ravi");
        students.put(2, "Pooja");
        System.out.println(students);
    }
}
'''
    if name == 'MultipleThreads':
        return '''public class MultipleThreads {
    public static void main(String[] args) {
        Thread thread1 = new Thread(() -> System.out.println("Thread 1 running"));
        Thread thread2 = new Thread(() -> System.out.println("Thread 2 running"));
        thread1.start();
        thread2.start();
    }
}
'''
    if name == 'RunnableInterfaceDemo':
        return '''public class RunnableInterfaceDemo {
    public static void main(String[] args) {
        Runnable task = () -> System.out.println("Runnable task executed");
        Thread thread = new Thread(task);
        thread.start();
    }
}
'''
    if name == 'ThreadClassDemo':
        return '''public class ThreadClassDemo extends Thread {
    @Override
    public void run() {
        System.out.println("ThreadClassDemo is running");
    }

    public static void main(String[] args) {
        new ThreadClassDemo().start();
    }
}
'''
    if name == 'ThreadNaming':
        return '''public class ThreadNaming {
    public static void main(String[] args) {
        Thread thread = new Thread(() -> System.out.println("Named thread running"));
        thread.setName("WorkerThread");
        thread.start();
        System.out.println("Thread name: " + thread.getName());
    }
}
'''
    if name == 'ThreadJoin':
        return '''public class ThreadJoin {
    public static void main(String[] args) {
        Thread thread = new Thread(() -> {
            try {
                Thread.sleep(500);
                System.out.println("Joined thread finished");
            } catch (InterruptedException ex) {
                Thread.currentThread().interrupt();
            }
        });
        thread.start();
        try {
            thread.join();
            System.out.println("Main thread resumed after join");
        } catch (InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
    }
}
'''
    if name == 'ThreadSleep':
        return '''public class ThreadSleep {
    public static void main(String[] args) {
        try {
            System.out.println("Sleeping...");
            Thread.sleep(500);
            System.out.println("Woke up");
        } catch (InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
    }
}
'''
    if name == 'ThreadStates':
        return '''public class ThreadStates {
    public static void main(String[] args) throws InterruptedException {
        Thread thread = new Thread(() -> {
            try {
                Thread.sleep(100);
            } catch (InterruptedException ex) {
                Thread.currentThread().interrupt();
            }
        });
        System.out.println("State before start: " + thread.getState());
        thread.start();
        System.out.println("State after start: " + thread.getState());
        thread.join();
        System.out.println("State after join: " + thread.getState());
    }
}
'''
    if name == 'ThreadYield':
        return '''public class ThreadYield {
    public static void main(String[] args) {
        Runnable task = () -> {
            System.out.println(Thread.currentThread().getName() + " before yield");
            Thread.yield();
            System.out.println(Thread.currentThread().getName() + " after yield");
        };
        new Thread(task, "Thread-A").start();
        new Thread(task, "Thread-B").start();
    }
}
'''
    if name == 'BankSynchronization':
        return '''public class BankSynchronization {
    private static class Account {
        private double balance = 1000.0;

        public synchronized void withdraw(double amount) {
            if (amount <= balance) {
                balance -= amount;
                System.out.println("Withdrawn: " + amount + ", remaining: " + balance);
            }
        }
    }

    public static void main(String[] args) {
        Account account = new Account();
        Runnable task = () -> account.withdraw(500);
        new Thread(task).start();
        new Thread(task).start();
    }
}
'''
    if name == 'CounterSynchronization':
        return '''public class CounterSynchronization {
    private static class Counter {
        private int count;

        public synchronized void increment() {
            count++;
        }

        public int getCount() {
            return count;
        }
    }

    public static void main(String[] args) throws InterruptedException {
        Counter counter = new Counter();
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                counter.increment();
            }
        });
        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                counter.increment();
            }
        });
        t1.start();
        t2.start();
        t1.join();
        t2.join();
        System.out.println("Count: " + counter.getCount());
    }
}
'''
    if name == 'SynchronizedBlock':
        return '''public class SynchronizedBlock {
    private final Object lock = new Object();
    private int count;

    public void increment() {
        synchronized (lock) {
            count++;
        }
    }

    public static void main(String[] args) throws InterruptedException {
        SynchronizedBlock demo = new SynchronizedBlock();
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) demo.increment();
        });
        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) demo.increment();
        });
        t1.start();
        t2.start();
        t1.join();
        t2.join();
        System.out.println("Count: " + demo.count);
    }
}
'''
    if name == 'SynchronizedMethod':
        return '''public class SynchronizedMethod {
    private int count;

    public synchronized void increment() {
        count++;
    }

    public static void main(String[] args) throws InterruptedException {
        SynchronizedMethod demo = new SynchronizedMethod();
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) demo.increment();
        });
        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) demo.increment();
        });
        t1.start();
        t2.start();
        t1.join();
        t2.join();
        System.out.println("Count: " + demo.count);
    }
}
'''
    if name == 'NotifyAllDemo':
        return '''public class NotifyAllDemo {
    private static class MessageQueue {
        public synchronized void produce() throws InterruptedException {
            System.out.println("Producer producing");
            wait();
        }

        public synchronized void consume() {
            System.out.println("Consumer notifying all");
            notifyAll();
        }
    }

    public static void main(String[] args) throws InterruptedException {
        MessageQueue queue = new MessageQueue();
        Thread t1 = new Thread(() -> {
            try {
                queue.produce();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });
        t1.start();
        Thread.sleep(100);
        queue.consume();
    }
}
'''
    if name == 'ProducerConsumer':
        return '''import java.util.LinkedList;
import java.util.Queue;

public class ProducerConsumer {
    public static void main(String[] args) {
        Queue<Integer> buffer = new LinkedList<>();
        int capacity = 5;

        Runnable producer = () -> {
            int value = 0;
            while (value < 5) {
                synchronized (buffer) {
                    while (buffer.size() == capacity) {
                        try {
                            buffer.wait();
                        } catch (InterruptedException ex) {
                            Thread.currentThread().interrupt();
                        }
                    }
                    buffer.add(value);
                    System.out.println("Produced " + value);
                    buffer.notify();
                }
                value++;
            }
        };
        Runnable consumer = () -> {
            while (true) {
                synchronized (buffer) {
                    while (buffer.isEmpty()) {
                        try {
                            buffer.wait();
                        } catch (InterruptedException ex) {
                            Thread.currentThread().interrupt();
                        }
                    }
                    int removed = buffer.poll();
                    System.out.println("Consumed " + removed);
                    buffer.notify();
                    if (removed == 4) {
                        break;
                    }
                }
            }
        };
        new Thread(producer).start();
        new Thread(consumer).start();
    }
}
'''
    if name == 'SharedResource':
        return '''public class SharedResource {
    private int value;

    public synchronized void setValue(int value) {
        this.value = value;
    }

    public synchronized int getValue() {
        return value;
    }

    public static void main(String[] args) {
        SharedResource resource = new SharedResource();
        Thread writer = new Thread(() -> resource.setValue(10));
        Thread reader = new Thread(() -> System.out.println(resource.getValue()));
        writer.start();
        reader.start();
    }
}
'''
    if name == 'WaitNotifyDemo':
        return '''public class WaitNotifyDemo {
    private static class Signal {
        public synchronized void doWait() {
            try {
                wait();
                System.out.println("Notified");
            } catch (InterruptedException ex) {
                Thread.currentThread().interrupt();
            }
        }

        public synchronized void doNotify() {
            notify();
        }
    }

    public static void main(String[] args) throws InterruptedException {
        Signal signal = new Signal();
        Thread waiter = new Thread(signal::doWait);
        waiter.start();
        Thread.sleep(100);
        synchronized (signal) {
            signal.doNotify();
        }
    }
}
'''
    if name == 'CurrentThreadDemo':
        return '''public class CurrentThreadDemo {
    public static void main(String[] args) {
        System.out.println("Current thread: " + Thread.currentThread().getName());
    }
}
'''
    if name == 'DaemonThread':
        return '''public class DaemonThread {
    public static void main(String[] args) {
        Thread daemon = new Thread(() -> {
            while (true) {
                System.out.println("Daemon thread running");
                try {
                    Thread.sleep(200);
                } catch (InterruptedException ex) {
                    Thread.currentThread().interrupt();
                }
            }
        });
        daemon.setDaemon(true);
        daemon.start();
        System.out.println("Main thread ends");
    }
}
'''
    if name == 'PriorityDemo':
        return '''public class PriorityDemo {
    public static void main(String[] args) {
        Thread high = new Thread(() -> System.out.println("High priority thread"));
        Thread low = new Thread(() -> System.out.println("Low priority thread"));
        high.setPriority(Thread.MAX_PRIORITY);
        low.setPriority(Thread.MIN_PRIORITY);
        low.start();
        high.start();
    }
}
'''
    if name == 'ThreadGroupDemo':
        return '''public class ThreadGroupDemo {
    public static void main(String[] args) {
        ThreadGroup group = new ThreadGroup("MyGroup");
        Thread t1 = new Thread(group, () -> System.out.println("Thread in group"));
        t1.start();
        System.out.println("Group name: " + group.getName());
    }
}
'''
    if name == 'CachedThreadPool':
        return '''import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class CachedThreadPool {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newCachedThreadPool();
        executor.submit(() -> System.out.println("Cached pool task"));
        executor.shutdown();
    }
}
'''
    if name == 'ExecutorServiceDemo':
        return '''import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ExecutorServiceDemo {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(2);
        executor.submit(() -> System.out.println("Executor task 1"));
        executor.submit(() -> System.out.println("Executor task 2"));
        executor.shutdown();
    }
}
'''
    if name == 'FixedThreadPool':
        return '''import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class FixedThreadPool {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(3);
        for (int i = 0; i < 3; i++) {
            executor.submit(() -> System.out.println("Fixed pool task"));
        }
        executor.shutdown();
    }
}
'''
    if name == 'ScheduledExecutor':
        return '''import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class ScheduledExecutor {
    public static void main(String[] args) {
        ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(1);
        scheduler.schedule(() -> System.out.println("Scheduled task executed"), 1, TimeUnit.SECONDS);
        scheduler.shutdown();
    }
}
'''
    if name == 'CallableDemo':
        return '''import java.util.concurrent.Callable;

public class CallableDemo {
    public static void main(String[] args) throws Exception {
        Callable<String> task = () -> "Callable result";
        System.out.println(task.call());
    }
}
'''
    if name == 'FutureDemo':
        return '''import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class FutureDemo {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newSingleThreadExecutor();
        Future<Integer> future = executor.submit(() -> 5 + 5);
        System.out.println("Result: " + future.get());
        executor.shutdown();
    }
}
'''
    if name == 'FutureTaskDemo':
        return '''import java.util.concurrent.FutureTask;

public class FutureTaskDemo {
    public static void main(String[] args) throws Exception {
        FutureTask<Integer> task = new FutureTask<>(() -> 20);
        new Thread(task).start();
        System.out.println("FutureTask result: " + task.get());
    }
}
'''
    if name == 'ResultFromThread':
        return '''import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class ResultFromThread {
    public static void main(String[] args) throws InterruptedException, ExecutionException {
        ExecutorService executor = Executors.newSingleThreadExecutor();
        Callable<String> task = () -> "Result from callable";
        Future<String> future = executor.submit(task);
        System.out.println(future.get());
        executor.shutdown();
    }
}
'''
    if name == 'CountDownLatchDemo':
        return '''import java.util.concurrent.CountDownLatch;

public class CountDownLatchDemo {
    public static void main(String[] args) throws InterruptedException {
        CountDownLatch latch = new CountDownLatch(2);
        Runnable worker = () -> {
            System.out.println(Thread.currentThread().getName() + " done");
            latch.countDown();
        };
        new Thread(worker).start();
        new Thread(worker).start();
        latch.await();
        System.out.println("All workers finished");
    }
}
'''
    if name == 'CyclicBarrierDemo':
        return '''import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CyclicBarrier;

public class CyclicBarrierDemo {
    public static void main(String[] args) throws InterruptedException, BrokenBarrierException {
        CyclicBarrier barrier = new CyclicBarrier(2, () -> System.out.println("Barrier reached"));
        Runnable task = () -> {
            try {
                System.out.println(Thread.currentThread().getName() + " waiting");
                barrier.await();
            } catch (Exception ex) {
                Thread.currentThread().interrupt();
            }
        };
        new Thread(task).start();
        new Thread(task).start();
    }
}
'''
    if name == 'ReentrantLockDemo':
        return '''import java.util.concurrent.locks.ReentrantLock;

public class ReentrantLockDemo {
    public static void main(String[] args) {
        ReentrantLock lock = new ReentrantLock();
        Runnable task = () -> {
            lock.lock();
            try {
                System.out.println(Thread.currentThread().getName() + " acquired lock");
            } finally {
                lock.unlock();
            }
        };
        new Thread(task).start();
        new Thread(task).start();
    }
}
'''
    if name == 'SemaphoreDemo':
        return '''import java.util.concurrent.Semaphore;

public class SemaphoreDemo {
    public static void main(String[] args) {
        Semaphore semaphore = new Semaphore(1);
        Runnable task = () -> {
            try {
                semaphore.acquire();
                System.out.println(Thread.currentThread().getName() + " acquired permit");
            } catch (InterruptedException ex) {
                Thread.currentThread().interrupt();
            } finally {
                semaphore.release();
            }
        };
        new Thread(task).start();
        new Thread(task).start();
    }
}
'''
    if name == 'BankTransaction':
        return '''public class BankTransaction {
    private static class Account {
        private double balance = 1000.0;

        public synchronized void deposit(double amount) {
            balance += amount;
            System.out.println("Deposited: " + amount);
        }

        public synchronized void withdraw(double amount) {
            if (amount <= balance) {
                balance -= amount;
                System.out.println("Withdrawn: " + amount);
            }
        }
    }

    public static void main(String[] args) {
        Account account = new Account();
        Thread t1 = new Thread(() -> account.deposit(200));
        Thread t2 = new Thread(() -> account.withdraw(150));
        t1.start();
        t2.start();
    }
}
'''
    if name == 'ChatApplication':
        return '''public class ChatApplication {
    public static void main(String[] args) {
        Thread user1 = new Thread(() -> System.out.println("User1: Hello"));
        Thread user2 = new Thread(() -> System.out.println("User2: Hi"));
        user1.start();
        user2.start();
    }
}
'''
    if name == 'TicketBooking':
        return '''public class TicketBooking {
    private static int tickets = 5;

    public static synchronized void bookTicket() {
        if (tickets > 0) {
            System.out.println("Ticket booked, remaining: " + (--tickets));
        }
    }

    public static void main(String[] args) {
        Runnable task = TicketBooking::bookTicket;
        new Thread(task).start();
        new Thread(task).start();
    }
}
'''
    if name == 'TrafficSignalSimulation':
        return '''public class TrafficSignalSimulation {
    public static void main(String[] args) {
        Thread northSouth = new Thread(() -> System.out.println("North-South green"));
        Thread eastWest = new Thread(() -> System.out.println("East-West green"));
        northSouth.start();
        eastWest.start();
    }
}
'''
    return f'public class {name} {{\n    public static void main(String[] args) {{\n        System.out.println("{name} Program");\n    }}\n}}\n'

for rel in files:
    path = base / rel
    name = path.stem
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(generate_content(name), encoding='utf-8')

print(f'Wrote {len(files)} files to module 3, 4, and 5.')
