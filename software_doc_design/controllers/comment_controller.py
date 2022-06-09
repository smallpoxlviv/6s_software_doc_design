from software_doc_design.controllers.abstract_controller import AbstractController
from software_doc_design.models import CommentModel


class CommentController(AbstractController):
    model_class = CommentModel
    model_name = 'comment'
