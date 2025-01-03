package com.example.appb.config;

import org.springframework.amqp.core.Queue;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class RabbitConfig {

    @Bean
    public Queue sendQueue() {
        return new Queue("appC-to-appA", false);
    }

    @Bean
    public Queue receiveQueue() {
        return new Queue("appA-to-appAll", false);
    }
}
