from dataclasses import dataclass

from flask import redirect

from software_doc_design.exceptions import NotFoundException
from software_doc_design.models.abstract_model import AbstractModel


@dataclass
class AbstractController:
    model_class: AbstractModel.__class__ = None
    model_name: str = None

    @classmethod
    def _save_model(cls, model: AbstractModel):
        try:
            model.save()
            return redirect('/')
        except Exception as exc:
            return f"error: {exc}"

    @classmethod
    def get(cls, pk: int):
        obj = cls.model_class.get_by_pk(pk=pk)
        if obj:
            return obj.json()
        raise NotFoundException(cls.model_name)

    @classmethod
    def get_all(cls):
        items = cls.model_class.get_all()
        return [item.json() for item in items]

    @classmethod
    def post(cls, data: dict):
        item = cls.model_class(data=data)
        return cls._save_model(item)

    @classmethod
    def put(cls, pk: int, data: dict):
        item = cls.model_class.get_by_pk(pk=pk)
        if item:
            for k, v in data.items():
                if v and hasattr(item, k):
                    setattr(item, k, v)
        else:
            item = cls.model_class(**data)
        return cls._save_model(item)

    @classmethod
    def delete(cls, pk):
        item = cls.model_class.get_by_pk(pk)
        if item:
            item.delete()
            return redirect('/')
        raise NotFoundException(cls.model_name)
