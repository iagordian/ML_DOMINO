
from .base import BaseModel
from order_check import get_order_vars

from typing import List
from pydantic import Field, validator
import numpy as np

class Domino(BaseModel):

    first: List[int] = Field(title='Верхний ряд')
    second: List[int] = Field(title='Нижний ряд')

    def __str__(self):
        f = list(map(lambda x: [x], self.first))
        s = list(map(lambda x: [x], self.second))
        return f.__repr__()[1:-1] + '\n' + s.__repr__()[1:-1]
    
    @validator('first', 'second')
    def to_np(cls, domino_iterable):

        if len(domino_iterable) == 5:
            domino_iterable += [0]

        return np.array(domino_iterable)   
        
    @property
    def order_vars(self):
        return get_order_vars(self.first.reshape(1, 6)), get_order_vars(self.second.reshape(1, 6))
    
