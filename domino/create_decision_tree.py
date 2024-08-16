
from config import RANDOM_SEED
from domino_generate import get_ordered_domino_array
from ML_learn import DominoDecisionTreeCreator
from db import model_to_db

import pandas as pd


ordered = get_ordered_domino_array(random_seed=RANDOM_SEED)

# print([(i, row[0]()) for i, row in ordered.test_data.iterrows() if row[0]() == [1, 1, 1, 3, 1, 5]])
# input()

test_rows = []
for i, first_row in ordered.test_data.iterrows():
    test_rows.append(first_row[0]())

train_rows = []
for i, first_row in ordered.train_data.iterrows():
    train_rows.append(first_row[0]())

train_data = pd.DataFrame(train_rows)
test_data = pd.DataFrame(test_rows)

decision_tree = DominoDecisionTreeCreator(train_data, test_data)
decision_tree.combine_test_data()
decision_tree.extract_order_vars()
decision_tree.fit()
decision_tree.extract_accuracy_score()
model_to_db(decision_tree.data)