
from .base import Model

from pydantic import Field, validator
from typing import Optional, ByteString, List, Union
import base64
import io

class ML_Object(Model):

    model_name: str = Field(max_length=64, primary_key=True, title='Название модели')
    model_obj: Optional[Union[ByteString, str]] = Field(None, title='Модель в байтах')
    threshold: Optional[float] = Field(None, title='Пороговое значние')
    logs: Optional[dict] = Field(None, title='Логирование процесса обучения')
    is_the_best_classifier_model: Optional[int] = Field(None, title='Флаг лучшей модели классификации')

    @validator('model_obj')
    def decode(cls, model_obj):

        if isinstance(model_obj, str):
            return base64.b64decode(model_obj.encode("utf-8"))

        return model_obj

    @property
    def encoded_data(self):
        content = self.model_dump(exclude_none=True)
        if content.get('model_obj'):
            content['model_obj'] = base64.b64encode(self.model_obj).decode("utf-8") 
        return content
    

class ML_ObjectsList(Model):
    models: List[ML_Object] = Field(title='Описание объектов ML')

    @property 
    def encoded_data(self):
        return {
            'models': [
                obj.encoded_data for obj in self.models
            ]
        }
    

class RandomForestObject(Model):

    field_size: int = Field(title='Размер ряда')
    model_obj: Optional[Union[ByteString, str]] = Field(None, title='Модель в байтах')

    @validator('model_obj')
    def decode(cls, model_obj):

        if isinstance(model_obj, str):
            return base64.b64decode(model_obj.encode("utf-8"))

        return model_obj
    
    @property
    def encoded_data(self):
        content = self.model_dump(exclude_none=True)
        if content.get('model_obj'):
            content['model_obj'] = base64.b64encode(self.model_obj).decode("utf-8") 
        return content
    
    
class RandomForestObjectsList(Model):
    models: List[RandomForestObject] = Field(title='Описание объектов ML')

    @property 
    def encoded_data(self):
        return {
            'models': [
                obj.encoded_data for obj in self.models
            ]
        }
