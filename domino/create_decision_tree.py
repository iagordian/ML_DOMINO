
from domino.config import RANDOM_SEED
from domino.domino_generate import get_six_ordered_domino_array
from domino.ML_learn import desicions_trees_learning_objects
from domino.db import model_to_db
from domino.order_check import is_standart
from domino.schemas import ML_Object

from sklearn.metrics import accuracy_score, f1_score
import pandas as pd
import numpy as np


ordered = get_six_ordered_domino_array(random_seed=RANDOM_SEED)

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
    creator_objects.append(decision_tree.model_obj)
    test_data_processed.append(decision_tree.test_data)

tree = creator_objects[1]
forest = creator_objects[0]

tree_data = test_data_processed[1]
fores_data = test_data_processed[0]

predicted = np.array(
    [tree.predict([tree_data[i]])[0] if is_standart(list(row)) else forest.predict([fores_data[i]])[0] for i, row in enumerate(test_data.values)]
)

model_name = 'ComplexDecisionTreeModel'
to_models_log_data = ML_Object(
    model_name = model_name,
    logs = {
        'model_name': model_name,
        'accuracy': accuracy_score(predicted, test_data[5])
    }
)
model_to_db(to_models_log_data)