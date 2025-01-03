package com.example.appb;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class AppbApplication {

	public static void main(String[] args) {
		SpringApplication.run(AppbApplication.class, args);
	}

}
