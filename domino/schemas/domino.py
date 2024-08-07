
from .base import BaseModel

from typing import List
from pydantic import Field

class Domino(BaseModel):

    first: List[int] = Field(title='Верхний ряд')
    second: List[int] = Field(title='Нижний ряд')

    def __str__(self):
        f = list(map(lambda x: [x], self.first))
        s = list(map(lambda x: [x], self.second))
        return f.__repr__()[1:-1] + '\n' + s.__repr__()[1:-1]
    
