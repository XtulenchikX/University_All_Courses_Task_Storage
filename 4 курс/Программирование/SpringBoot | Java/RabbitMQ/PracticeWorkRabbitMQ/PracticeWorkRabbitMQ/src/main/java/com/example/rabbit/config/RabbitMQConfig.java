package com.example.rabbit.config;

import org.springframework.amqp.core.Queue;
import org.springframework.amqp.core.TopicExchange;
import org.springframework.amqp.core.BindingBuilder;
import org.springframework.amqp.core.FanoutExchange;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import org.springframework.amqp.core.Binding;

@Configuration
public class RabbitMQConfig {

    @Bean
    public Queue taskQueue() {
        return new Queue("task_queue", true);
    }

    @Bean
    public FanoutExchange fanoutExchange() {
        return new FanoutExchange("logs");
    }

    @Bean
    public TopicExchange directExchange() {
        return new TopicExchange("direct_logs");
    }

    @Bean
    public Queue infoQueue() {
        return new Queue("info", true);
    }

    @Bean
    public Queue errorQueue() {
        return new Queue("error", true);
    }

    @Bean
    public Queue warningQueue() {
        return new Queue("warning", true);
    }

    @Bean
    public Binding bindingInfo(Queue infoQueue, TopicExchange directExchange) { return BindingBuilder.bind(infoQueue).to(directExchange).with("info"); }

    @Bean
    public Binding bindingError(Queue errorQueue, TopicExchange directExchange) { return BindingBuilder.bind(errorQueue).to(directExchange).with("error"); }

    @Bean
    public Binding bindingWarning(Queue warningQueue, TopicExchange directExchange) { return BindingBuilder.bind(warningQueue).to(directExchange).with("warning"); }
}
