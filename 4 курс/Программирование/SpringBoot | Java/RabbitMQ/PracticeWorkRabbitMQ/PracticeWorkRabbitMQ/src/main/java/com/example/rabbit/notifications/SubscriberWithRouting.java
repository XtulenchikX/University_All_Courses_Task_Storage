package com.example.rabbit.notifications;

import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

@Component
public class SubscriberWithRouting {

    @RabbitListener(queues = "info")
    public void receiveInfoMessages(String message) {
        System.out.println("Received Info: " + message);
    }

    @RabbitListener(queues = "error")
    public void receiveErrorMessages(String message) {
        System.out.println("Received Error: " + message);
    }

    @RabbitListener(queues = "warning")
    public void receiveWarningMessages(String message) {
        System.out.println("Received Warning: " + message);
    }
}
