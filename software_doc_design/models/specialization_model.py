import json

from sqlalchemy import Column, Integer, String, Text, DATETIME, ForeignKey
from sqlalchemy.orm import relationship

from software_doc_design.models.abstract_model import AbstractModel


class SpecializationModel(AbstractModel):
    __tablename__ = 'specializations'

    pk = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    how_it_works = Column(Text, nullable=True)
    faq = Column(Text, nullable=True)

    course_pk = Column(Integer, ForeignKey('courses.pk'), nullable=False)
    course = relationship("CourseModel")

    instructor_pk = Column(Integer, ForeignKey('instructors.pk'), nullable=False)
    instructor = relationship("InstructorModel")

    rating_pk = Column(Integer, ForeignKey('ratings.pk'), nullable=False)
    rating = relationship("RatingModel")

    def _init_from_list(self, data: list):
        self.name = data[0]
        self.how_it_works = data[1]
        self.faq = data[2]
        self.course_pk = int(data[3])
        self.instructor_pk = int(data[4])
        self.rating_pk = int(data[5])

    def _init_from_dict(self, data: dict):
        self.name = data.get('name')
        self.how_it_works = data.get('how_it_works')
        self.faq = data.get('faq')
        self.course_pk = int(data.get('course_pk'))
        self.instructor_pk = int(data.get('instructor_pk'))
        self.rating_pk = int(data.get('rating_pk'))

    def json(self):
        return {
            'pk': self.pk,
            'name': self.name,
            'how_it_works': self.how_it_works,
            'faq': json.loads(self.faq if self.faq else '{}'),
            'course': self.course,
            'instructor': self.instructor,
            'rating': self.rating,
            'course_pk': self.course_pk,
            'instructor_pk': self.instructor_pk,
            'rating_pk': self.rating_pk,
        }
