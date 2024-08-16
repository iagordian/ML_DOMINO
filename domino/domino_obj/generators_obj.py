
import random
import uuid
from typing import List, Callable

class DominoCreater:

    def __init__(self):
        self.uid = uuid.uuid4()

    def __repr__(self):
        return f'{self.uid}: {", ".join(map(str, self()))}'

    def __call__(self) -> List[int]:
        '''Генерирует линию домино'''
        return [self.func(n) for n in range(6)]

class OrderedDominoCreater(DominoCreater):

    '''
    При инициализации экземпляра принимает функцию
    для генерации упорядоченного ряда
    '''

    def __init__(self, func: Callable):
        self.func = func
        super().__init__()

class RandomDominoCreater(DominoCreater):

    '''
    Имеет собственную функцию для генерации случайного ряда домино
    '''

    def __init__(self, random_seed=None):

        self.func = lambda n: random.randint(0, 6)
        super().__init__()

        # Устанавливает random.seed для генерации воспроизводимых
        # случайных рядов домино.
        if random_seed is not None:
            random.seed(random_seed)