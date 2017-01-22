package chapter01;

import java.util.ArrayList;
import java.util.List;

public class BookShelf implements Aggregate {

	private List<Book> books;
	
	public BookShelf() {
		this.books = new ArrayList<Book>(); 
	}
	
	public Book getBookAt(int index) {
		return books.get(index);
	}
	
	public void appendBook(Book book) {
		books.add(book);
	}
	
	public int getLength() {
		return this.books.size();
	}

	public Iterator iterator() {
		return (Iterator) new BookShelfIterator(this);
	}

}
