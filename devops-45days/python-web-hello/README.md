# Python Web Hello World with Flask

A simple Python web application using Flask framework that displays "Hello World" in a browser.

## Prerequisites
- Python 3.6+
- pip (Python package installer)

## Project Structure
```
python-web-hello/
├── venv/               # Virtual environment (created after setup)
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Setup and Installation

### 1. Check Python Installation
```bash
python3 --version
pip3 --version
```

### 2. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

### 3. Install Flask
```bash
# Make sure virtual environment is activated
pip install Flask==3.0.0

# Or install from requirements file
pip install -r requirements.txt
```

### 4. Verify Flask Installation
```bash
python3 -c "import flask; print(flask.__version__)"
```

### 5. Deactivate Virtual Environment (when done)
```bash
deactivate
```

## Run the Application

**Important:** Make sure your virtual environment is activated first:
```bash
source venv/bin/activate  # On macOS/Linux
# or
# venv\Scripts\activate   # On Windows
```

### Method 1: Direct execution
```bash
python3 app.py
```

### Method 2: Using Flask command
```bash
export FLASK_APP=app.py
flask run
```

### Method 3: Direct execution with shebang
```bash
./app.py
```

## Access the Application

After starting the application, you'll see output like:
```
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://[your-ip]:5000
```

### Available URLs:
- **Main page:** http://localhost:5000 or http://127.0.0.1:5000
- **Personalized greeting:** http://localhost:5000/hello/YourName

### Expected Output:
- **http://localhost:5000** → `Hello World`
- **http://localhost:5000/hello/John** → `Hello John!`

## What happens when you run the application?

When you execute `python3 app.py`, the following occurs:

### 1. **Flask Application Initialization:**
```python
app = Flask(__name__)
```
- Creates a Flask application instance
- `__name__` tells Flask where to find resources

### 2. **Route Registration:**
```python
@app.route('/')
def hello_world():
    return "Hello World"
```
- `@app.route('/')` is a decorator that maps URL `/` to the function
- When someone visits the root URL, `hello_world()` function is called

### 3. **Development Server Startup:**
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```
- Starts Flask's built-in development server
- `debug=True`: Enables auto-reload and error messages
- `host='0.0.0.0'`: Makes server accessible from any IP
- `port=5000`: Server listens on port 5000

### 4. **Request Handling:**
- Browser sends HTTP GET request to `http://localhost:5000`
- Flask routes the request to appropriate function
- Function returns response string
- Flask sends HTTP response back to browser

## Code Explanation

### Complete Code:
```python
#!/usr/bin/env python3

from flask import Flask

# Create Flask application instance
app = Flask(__name__)

@app.route('/')
def hello_world():
    """Return Hello World message for the root URL"""
    return "Hello World"

@app.route('/hello/<name>')
def hello_name(name):
    """Return personalized greeting"""
    return f"Hello {name}!"

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Line-by-Line Breakdown:

1. **`#!/usr/bin/env python3`** - Shebang line for direct execution

2. **`from flask import Flask`** - Import Flask class
   - Flask is the main class for creating web applications

3. **`app = Flask(__name__)`** - Create Flask app instance
   - `__name__` helps Flask locate resources relative to the module

4. **`@app.route('/')`** - Route decorator
   - Maps URL path `/` to the following function
   - Decorator pattern for URL routing

5. **`def hello_world():`** - View function
   - Handles requests to the root URL
   - Returns response that will be sent to browser

6. **`@app.route('/hello/<name>')`** - Dynamic route
   - `<name>` is a variable part of the URL
   - Captures URL segment and passes it to function

7. **`app.run(debug=True, host='0.0.0.0', port=5000)`** - Start server
   - Only runs when script is executed directly (not imported)

## Flask Concepts Demonstrated

### 1. **Web Framework**
- **Purpose:** Handles HTTP requests and responses
- **Routing:** Maps URLs to Python functions
- **WSGI:** Web Server Gateway Interface compliance

### 2. **Decorators**
- **`@app.route()`:** Python decorator for URL mapping
- **Syntax:** `@decorator` above function definition
- **Purpose:** Adds functionality without modifying function code

### 3. **HTTP Methods**
- **GET:** Default method for `@app.route()`
- **Other methods:** POST, PUT, DELETE can be specified
- **RESTful:** Following REST API conventions

### 4. **URL Variables**
- **Dynamic routes:** `<variable_name>` in URL pattern
- **Type conversion:** `<int:id>`, `<float:price>`, etc.
- **Function parameters:** URL variables become function arguments

## Development vs Production

### Development Mode (what we're using):
```python
app.run(debug=True)
```
- **Auto-reload:** Restarts server when code changes
- **Debug mode:** Shows detailed error pages
- **Not secure:** Should not be used in production

### Production Deployment:
```bash
# Using Gunicorn (production WSGI server)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Testing the Application

### Manual Testing:
```bash
# Start the application
python3 app.py

# In another terminal, test with curl
curl http://localhost:5000
curl http://localhost:5000/hello/Python
```

### Expected Responses:
```bash
$ curl http://localhost:5000
Hello World

$ curl http://localhost:5000/hello/Python
Hello Python!
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'flask'"
```bash
pip3 install Flask
```

### "Address already in use" error
```bash
# Find process using port 5000
lsof -i :5000

# Kill the process (replace PID with actual process ID)
kill -9 <PID>

# Or use a different port
app.run(port=5001)
```

### "Permission denied" error
```bash
chmod +x app.py
```

## Flask vs Other Python Web Frameworks

### Flask (Micro Framework)
- **Pros:** Lightweight, flexible, easy to learn
- **Cons:** Minimal built-in features
- **Best for:** Small to medium applications, APIs

### Django (Full Framework)
- **Pros:** Batteries included, admin interface, ORM
- **Cons:** Heavier, steeper learning curve
- **Best for:** Large applications, rapid development

### FastAPI (Modern Framework)
- **Pros:** Fast, automatic API documentation, type hints
- **Cons:** Newer, smaller ecosystem
- **Best for:** APIs, modern Python features

## Next Steps

Once you understand this basic Flask app, explore:

1. **Templates:** HTML templates with Jinja2
2. **Static Files:** CSS, JavaScript, images
3. **Forms:** Handle user input
4. **Database:** SQLite, PostgreSQL integration
5. **Authentication:** User login/logout
6. **REST APIs:** JSON responses
7. **Deployment:** Heroku, AWS, Docker

## Advanced Example with HTML Template

Create a `templates` folder and HTML file:

```bash
mkdir templates
```

**templates/index.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Python Flask Hello World</title>
</head>
<body>
    <h1>{{ message }}</h1>
    <p>Welcome to Flask web application!</p>
</body>
</html>
```

**Updated app.py:**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', message='Hello World')
```

## Summary

This Flask "Hello World" application demonstrates:
- ✅ Web framework basics (Flask)
- ✅ HTTP request/response cycle
- ✅ URL routing and decorators
- ✅ Dynamic URL parameters
- ✅ Development server setup
- ✅ Browser-accessible Python application

Perfect introduction to Python web development!
