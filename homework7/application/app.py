import json
import logging
import os

import requests
from flask import Flask, request, jsonify
from werkzeug.serving import WSGIRequestHandler

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

@app.before_request
def log_request_info():
    app.logger.info('Headers: %s', dict(request.headers))
    app.logger.info('Body: %s', request.get_data())

app_data = {}
user_id_seq = 1

surname_host = os.environ['MOCK_HOST']
surname_port = os.environ['MOCK_PORT']
URL = f'http://{surname_host}:{surname_port}'


@app.route('/add_user', methods=['POST'])
def create_user():
    global user_id_seq

    user_name = json.loads(request.data)['name']
    if user_name not in app_data:
        app_data[user_name] = user_id_seq
        user_id_seq += 1

        surname = None
        try:
            data_post = {'name': user_name}
            response = requests.post(f'{URL}/surname', json=data_post)

            if response.status_code == 201:
                surname = response.json()
        except Exception as e:
            print(f'Unable to get surname from external system:\n{e}')
            print(f'No surname found for user {user_name}')

        data = {'name': user_name,
                'surname': surname}

        return jsonify(data), 201

    else:
        return jsonify(f'User_name {user_name} already exists: id: {app_data[user_name]}'), 400


@app.route('/user/<name>', methods=['GET'])
def get_user_info_by_name(name):
    if user_id := app_data.get(name):
        surname = None

        try:
            data = {'name': name}
            response = requests.get(f'{URL}/surname/{name}', json=data)
            if response.status_code == 200:
                surname = response.json()
        except Exception as e:
            print(f'Unable to get surname from external system:\n{e}')
            print(f'No surname found for user {name}')
        data = {'user_id': user_id,
                'name': name,
                'surname': surname}

        return jsonify(data), 200

    else:
        return jsonify(f'User_name {name} not found'), 404


@app.route('/user/<name>', methods=['PUT'])
def update_user_surname_by_name(name):
    surname = json.loads(request.data)['surname']

    if name in app_data:

        try:
            data = {'surname': surname}
            response = requests.put(f'{URL}/surname/{name}', json=data)

            if response.status_code == 204:
                return '', 204
        except Exception as e:
            print(f'Unable to get surname from external system:\n{e}')
            print(f'No surname found for user {name}')
    else:
        return jsonify(f'User_name {name} not found'), 404


@app.route('/user/<name>', methods=['DELETE'])
def delete_user_surname_by_name(name):
    if name in app_data:
        try:
            response = requests.delete(f'{URL}/surname/{name}')
            if response.status_code == 204:
                return '', 204

        except Exception as e:
            print(f'Unable to get surname from external system:\n{e}')
            print(f'No surname found for user {name}')
    else:
        return jsonify(f'User_name {name} not found'), 404


if __name__ == '__main__':
    host = os.environ.get('APP_HOST', '127.0.0.1')
    port = os.environ.get('APP_PORT', '8083')

    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host=host, port=port)
