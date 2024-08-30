
from .abstract import LearningObject
from domino.schemas import ML_Object
from domino.best_model_container import BestModelContainer
from domino.config import DATA_PACKAGES_DIR
from domino.files_navigation import join_file_path
from domino.best_model_container import BestThresholdContainer

from abc import ABC
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
import joblib
import io
import numpy as np
from typing import Optional, ByteString


class ClassificatorLearning(LearningObject, ABC):

    def __init__(self, train_data: pd.DataFrame, train_target: pd.DataFrame, test_data: pd.DataFrame, test_target: pd.DataFrame):
        super().__init__()        

        self.test_data = test_data
        self.train_data = train_data

        self.train_target = train_target
        self.test_target = test_target

        self.scaler = StandardScaler()
        self.scale_data()

        self.f1 = None

    @property
    def scaler_data(self) -> ML_Object:
        return ML_Object(
            model_name='StandardScaler',
            model_obj=self.scaler_to_bytes()
        )
    
    def save_scaler(self):
        '''Сохранение Scaler  в файле'''
        model_name='StandardScaler_bytes'
        model_name = join_file_path(DATA_PACKAGES_DIR, model_name)
        model_obj=self.scaler_to_bytes()
        self.save_file(model_name, model_obj)
          
    def predict(self, data: np.ndarray, alpha: Optional[int]=None) -> bool:
        '''Возвращает предсказание объекта классификатора'''
        if alpha is None:
            alpha = self.threshold
        return self.model_obj.predict_proba(data)[:, 1] > alpha
    
    def scale_data(self):
        '''Применяет обучение объекта StandartScler на данные для обучения'''      
        self.test_data = self.scaler.fit_transform(self.test_data)
        self.train_data = self.scaler.transform(self.train_data)
   

    def add_weights_to_log(self):
        '''Добавляет веса элементов в предсказании моделей и добавляет в логи'''
        names = ['entrope', 'entrope_secondary', 'entrope_ternary', 'clear_ordered',
                 'secondary_ordered', 'ternary_ordered', 'order_degree', 'binary_order_degree']
        coefs = list(*self.model_obj.coef_)
        self.log_data['AUC'] = self.threshold

        self.log_data['intercept_'] = self.model_obj.intercept_[0]
        self.log_data['coef_'] = coefs
        self.log_data['col_names'] = {name: coef for name, coef in zip(names, coefs)}
    
    
    def log(self):
        '''Записывает данные модели в лог-файль'''
        self.add_weights_to_log()

        target_pred = self.predict(self.test_data)
        accuracy = accuracy_score(self.test_target, target_pred)
        recall = recall_score(self.test_target, target_pred)
        precision = precision_score(self.test_target, target_pred)

        if self.f1 is None:
            self.f1 = f1_score(self.test_target, target_pred, average='micro')
        
        self.log_data['precision'] = precision
        self.log_data['recall'] = recall
        self.log_data['accuracy'] = accuracy
        self.log_data['f1'] = self.f1

    def scaler_to_bytes(self) -> ByteString:
        '''Сохраняет StandartScler в байтовую строку'''
        bytes_container = io.BytesIO()
        joblib.dump(self.scaler, bytes_container)
        bytes_container.seek(0)

        return bytes_container.getvalue()
    
    def extract_auc(self):
        '''Выбрает наиболее опитмальный threshold для модели обучения'''

        best_auc_container = BestThresholdContainer()

        for a in range(40, 90):
            target_pred = (self.predict(self.test_data, (a / 100))).astype('int').transpose()
            f1 = f1_score(self.test_target, target_pred, average='micro')
            best_auc_container[f1] = a / 100

        self.threshold = best_auc_container.best_threshold
    
    def add_score_data(self, best_model_container: BestModelContainer):
        '''Добавляет данные о собственной ошибке в список лучших моделей'''
        best_model_container[self.f1] = self.model_name