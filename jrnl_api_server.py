#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, abort, request, jsonify
import datetime
import os

app = Flask(__name__)
TOKEN = "/xxx"

@app.route(TOKEN+'/append_jrnl', methods=['POST'])
def append_jrnl():
    if not request.json or 'text' not in request.json:
        abort(400)
    text = request.json['text']
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M ')
    content = time + text + '\n'
    path = '/home/wogong/Dropbox/Dat/jrnl/'
    filename = path + date + '.txt'
    if not os.path.exists(filename):
        os.system(r"touch {}".format(path))
    with open(filename, 'a+') as f:
        f.write(content)
    return 'success'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8383, debug=True)

