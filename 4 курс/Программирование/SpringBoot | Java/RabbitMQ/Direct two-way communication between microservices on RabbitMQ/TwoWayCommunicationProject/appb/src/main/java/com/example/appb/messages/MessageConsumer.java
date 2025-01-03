package com.example.appb.messages;

import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Service;

@Service
public class MessageConsumer {

    @RabbitListener(queues = "appA-to-appAll")
    public void receiveMessage(String message) {
        System.out.println("Received: " + message);
    }
}
