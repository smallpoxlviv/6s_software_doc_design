from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from software_doc_design.models.abstract_model import AbstractModel


class SyllabusModel(AbstractModel):
    __tablename__ = 'syllabuses'

    pk = Column(Integer, primary_key=True)

    rating_pk = Column(Integer, ForeignKey('ratings.pk'), nullable=False)
    rating = relationship("RatingModel")

    week_pk = Column(Integer, ForeignKey('weeks.pk'), nullable=False)
    week = relationship("WeekModel")

    def _init_from_list(self, data: list):
        self.rating_pk = int(data[0])
        self.week_pk = int(data[1])

    def _init_from_dict(self, data: dict):
        self.rating_pk = int(data.get('rating_pk'))
        self.week_pk = int(data.get('week_pk'))

    def json(self):
        return {
            'pk': self.pk,
            'rating': self.rating,
            'week': self.week,
        }
