"""Main application routes."""
from flask import jsonify
from app import create_app
import os

app = create_app()


@app.route('/')
def home():
    """Home endpoint."""
    return jsonify({
        "message": "Welcome to Secure CI/CD Pipeline Demo",
        "status": "healthy",
        "version": "1.0.0"
    })


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "secure-cicd-pipeline"
    }), 200


@app.route('/api/info')
def info():
    """Application info endpoint."""
    return jsonify({
        "application": "Secure CI/CD Pipeline",
        "description": "Automated deployment with security scanning",
        "environment": os.getenv("ENVIRONMENT", "development"),
        "features": [
            "Automated Testing",
            "Security Scanning",
            "Container Deployment",
            "Azure Integration"
        ]
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)