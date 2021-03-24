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
    word_list = []
    input_file = request.files['file']
    file_content = input_file.read().decode('utf-8').strip()
    if file_content:
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

    resp = {"longest_words": longest_words}
    return jsonify(resp)

if __name__ == "__main__":
    app.run(host=DEFAULT_HOST, debug=True)
