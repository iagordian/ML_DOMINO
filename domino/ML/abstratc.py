
from abc import ABC
import joblib
import io
from typing import Optional

from domino.db import get_ml_learned
from domino.schemas import ML_Object

class Model(ABC):

    model_name = None

    '''
    Абстрактный объект модели ML 
    '''

    def __init__(self, model, ml_scheme):
        self.model = model
        self.ml_scheme = ml_scheme

    @classmethod
    def open(cls, ml_scheme: Optional[ML_Object] = None):
        '''Читает модель из файла'''

        if ml_scheme is None:
            ml_scheme = get_ml_learned(cls.model_name)
            
        bytes_container = ml_scheme.model_obj
        model = joblib.load(io.BytesIO(bytes_container))
        return cls(model, ml_scheme)
