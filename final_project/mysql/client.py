import sqlalchemy
from sqlalchemy.orm import sessionmaker
import allure
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
        self.session.commit()

    @allure.step('Добавление пользователя в базу')
    def add_user(self, user_data):
        user_data = TestUsers(**user_data, access=1)
        self.session.add(user_data)
        self.session.commit()

    @allure.step('Изменение доступа пользователя')
    def set_user_access(self, username, access_status):
        self.session.commit()
        self.session.query(TestUsers).filter(TestUsers.username == username).update({"access": access_status})
        self.session.commit()

    def get_all_fields_by_username(self, username):
        self.session.commit()
        data = self.session.query(TestUsers).filter(TestUsers.username == username).first()

        return data

