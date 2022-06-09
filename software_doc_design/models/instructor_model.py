import json

from sqlalchemy import Column, Integer, Float, String, Text

from software_doc_design.models.abstract_model import AbstractModel


class InstructorModel(AbstractModel):
    __tablename__ = 'instructors'

    pk = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    bio = Column(Text, nullable=False)
    course_ids = Column(Text, nullable=False)
    social_networks = Column(Text, nullable=False)

    def _init_from_list(self, data: list):
        self.name = data[0]
        self.bio = data[1]
        self.course_ids = data[2]
        self.social_networks = data[3]

    def _init_from_dict(self, data: dict):
        self.name = data.get('name')
        self.bio = data.get('bio')
        self.course_ids = data.get('course_ids')
        self.social_networks = data.get('social_networks')

    def json(self):
        return {
            'pk': self.pk,
            'name': self.name,
            'bio': self.bio,
            'course_ids':  json.loads(self.course_ids if self.course_ids else '[]'),
            'social_networks':  json.loads(self.social_networks if self.social_networks else '[]'),
        }
