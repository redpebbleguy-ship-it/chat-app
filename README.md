# Real-Time Chat App

A simple real-time chat website built with Python, Flask, and Socket.IO.

## How to run locally
pip install -r requirements.txt
python app.py

## Deploying on Render
1. Upload this folder to GitHub
2. Create a new Web Service on Render
3. Use this start command:
   gunicorn --worker-class eventlet -w 1 app:app
