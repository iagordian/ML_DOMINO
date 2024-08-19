

from .abstract import LearningObject
from order_check import process_order_vars_full

from abc import ABC
import pandas as pd
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


        self.train_data = process_order_vars_full(self.train_data_base, *self.process_domino_funcs)
        self.test_data = process_order_vars_full(self.test_data_base, *self.process_domino_funcs)

    def to_log(self):

        predicted = self.model_obj.predict(self.test_data)
        accuracy = accuracy_score(predicted, self.test_target)
        
        self.log_data['accuracy'] = accuracy
