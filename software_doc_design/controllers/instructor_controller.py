from ..controllers.abstract_controller import AbstractController
from ..models import InstructorModel


class InstructorController(AbstractController):
    model_class = InstructorModel
    model_name = 'instructor'
