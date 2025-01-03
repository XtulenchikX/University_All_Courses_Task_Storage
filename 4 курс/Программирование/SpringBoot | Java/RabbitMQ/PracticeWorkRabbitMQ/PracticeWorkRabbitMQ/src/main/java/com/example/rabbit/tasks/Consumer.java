package com.example.rabbit.tasks;

import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

@Component
public class Consumer {

    @RabbitListener(queues = "task_queue")
    public void receiveMessage(String message) {
        System.out.println("Received: " + message);
    }
}
