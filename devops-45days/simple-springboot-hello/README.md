# Simple Spring Boot Hello World

A minimal Spring Boot application that prints "Hello World".

## Prerequisites
- Java 17+
- Maven 3.6+

## Java Setup (Important!)
If you get "Unable to locate a Java Runtime" error when running the JAR:

### Check your Java installation:
```bash
mvn -version  # This shows which Java Maven is using
```

### Fix Java PATH (macOS with Homebrew):
```bash
# Add to your ~/.zshrc or ~/.bash_profile
export JAVA_HOME=/opt/homebrew/Cellar/openjdk/24.0.1/libexec/openjdk.jdk/Contents/Home
export PATH=$JAVA_HOME/bin:$PATH

# Reload your shell
source ~/.zshrc
```

### Alternative: Use Maven to run the JAR
```bash
mvn exec:java -Dexec.mainClass="com.example.HelloApplication"
```

## Run the application
```bash
mvn spring-boot:run
```

## Access
Open browser: http://localhost:8080

You will see: **Hello World**

## What happens when you run `mvn spring-boot:run`?

When you execute `mvn spring-boot:run`, Maven performs the following steps:

1. **Compilation Phase:**
   - Compiles Java source files from `src/main/java/`
   - Places compiled `.class` files in `target/classes/`

2. **Resource Processing:**
   - Copies resources from `src/main/resources/` to `target/classes/`

3. **Spring Boot Plugin Execution:**
   - The `spring-boot-maven-plugin` starts the application
   - Creates an embedded Tomcat server on port 8080
   - Loads the Spring application context
   - Scans for components (@RestController, @Service, etc.)

4. **Application Startup:**
   - Runs `HelloApplication.main()` method
   - Spring Boot auto-configuration kicks in
   - Embedded Tomcat server starts
   - Application becomes ready to serve requests

5. **Console Output:**
   ```
   Started HelloApplication in X.XXX seconds
   ```

## Target Folder Contents

After running `mvn spring-boot:run` or `mvn compile`, the `target/` folder contains:

```
target/
├── classes/                          # Compiled Java classes
│   └── com/example/
│       ├── HelloApplication.class    # Compiled main class
│       └── HelloController.class     # Compiled controller class
├── generated-sources/                # Auto-generated source files
├── maven-archiver/                   # Maven metadata
├── maven-status/                     # Compilation status
└── [JAR file if you run mvn package] # Executable JAR (if packaged)
```

### Key Files in target/classes/:
- **HelloApplication.class** - Bytecode of your main Spring Boot application
- **HelloController.class** - Bytecode of your REST controller

### To see target folder contents:
```bash
# After running the application
ls -la target/
ls -la target/classes/com/example/
```

### To create executable JAR:
```bash
mvn clean package
# Creates: target/simple-hello-1.0.0.jar
```

The JAR file can then be run independently:
```bash
java -jar target/simple-hello-1.0.0.jar
```

### If you get "Unable to locate a Java Runtime" error:
```bash
# Option 1: Set JAVA_HOME and PATH (see Java Setup section above)

# Option 2: Use the full path to Java
/opt/homebrew/Cellar/openjdk/24.0.1/libexec/openjdk.jdk/Contents/Home/bin/java -jar target/simple-hello-1.0.0.jar

# Option 3: Use the provided script
./run-jar.sh

# Option 4: Use Maven to run
mvn spring-boot:run
```
