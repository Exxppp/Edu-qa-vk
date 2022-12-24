import json
import os

from faker import Faker
from flask import Flask, jsonify, request
from werkzeug.serving import WSGIRequestHandler

app = Flask(__name__)

surname_data = {}

fake = Faker()


def generate_surname():
    return fake.lexify('???????')


@app.route('/surname', methods=['POST'])
def add_surname():
    name = json.loads(request.data)['name']
    if name not in surname_data:
        surname_data[name] = generate_surname()
        return jsonify(surname_data[name]), 201
    else:
        return jsonify(f'User_name {name} already exists: surname: {surname_data[name]}'), 400


@app.route('/surname/<name>', methods=['GET'])
def get_user_surname(name):
    if surname := surname_data.get(name):
        return jsonify(surname), 200
    else:
        return jsonify(f'Surname for user "{name}" not found'), 404


@app.route('/surname/<name>', methods=['PUT'])
def update_user_surname(name):
    surname = json.loads(request.data)['surname']

    if name in surname_data:
        surname_data[name] = surname
        return '', 204
    else:
        return jsonify(f'Surname for user "{name}" not found'), 404


@app.route('/surname/<name>', methods=['DELETE'])
def delete_user_surname(name):
    if name in surname_data:
        surname_data.pop(name)
        return '', 204
    else:
        return jsonify(f'Surname for user "{name}" not found'), 404


if __name__ == '__main__':
    host = os.environ.get('MOCK_HOST', '127.0.0.1')
    port = os.environ.get('MOCK_PORT', '8082')

    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host=host, port=port)
