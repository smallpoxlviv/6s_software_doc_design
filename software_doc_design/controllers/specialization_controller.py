from software_doc_design.controllers.abstract_controller import AbstractController
from software_doc_design.models import SpecializationModel


class SpecializationController(AbstractController):
    model_class = SpecializationModel
    model_name = 'specialization'
