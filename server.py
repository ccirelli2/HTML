#!/usr/bin/env python3
from flask import Flask, send_from_directory


# set the project root directory as the static folder, you can set others.
print(__name__)
app = Flask(__name__,  # https://stackoverflow.com/a/42791810/808603
            static_url_path='',
            static_folder='static',
            template_folder='templates')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
