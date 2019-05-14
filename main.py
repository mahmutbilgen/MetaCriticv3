#!/usr/local/bin/python3

import urllib
from flask import Flask, jsonify
from htmlparse.parser import HtmlParser

app = Flask(__name__,static_url_path='')


@app.route('/games/<path:gametitle>')
def game(gametitle):
    g = urllib.parse.unquote(gametitle)
    r = HtmlParser().get_game(g)
    return jsonify({'title': r[0], 'score': r[1]})


@app.route('/games')
def games_all():
    r = HtmlParser().get_all()
    return jsonify(r)


@app.route('/')
def index():
    return app.send_static_file('index.html')

def main():
    app.run(host='0.0.0.0', debug=True, port=8080)


if __name__ == '__main__':
    main()
