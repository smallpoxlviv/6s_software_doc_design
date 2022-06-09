import json
from abc import abstractmethod

from ..db import Base, session


class AbstractModel(Base):
    __abstract__ = True

    def __init__(self, data: dict = None, data_list: list = None):
        if data_list:
            self._init_from_list(data_list)
        elif data:
            self._init_from_dict(data)

    def __str__(self):
        result = '\n'
        for key, value in self.json().items():
            result = result + f'{key}: {value}\n'
        return result

    @abstractmethod
    def _init_from_list(self, data: list):
        raise NotImplementedError

    @abstractmethod
    def _init_from_dict(self, data: dict):
        raise NotImplementedError

    @classmethod
    def __commit(cls):
        session.commit()

    def save(self):
        session.add(self)
        self.__commit()

    @classmethod
    def get_by_pk(cls, pk):
        return session.query(cls).filter_by(pk=pk).first()

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    def delete(self):
        session.delete(self)
        self.__commit()

    @abstractmethod
    def json(self):
        raise NotImplementedError
