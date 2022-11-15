from api.api_base import ApiBase
from static.data import DataBuilder


class ApiClient(ApiBase):

    def get_token(self):
        self._request(method='GET', location='csrf', allow_redirects=True)

    def post_login(self):
        headers = {
            'Referer': 'https://target-sandbox.my.com/',
        }

        data = DataBuilder.data_auth(login=self.login, password=self.password)
        self._request(method='POST', location='auth', headers=headers, data=data,
                      allow_redirects=True, base_url='https://auth-ac.my.com/')
        self.get_token()
        self.session.headers.update({'X-CSRFToken': self.session.cookies['csrftoken']})

    def create_company(self, name):
        location = '/api/v2/campaigns.json'
        data = DataBuilder.data_create_company(name)

        company = self._request(method='POST', location=location, json=data, jsonify=True)

        self.id_last_company = company['id']

    def delete_company(self, id_company):
        if self.id_last_company is None:
            return
        location = '/api/v2/campaigns/mass_action.json'
        data = DataBuilder.data_delete_company(id_company)
        self._request(method='POST', location=location, json=data, jsonify=False, expected_status=204)
        self.id_last_company = None

    def get_name_company(self):
        location = '/api/v2/campaigns.json'
        params = {'fields': 'name', '_status__in': 'active'}
        name = self._request(method='GET', location=location, params=params, jsonify=True)
        return name['items'][0]['name']

    def create_segment(self, name):
        location = 'api/v2/remarketing/segments.json'
        data = DataBuilder.data_create_segment(name)

        segment = self._request(method='POST', location=location, json=data, jsonify=True)
        self.id_last_segment_in_audience = segment['id']

    def delete_segment_in_audience(self, id_segment):
        location = f'/api/v2/remarketing/segments/{id_segment}.json'

        self._request(method='DELETE', location=location, jsonify=False, expected_status=204)
        self.id_last_segment_in_audience = None

    def get_name_segment(self):
        location = '/api/v2/remarketing/segments.json'
        params = {'fields': 'name'}

        name = self._request(method='GET', location=location, params=params, jsonify=True)
        return name['items'][0]['name']

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
        data = DataBuilder.data_create_source_vk_edu(id_vk_edu)
        create_data_source_vk_edu = self._request(method='POST', location=location, json=data,
                                                  jsonify=True, expected_status=201)
        self.id_last_groups = create_data_source_vk_edu['items'][0]['id']
        self.object_id_last = create_data_source_vk_edu['items'][0]['object_id']

    def delete_data_source_vk_group(self, id_vk_group):
        if self.id_last_groups is None:
            return
        location = f'/api/v2/remarketing/vk_groups/{id_vk_group}.json'

        self._request(method='DELETE', location=location, jsonify=False, expected_status=204)
        self.id_last_groups = None

    def create_segment_vk_group(self, name):
        location = 'api/v2/remarketing/segments.json'
        data = DataBuilder.data_create_segment_vk_edu(self.object_id_last, name)

        segment = self._request(method='POST', location=location, json=data, jsonify=True)
        self.id_last_segment_in_audience = segment['id']
