
from domino.domino_generate import get_random_array, get_six_ordered_domino_array

randoms = get_random_array() 
ordered = get_six_ordered_domino_array()

ordered.train_data.to_excel('train_data_base.xlsx', index=False)
ordered.test_data.to_excel('test_data_base.xlsx', index=False)
ordered.data.to_excel('data_base.xlsx', index=False)