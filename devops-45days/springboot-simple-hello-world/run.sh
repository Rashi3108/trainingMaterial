#!/bin/bash

# Simple Spring Boot Hello World Application Runner Script

echo "🚀 Simple Spring Boot Hello World Application"
echo "=============================================="

# Check if Java is installed
if ! command -v java &> /dev/null; then
    echo "❌ Java is not installed. Please install Java 17 or higher."
    exit 1
fi

# Check if Maven is installed
if ! command -v mvn &> /dev/null; then
    echo "❌ Maven is not installed. Please install Maven."
    exit 1
fi

echo "✅ Java version: $(java -version 2>&1 | head -n 1)"
echo "✅ Maven version: $(mvn -version | head -n 1)"

echo ""
echo "Choose an option:"
echo "1. Run the application (mvn spring-boot:run)"
echo "2. Build and run JAR file"
echo "3. Run tests"
echo "4. Clean and compile"
echo "5. Show application info"
echo ""

read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo ""
        echo "🏃‍♂️ Starting Spring Boot application..."
        echo "📱 Application will be available at: http://localhost:8080"
        echo "🌐 Available endpoints:"
        echo "   • http://localhost:8080/ - Home page"
        echo "   • http://localhost:8080/hello - Hello message"
        echo "   • http://localhost:8080/hello/YourName - Personalized greeting"
        echo ""
        echo "Press Ctrl+C to stop the application"
        echo ""
        mvn spring-boot:run
        ;;
    2)
        echo ""
        echo "🔨 Building application..."
        mvn clean package -DskipTests
        
        if [ $? -eq 0 ]; then
            echo "✅ Build successful!"
            echo ""
            echo "🏃‍♂️ Running JAR file..."
            echo "📱 Application will be available at: http://localhost:8080"
            echo ""
            java -jar target/springboot-simple-hello-world-1.0.0.jar
        else
            echo "❌ Build failed!"
            exit 1
        fi
        ;;
    3)
        echo ""
        echo "🧪 Running tests..."
        mvn test
        ;;
    4)
        echo ""
        echo "🧹 Cleaning and compiling..."
        mvn clean compile
        ;;
    5)
        echo ""
        echo "📋 Application Information"
        echo "========================="
        echo "Name: Simple Spring Boot Hello World"
        echo "Version: 1.0.0"
        echo "Java Version: $(java -version 2>&1 | head -n 1)"
        echo "Maven Version: $(mvn -version | head -n 1)"
        echo ""
        echo "📁 Project Structure:"
        find . -name "*.java" -o -name "*.properties" -o -name "*.xml" | head -10
        echo ""
        echo "🌐 Available Endpoints:"
        echo "  GET  /                    - Home page"
        echo "  GET  /hello               - Simple hello message"
        echo "  GET  /hello/{name}        - Personalized greeting"
        ;;
    *)
        echo "❌ Invalid choice. Please run the script again and choose 1-5."
        exit 1
        ;;
esac
