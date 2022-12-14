import sqlalchemy
from sqlalchemy.orm import sessionmaker

from mysql.models.model import TestUsers


class MysqlClient:

    def __init__(self, db_name, user, password):
        self.user = user
        self.port = '3306'
        self.password = password
        self.host = '127.0.0.1'
        self.db_name = db_name

        self.connection = None
        self.engine = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}'
        self.engine = sqlalchemy.create_engine(url)
        self.connection = self.engine.connect()

        session = sessionmaker(bind=self.connection.engine)
        self.session = session()

    def clear_table(self):
        self.connect(db_created=True)
        self.session.query(TestUsers).delete()

    def execute_query(self, query, fetch=False, values=None):
        if values:
            res = self.connection.execute(query, values)
        else:
            res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def get_all_records_in_table(self, table, **filters):
        self.session.commit()
        return self.session.query(table).filter_by(**filters).all()


sql = MysqlClient(user='root', password='pass', db_name='DB_MYAPP')
sql.connect()
print(sql.get_all_records_in_table(TestUsers))
