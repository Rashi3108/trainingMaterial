#!/bin/bash

# Simple script to compile and run the Java Hello World application

echo "🚀 Minimal Java Hello World Application"
echo "========================================"

# Set JAVA_HOME to the Java installation used by Maven
export JAVA_HOME="/opt/homebrew/Cellar/openjdk/24.0.1/libexec/openjdk.jdk/Contents/Home"
export PATH="$JAVA_HOME/bin:$PATH"

# Check if Java is installed
if ! command -v java &> /dev/null; then
    echo "❌ Java is not installed. Please install Java first."
    exit 1
fi

# Check if javac (Java compiler) is installed
if ! command -v javac &> /dev/null; then
    echo "❌ Java compiler (javac) is not installed. Please install JDK."
    exit 1
fi

echo "✅ Java version: $(java -version 2>&1 | head -n 1)"
echo "✅ Java compiler version: $(javac -version 2>&1)"

echo ""
echo "📝 Compiling HelloWorld.java..."
javac HelloWorld.java

if [ $? -eq 0 ]; then
    echo "✅ Compilation successful!"
    echo ""
    echo "🏃‍♂️ Running the application..."
    echo "================================"
    java HelloWorld
    echo "================================"
    echo "✅ Application executed successfully!"
else
    echo "❌ Compilation failed!"
    exit 1
fi

echo ""
echo "📁 Files created:"
ls -la *.class 2>/dev/null || echo "No .class files found"
