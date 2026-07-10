public class GradeCalculator {

    public static void main(String[] args) {
        int score = 87;
        System.out.println("Score: " + score);
        System.out.println("Grade: " + calculateGrade(score));
    }

    private static String calculateGrade(int score) {
        if (score >= 90) {
            return "A";
        } else if (score >= 80) {
            return "B";
        } else if (score >= 70) {
            return "C";
        } else if (score >= 60) {
            return "D";
        } else {
            return "F";
        }
    }
}
