
import uuid
from typing import List, Callable
import numpy as np
from abc import ABC

class DominoCreater(ABC):

    row_size = None

    def __init__(self):
        self.uid = uuid.uuid4()

    def __repr__(self):
        return f'{self.uid}: {", ".join(map(str, self()))}'

    def __call__(self) -> List[int]:
        '''Генерирует линию домино'''
        return np.array([self.func(n) for n in range(self.row_size)])
    
class OrderedDominoCreater(DominoCreater):

    def __init__(self, func: Callable):
        self.func = func
        super().__init__()