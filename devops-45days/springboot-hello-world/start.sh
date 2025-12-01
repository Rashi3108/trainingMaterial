#!/bin/bash

# Spring Boot Hello World Application Startup Script
# This script provides an easy way to start the application

echo "🚀 Starting Spring Boot Hello World Application..."
echo "=================================================="

# Check if Java is installed
if ! command -v java &> /dev/null; then
    echo "❌ Java is not installed. Please install Java 17 or higher."
    echo "   Visit: https://adoptium.net/ to download Java"
    exit 1
fi

# Check if Maven is installed
if ! command -v mvn &> /dev/null; then
    echo "❌ Maven is not installed. Please install Maven 3.6 or higher."
    echo "   Visit: https://maven.apache.org/download.cgi to download Maven"
    exit 1
fi

# Display Java and Maven versions
echo "☕ Java Version:"
java -version
echo ""
echo "📦 Maven Version:"
mvn -version
echo ""

# Build and run the application
echo "🔨 Building the application..."
mvn clean compile

if [ $? -eq 0 ]; then
    echo "✅ Build successful!"
    echo ""
    echo "🏃 Starting the application..."
    echo "   The application will be available at: http://localhost:8080"
    echo "   Press Ctrl+C to stop the application"
    echo ""
    
    # Start the Spring Boot application
    mvn spring-boot:run
else
    echo "❌ Build failed. Please check the error messages above."
    exit 1
fi
