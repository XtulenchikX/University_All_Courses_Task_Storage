package com.example.appa;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class AppaApplication {

	public static void main(String[] args) {
		SpringApplication.run(AppaApplication.class, args);
	}

}
