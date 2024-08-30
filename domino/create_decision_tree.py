
from domino.config import RANDOM_SEED
from domino.ML_learn import desicions_trees_learning_objects
from domino.db import model_to_db, save_thresholdes
from domino.order_check import is_standart
from domino.schemas import ML_Object

from domino.domino_generate import get_six_ordered_domino_array, get_seven_ordered_domino_array, \
    get_nine_ordered_domino_array, get_ten_ordered_domino_array, get_eleven_ordered_domino_array, \
    get_twelve_ordered_domino_array, get_fifteen_ordered_domino_array, get_eighteen_ordered_domino_array

from sklearn.metrics import accuracy_score, f1_score
import pandas as pd
import numpy as np


ordered = get_six_ordered_domino_array(random_seed=RANDOM_SEED)

different_size_samples = [
    get_seven_ordered_domino_array().data,
    get_nine_ordered_domino_array().data,
    get_ten_ordered_domino_array().data,
    get_eleven_ordered_domino_array().data,
    get_twelve_ordered_domino_array().data,
    get_fifteen_ordered_domino_array().data,
    get_eighteen_ordered_domino_array().data,
]


test_rows = []
for i, row in ordered.test_data.iterrows():
    test_rows.append(row)

train_rows = []
for i, row in ordered.train_data.iterrows():
    train_rows.append(row)

train_data = pd.DataFrame(train_rows)
test_data = pd.DataFrame(test_rows)

creator_objects = []
test_data_processed = []

for decision_tree_creator in desicions_trees_learning_objects:

    decision_tree = decision_tree_creator(train_data, test_data)
    decision_tree.extract_order_vars()
    decision_tree.fit()
    decision_tree.to_log()
    decision_tree.save_file()
    model_to_db(decision_tree.data)
    creator_objects.append(decision_tree)
    test_data_processed.append(decision_tree.test_data)

forest_creator = creator_objects[0]
tree_creator = creator_objects[1]

for sample in different_size_samples:
    forest_creator.calculate_thresholdes(sample)
save_thresholdes(forest_creator.thresholdes)

tree_data = test_data_processed[1]
fores_data = test_data_processed[0]

model_name = 'ComplexDecisionTreeModel'
complex_model_logs = {
    'model_name': model_name
}

predicted = np.array(
    [tree_creator.get_predict(np.array([tree_data[i]])) if is_standart(list(row)) else forest_creator.get_predict(row) for i, row in enumerate(test_data.values)]
)
complex_model_logs['accuracy_6'] = accuracy_score(predicted, test_data[5])

for test_data in different_size_samples:

    tree_data = tree_creator.process_data(test_data)
    predicted = np.array(
        [tree_creator.get_predict(np.array([tree_data[i]])) if is_standart(list(row)) else forest_creator.get_predict(row) for i, row in enumerate(test_data.values)]
    )
    complex_model_logs[f'accuracy_{test_data.columns[-1] + 1}'] = accuracy_score(predicted, test_data[test_data.columns[-1]])


to_models_log_data = ML_Object(
    model_name = model_name,
    logs = complex_model_logs
)
model_to_db(to_models_log_data)