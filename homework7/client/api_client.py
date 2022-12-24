from urllib.parse import urljoin

import requests

import settings


class ApiClient:
    def __init__(self):
        self.base_url = f'http://{settings.APP_HOST}:{settings.APP_PORT}'
        self.session = requests.Session()

    def _request(self, method, location, headers=None, data=None, params=None, allow_redirects=False,
                 jsonify=False, base_url=None, json=None):
        if base_url is None:
            url = urljoin(self.base_url, location)
        else:
            url = urljoin(base_url, location)

        response = self.session.request(method=method, url=url, headers=headers, data=data, params=params,
                                        allow_redirects=allow_redirects, json=json)
        if jsonify:
            json_response: dict = response.json()

            return json_response
        return response

    def create_user_by_name(self, name):
        location = '/add_user'
        data = {'name': name}
        user = self._request('POST', location, json=data)
        return user.json()

    def get_user_by_name(self, name):
        location = f'/user/{name}'
        data = {'name': name}
        user = self._request('GET', location, json=data, jsonify=True)
        return user

    def update_surname_by_name(self, name, surname):
        location = f'/user/{name}'
        data = {'surname': surname}
        self._request('PUT', location, json=data)

    def delete_user_by_name(self, name):
        location = f'/user/{name}'
        self._request('DELETE', location)
