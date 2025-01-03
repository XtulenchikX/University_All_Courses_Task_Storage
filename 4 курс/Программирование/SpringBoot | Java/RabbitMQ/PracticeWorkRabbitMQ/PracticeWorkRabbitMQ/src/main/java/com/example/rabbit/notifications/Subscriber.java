package com.example.rabbit.notifications;

import org.springframework.amqp.rabbit.annotation.QueueBinding;
import org.springframework.amqp.rabbit.annotation.Queue;
import org.springframework.amqp.rabbit.annotation.Exchange;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

@Component
public class Subscriber {

    @RabbitListener(bindings = @QueueBinding(value = @Queue(value = "dynamic_queue", durable = "true"), exchange = @Exchange(value = "logs", type = "fanout")))
    public void receiveMessage(String message) {
        System.out.println("Received message: " + message);
    }
}
