from flask import request, jsonify
from app import app


@app.route('/api/home')
def home():
    return {'hi':'hello'}










