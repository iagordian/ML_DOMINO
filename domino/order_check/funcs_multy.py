
from typing import List
import numpy as np
import pandas as pd
from copy import copy

from entrope import get_entrope, get_ternary_growth_entrope, get_secondary_growth_entrope
from .funcs_self import get_order_mark, get_binary_order_mark, get_ternary_order_mark, \
    get_secondary_order_mark, get_clear_order_mark, is_balanced, relations_is_balanced, \
    is_binary_balanced, is_ternary_balanced, is_middle_equal, is_thernary_equal, \
    binary_relations_is_balanced


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

def get_order_vars(data):

  order_vars_data = np.zeros((data.shape[0], 84))

  if isinstance(data, pd.DataFrame):
     interations = data.values
  if isinstance(data, np.ndarray):
     interations = data

  for i, row in enumerate(interations):

    row = copy(row)

    for num in range(7):
      row[-1] = num
      entrope = get_entrope(row)
      order_mark = get_order_mark(row)
      entrope_order_combine = order_mark ** entrope

      order_vars_data[i][num * 10] = is_balanced(row)
      order_vars_data[i][num * 10 + 1] = order_mark
      order_vars_data[i][num * 10 + 2] = get_secondary_growth_entrope(entrope, row)
      order_vars_data[i][num * 10 + 3] = entrope_order_combine
      order_vars_data[i][num * 10 + 4] = get_binary_order_mark(row)
      order_vars_data[i][num * 10 + 5] = get_clear_order_mark(row)
      order_vars_data[i][num * 10 + 6] = is_binary_balanced(row)
      order_vars_data[i][num * 10 + 7] = is_ternary_balanced(row)
      order_vars_data[i][num * 10 + 8] = is_middle_equal(row)
      order_vars_data[i][num * 10 + 9] = is_thernary_equal(row)
      order_vars_data[i][num * 10 + 10] = relations_is_balanced(row)
      order_vars_data[i][num * 10 + 11] = binary_relations_is_balanced(row)

  return order_vars_data