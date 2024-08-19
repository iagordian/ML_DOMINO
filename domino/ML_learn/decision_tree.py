
from .abstract_decision_tree import DescisionTreeLearning
from order_check import balanced_mark, get_order_mark, \
    get_entrope_order_combine, is_bidirectional_balanced, \
    is_stepped_balanced, is_pair_steped_balanced
from entrope import get_secondary_growth_entrope_full
from config import RANDOM_SEED

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier



class RandomForestClassifierCreator(DescisionTreeLearning):

    model_obj_type = RandomForestClassifier
    process_domino_funcs = [
        balanced_mark, get_secondary_growth_entrope_full,
        get_entrope_order_combine, get_order_mark
    ]
    model_params = {
        'n_estimators': 64, 
        'max_depth': 16, 
        'min_samples_split': 4, 
        'random_state': RANDOM_SEED
    }


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