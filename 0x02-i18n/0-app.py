#!/usr/bin/env python3
"""
A simple Flask web app to display a 'Hello world' message on the homepage.
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Render the homepage with a welcome message."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

