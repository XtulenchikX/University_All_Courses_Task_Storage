package com.example.rabbit.notifications;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.stereotype.Component;

@Component
public class Publisher {

    @Autowired
    private RabbitTemplate rabbitTemplate;

    public void publishMessage(String message) {
        rabbitTemplate.convertAndSend("logs", "", message);
        System.out.println("Published: " + message);
    }
}
