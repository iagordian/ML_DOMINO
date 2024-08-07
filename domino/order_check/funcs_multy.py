
from typing import List
import numpy as np

from entrope import get_entrope, get_ternary_growth_entrope, get_secondary_growth_entrope
from .funcs_self import get_order_mark, get_binary_order_mark, get_ternary_order_mark, \
    get_secondary_order_mark, get_clear_order_mark


def get_order_marks_array(data: List[float]) -> List[float]:
    '''Возвращает массив оценок упорядоченности для массива'''

    entrope = get_entrope(data)
    entrope_secondary = get_secondary_growth_entrope(entrope, data)
    entrope_ternary = get_ternary_growth_entrope(entrope, data)

    order_degree = get_order_mark(data)
    binary_order_degree = get_binary_order_mark(data)

    clear_ordered = get_clear_order_mark(data)
    ternary_ordered = get_ternary_order_mark(data)
    secondary_ordered = get_secondary_order_mark(data)

    return [entrope, entrope_secondary, entrope_ternary, clear_ordered,
            secondary_ordered, ternary_ordered, order_degree, binary_order_degree]

def get_domino_order_marks_array(first: List[float], second: List[float], mark_array: bool=False) -> List[float]:

    if mark_array:
        first = get_order_marks_array(first)
        second = get_order_marks_array(second)

    order_difs = [(of - os) ** 2 for of, os in zip(first, second)]

    ordered_marks_array = first + second + order_difs
    return ordered_marks_array

