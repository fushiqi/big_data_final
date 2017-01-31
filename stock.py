from flask import Flask, request, jsonify, session, g, redirect, url_for, abort, \
    render_template, flash
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search():
    ticker = request.args['ticker']
    # connect to database and find data
    if ticker:
        return jsonify({'ticker': ticker})
    return jsonify({'error': 'Missing data!'})


if __name__ == '__main__':
    app.debug = True
    app.run()
