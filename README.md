# Cloud Lab Project
Simple web application for Cloud Computing class.

## Description
This application demonstrates the process of deploying a Python/Flask server on a PaaS platform.

## Technology Stack
- **Language:** Python 3.10+
- **Framework:** Flask
- **PaaS:** Render
- **Server:** Gunicorn

## Local Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run app: `python app.py`
3. Access at: `http://localhost:5000`

## Deployment Info
- **Platform:** Render (Free Tier)
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`