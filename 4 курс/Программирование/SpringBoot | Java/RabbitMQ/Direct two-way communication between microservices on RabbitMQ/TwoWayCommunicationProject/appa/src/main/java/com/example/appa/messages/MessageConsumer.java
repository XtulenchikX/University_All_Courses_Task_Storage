package com.example.appa.messages;

import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Service;

@Service
public class MessageConsumer {

    @RabbitListener(queues = {"appB-to-appA", "appC-to-appA"})
    public void receiveMessage(String message) {
        System.out.println("Received: " + message);
    }
}
