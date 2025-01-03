package com.example.appa.config;

import org.springframework.amqp.core.Queue;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class RabbitConfig {

    @Bean
    public Queue sendQueue() {
        return new Queue("appA-to-appAll", false);
    }

    @Bean
    public Queue receiveQueueB() {
        return new Queue("appB-to-appA", false);
    }

    @Bean
    public Queue receiveQueueC() {
        return new Queue("appC-to-appA", false);
    }
}
