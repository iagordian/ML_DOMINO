

from .abstract import LearningObject
from domino.order_check import process_order_vars_full

from abc import ABC
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

class DescisionTreeLearning(LearningObject, ABC):

    prefix = None
    process_domino_funcs = None

    def __init__(self, train_data: pd.DataFrame, test_data: pd.DataFrame):
        super().__init__()

        self.threshold = None

        self.train_data_base = train_data
        self.train_target = train_data[5]
        self.test_data_base = test_data
        self.test_target = test_data[5]

    def extract_order_vars(self):
        '''Преобразует базовые данные о наборах к анализируемым данным'''

        self.train_data = self.process_data(self.train_data_base)
        self.test_data = self.process_data(self.test_data_base)

    def process_data(self, data: pd.DataFrame):
        return process_order_vars_full(data, *self.process_domino_funcs)
    
    def get_predict(self, processed_data: np.ndarray) -> int:
        return int(self.model_obj.predict(processed_data)[0])

    def to_log(self):
        '''Сохраняет данные о собственной точности в лог'''

        predicted = self.model_obj.predict(self.test_data)
        accuracy = accuracy_score(predicted, self.test_target)
        
        self.log_data['accuracy'] = accuracy
