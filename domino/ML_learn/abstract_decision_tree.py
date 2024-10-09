

from .abstract import LearningObject
from domino.order_check import process_order_vars_full, complex_ensemble_funcs
from domino.schemas import RandomForestObject

from abc import ABC
from typing import Optional
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

class RandomForestLearning(LearningObject, ABC):

    model_obj_type = RandomForestClassifier
    process_domino_funcs = complex_ensemble_funcs
    field_size = None

    def __init__(self, train_data: pd.DataFrame, test_data: Optional[pd.DataFrame] = None):
        super().__init__()

        self.threshold = None

        self.train_data_base = train_data
        self.train_target = train_data.values[:, -1]
        self.test_data_base = test_data
        self.test_target = test_data.values[:, -1] if test_data is not None else None

    @property
    def data(self) -> RandomForestObject:
        return RandomForestObject(
            field_size=self.field_size,
            model_obj=self.to_bytes(),
        )

    @property
    def feature_importances(self):
        return np.sum(self.model_obj.feature_importances_.reshape(complex_ensemble_funcs.processed_data_arr_length, 7), axis=1)

    def extract_order_vars(self):
        '''Преобразует базовые данные о наборах к анализируемым данным'''

        self.train_data = self.process_data(self.train_data_base)
        
        if self.test_data_base is not None:
            self.test_data = self.process_data(self.test_data_base)
        else:
            self.test_data = None

    def process_data(self, data: pd.DataFrame):
        return process_order_vars_full(data, self.process_domino_funcs)
    
    def get_predict(self, processed_data: np.ndarray) -> int:
        return int(self.model_obj.predict(processed_data)[0])

    def to_log(self):
        '''Сохраняет данные о собственной точности в лог'''

        predicted = self.model_obj.predict(self.test_data)
        accuracy = accuracy_score(predicted, self.test_target)
        
        self.log_data['accuracy'] = accuracy

    

