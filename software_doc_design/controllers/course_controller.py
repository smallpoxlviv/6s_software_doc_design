from software_doc_design.controllers.abstract_controller import AbstractController
from software_doc_design.models import CourseModel


class CourseController(AbstractController):
    model_class = CourseModel
    model_name = 'course'
