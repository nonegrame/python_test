import json

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return json.dumps('{"data": "hello"}')
