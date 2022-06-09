from sqlalchemy import Column, Integer, Float

from software_doc_design.models.abstract_model import AbstractModel


class RatingModel(AbstractModel):
    __tablename__ = 'ratings'

    pk = Column(Integer, primary_key=True)
    ratings_count = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)

    def _init_from_list(self, data: list):
        self.ratings_count = int(data[0])
        self.rating = float(data[1])

    def _init_from_dict(self, data: dict):
        self.ratings_count = int(data.get('ratings_count'))
        self.rating = float(data.get('rating'))

    def json(self):
        return {
            'pk': self.pk,
            'ratings_count': self.ratings_count,
            'rating': self.rating,
        }
