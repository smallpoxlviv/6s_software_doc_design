from ..controllers.abstract_controller import AbstractController
from ..models import SyllabusModel


class SyllabusController(AbstractController):
    model_class = SyllabusModel
    model_name = 'syllabus'
