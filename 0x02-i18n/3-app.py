#!/usr/bin/env python3
"""
Flask app with Babel for internationalization and translations.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)

class Config:
    """Configuration for Babel with languages, locale, and timezone."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Determine the best match for supported languages using request headers."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Render the homepage with translated text."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

