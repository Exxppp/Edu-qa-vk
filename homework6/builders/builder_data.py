from utils.log import *


class DataBuilder:

    def get_data(self, name):
        data = []
        if name == 'total_number':
            data = count_lines()
        if name == 'request_type':
            data = count_request()
        if name == 'top_request':
            data = most_frequent_requests()
        if name == 'largest_requests':
            data = largest_requests_in_size_with_4xx_error()
        if name == 'top_users':
            data = users_with_5xx_error()

        self.first_record = self.get_first_input_record(name, data[0])
        self.len_data = len(data)

        return data

    def get_first_input_record(self, name: str, data: dict):
        first_record = f'{name} id=1'
        for key, value in data.items():
            first_record += f', {key}={value}'

        return first_record
