
from .abstract import LearningObject
from order_check import get_order_vars
from config import RANDOM_SEED

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score


class DominoDecisionTreeCreator(LearningObject):

    model_obj_type = RandomForestClassifier
    model_params = {
        'n_estimators': 32, 
        'max_depth': 16, 
        'min_samples_split': 2, 
        'random_state': RANDOM_SEED
    }

    def __init__(self, train_data: pd.DataFrame, test_data: pd.DataFrame):
        super().__init__()

        self.threshold = None

        self.train_data_base = train_data
        self.train_target = train_data[5]
        self.test_data_base = test_data
        self.test_target = test_data[5]

    def extract_order_vars(self):

        self.train_data = get_order_vars(self.train_data_base)
        self.test_data = get_order_vars(self.test_data_base)

        # n_estimators = [2 ** i for i in range(11)] + [100]
        # max_depth = [2 ** i for i in range(11)]
        # min_samples_split = [2 ** i for i in range(1, 4)]
        # params = []
        # models = {}

        # for n in n_estimators:
        #     for d in max_depth:
        #         for m in min_samples_split:

        #             forest_model = RandomForestClassifier(
        #                 n_estimators=n,
        #                 max_depth=d,
        #                 min_samples_split=m,
        #                 random_state=42
        #             )

        #             forest_model.fit(self.train_data, self.train_target)
        #             test_predict = forest_model.predict(self.test_data)
        #             f1 = f1_score(self.test_target, test_predict, average='micro')

        #             if f1 not in models:
        #                 models[f1] = forest_model
        #                 params.append((f1, n, d, m))

        # params = sorted(params, reverse=True)
        # model = models[params[0][0]]

        # test_predict = model.predict(self.test_data)
        # print(test_predict[self.test_target != test_predict])
        # print(self.test_target[self.test_target != test_predict])
        # print(self.test_data_base[self.test_target != test_predict])

        # print(params[0], self.test_data_base.shape)
        # input()

    def combine_test_data(self):

        rows = []

        for first_row in self.test_data_base.values:
            for second_row in self.test_data_base.values:
                rows.append(np.concat([first_row, second_row]))

        self.test_data_global = pd.DataFrame(rows)
        self.test_data_global_target = self.test_data_global[5] * 7 + self.test_data_global[11]


    def extract_accuracy_score(self):

        up_data = get_order_vars(self.test_data_global.iloc[:, :6])
        down_data = get_order_vars(self.test_data_global.iloc[:, 6:])

        predict_global = self.model_obj.predict(up_data) * 7 + self.model_obj.predict(down_data)

        self.accuracy = accuracy_score(predict_global, self.test_data_global_target)        
        self.log_data['accuracy'] = self.accuracy
