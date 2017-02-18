package com.bleehouse.readinglist;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/")
public class ReadingListController {
	private static final String reader="craig";
	
	private ReadingListReposigitory readingListReposigitory;
	
	@Autowired
	public ReadingListController(ReadingListReposigitory readingListReposigitory){
		this.readingListReposigitory = readingListReposigitory;
	}
	
	@RequestMapping(method=RequestMethod.GET)
	public String readersBooks(Model model) {
		List<Book> readingList = readingListReposigitory.findByReader(reader);
		if (readingList != null) {
			model.addAttribute("books", readingList);
		}
		return "readingList";
	}

	@RequestMapping(method=RequestMethod.POST)
	public String addToReadingList(Book book) {
		book.setReader(reader);
		readingListReposigitory.save(book);
		return "redirect:/";
	}	
	
}
