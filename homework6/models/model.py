from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TotalNumber(Base):
    __tablename__ = 'total_number'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'total_number id={self.id}, count={self.count}'

    id = Column(Integer, primary_key=True, autoincrement=True)
    count = Column(Integer)


class RequestType(Base):
    __tablename__ = 'request_type'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'request_type id={self.id}, type={self.type}, count={self.count}'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(VARCHAR(20))
    count = Column(Integer, nullable=False)


class TopRequest(Base):
    __tablename__ = 'top_request'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'top_request id={self.id}, url={self.url}, count={self.count}'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(VARCHAR(80), nullable=False)
    count = Column(Integer, nullable=False)


class LargestRequests(Base):
    __tablename__ = 'largest_requests'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return (f'largest_requests id={self.id}, url={self.url}, status_code={self.status_code}, '
                f'byte_size={self.byte_size}, ip={self.ip}')

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(VARCHAR(240), nullable=False)
    status_code = Column(Integer, nullable=False)
    byte_size = Column(Integer, nullable=False)
    ip = Column(VARCHAR(20), nullable=False)


class TopUsers(Base):
    __tablename__ = 'top_users'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'top_users id={self.id}, ip={self.ip}, count={self.count}'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(VARCHAR(80), nullable=False)
    count = Column(Integer, nullable=False)
