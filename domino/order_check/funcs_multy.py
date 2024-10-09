
from typing import List
import numpy as np
import pandas as pd

from domino.entrope import get_entrope, get_secondary_growth_entrope, caculate_entrope
from .funcs_self import get_order_mark


def ordered_balance(data: np.ndarray) -> float:
    
    '''Возвращает значение энтропии между случаями возрастания и убывания чисел'''

    increase = 0
    reverse = 0

    for i, el in enumerate(data[1:]):

        increase += el > data[i]
        reverse += el < data[i]

    ordered_maks = [increase, reverse]

    return caculate_entrope(*ordered_maks)


def get_entrope_order_combine(data: List[int]) -> float:
  '''Возвращает произведения энтропии для ряда и степени его упорядоченности'''
  return get_order_mark(data) * get_entrope(data)

def get_secondary_entrope_order_combine(data: List[int]) -> float:
  '''Возвращает произведения энтропии для ряда и степени его упорядоченности'''
  return get_order_mark(data) * get_secondary_growth_entrope(data)


def bidirectional_balance_entrope(data):
   iter_length = len(data) // 2
   balance = list()

   for i in range(iter_length):
      balance.append(data[i] - data[-(i + 1)])

   return len(balance) / iter_length

def hulf_balance_entrope(data):
   iter_length = len(data) // 2
   balance = list()

   for i in range(iter_length):
      balance.append(data[i] - data[i + iter_length])

   return len(balance) / iter_length

def sin_cos_entrope(data):

   sin = 0
   cos = 0
   
   for i, el in enumerate(data[1:]):
      sin += (i % 2 == 1 and el > data[i]) or (i % 2 == 0 and el < data[i])
      cos += (i % 2 == 1 and el < data[i]) or (i % 2 == 0 and el > data[i])

   return caculate_entrope(sin, cos)