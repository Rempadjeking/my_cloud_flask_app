from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "project_name": "Cloud Deployment Lab",
        "author": "Student",
        "description": "Simple Flask app deployed on Render PaaS",
        "stack": ["Python", "Flask", "Gunicorn"]
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)