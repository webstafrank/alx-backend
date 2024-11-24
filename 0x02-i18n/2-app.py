#!/usr/bin/env python3
"""
A Flask web app configured with Flask-Babel for internationalization.
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# Configuration class for setting available languages and default settings
class Config:
    """Configuration for Babel with languages, locale, and timezone."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Apply configuration to the Flask app
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Determine the best match for supported languages using request headers."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Render the homepage with a welcome message."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

