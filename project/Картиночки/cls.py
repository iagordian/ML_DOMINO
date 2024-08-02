
from typing import Callable, List
import random
import pandas as pd
import numpy as np
import uuid


class CreateDominoFunc:

    def __init__(self):
        self.uid = uuid.uuid4()

    def __repr__(self):
        return f'{self.uid}: {", ".join(map(str, self.get_line()))}'

    def get_line(self) -> List[int]:
        '''Генерирует линию домино'''
        return [self.func(n) for n in range(6)]
    
class CreateOrderedDomino(CreateDominoFunc):

    '''
    При инициализации экземпляра принимает функцию
    для генерации упорядоченного ряда
    '''

    def __init__(self, func: Callable):
        self.func = func
        super().__init__()

class CreateRandomDomino(CreateDominoFunc):

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


class Domino:

    '''
    Класс для описания набора домино
    '''

    def __init__(self, first: List[int], second: List[int]):
        self.first = first
        self.second = second

        self.first_answer = first[-1]
        self.second_answer = second[-1]

    def __repr__(self):
        return np.array([self.first, self.second]).__repr__()
    
    def mystery(self):

        '''
        Возвращает изображение рядов с замазанными крайними значениями
        '''
        
        f = self.first[:-1] + ['?']
        s = self.second[:-1] + ['?']

        mistery = pd.DataFrame([f, s], columns=range(1, 7), index=['up', 'down'])
        print(mistery)

    def answer_check(self, first_answer: int, second_answer: int):

        '''
        Проверяет принятые ответы на соответствие сохраненным
        ответам
        '''

        return all([
            first_answer == self.first_answer,
            second_answer == self.second_answer
        ])



