package com.example.helloworld;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.TestPropertySource;

/**
 * Basic integration tests for the Spring Boot Hello World application
 */
@SpringBootTest
@TestPropertySource(locations = "classpath:application.properties")
class HelloWorldApplicationTests {

    /**
     * Test that the Spring Boot application context loads successfully
     */
    @Test
    void contextLoads() {
        // This test will pass if the application context loads without errors
        // Spring Boot will automatically validate the configuration and dependencies
    }
}
