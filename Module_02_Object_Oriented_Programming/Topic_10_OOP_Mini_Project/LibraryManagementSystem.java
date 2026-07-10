import java.util.ArrayList;
import java.util.List;

class LibraryBook {
    private String title;
    private String author;
    private boolean available;

    public LibraryBook(String title, String author) {
        this.title = title;
        this.author = author;
        this.available = true;
    }

    public String getDetails() {
        return title + " by " + author + " (" + (available ? "Available" : "Not Available") + ")";
    }
}

public class LibraryManagementSystem {
    public static void main(String[] args) {
        List<LibraryBook> books = new ArrayList<>();
        books.add(new LibraryBook("The Alchemist", "Paulo Coelho"));
        books.add(new LibraryBook("To Kill a Mockingbird", "Harper Lee"));

        for (LibraryBook book : books) {
            System.out.println(book.getDetails());
        }
    }
}
