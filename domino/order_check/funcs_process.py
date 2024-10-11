
from .domino_process_func_obj import ProcessFunc, ProcessFuncsList

import numpy as np
import pandas as pd
from typing import List, Callable
from copy import copy

def process_order_vars(data: np.ndarray, process_func: ProcessFunc) -> np.ndarray:
  '''Возвращает данные об упорядоченности ряда для обработки моделью'''

  order_vars_data = np.zeros((data.shape[0], process_func.process_volume))

  if isinstance(data, pd.DataFrame):
     interations = data.values
  if isinstance(data, np.ndarray):
     interations = data

  for i, row in enumerate(interations):

    row = copy(row)

    for num in range(7):
      row[-1] = num

      if process_func.process_full:
        order_vars_data[i][num] = process_func(row)

      if process_func.process_important:
        order_vars_data[i][process_func.process_full * 7 + num] = process_func(row, extract_important=True)

  return order_vars_data

def process_order_vars_full(data: np.ndarray, process_funcs: ProcessFuncsList) -> np.ndarray:
  '''Возвращает данные об упорядоченности ряда на основании нескольких функций'''
  return np.concatenate([
      process_order_vars(data, process_func) for process_func in process_funcs
  ], axis=1)


def get_order_marks_array(data: List[float], complex_ensemble_funcs: List[Callable]) -> List[float]:
    '''Возвращает массив оценок упорядоченности для массива'''

    if isinstance(data, (pd.Series, list)):
       data = np.array(data)
           
    exit = []
    for process_func in complex_ensemble_funcs:
       
       if process_func.process_full:
         val = process_func(data)
         if np.isnan(val):
            val = 0
         exit.append(val)

       if process_func.process_important:
         val = process_func(data, extract_important=True)
         if np.isnan(val):
            val = 0
         exit.append(val)

    return np.array(exit)

def get_domino_order_marks_array(first: np.ndarray, second: np.ndarray, complex_ensemble_funcs: ProcessFuncsList):
   
    return np.concatenate([
        get_order_marks_array(first, complex_ensemble_funcs).reshape(1, complex_ensemble_funcs.processed_data_arr_length),
        get_order_marks_array(second, complex_ensemble_funcs).reshape(1, complex_ensemble_funcs.processed_data_arr_length),
    ], axis=1)


def get_learning_data_combine(arrays_ordered: List[List[float]], arrays_random: List[List[float]], marcs_array_func: Callable) -> List[List[float]]:
        '''
        Возвращает все комбинации по 2 для переданных массивов
        '''

        ordered_size = len(arrays_ordered) ** 2
        random_size = len(arrays_random) ** 2

        f = np.ones(ordered_size).reshape(-1, 1)
        c = np.zeros(random_size).reshape(-1, 1)        
        target = np.concatenate([
           f, c
        ], axis=0)
        
        arrays_ordered = np.apply_along_axis(marcs_array_func, axis=1, arr=arrays_ordered)
        arrays_random = np.apply_along_axis(marcs_array_func, axis=1, arr=arrays_random)

        rows_ordered = []
        rows_random = []

        for f in arrays_ordered:
           for c in arrays_ordered:
              rows_ordered.append(np.concatenate([
                f, c
              ], axis=0))

        for f in arrays_random:
           for c in arrays_random:
              rows_random.append(np.concatenate([
                f, c
              ], axis=0))

        rows = np.concatenate([
           rows_ordered, rows_random
        ], axis=0)

        return rows, target