
from .base import BaseModel

from typing import List
from pydantic import Field, validator
import numpy as np

class Domino(BaseModel):

    up: List[int] = Field(title='Верхний ряд')
    down: List[int] = Field(title='Нижний ряд')

    def __str__(self):
        f = list(map(lambda x: [x], self.up))
        s = list(map(lambda x: [x], self.down))
        return f.__repr__()[1:-1] + '\n' + s.__repr__()[1:-1]
    
    @validator('up', 'down')
    def to_np(cls, domino_iterable):

        if len(domino_iterable) == 5:
            domino_iterable += [0]

        return np.array(domino_iterable)
    
    @property
    def data(self):
        up = self.up.reshape(1, 6)
        down = self.down.reshape(1, 6)
        return up, down
