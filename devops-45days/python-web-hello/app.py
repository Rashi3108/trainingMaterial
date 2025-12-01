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
