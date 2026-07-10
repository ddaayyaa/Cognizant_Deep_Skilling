public class TicketBooking {
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
