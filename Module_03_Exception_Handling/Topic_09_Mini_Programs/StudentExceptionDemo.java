public class StudentExceptionDemo {
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
