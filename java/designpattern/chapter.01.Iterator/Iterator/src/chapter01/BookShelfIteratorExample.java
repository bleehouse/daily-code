package chapter01;

public class BookShelfIteratorExample {

	public static void main(String[] args) {

		BookShelf bookshelf = new BookShelf();
		
		bookshelf.appendBook(new Book("Around the World in 80 Days"));
		bookshelf.appendBook(new Book("Bible"));
		bookshelf.appendBook(new Book("Cinderella"));
		bookshelf.appendBook(new Book("Daddy-Long-Legs"));
		
		Iterator it = (Iterator) bookshelf.iterator();
		
		while(it.hasNext()) {
			Book book = (Book)it.next();
			System.out.println(book.getName());
		}
	}
}

