

from .abstratc import Model
from domino.schemas import Domino
from domino.order_check import balanced_mark, get_order_mark, \
    get_entrope_order_combine, is_bidirectional_balanced, \
    is_stepped_balanced, is_pair_steped_balanced, is_standart, \
    process_order_vars_full
from domino.entrope import get_secondary_growth_entrope_full
from domino.db import get_ml_learned, get_threshold

import io
import joblib
from typing import List, Optional, Tuple
import numpy as np

class DominoDecisionTree(Model):

    forest_model_name = 'RandomForestClassifier'
    tree_model_name = 'DecisionTreeClassifier'

    forest_model_process_funcs = [
        balanced_mark, get_secondary_growth_entrope_full,
        get_entrope_order_combine, get_order_mark
    ]

    tree_model_process_funcs = [
        is_bidirectional_balanced, is_stepped_balanced, 
        is_pair_steped_balanced,
    ]

    def __init__(self, tree_model, forest_model):
        self.forest_model = forest_model
        self.tree_model = tree_model
        self.forest_model_threshold = 0.5

    @classmethod
    def open(cls):
        '''
        Извлекает из БД модели RandomForestClassifier и DecisionTreeClassifier
        и создает на их основе объект
        '''
        forest_model = cls.open_model(cls.forest_model_name)
        tree_model = cls.open_model(cls.tree_model_name)

        return cls(tree_model, forest_model)

    @classmethod
    def open_model(cls, model_name):
        '''Извлекает из БД указанную модель'''
        ml_scheme = get_ml_learned(model_name)            
        bytes_container = ml_scheme.model_obj
        model = joblib.load(io.BytesIO(bytes_container))
        return model


    def predict(self, domino: Domino, upgrade: Optional[bool] = True) -> int:
        '''Предсказывает недостающее число в ряду'''
        up_data, down_data = domino.data
        self.forest_model_threshold = get_threshold(domino.size)
        up_data = self.update_input_data(up_data, upgrade=upgrade)
        down_data = self.update_input_data(down_data, upgrade=upgrade)
        up_predicted, up_sure = self.get_prediction(up_data)
        down_predicted, down_sure = self.get_prediction(down_data)
        return up_predicted, down_predicted, up_sure and down_sure
    
    
    def get_prediction(self, data: List[int]) -> Tuple[int, bool]:
        '''Выбирает нужную модель для предсказания числа в ряду и делает на основании этого предсказание'''

        if is_standart(data[0]):
            return self.predict_by_model(self.tree_model, self.tree_model_process_funcs, data), True
        
        predict_proba = self.predict_proba_by_model(self.forest_model, self.forest_model_process_funcs, data)

        if not self.is_predict_enouth(predict_proba):        
            while len(data[0]) > 6:
                data = data[:, 1:]
                predict_proba = self.predict_proba_by_model(self.forest_model, self.forest_model_process_funcs, data)
                if self.is_predict_enouth(predict_proba):
                    is_sure = True
                    break
            else:
                is_sure = False

        else:
            is_sure = True

        return int(np.argmax(predict_proba, axis=1)[0]), is_sure
    
    def predict_by_model(self, model, process_funcks, data) -> int:
        '''Возвращает предсказание выбранной модели принятия решений'''
        process_data = process_order_vars_full(data, *process_funcks)
        return int(model.predict(process_data)[0])
    
    def predict_proba_by_model(self, model, process_funcks, data) -> int:
        '''Возвращает предсказание выбранной модели принятия решений'''
        process_data = process_order_vars_full(data, *process_funcks)
        return model.predict_proba(process_data)
    
    def is_predict_enouth(self, predict: np.ndarray) -> bool:
        '''Проверяет, преодалевает ли вероятность в predict_proba порог значимости'''
        return bool(np.sum(predict > self.forest_model_threshold, axis=1)[0])
    
    def ordered_check(self, domino: Domino) -> bool:
        '''Проверяет совпадение предсказанной и реальной домино в переданном ряде'''
        up, down, is_sure = self.predict(domino, upgrade=False)
        return all([
            up == domino.up[-1],
            down == domino.down[-1],
            is_sure
        ])
    
    def update_input_data(self, data: List[int], upgrade: Optional[bool] = True):

        if upgrade:
            data = data + [0]

        return np.array(data).reshape((1, len(data)))