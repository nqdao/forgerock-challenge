import os
from flask import Flask, abort, session, request, redirect
from flask.json import jsonify

app = Flask(__name__)

DEFAULT_HOST='0.0.0.0'

@app.route('/', methods=['GET'])
def default():
    return jsonify({'message': 'Hello World!'})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'UP'})

if __name__ == "__main__":
    app.run(host=DEFAULT_HOST, debug=True)
