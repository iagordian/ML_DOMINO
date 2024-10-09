
import numpy as np
from typing import List, Optional
from functools import lru_cache

@lru_cache
def caculate_entrope(*args, total=None) -> float:
  '''Возвращает значение энтропии для переданных элементов'''

  if total is None:
    total = sum(args)

  if total == 0:
     return 0

  args = map(lambda arg: arg / total, args)
  result = sum(arg * np.log2(to_log(arg)) for arg in args)
  return -result

def to_log(val):
   return val or 1

def get_entrope(data: np.ndarray) -> float:
    '''Возвращает значение энтропии для переданного массива'''

    elems = np.unique(data)
    elems_cnt = [np.sum(data==el) for el in elems]
    return caculate_entrope(*elems_cnt, total=len(data))

def entrope_change(data):
    return get_entrope(data) - get_entrope(data[:-1])

def get_secondary_growth_entrope(data: np.ndarray, entrope: Optional[float] = None) -> float:
    '''Возвращает прирост к энтропии при делении массива на 2'''
    if entrope is None:
        entrope = get_entrope(data)
    center = len(data) // 2
    return entrope - 0.5 * (get_entrope(data[:center]) + get_entrope(data[center:]))


