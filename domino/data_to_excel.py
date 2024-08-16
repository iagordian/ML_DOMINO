
from domino_generate import get_random_array, get_ordered_domino_array
import pandas as pd

randoms = get_random_array() 
ordered = get_ordered_domino_array()

rows = []
test_rows = []

for i, first_row in ordered.test_data.iterrows():
    test_rows.append(first_row[0]())
    for j, second_row in ordered.test_data.iterrows():
        rows.append(first_row[0]() + second_row[0]())

# for i, first_row in randoms.data.iterrows():
#     for j, second_row in randoms.data.iterrows():
#         rows.append(list(first_row) + list(second_row))

test_data = pd.DataFrame(rows)
test_data.to_excel('test_data.xlsx', index=False)

rows = []
train_rows = []

for i, first_row in ordered.train_data.iterrows():
    train_rows.append(first_row[0]())
    for j, second_row in ordered.train_data.iterrows():
        rows.append(first_row[0]() + second_row[0]())

# for i, first_row in randoms.data.iterrows():
#     for j, second_row in randoms.data.iterrows():
#         rows.append(list(first_row) + list(second_row))

data = pd.DataFrame(rows)
data.to_excel('train_data.xlsx', index=False)

data = pd.DataFrame(train_rows)
data.to_excel('train_data_base.xlsx', index=False)

data = pd.DataFrame(test_rows)
data.to_excel('test_data_base.xlsx', index=False)