from flask import request, jsonify
from app import app


@app.route('/api/home')
def home():
    return {'hi':'hello'}

@app.route('/api/get_data', methods=['POST'])
def get_data():

    data = request.get_json()
    print(data)
    return {'hi':'done'}








