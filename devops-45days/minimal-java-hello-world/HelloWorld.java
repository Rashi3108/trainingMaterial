/**
 * The most basic Java Hello World application
 * This is a simple console application that prints "Hello, World!" to the terminal
 */
public class HelloWorld {
    
    /**
     * The main method - entry point of any Java application
     * @param args command line arguments (not used in this simple example)
     */
    public static void main(String[] args) {
        // Print Hello World message to the console
        System.out.println("Hello, World!");
        System.out.println("This is a minimal Java application running locally.");
        System.out.println("Java version: " + System.getProperty("java.version"));
        System.out.println("Operating System: " + System.getProperty("os.name"));
        System.out.println("User: " + System.getProperty("user.name"));
    }
}
