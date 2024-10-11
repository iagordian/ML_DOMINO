

from .abstratc import Model
from domino.schemas import Domino
from domino.order_check import complex_ensemble_funcs, process_order_vars_full
from domino.db import get_random_forest_learned

import io
import joblib
from typing import List, Optional, Tuple
import numpy as np

class DominoDecisionTree(Model):

    forest_model_process_funcs = complex_ensemble_funcs

    def __init__(self, forest_model):
        self.forest_model = forest_model


    @classmethod
    def open(cls, field_size: int):
        '''
        Извлекает из БД модели RandomForestClassifier и DecisionTreeClassifier
        и создает на их основе объект
        '''

        forest_model = get_random_forest_learned(field_size)
        bytes_container = forest_model.model_obj
        forest_model = joblib.load(io.BytesIO(bytes_container))
        return cls(forest_model)


    def predict(self, domino: Domino, upgrade: Optional[bool] = True) -> int:
        '''Предсказывает недостающее число в ряду'''
        up_data, down_data = domino.data
        up_data = self.update_input_data(up_data, upgrade=upgrade)
        down_data = self.update_input_data(down_data, upgrade=upgrade)
        up_predicted, is_sure = self.get_prediction(up_data)
        down_predicted, is_sure = self.get_prediction(down_data)
        return up_predicted, down_predicted, is_sure and is_sure
    
    
    def get_prediction(self, data) -> int:
        '''Возвращает предсказание выбранной модели принятия решений'''
        process_data = process_order_vars_full(data, self.forest_model_process_funcs)
        return int(self.forest_model.predict(process_data)[0]), bool(np.sum(self.forest_model.predict_proba(process_data)[0] > 0.4))
    
    
    def ordered_check(self, domino: Domino) -> bool:
        '''Проверяет совпадение предсказанной и реальной домино в переданном ряде'''
        up, down, is_sure = self.predict(domino, upgrade=False)
        return all([
            up == domino.up[-1],
            down == domino.down[-1],
            is_sure
        ])
    
    def update_input_data(self, data: np.ndarray, upgrade: Optional[bool] = True):

        if upgrade:
            data = np.concatenate([data, np.zeros(1)])

        return np.array(data).reshape((1, len(data)))