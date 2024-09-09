
from .abstract_decision_tree import DescisionTreeLearning
from domino.order_check import balanced_mark, get_order_mark, \
    get_entrope_order_combine, is_bidirectional_balanced, \
    is_stepped_balanced, is_pair_steped_balanced, \
    honest_ordered_combine, difs_balance, difs_order_combine, \
    ordered_balance_entrope_combine

from domino.entrope import get_secondary_growth_entrope_full
from domino.config import RANDOM_SEED
from domino.best_model_container import BestThresholdContainer

import pandas as pd
import numpy as np
from typing import Optional
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score




class RandomForestClassifierCreator(DescisionTreeLearning):

    model_obj_type = RandomForestClassifier
    process_domino_funcs = [
        balanced_mark, get_secondary_growth_entrope_full,
        get_entrope_order_combine, get_order_mark,
        honest_ordered_combine, difs_balance,
        difs_order_combine, ordered_balance_entrope_combine
    ]
    model_params = {
        'n_estimators': 128, 
        'max_depth': 16, 
        'min_samples_split': 4, 
        'random_state': RANDOM_SEED
    }
    thresholdes = {}

    def calculate_thresholdes(self, test_data: pd.DataFrame):

        sample_size, arr_size = test_data.shape 
        best_threshold_container = BestThresholdContainer()

        for t in range(5, 100, 5):

            test_target = test_data[arr_size - 1]
            predicted = []
            threshold = t / 100

            for ind in range(sample_size):
                
                test_arr = test_data.iloc[ind]
                predicted.append(self.get_predict(test_arr, threshold))

            best_threshold_container[accuracy_score(test_target, predicted)] = threshold

        self.thresholdes[arr_size] = best_threshold_container.best_threshold

    def get_predict(self, data: np.ndarray, threshold: Optional[float] = None) -> int:

        arr_size = len(data)
        if arr_size == 6:
            processed_data = self.process_data(np.array([data]))
            return super().get_predict(processed_data)

        if threshold is None:
            threshold = self.thresholdes[arr_size]

        while len(data) > 6:
            processed_data = self.process_data(np.array([data]))
            predict_proba = self.model_obj.predict_proba(processed_data)

            if np.sum(predict_proba > threshold, axis=1)[0]:
                return int(np.argmax(predict_proba, axis=1)[0])

            data = data[1:]

        else:
            processed_data = self.process_data(np.array([data]))
            return super().get_predict(processed_data)
        
    
class DescisionTreeCreator(DescisionTreeLearning):

    model_obj_type = DecisionTreeClassifier
    process_domino_funcs = [
        is_bidirectional_balanced, is_stepped_balanced, 
        is_pair_steped_balanced,
    ]
    model_params = {
        'max_depth': 32, 
        'min_samples_split': 4, 
        'random_state': RANDOM_SEED
    }



desicions_trees_learning_objects = [
    RandomForestClassifierCreator,
    DescisionTreeCreator
]