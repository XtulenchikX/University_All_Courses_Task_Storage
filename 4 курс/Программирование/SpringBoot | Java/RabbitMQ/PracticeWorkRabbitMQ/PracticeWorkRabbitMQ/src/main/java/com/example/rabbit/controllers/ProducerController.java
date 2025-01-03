package com.example.rabbit.controllers;

import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/producer")
public class ProducerController {

    private final RabbitTemplate rabbitTemplate;

    private String queueName = "task_queue";

    public ProducerController(RabbitTemplate rabbitTemplate) {
        this.rabbitTemplate = rabbitTemplate;
    }

    @PostMapping("/send")
    public ResponseEntity<String> sendMessage(@RequestParam String message) {
        rabbitTemplate.convertAndSend(queueName, message);
        return ResponseEntity.ok("Message sent to queue: " + queueName + ", message: " + message);
    }
}
