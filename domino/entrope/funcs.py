
import numpy as np
from typing import List

def get_entrope(data: List[int]) -> float:
    '''Возвращает значение энтропии для переданного массива'''

    unique = np.unique(data)
    length = len(data)

    entrope = 0
    for el in unique:
        freack = np.sum(data==el) / length
        entrope += freack * np.log2(freack)

    return -entrope

def get_secondary_growth_entrope(entrope: float, data: List[int]) -> float:
    '''Возвращает прирост к энтропии при делении массива на 2'''
    return entrope - 0.5 * (get_entrope(data[:3]) + get_entrope(data[3:]))

def get_ternary_growth_entrope(entrope: float, data: List[int]) -> float:
    '''Возвращает прирост к энтропии при делении массива на 3'''
    return entrope - (1 / 3) * (get_entrope(data[:2]) + get_entrope(data[2:4]) + get_entrope(data[4:]))