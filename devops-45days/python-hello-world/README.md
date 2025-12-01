# Simple Python Hello World

A minimal Python application that prints "Hello World".

## Prerequisites
- Python 3.6+ (Python 3 is recommended)

## Check Python Installation
```bash
python3 --version
# or
python --version
```

## Project Structure
```
python-hello-world/
├── hello.py          # Main Python script
└── README.md         # This file
```

## Run the application

### Method 1: Using python3 command
```bash
python3 hello.py
```

### Method 2: Using python command (if Python 3 is default)
```bash
python hello.py
```

### Method 3: Direct execution (Unix/Linux/macOS)
```bash
./hello.py
```

## Expected Output
```
Hello World
```

## What happens when you run the application?

When you execute `python3 hello.py`, Python performs the following steps:

1. **Python Interpreter Startup:**
   - Python interpreter starts and reads the `hello.py` file
   - Parses the Python code and converts it to bytecode

2. **Code Execution:**
   - Python executes the script line by line
   - Checks the `if __name__ == "__main__":` condition
   - Since the script is run directly (not imported), this condition is True

3. **Function Call:**
   - Calls the `main()` function
   - Executes `print("Hello World")`
   - Outputs "Hello World" to the console

4. **Program Termination:**
   - Script execution completes
   - Python interpreter exits

## Code Explanation

### The Complete Code:
```python
#!/usr/bin/env python3

def main():
    print("Hello World")

if __name__ == "__main__":
    main()
```

### Line-by-Line Breakdown:

1. **`#!/usr/bin/env python3`** - Shebang line
   - Tells the system to use Python 3 interpreter
   - Allows direct execution with `./hello.py`

2. **`def main():`** - Function definition
   - Defines a function named `main`
   - Contains the main logic of our program

3. **`print("Hello World")`** - Print statement
   - Outputs the text "Hello World" to the console
   - `print()` is a built-in Python function

4. **`if __name__ == "__main__":`** - Main guard
   - Checks if the script is being run directly (not imported)
   - `__name__` is a special variable in Python
   - When script is run directly, `__name__` equals `"__main__"`

5. **`main()`** - Function call
   - Calls the `main()` function we defined above

## Python Concepts Demonstrated

### 1. Functions
- **Definition:** `def main():` creates a function
- **Call:** `main()` executes the function
- **Purpose:** Organizes code into reusable blocks

### 2. Built-in Functions
- **`print()`:** Outputs text to the console
- **Standard library function:** Available without importing

### 3. Special Variables
- **`__name__`:** Contains the name of the current module
- **`__main__`:** Special value when script is run directly

### 4. Conditional Execution
- **`if` statement:** Executes code only when condition is True
- **Main guard:** Prevents code execution when module is imported

## Python Bytecode

When you run the script, Python creates bytecode files:

### Check for bytecode files:
```bash
# After running the script, check for __pycache__ directory
ls -la
ls -la __pycache__/ 2>/dev/null || echo "No bytecode cache found"
```

### What is bytecode?
- Python compiles your source code to bytecode (.pyc files)
- Bytecode is stored in `__pycache__/` directory
- Makes subsequent runs faster
- Platform-independent intermediate representation

## Different Ways to Run Python Code

### 1. Script Execution (what we're doing)
```bash
python3 hello.py
```

### 2. Interactive Mode
```bash
python3
>>> print("Hello World")
>>> exit()
```

### 3. One-liner
```bash
python3 -c "print('Hello World')"
```

### 4. Module execution
```bash
# If hello.py was in a package
python3 -m hello
```

## Python Installation Check

### Check Python version:
```bash
python3 --version
```

### Check Python location:
```bash
which python3
```

### Check installed packages:
```bash
pip3 list
```

## Troubleshooting

### "python3: command not found"
- **macOS:** Install Python via Homebrew: `brew install python`
- **Linux:** Install via package manager: `sudo apt install python3`
- **Windows:** Download from python.org

### "Permission denied" error
```bash
chmod +x hello.py
./hello.py
```

### Different Python versions
```bash
# Check all available Python versions
ls /usr/bin/python*
```

## Next Steps

Once you understand this basic example, you can explore:

1. **Variables and Data Types**
2. **User Input:** `input()` function
3. **Command Line Arguments:** `sys.argv`
4. **File Operations:** Reading and writing files
5. **Modules and Packages:** Organizing larger programs
6. **Error Handling:** try/except blocks
7. **Object-Oriented Programming:** Classes and objects

## Advanced Example

Here's a slightly more advanced version:

```python
#!/usr/bin/env python3
import sys

def greet(name="World"):
    """Print a greeting message."""
    print(f"Hello {name}")

def main():
    """Main function with command line argument support."""
    if len(sys.argv) > 1:
        name = sys.argv[1]
        greet(name)
    else:
        greet()

if __name__ == "__main__":
    main()
```

Usage:
```bash
python3 hello.py          # Output: Hello World
python3 hello.py John     # Output: Hello John
```

## Summary

This simple Python "Hello World" application demonstrates:
- ✅ Basic Python syntax and structure
- ✅ Function definition and calling
- ✅ Print statement usage
- ✅ Main guard pattern
- ✅ Shebang line for direct execution
- ✅ Python execution model

Perfect starting point for learning Python programming!
