public class LeapYearChecker {

    public static void main(String[] args) {
        int[] years = {2000, 2004, 1900, 2023, 2024};
        for (int year : years) {
            System.out.println(year + " is " + (isLeapYear(year) ? "a leap year." : "not a leap year."));
        }
    }

    private static boolean isLeapYear(int year) {
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    }
}
