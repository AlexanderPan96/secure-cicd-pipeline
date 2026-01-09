"""Application factory for Flask app."""
from flask import Flask


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Import routes
    from app import main

    return app
