#!/bin/bash

# Simple script to run the Spring Boot JAR with correct Java path

echo "🚀 Starting Spring Boot Hello World application..."
echo "📍 URL: http://localhost:8080"
echo "⏹️  Press Ctrl+C to stop"
echo ""

# Use the Java that Maven uses
/opt/homebrew/Cellar/openjdk/24.0.1/libexec/openjdk.jdk/Contents/Home/bin/java -jar target/simple-hello-1.0.0.jar
