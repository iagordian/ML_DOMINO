
from typing import List, Optional
import numpy as np

def get_order_mark(data: List[int]) -> int:
    '''Возвращает оценку для упорядоченности переданной последовательности'''

    ordered = [
        cnt_increase(data),
        cnt_reverse(data),
        cnt_equability(data)
    ]

    if len(data) > 2:
        ordered += [
            cnt_sin(data),
            cnt_cos(data)
        ]

    return max(ordered)

def get_binary_order_mark(data: List[int]) -> float:
    '''Возвращает среднюю оценку упорядоченности между двумя половинами массива'''
    return (get_order_mark(data[:3]) + get_order_mark(data[3:])) / 2

def get_ternary_order_mark(data: List[int]) -> int:
    '''Возвращает соответствие порядка 3 частей массива друг другу'''

    return int(any([
        all([data[0] > data[1], data[2] > data[3], data[4] > data[5]]),
        all([data[0] < data[1], data[2] < data[3], data[4] < data[5]]),
        all([data[0] == data[1], data[2] == data[3], data[4] == data[5]])
    ]))

def get_secondary_order_mark(data: List[int]) -> int:
    '''Возвращает соответствие порядка 2 частей массива друг другу'''

    return int(any([
        all([data[0] > data[1], data[1] > data[2], data[3] > data[4], data[4] > data[5]]),
        all([data[0] < data[1], data[1] < data[2], data[3] < data[4], data[4] < data[5]]),
        all([data[0] == data[1], data[1] == data[2], data[3] == data[4], data[4] == data[5]])
    ]))

def get_clear_order_mark(data: List[int]) -> int:
    '''Возвращает соответствие порядка всех частей массива друг другу'''

    return int(any([
        all([data[0] > data[1], data[1] > data[2], data[2] > data[3],
             data[3] > data[4], data[4] > data[5]]),
        all([data[0] < data[1], data[1] < data[2], data[2] < data[3],
             data[3] < data[4], data[4] < data[5]]),
        all([data[0] == data[1], data[1] == data[2], data[2] == data[3],
             data[3] == data[4], data[4] == data[5]]),
    ]))

def cnt_increase(data: List[int]) -> float:
    '''Возвращает число случаев возрастания в последовательности'''
    return sum([el > data[i] for i, el in enumerate(data[1:])])

def cnt_reverse(data: List[int]) -> float:
    '''Возвращает число случаев убывания в последовательности'''
    return sum([el < data[i] for i, el in enumerate(data[1:])])

def cnt_equability(data: List[int]) -> float:
    '''Возвращает число случаев совпадения рядом стоящих элементов в последовательности'''
    return sum([el == data[i] for i, el in enumerate(data[1:])])

def cnt_sin(data: List[int]) -> float:
    '''Возвращает число случаев возрастания для четной или убывания для нечетной позиций в последовательности'''
    return sum([el > data[i] if i % 2 else el < data[i] for i, el in enumerate(data[1:])])

def cnt_cos(data: List[int]) -> float:
    '''Возвращает число случаев возрастания для нечетной или убывания для четной позиций в последовательности'''
    return sum([el > data[i] if not i % 2 else el < data[i] for i, el in enumerate(data[1:])])


def balanced_mark(data: List[int]) -> bool:
  '''Проверяет состояние сбалансированности числового ряда'''
  return len(set([np.sum(data == el) for el in np.unique(data)]))



def is_bidirectional_balanced(data, full_array=True) -> bool:
    '''Проверяет прямую упорядоченность массива между двумя его частями'''  
    conditions = [
        data[2] == data[3],
        data[1] == data[4],
    ]
    if full_array:
        conditions.append(data[0] == data[5])

    return all(conditions)

def is_stepped_balanced(data, full_array=True) -> bool:
    '''Проверяет упорядоченность массива между четными/нечетными элементами'''

    conditions = [
        data[5] - data[3] == data[3] - data[1],
    ]
    if full_array:
        conditions.append(data[4] - data[2] == data[2] - data[0])

    return all(conditions)


def is_pair_steped_balanced(data, full_array: Optional[bool]=True) -> bool:
    '''Проверяет прямую упорядоченность массива между двумя его частями'''
    conditions = [
        data[0] - data[3] == data[1] - data[4],
    ]
    if full_array:
        conditions.append(data[1] - data[4] == data[2] - data[5])

    return all(conditions)
