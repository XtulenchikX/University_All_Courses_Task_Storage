package com.example.rabbit.notifications;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.stereotype.Component;

@Component
public class PublisherWithRouting {

    @Autowired
    private RabbitTemplate rabbitTemplate;

    public void sendMessage(String routingKey, String message) {
        rabbitTemplate.convertAndSend("direct_logs", routingKey, message);
        System.out.println("Sent with routing key " + routingKey + ": " + message);
    }
}
