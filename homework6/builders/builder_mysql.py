from sqlalchemy import text


class MysqlBuilder:

    def __init__(self, client):
        self.client = client

    def create_table(self, table_name, data):
        if table_name == 'total_number':
            self.create_total_number(data)

        if table_name == 'request_type':
            self.create_request_type(data)

        if table_name == 'top_request':
            self.create_top_request(data)

        if table_name == 'largest_requests':
            self.create_largest_requests(data)

        if table_name == 'top_users':
            self.create_top_users(data)

    def create_total_number(self, data):
        self.client.execute_query(text('insert into `total_number` (`count`) values (:count)'),
                                  values=data)

    def create_request_type(self, data):
        self.client.execute_query(text('insert into `request_type` (`type`, `count`) values (:type, :count)'),
                                  values=data)

    def create_top_request(self, data):
        self.client.execute_query(text('insert into `top_request` (`url`, `count`) values (:url, :count)'),
                                  values=data)

    def create_largest_requests(self, data):
        self.client.execute_query(text('insert into `largest_requests` (`url`, `status_code`, `byte_size`, `ip`)'
                                       'values (:url, :status_code, :byte_size, :ip)'), values=data)

    def create_top_users(self, data):
        self.client.execute_query(text('insert into `top_users` (`ip`, `count`) values (:ip, :count)'),
                                  values=data)
