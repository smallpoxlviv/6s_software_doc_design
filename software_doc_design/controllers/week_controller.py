from ..controllers.abstract_controller import AbstractController
from ..models.week_model import WeekModel


class WeekController(AbstractController):
    model_class = WeekModel
    model_name = 'week'
