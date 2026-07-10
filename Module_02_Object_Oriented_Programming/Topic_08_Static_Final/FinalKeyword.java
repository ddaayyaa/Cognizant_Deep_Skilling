public class FinalKeyword {
    private final String companyName = "ABC Technologies";

    public void displayCompany() {
        System.out.println("Company: " + companyName);
    }

    public static void main(String[] args) {
        FinalKeyword example = new FinalKeyword();
        example.displayCompany();
    }
}
