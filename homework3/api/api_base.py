from urllib.parse import urljoin

import requests


class ResponseStatusCodeException(Exception):
    pass


class ApiBase:
    def __init__(self, login: str, password: str, base_url=None):
        if base_url is None:
            base_url = 'https://target-sandbox.my.com/'
        self.base_url = base_url
        self.login = login
        self.password = password
        self.session = requests.Session()

    def _request(self, method, location, headers=None, data=None, params=None, allow_redirects=False,
                 jsonify=False, base_url=None, json=None, expected_status=200):
        if base_url is None:
            url = urljoin(self.base_url, location)
        else:
            url = urljoin(base_url, location)

        response = self.session.request(method=method, url=url, headers=headers, data=data, params=params,
                                        allow_redirects=allow_redirects, json=json)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Expected {expected_status}, but got {response.status_code}')
        if jsonify:
            json_response: dict = response.json()

            return json_response
        return response
