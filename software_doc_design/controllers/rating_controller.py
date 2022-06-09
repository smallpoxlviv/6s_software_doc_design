from ..controllers.abstract_controller import AbstractController
from ..models import RatingModel


class RatingController(AbstractController):
    model_class = RatingModel
    model_name = 'rating'
