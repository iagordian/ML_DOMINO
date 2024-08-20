
from abc import ABC
from typing import Callable
from sklearn.model_selection import train_test_split
import pandas as pd
import random

from .generators_obj import RandomDominoCreater, OrderedDominoCreater

class DominoArray(ABC):

  def print(self):
    for i, line in enumerate(self.data, start=1):
      print(f'{i}: {line}')

  @property
  def size(self):
    funcs_array_size = len(self.data)
    return f'{funcs_array_size} ({funcs_array_size ** 2} комбинаций)'

  def __iter__(self):
    yield from self.data.iterrows()

  def __len__(self):
    return len(self.data)

  def train_test_split(self, random_seed=None):
    '''Разбивка наборов на тренировочную и тестовую части'''
    random_seed = random_seed or random.randint(0, 100)
    self.train_data, self.test_data = train_test_split(self.data, test_size=0.3, random_state=random_seed)

class OrderedArray(DominoArray):

  '''
  Набор домино, созданный при помощи функции
  '''

  def __init__(self, *funcs: OrderedDominoCreater):

    self.data = pd.DataFrame(funcs)
    self.check_unitue(funcs)

  def check_unitue(self, funcs):

    '''Проверка того, что все функцию дают уникальные комбинации'''
    unique = []
    task_unique = []

    for i, func in enumerate(funcs, start=1):
      line = func()
      try:
        assert line not in unique
        assert line[:-1] not in task_unique
        assert min(line) >= 0
        assert max(line) <= 6
      except Exception as e:
        print(line)
        print(i)
        raise e
      unique.append(line)
      task_unique.append(line[:-1])


  def try_func(self, func: Callable) -> bool:
    '''Проверяет, генерирует ли переданная функция новую последовательность'''
    line = [func(i) for i in range(6)]
    return all([
      line not in self.data,
      line[:-1] not in self.task_data
    ])

class RandomArray(OrderedArray):
  '''
  Набор домино, созданный при помощи генератора случайных чисел
  '''

  def __init__(self, size, random_seed=None):

    data = []
    creater = RandomDominoCreater(random_seed)
    while len(data) != size:
      line = creater()

      # Ограничение на последовательность - уникальных элементов должно быть больше 2
      if len(set(line)) > 2:
        data.append(list(line))

    self.data = pd.DataFrame(data)