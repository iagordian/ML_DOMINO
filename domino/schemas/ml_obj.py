
from .base import Model

from pydantic import Field
from typing import Optional, AnyStr

class ML_Object(Model):

    model_name: str = Field(max_length=64, primary_key=True, title='Название модели')
    model_obj: AnyStr = Field(None, title='Модель в байтах')
    threshold: Optional[float] = Field(None, title='Пороговое значние')
    logs: Optional[dict] = Field(None, title='Логирование процесса обучения')
