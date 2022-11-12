from test_mysql.base import BaseSql


class TestTotalNumber(BaseSql):

    def prepare(self):
        self.builder.create_total_number()

    def test_total_number(self):
        number_of_records = self.get_table_total_number()

        assert len(number_of_records) == 1


class TestRequestType(BaseSql):

    def prepare(self):
        self.builder.create_request_type()

    def test_request_type(self):
        number_of_records = self.get_table_request_type()

        assert len(number_of_records) == 4


class TestTopTenRequest(BaseSql):

    def prepare(self):
        self.builder.create_top_ten_request()

    def test_top_ten_request(self):
        number_of_records = self.get_table_top_ten_request()

        assert len(number_of_records) == 10


class TestTopFiveBySize(BaseSql):

    def prepare(self):
        self.builder.create_top_five_by_size()

    def test_top_five_by_size(self):
        number_of_records = self.get_table_top_five_by_size()

        assert len(number_of_records) == 5


class TestTopFiveUsers(BaseSql):

    def prepare(self):
        self.builder.create_top_five_users()

    def test_top_five_users(self):
        number_of_records = self.get_table_top_five_users()

        assert len(number_of_records) == 5
