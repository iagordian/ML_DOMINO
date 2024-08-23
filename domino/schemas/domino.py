
from .base import Model

from typing import List
from pydantic import Field, validator
import numpy as np

class Domino(Model):

    up: List[int] = Field(title='Верхний ряд')
    down: List[int] = Field(title='Нижний ряд')

    def __str__(self):
        f = list(map(lambda x: [x], self.up))
        s = list(map(lambda x: [x], self.down))
        return f.__repr__()[1:-1] + '\n' + s.__repr__()[1:-1]
        
    @property
    def data(self):
        return self.up, self.down
