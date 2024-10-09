
from typing import Optional, Callable
import numpy as np
from statistics import mean

class ProcessFunc:

  def __init__(
      self,
      base_func: Callable,
      label: str,
      procces_volume_param: Optional[str] = 'full',
  ):
    
    self.base_func = base_func
    self.label = label
    self.procces_volume_param = procces_volume_param

  def __call__(self, data: np.ndarray, extract_important: Optional[bool] = False):

    if extract_important:

      exsit = []
      for arr in self.extract_important(data):
        val = self.base_func(arr)
        exsit.append(val)

      return min(exsit)
    
    else:
      return self.base_func(data)
  
  @property
  def process_volume(self) -> int:
    return {'both': 2}.get(self.procces_volume_param, 1) * 7

  @property
  def process_full(self) -> bool:
    return self.procces_volume_param in ['full', 'both']

  @property
  def process_important(self) -> bool:
    return self.procces_volume_param in ['important', 'both']

  def extract_important(self, data: np.ndarray):

    if isinstance(data, list):
      data = np.array(list(map(int, data)))

    length = len(data)
    iteration_length = length // 2
    indexes = np.arange(length)
    for i in range(2, iteration_length):
        yield data[indexes % i == indexes[-1] % i]

  
class ProcessFuncsList:

  def __init__(self, *process_funcs):
    self.funcs = process_funcs

  def __iter__(self):
    yield from self.funcs

  @property
  def processed_data_arr_length(self):
    return sum({'both': 2}.get(func.procces_volume_param, 1) for func in self)
  
  @property
  def labels_generator(self):

    for func in self.funcs:

      if func.process_full:
        yield func.label

      if func.process_important:
        yield func.label + '\n' + '(извлечено основное)'

  @property
  def labels_generator_simple(self):

    for func in self.funcs:

      if func.process_full:
        yield func.label.replace('\n', ' ')

      if func.process_important:
        yield func.label.replace('\n', ' ') + ' (извлечено основное)'

  @property
  def lables(self):
    return list(self.labels_generator)