from flask import Flask, jsonify, request
import sys
from inference import inference
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'name': 'John Doe',
        'age': 30,
        'occupation': 'Software Developer'
    }
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    response = {
        'message': 'Data received successfully',
        'received_data': inference(data)
    }
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True)
