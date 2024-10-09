
from typing import List, Optional
import numpy as np
from functools import lru_cache

def get_order_mark(data: List[int]) -> int:
    '''Возвращает оценку для упорядоченности переданной последовательности'''

    increase = 0
    reverse = 0
    equability = 0

    for i, el in enumerate(data[1:]):

        increase += el > data[i]
        reverse += el < data[i]
        equability += el == data[i]

    ordered_maks = [increase, reverse, equability] 

    return calculate_order_mark(*ordered_maks, length = len(data) - 1)

@lru_cache
def calculate_order_mark(*args, length: Optional[int] = None):

    if length is None:
        length = len(args)

    return max(args) / (length - 1)

def balanced_mark(data) -> int:
    '''Возвращает значение сбалансированности для переданного массива'''
    return len(set([np.sum(data == el) for el in data]))

