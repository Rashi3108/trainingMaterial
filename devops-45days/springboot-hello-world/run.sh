#!/bin/bash

# Spring Boot Hello World Application Runner Script

echo "🚀 Spring Boot Hello World Application Runner"
echo "=============================================="

# Check if Java is installed
if ! command -v java &> /dev/null; then
    echo "❌ Java is not installed. Please install Java 17 or higher."
    exit 1
fi

# Check Java version
JAVA_VERSION=$(java -version 2>&1 | awk -F '"' '/version/ {print $2}' | cut -d'.' -f1)
if [ "$JAVA_VERSION" -lt 17 ]; then
    echo "❌ Java 17 or higher is required. Current version: $JAVA_VERSION"
    exit 1
fi

echo "✅ Java version check passed"

# Check if Maven is installed
if ! command -v mvn &> /dev/null; then
    echo "❌ Maven is not installed. Please install Maven 3.6 or higher."
    exit 1
fi

echo "✅ Maven check passed"

# Navigate to project directory
cd "$(dirname "$0")"

echo ""
echo "Choose an option:"
echo "1. Run the application (mvn spring-boot:run)"
echo "2. Build and run JAR file"
echo "3. Run tests"
echo "4. Clean and build"
echo "5. Show application info"
echo ""

read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo ""
        echo "🏃‍♂️ Running Spring Boot application..."
        echo "📱 Application will be available at: http://localhost:8080"
        echo "🔍 Health check: http://localhost:8080/actuator/health"
        echo "ℹ️  Application info: http://localhost:8080/info"
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
            java -jar target/springboot-hello-world-1.0.0.jar
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
        echo "🧹 Cleaning and building..."
        mvn clean compile
        ;;
    5)
        echo ""
        echo "📋 Application Information"
        echo "========================="
        echo "Name: SpringBoot Hello World"
        echo "Version: 1.0.0"
        echo "Java Version: $(java -version 2>&1 | head -n 1)"
        echo "Maven Version: $(mvn -version | head -n 1)"
        echo ""
        echo "📁 Project Structure:"
        find . -type f -name "*.java" -o -name "*.properties" -o -name "*.xml" | head -10
        echo ""
        echo "🌐 Available Endpoints:"
        echo "  GET  /                    - Home page"
        echo "  GET  /hello               - Simple hello"
        echo "  GET  /hello/{name}        - Personalized hello"
        echo "  GET  /greet?name={name}   - Greet with parameter"
        echo "  GET  /info                - Application info"
        echo "  GET  /actuator/health     - Health check"
        ;;
    *)
        echo "❌ Invalid choice. Please run the script again and choose 1-5."
        exit 1
        ;;
esac
