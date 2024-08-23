
import random

from .generator_obj_abs import OrderedDominoCreater, DominoCreater

class SixOrderedDominoCreater(OrderedDominoCreater):
    pass
    
class SevenOrderedDominoCreater(OrderedDominoCreater):
    row_size = 7

class NineOrderedDominoCreater(OrderedDominoCreater):
    row_size = 9

class TenOrderedDominoCreater(OrderedDominoCreater):
    row_size = 10

class ElevenOrderedDominoCreater(OrderedDominoCreater):
    row_size = 11

class TwelveOrderedDominoCreater(OrderedDominoCreater):
    row_size = 12

class FifteenOrderedDominoCreater(OrderedDominoCreater):
    row_size = 15

class EighteenOrderedDominoCreater(OrderedDominoCreater):
    row_size = 18

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