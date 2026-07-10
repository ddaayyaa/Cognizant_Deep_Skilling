public class ThisConstructor {
    private String title;
    private String author;

    public ThisConstructor() {
        this("Unknown", "Unknown");
    }

    public ThisConstructor(String title, String author) {
        this.title = title;
        this.author = author;
    }

    public void display() {
        System.out.println("Title : " + title);
        System.out.println("Author: " + author);
    }

    public static void main(String[] args) {
        ThisConstructor book = new ThisConstructor("Java Basics", "Ravi");
        book.display();
    }
}
