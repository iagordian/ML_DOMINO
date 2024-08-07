
from .base import Model

from pydantic import Field, UUID4, ConfigDict
import uuid
from typing import Optional, List

class Picture(Model):
    model_config = ConfigDict(title="Изображение домино")

    uid: Optional[UUID4] = Field(default_factory=uuid.uuid4, title='Уникальный идентификатор')
    up: Optional[int] = Field(None, title='Верхнее значение')
    down: Optional[int] = Field(None, title='Нижнее значение')
    img: str = Field(title='Изображение домино в байт')

class PicturesLst(Model):
    model_config = ConfigDict(title="Перечень изображений домино")
    pictures: List[Picture] = Field(title='Список изображений')