package com.example.helloworld.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

/**
 * Web Controller for handling HTTP requests
 * 
 * The @Controller annotation indicates that this class serves as a controller
 * in the Spring MVC framework
 */
@Controller
public class HelloWorldController {

    /**
     * Handles GET requests to the root path "/"
     * Returns the main HTML page using Thymeleaf template
     * 
     * @param name optional request parameter for personalized greeting
     * @param model Spring MVC model to pass data to the view
     * @return the name of the Thymeleaf template to render
     */
    @GetMapping("/")
    public String home(@RequestParam(value = "name", defaultValue = "World") String name, Model model) {
        // Add attributes to the model that will be available in the template
        model.addAttribute("greeting", "Hello, " + name + "!");
        model.addAttribute("currentTime", LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")));
        model.addAttribute("name", name);
        
        return "index"; // This refers to src/main/resources/templates/index.html
    }

    /**
     * REST API endpoint that returns JSON response
     * The @ResponseBody annotation indicates that the return value should be written directly to the HTTP response body
     * 
     * @param name optional request parameter for personalized greeting
     * @return JSON response as a string
     */
    @GetMapping("/api/hello")
    @ResponseBody
    public String helloApi(@RequestParam(value = "name", defaultValue = "World") String name) {
        return String.format("{\"message\": \"Hello, %s!\", \"timestamp\": \"%s\"}", 
                           name, 
                           LocalDateTime.now().format(DateTimeFormatter.ISO_LOCAL_DATE_TIME));
    }

    /**
     * Health check endpoint
     * 
     * @return simple status message
     */
    @GetMapping("/health")
    @ResponseBody
    public String health() {
        return "{\"status\": \"UP\", \"service\": \"Spring Boot Hello World\"}";
    }
}
