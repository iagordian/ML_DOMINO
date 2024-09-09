
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
    center = len(data) // 2
    return entrope - 0.5 * (get_entrope(data[:center]) + get_entrope(data[center:]))

def get_ternary_growth_entrope(entrope: float, data: List[int]) -> float:
    '''Возвращает прирост к энтропии при делении массива на 3'''    
    third = len(data) // 3
    return entrope - (1 / 3) * (get_entrope(data[:third]) + get_entrope(data[third:third * 2]) + get_entrope(data[third * 2:]))

def get_secondary_growth_entrope_full(data: List[int]) -> float:
    '''Возвращает прирост к энтропии при делении массива на 2'''
    entrope = get_entrope(data)
    center = len(data) // 2
    return entrope - 0.5 * (get_entrope(data[:center]) + get_entrope(data[center:]))

def get_ternary_growth_entrope_full(data: List[int]) -> float:
    '''Возвращает прирост к энтропии при делении массива на 3'''    
    entrope = get_entrope(data)
    third = len(data) // 3
    return entrope - (1 / 3) * (get_entrope(data[:third]) + get_entrope(data[third:third * 2]) + get_entrope(data[third * 2:]))