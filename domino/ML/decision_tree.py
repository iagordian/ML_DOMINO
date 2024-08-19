

from .abstratc import Model
from schemas import Domino
from order_check import balanced_mark, get_order_mark, \
    get_entrope_order_combine, is_bidirectional_balanced, \
    is_stepped_balanced, is_pair_steped_balanced, is_standart, \
    process_order_vars_full
from entrope import get_secondary_growth_entrope_full
from db import get_ml_learned

import io
import joblib
from typing import List

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

    @classmethod
    def open(cls):
        forest_model = cls.open_model(cls.forest_model_name)
        tree_model = cls.open_model(cls.tree_model_name)

        return cls(tree_model, forest_model)

    @classmethod
    def open_model(cls, model_name):

        ml_scheme = get_ml_learned(model_name)            
        bytes_container = ml_scheme.model_obj
        model = joblib.load(io.BytesIO(bytes_container))
        return model


    def predict(self, domino: Domino):
        up_data, down_data = domino.data
        return self.get_prediction(up_data), self.get_prediction(down_data)
    
    def get_prediction(self, data: List[int]):

        if is_standart(data[0]):
            return self.predict_by_model(self.tree_model, self.tree_model_process_funcs, data)
        
        return self.predict_by_model(self.forest_model, self.forest_model_process_funcs, data)
    
    def predict_by_model(self, model, process_funcks, data):
        process_data = process_order_vars_full(data, *process_funcks)
        return int(model.predict(process_data)[0])

    
    def ordered_check(self, domino: Domino):

        up, down = self.predict(domino)
        return all([
            up == domino.up[-1],
            down == domino.down[-1]
        ])