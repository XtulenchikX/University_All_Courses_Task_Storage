package com.example.rabbit.tasks;

import org.springframework.amqp.core.MessageProperties;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.stereotype.Component;

@Component
public class Producer {

    @Autowired
    private RabbitTemplate rabbitTemplate;

    public void sendTask(String message) {
        rabbitTemplate.convertAndSend("task_queue", message, m -> {
            m.getMessageProperties().setDeliveryMode(MessageProperties.DEFAULT_DELIVERY_MODE);
            return m;
        });
        System.out.println("Sent: " + message);
    }
}
