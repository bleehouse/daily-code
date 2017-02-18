package com.bleehouse.readinglist;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;

public interface ReadingListReposigitory extends JpaRepository<Book, Long> {
	List<Book> findByReader(String reader);
}
