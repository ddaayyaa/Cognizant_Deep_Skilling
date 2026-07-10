import java.util.ArrayList;
import java.util.List;

public class LibraryManagementSystem {

    public static void main(String[] args) {
        Library library = new Library();
        library.addBook(new Book("B001", "Java Basics"));
        library.addBook(new Book("B002", "Data Structures"));
        library.showBooks();
    }
}

class Library {
    private List<Book> books = new ArrayList<>();

    public void addBook(Book book) {
        books.add(book);
    }

    public void showBooks() {
        for (Book book : books) {
            System.out.println(book.getId() + ": " + book.getTitle());
        }
    }
}

class Book {
    private String id;
    private String title;

    public Book(String id, String title) {
        this.id = id;
        this.title = title;
    }

    public String getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }
}
