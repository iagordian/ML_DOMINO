
from typing import List
import numpy as np
import pandas as pd

from domino.order_check import get_order_marks_array, get_domino_order_marks_array

def extract_ordered_marks(arrays: pd.DataFrame, is_callable: bool = False) -> List[List[float]]:
        '''
        Возвращает оценки упорядоченности для переданных массивов
        '''

        rows = []

        for i, row in arrays.iterrows():
            rows.append(get_order_marks_array(row))

        return rows

def get_learning_data_combine(arrays_ordered: List[List[float]], arrays_random: List[List[float]]) -> List[List[float]]:
        '''
        Возвращает все комбинации по 2 для переданных массивов
        '''

        rows = []
        f = [1 for _ in range(len(arrays_ordered) ** 2)]
        s = [0 for _ in range(len(arrays_random) ** 2)]
        target = np.array([f + s]).reshape(-1, 1)


        for f_row in arrays_ordered:
            for s_row in arrays_ordered:
                marks = get_domino_order_marks_array(f_row, s_row)
                rows.append(marks)

        for f_row in arrays_random:
            for s_row in arrays_random:
                marks = get_domino_order_marks_array(f_row, s_row)
                rows.append(marks)

        return rows, target