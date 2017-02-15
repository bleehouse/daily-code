package com.example.entity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;


@Entity
@lombok.Getter
@lombok.Setter
@lombok.ToString()
public class Member {

	@Id
	@GeneratedValue(strategy=GenerationType.AUTO)
	private long id;
 
	@Column
	private String name;
 
	@Column
	private int age;
 
	public Member() {}	
	
	public Member(String name, int age) {
		this.name = name;
		this.age = age;
	}
}
