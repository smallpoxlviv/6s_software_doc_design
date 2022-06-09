import json

from sqlalchemy import Column, Integer, String, Text, DATETIME, ForeignKey
from sqlalchemy.orm import relationship

from software_doc_design.models.abstract_model import AbstractModel


class CourseModel(AbstractModel):
    __tablename__ = 'courses'

    pk = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    faq = Column(Text, nullable=True)

    instructor_pk = Column(Integer, ForeignKey('instructors.pk'), nullable=False)
    instructor = relationship("InstructorModel")

    syllabus_pk = Column(Integer, ForeignKey('syllabuses.pk'), nullable=False)
    syllabus = relationship("SyllabusModel")

    rating_pk = Column(Integer, ForeignKey('ratings.pk'), nullable=False)
    rating = relationship("RatingModel")

    comment_pk = Column(Integer, ForeignKey('comments.pk'), nullable=False)
    comment = relationship("CommentModel")

    def _init_from_list(self, data: list):
        self.name = data[0]
        self.faq = data[1]
        self.instructor_pk = int(data[2])
        self.syllabus_pk = int(data[3])
        self.rating_pk = int(data[4])
        self.comment_pk = int(data[5])

    def _init_from_dict(self, data: dict):
        self.name = data.get('name')
        self.faq = data.get('faq')
        self.instructor_pk = int(data.get('instructor_pk'))
        self.syllabus_pk = int(data.get('syllabus_pk'))
        self.rating_pk = int(data.get('rating_pk'))
        self.comment_pk = int(data.get('comment_pk'))

    def json(self):
        return {
            'pk': self.pk,
            'name': self.name,
            'faq': json.loads(self.faq if self.faq else '{}'),
            'instructor': self.instructor,
            'syllabus': self.syllabus,
            'rating': self.rating,
            'comment': self.comment,
            'instructor_pk': self.instructor_pk,
            'syllabus_pk': self.syllabus_pk,
            'rating_pk': self.rating_pk,
            'comment_pk': self.comment_pk,
        }
