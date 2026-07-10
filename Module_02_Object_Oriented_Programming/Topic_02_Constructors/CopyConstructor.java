public class CopyConstructor {
    private String title;
    private String author;

    public CopyConstructor(String title, String author) {
        this.title = title;
        this.author = author;
    }

    public CopyConstructor(CopyConstructor original) {
        this.title = original.title;
        this.author = original.author;
    }

    public void printDetails() {
        System.out.println("Title : " + title);
        System.out.println("Author: " + author);
    }

    public static void main(String[] args) {
        CopyConstructor firstBook = new CopyConstructor("Clean Code", "Robert C. Martin");
        CopyConstructor copiedBook = new CopyConstructor(firstBook);
        firstBook.printDetails();
        System.out.println();
        copiedBook.printDetails();
    }
}
