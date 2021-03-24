import os
from flask import Flask, abort, session, request, redirect
from flask.json import jsonify

from utils import *

app = Flask(__name__)

DEFAULT_HOST='0.0.0.0'

@app.route('/', methods=['GET'])
def default():
    return jsonify({'message': 'Hello World!'})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'UP'})

@app.route('/longest-words', methods=['POST'])
def longest_words():
    input_file = request.files['file']
    file_content = input_file.read().decode('utf-8').strip()
    if not file_content:
        return jsonify({"longest_words": []})

    result = get_longest_words(file_content.split())
    return jsonify({"longest_words": result})

@app.route('/word-count', methods=['POST'])
def word_count():
    input_file = request.files['file']
    file_content = input_file.read().decode('utf-8').strip()
    if not file_content:
        return jsonify({"word_count": 0})

    result = get_word_count(file_content.split())
    return jsonify({"word_count": result})

@app.route('/average-length', methods=['POST'])
def average_length():
    input_file = request.files['file']
    file_content = input_file.read().decode('utf-8').strip()
    if not file_content:
        return jsonify({"average_length": 0})

    result = get_average_length(file_content.split())
    return jsonify({"average_length": result})

@app.route('/unique-count', methods=['POST'])
def unique_count():
    input_file = request.files['file']
    file_content = input_file.read().decode('utf-8').strip()
    if not file_content:
        return jsonify({"unique_count": 0})

    result = get_unique_count(file_content.split())
    return jsonify({"unique_count": result})

@app.route('/palindrome-count', methods=['POST'])
def palindrome_count():
    input_file = request.files['file']
    file_content = input_file.read().decode('utf-8').strip()
    if not file_content:
        return jsonify({"palindrome_count": 0})

    result = get_palindrome_count(file_content.split())
    return jsonify({"palindrome_count": result})

if __name__ == "__main__":
    app.run(host=DEFAULT_HOST, debug=True)
