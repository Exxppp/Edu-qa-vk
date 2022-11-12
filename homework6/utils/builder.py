from sqlalchemy import text

from utils.log import *


class MysqlBuilder:
    def __init__(self, client):
        self.client = client

    def create_total_number(self):
        data = count_lines()
        self.client.execute_query(f'insert into `total_number` (`count`) values ("{data}")')

    def create_request_type(self):
        data = count_request()
        self.client.execute_query(text('insert into `request_type` (`type`, `count`) values (:type, :count)'),
                                  values=data)

    def create_top_ten_request(self):
        data = most_frequent_requests()
        self.client.execute_query(text('insert into `top_ten_request` (`url`, `count`) values (:url, :count)'),
                                  values=data)

    def create_top_five_by_size(self):
        data = five_largest_requests_in_size_with_4xx_error()
        self.client.execute_query(text('insert into `top_five_by_size` (`url`, `status_code`, `byte_size`, `ip`)'
                                       'values (:url, :status_code, :byte_size, :ip)'), values=data)

    def create_top_five_users(self):
        data = top_five_users_with_5xx_error()
        self.client.execute_query(text('insert into `top_five_users` (`ip`, `count`) values (:ip, :count)'),
                                  values=data)
