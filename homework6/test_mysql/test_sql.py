import pytest

from static.tables import EXISTING_TABLES
from test_mysql.base import BaseSql


@pytest.mark.parametrize('table, name',
                         tuple(zip(EXISTING_TABLES['tables'], EXISTING_TABLES['names'])))
class TestSql(BaseSql):

    def test_total_number(self, table, name):
        self.prepare(name)
        records = self.get_all_records_in_table(table)

        assert len(records) == self.data.len_data
        assert str(records[0]) == self.data.first_record
