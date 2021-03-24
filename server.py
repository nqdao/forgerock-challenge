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

@app.route('/longest-words', methods=['POST'])
def longest_words():
    input_file = request.files['file']
    file_content = input_file.read().decode('utf-8').strip()
    if not file_content:
        return jsonify({"longest_words": []})

    word_list = file_content.split(" ")
    longest_words = []
    max_len = 0
    if word_list:
        for word in word_list:
            if len(word) > max_len:
                max_len = len(word)
                longest_words = [word]
            elif len(word) == max_len:
                longest_words.append(word)

    return jsonify({"longest_words": longest_words})

@app.route('/word-count', methods=['POST'])
def word_count():
    input_file = request.files['file']
    file_content = input_file.read().decode('utf-8').strip()
    if not file_content:
        return jsonify({"word_count": 0})

    word_list = file_content.split(" ")

    return jsonify({"word_count": len(word_list)})

@app.route('/average-length', methods=['POST'])
def average_length():
    input_file = request.files['file']
    file_content = input_file.read().decode('utf-8').strip()
    if not file_content:
        return jsonify({"average_length": 0})

    word_lengths = [len(word) for word in file_content.split(" ")]

    return jsonify({"average_length": sum(word_lengths)/len(word_lengths)})

@app.route('/unique-count', methods=['POST'])
def unique_count():
    input_file = request.files['file']
    file_content = input_file.read().decode('utf-8').strip()
    if not file_content:
        return jsonify({"unique_count": 0})

    unique_words = []
    for word in file_content.split(" "):
        if word not in unique_words:
            unique_words.append(word)

    return jsonify({"unique_count": len(unique_words)})

if __name__ == "__main__":
    app.run(host=DEFAULT_HOST, debug=True)
