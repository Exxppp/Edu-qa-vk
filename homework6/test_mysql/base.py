import pytest

from models.model import TotalNumber, RequestType, TopTenRequest, TopFiveBySize, TopFiveUsers
from mysql.client import MysqlClient
from utils.builder import MysqlBuilder


class BaseSql:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.client: MysqlClient = mysql_client
        self.builder: MysqlBuilder = MysqlBuilder(self.client)
        self.prepare()

    def get_table_total_number(self, **filters):
        self.client.session.commit()
        return self.client.session.query(TotalNumber).filter_by(**filters).all()

    def get_table_request_type(self, **filters):
        self.client.session.commit()
        return self.client.session.query(RequestType).filter_by(**filters).all()

    def get_table_top_ten_request(self, **filters):
        self.client.session.commit()
        return self.client.session.query(TopTenRequest).filter_by(**filters).all()

    def get_table_top_five_by_size(self, **filters):
        self.client.session.commit()
        return self.client.session.query(TopFiveBySize).filter_by(**filters).all()

    def get_table_top_five_users(self, **filters):
        self.client.session.commit()
        return self.client.session.query(TopFiveUsers).filter_by(**filters).all()
