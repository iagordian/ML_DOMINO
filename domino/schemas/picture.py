
from .base import Model

from pydantic import Field, UUID4, ConfigDict, validator
import uuid
from typing import Optional, List

class Picture(Model):
    model_config = ConfigDict(title="Изображение домино")

    uid: Optional[UUID4] = Field(default_factory=uuid.uuid4, title='Уникальный идентификатор')
    up: Optional[int] = Field(None, title='Верхнее значение')
    down: Optional[int] = Field(None, title='Нижнее значение')
    img: Optional[str] = Field(title='Изображение домино в байт')

class PicturesLst(Model):
    model_config = ConfigDict(title="Перечень изображений домино")
    pictures: List[Picture] = Field(title='Список изображений')

class PictureAnswer(Picture):
    
    @validator('img')
    def img_to_teg(cls, img_data):
        return f'<img id="answer_picture" src="data:;base64,{img_data}">'