


from .abstratc import Model
from domino.schemas import Domino
from domino.order_check import mark_both_domino_to_classificate
from domino.db import get_ml_learned, get_best_classifier_model

import joblib
import numpy as np
import io
from typing import List

class DominoClassificator(Model):

    def __init__(self, model, ml_scheme):
        super().__init__(model, ml_scheme)
        self.threshold = self.ml_scheme.threshold
        self.open_scaler()

    @classmethod
    def open(cls):
        '''Открывает файл с лучшей моделью классификатора'''
        best_model = get_best_classifier_model()
        return super().open(best_model)

    def order_check(self, domino: Domino) -> bool:
        '''Проверяет принадлежность переданного домино к упорядоченным'''
        up_data, down_data = domino.data
        ordered_marks_array = mark_both_domino_to_classificate(up_data, down_data)
        ordered_marks_array = self.scaler.transform(ordered_marks_array)

        return self.predict(ordered_marks_array) > self.threshold

    def open_scaler(self):
        '''Открывает объект StandardScaler'''
        ml_scheme = get_ml_learned('StandardScaler')
        bytes_container = ml_scheme.model_obj
        scaler_obj = joblib.load(io.BytesIO(bytes_container))
        self.scaler = scaler_obj

    def predict(self, ordered_marks_array: List[float]):
        '''Предсказание модели классификатора'''

        if hasattr(self.model, 'predict_proba'):
            return self.model.predict_proba(ordered_marks_array)[:, 1]
        
        if hasattr(self.model, 'predict'):
            return self.model.predict(ordered_marks_array)[0]