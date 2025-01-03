package com.example.appa.messages;

import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

@Service
public class MessageProducer {

    private final RabbitTemplate rabbitTemplate;

    public MessageProducer(RabbitTemplate rabbitTemplate) {
        this.rabbitTemplate = rabbitTemplate;
    }

    @Scheduled(fixedRate = 10000)
    public void sendMessage() {
        String message = "Message from A";
        String queue = "appA-to-appAll";
        rabbitTemplate.convertAndSend(queue, message);
        System.out.println("Sent: " + message);
    }
}
