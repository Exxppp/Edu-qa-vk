from sqlalchemy import Column, Integer, VARCHAR, SmallInteger, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TestUsers(Base):
    __tablename__ = 'test_users'
    __table_arg__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255), nullable=False)
    surname = Column(VARCHAR(255), nullable=False)
    middle_name = Column(VARCHAR(255), nullable=True)
    username = Column(VARCHAR(16), nullable=True, unique=True)
    password = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(64), nullable=False, unique=True)
    access = Column(SmallInteger, nullable=True)
    active = Column(SmallInteger, nullable=True)
    start_active_time = Column(DateTime, nullable=True)
