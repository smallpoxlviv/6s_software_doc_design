import json

from sqlalchemy import Column, Integer, String, Float, Text

from software_doc_design.models.abstract_model import AbstractModel


class WeekModel(AbstractModel):
    __tablename__ = 'weeks'

    pk = Column(Integer, primary_key=True)
    hours = Column(Float, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(512), nullable=False)
    videos = Column(Text(16383))
    readings = Column(Text(16383))
    quizzes = Column(Text(16383))

    def _init_from_list(self, data: list):
        self.hours = float(data[0])
        self.name = data[1]
        self.description = data[2]
        self.videos = data[3]
        self.readings = data[4]
        self.quizzes = data[5]

    def _init_from_dict(self, data: dict):
        self.hours = float(data.get('hours'))
        self.name = data.get('name')
        self.description = data.get('description')
        self.videos = data.get('videos')
        self.readings = data.get('readings')
        self.quizzes = data.get('quizzes')

    def json(self):
        return {
            'pk': self.pk,
            'hours': self.hours,
            'name': self.name,
            'description': self.description,
            'videos': json.loads(self.videos if self.videos else '[]'),
            'readings': json.loads(self.readings if self.readings else '[]'),
            'quizzes': json.loads(self.quizzes if self.quizzes else '[]'),
        }
