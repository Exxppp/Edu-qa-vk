from urllib.parse import urljoin
from builder import Builder
import requests


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:

    def __init__(self, login: str, password: str, base_url=None):
        if base_url is None:
            base_url = 'https://target-sandbox.my.com/'
        self.base_url = base_url
        self.login = login
        self.password = password
        self.session = requests.Session()
        self.id_last_company = None
        self.id_last_segment_in_audience = None
        self.id_last_groups = None
        self.object_id_last = None

    def get_token(self):
        self._request(method='GET', location='csrf', allow_redirects=True)

    def post_login(self):
        headers = {
            'Referer': 'https://target-sandbox.my.com/',
        }

        data = {
            'email': self.login,
            'password': self.password,
            'continue': 'https://target-sandbox.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/'
        }
        self._request(method='POST', location='auth', headers=headers, data=data,
                      allow_redirects=True, base_url='https://auth-ac.my.com/')
        self.get_token()

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

    def create_company(self):
        company_data = Builder.ad()
        location = '/api/v2/campaigns.json'
        data = {"name": company_data.name,
                "objective": "general_ttm",
                "price": company_data.price,
                "package_id": 451, "banners": [{"urls": {"primary": {"id": 697543}},
                                                "textblocks": {"title_25": {"text": company_data.title},
                                                               "text_90": {"text": company_data.text}},
                                                "content": {"image_90x75": {"id": 8700}}}]}

        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken'],
        }

        company = self._request(method='POST', location=location, headers=headers, json=data, jsonify=True)

        self.id_last_company = company['id']

        return company

    def delete_company(self, id_company):
        if self.id_last_company is None:
            return
        location = '/api/v2/campaigns/mass_action.json'
        data = [
            {"id": id_company, "status": "deleted"}
        ]
        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken'],
        }
        delete_company = self._request(method='POST', location=location, headers=headers, json=data, jsonify=False,
                                       expected_status=204)
        self.id_last_company = None
        return delete_company

    def create_segment(self):
        location = 'api/v2/remarketing/segments.json'
        segment_data = Builder.segments()
        data = {"name": segment_data.name,
                "pass_condition": 1,
                "relations": [{"object_type": "remarketing_player",
                               "params": {"type": "positive",
                                          "left": 365,
                                          "right": 0}},
                              {"object_type": "remarketing_payer",
                               "params": {"type": "positive",
                                          "left": 365,
                                          "right": 0}}],
                "logicType": "or"}
        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken'],
        }
        segment = self._request(method='POST', location=location, headers=headers, json=data, jsonify=True)
        self.id_last_segment_in_audience = segment['id']

        return segment

    def delete_segment_in_audience(self, id_segment):
        location = f'/api/v2/remarketing/segments/{id_segment}.json'
        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken'],
        }
        delete_segment = self._request(method='DELETE', location=location, headers=headers, jsonify=False,
                                       expected_status=204)
        self.id_last_segment_in_audience = None

        return delete_segment

    def get_id_vk_edu(self):
        location = '/api/v2/vk_groups.json'
        params = {
            '_q': 'https://vk.com/vkedu'
        }
        id_vk_edu = self._request(method='GET', location=location, params=params, jsonify=True)

        return id_vk_edu['items'][0]['id']

    def create_data_source_vk_edu(self):
        location = '/api/v2/remarketing/vk_groups/bulk.json'
        id_vk_edu = self.get_id_vk_edu()
        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken'],
        }
        data = {
            "items": [{"object_id": id_vk_edu}]
        }
        create_data_source_vk_edu = self._request(method='POST', location=location, headers=headers, json=data,
                                                  jsonify=True, expected_status=201)
        self.id_last_groups = create_data_source_vk_edu['items'][0]['id']
        self.object_id_last = create_data_source_vk_edu['items'][0]['object_id']

        return create_data_source_vk_edu

    def delete_data_source_vk_group(self, id_vk_group):
        if self.id_last_groups is None:
            return
        location = f'/api/v2/remarketing/vk_groups/{id_vk_group}.json'
        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken'],
        }
        delete_segment = self._request(method='DELETE', location=location, headers=headers, jsonify=False,
                                       expected_status=204)
        self.id_last_groups = None

        return delete_segment

    def create_segment_vk_group(self):
        location = 'api/v2/remarketing/segments.json'
        segment_data = Builder.segments()
        data = {
            "name": segment_data.name,
            "pass_condition": 1,
            "relations": [{"object_type": "remarketing_vk_group",
                           "params": {"source_id": self.object_id_last,
                                      "type": "positive"}}],
            "logicType": "or"
        }
        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken'],
        }
        segment = self._request(method='POST', location=location, headers=headers, json=data, jsonify=True)
        self.id_last_segment_in_audience = segment['id']

        return segment
