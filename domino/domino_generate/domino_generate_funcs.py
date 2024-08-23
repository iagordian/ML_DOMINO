
from domino.domino_obj import OrderedArray, OrderedDominoCreater, \
    RandomArray
from .domino_generate_arrays import domino_array_small, seven_size_domino_array, \
    nine_size_domino_array, ten_size_domino_array, eleven_size_domino_array, \
    twelve_size_domino_array, fifteen_size_domino_array, eighteen_size_domino_array

from functools import partial
from typing import List

'''
Файл хранит в себе константные наборы Домино
для обучения ML моделей
'''

def get_ordered_domino_array(domino_funcs_array: List[OrderedDominoCreater], random_seed=None) -> OrderedArray:
    '''Возвращает набор упорядоченных рядов домино'''
    ordered_domino_array = OrderedArray(
        *domino_funcs_array
    )
    ordered_domino_array.train_test_split(random_seed)
    return ordered_domino_array

def get_random_array(random_seed=None) -> RandomArray:
    '''Возвращает набор неупорядоченных рядов домино'''
    randoms_array = RandomArray(516, random_seed=random_seed)
    randoms_array.train_test_split(random_seed)
    return randoms_array

get_six_ordered_domino_array = partial(get_ordered_domino_array, domino_array_small)
get_seven_ordered_domino_array = partial(get_ordered_domino_array, seven_size_domino_array)
get_nine_ordered_domino_array = partial(get_ordered_domino_array, nine_size_domino_array)
get_ten_ordered_domino_array = partial(get_ordered_domino_array, ten_size_domino_array)
get_eleven_ordered_domino_array = partial(get_ordered_domino_array, eleven_size_domino_array)
get_twelve_ordered_domino_array = partial(get_ordered_domino_array, twelve_size_domino_array)
get_fifteen_ordered_domino_array = partial(get_ordered_domino_array, fifteen_size_domino_array)
get_eighteen_ordered_domino_array = partial(get_ordered_domino_array, eighteen_size_domino_array)

all_samples = {
    6: domino_array_small,
    7: seven_size_domino_array,
    9: nine_size_domino_array,
    10: ten_size_domino_array,
    11: eleven_size_domino_array,
    12: twelve_size_domino_array,
    15: fifteen_size_domino_array,
    18: eighteen_size_domino_array
}