import json

from sqlalchemy import Column, Integer, String, Text, DATETIME

from software_doc_design.models.abstract_model import AbstractModel


class CommentModel(AbstractModel):
    __tablename__ = 'comments'

    pk = Column(Integer, primary_key=True)
    data = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    comment = Column(Text, nullable=False)

    def _init_from_list(self, data: list):
        self.data = data[0]
        self.author = data[1]
        self.comment = data[2]

    def _init_from_dict(self, data: dict):
        self.data = data.get('data')
        self.author = data.get('author')
        self.comment = data.get('comment')

    def json(self):
        return {
            'pk': self.pk,
            'data': self.data,
            'author': self.author,
            'comment': self.comment,
        }
