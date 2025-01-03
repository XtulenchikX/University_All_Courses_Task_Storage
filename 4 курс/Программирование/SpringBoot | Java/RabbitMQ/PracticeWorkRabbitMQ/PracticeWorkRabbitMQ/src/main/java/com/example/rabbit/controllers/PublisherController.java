package com.example.rabbit.controllers;

import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/publisher")
public class PublisherController {

    private final RabbitTemplate rabbitTemplate;

    private String exchangeName = "direct_logs";
    private String fallbackName = "logs";

    public PublisherController(RabbitTemplate rabbitTemplate) {
        this.rabbitTemplate = rabbitTemplate;
    }

    @PostMapping("/publish")
    public ResponseEntity<String> publishMessage(@RequestParam String message, @RequestParam(required = false) String routingKey) {
        String queue = routingKey != null ? exchangeName : fallbackName;
        if (routingKey != null) {
            rabbitTemplate.convertAndSend(queue, routingKey, message);
        } else {
            rabbitTemplate.convertAndSend(queue, "", message);
        }

        return ResponseEntity.ok("Message published to exchange: " + queue + " with routing key: "
                + (routingKey != null ? routingKey : "no routing key") + ", message: " + message);
    }
}
