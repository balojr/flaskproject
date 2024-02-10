from flask import Flask, jsonify, request
from functions import getArea as function1
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/name/<name>', methods=['GET'])
def getName(name):
    user = {
        'name': 'martin',
        'id': 1
    }

    response = {
        "error": "false",
        "data": user
    }

    return jsonify(response), 200

@app.route('/area/<radius>', methods=['GET'])
def get_area(radius):
    response = {
        "error":"false",
        "data" :  {
            'area' : function1(radius)
        }
    }
    return jsonify(response), 200

@app.route('/post-area', methods=['POST'])
def post_area():
    radius = request.json['radius']
    return get_area(radius)


if __name__ == '__main__':
    app.run()
