import pytest

from builders.builder_data import DataBuilder
from builders.builder_mysql import MysqlBuilder
from mysql.client import MysqlClient


class BaseSql:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.client: MysqlClient = mysql_client
        self.data: DataBuilder = DataBuilder()
        self.builder: MysqlBuilder = MysqlBuilder(self.client)

    def prepare(self, table_name):
        data = self.data.get_data(table_name)
        self.builder.create_table(table_name, data)

    def get_all_records_in_table(self, table, **filters):
        self.client.session.commit()
        return self.client.session.query(table).filter_by(**filters).all()
