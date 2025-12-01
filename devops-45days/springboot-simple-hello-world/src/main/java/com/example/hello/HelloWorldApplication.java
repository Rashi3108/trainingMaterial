package com.example.hello;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Simple Spring Boot Hello World Application
 * 
 * This is the main class that starts our Spring Boot application.
 * The @SpringBootApplication annotation enables auto-configuration,
 * component scanning, and configuration properties.
 */
@SpringBootApplication
public class HelloWorldApplication {

    /**
     * Main method - entry point of the Spring Boot application
     * 
     * @param args command line arguments
     */
    public static void main(String[] args) {
        SpringApplication.run(HelloWorldApplication.class, args);
        System.out.println("🚀 Spring Boot Hello World Application Started!");
        System.out.println("📱 Open your browser and go to: http://localhost:8080");
        System.out.println("🌐 Available endpoints:");
        System.out.println("   • http://localhost:8080/ - Home page");
        System.out.println("   • http://localhost:8080/hello - Hello message");
        System.out.println("   • http://localhost:8080/hello/YourName - Personalized greeting");
    }
}
