
from .base import Model

from pydantic import Field, validator
from typing import Optional, ByteString, List, AnyStr, Union

class ML_Object(Model):

    model_name: str = Field(max_length=64, primary_key=True, title='Название модели')
    model_obj: Optional[Union[ByteString, bool]] = Field(None, title='Модель в байтах')
    threshold: Optional[float] = Field(None, title='Пороговое значние')
    logs: Optional[dict] = Field(None, title='Логирование процесса обучения')
    is_the_best_classifier_model: Optional[int] = Field(None, title='Флаг лучшей модели классификации')


class ML_Objects_List(Model):
    models: List[ML_Object] = Field(title='Описание объектов ML')