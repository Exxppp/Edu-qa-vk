from faker import Faker
from flask import Flask, jsonify
from werkzeug.serving import WSGIRequestHandler

app = Flask(__name__)

fake = Faker()
users_id = {}


@app.route('/vk_id/<username>')
def get_id(username):
    try:
        if username not in users_id:
            id_user = fake.unique.pyint()
            users_id[username] = id_user
            return jsonify({'vk_id': id_user}), 200
        else:
            return jsonify({'vk_id': users_id[username]}), 200
    except Exception:
        return jsonify({}), 404


@app.route('/status')
def status():
    return jsonify({'message': 'OK'}), 200


if __name__ == '__main__':
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host='0.0.0.0', port=8090)
