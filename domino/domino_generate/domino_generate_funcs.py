
from domino.domino_obj import OrderedArray, OrderedDominoCreater, \
    RandomArray
from .simple_generate_funcs import generate_honest_stapped_rows, generate_pair_balanced_rows, \
    generate_bidirectional_balanced_rows, generate_hulf_balanced_rows
from .domino_generate_arrays import domino_array_small, seven_size_domino_array, \
    nine_size_domino_array, ten_size_domino_array, eleven_size_domino_array, \
    twelve_size_domino_array, fifteen_size_domino_array, eighteen_size_domino_array, \
    standart_domino_array, thirteen_size_domino_array, eight_size_domino_array, \
    fourteen_size_domino_array, sixteen_size_domino_array, seventeen_size_domino_array

from functools import partial
from typing import List, Optional
import pandas as pd

'''
Файл хранит в себе константные наборы Домино
для обучения ML моделей
'''

def get_ordered_domino_array(domino_funcs_array: List[OrderedDominoCreater], random_seed=None, additional_train: Optional[List[int]] = None,
                             additional_data: Optional[List[int]] = None) -> OrderedArray:
    '''Возвращает набор упорядоченных рядов домино'''
    ordered_domino_array = OrderedArray(
        *domino_funcs_array
    )
    if additional_data is not None:
        ordered_domino_array.data = pd.concat([
            ordered_domino_array.data,
            pd.DataFrame(additional_data)
        ])
    ordered_domino_array.drop_duplicates()
    ordered_domino_array.train_test_split(random_seed=random_seed)
    if additional_train is not None:
        ordered_domino_array.train_data = pd.concat([
            ordered_domino_array.train_data,
            pd.DataFrame(additional_train)
        ])

    return ordered_domino_array

def get_random_array(random_seed=None) -> RandomArray:
    '''Возвращает набор неупорядоченных рядов домино'''
    randoms_array = RandomArray(516, random_seed=random_seed)
    randoms_array.drop_duplicates()
    randoms_array.train_test_split(random_seed=random_seed)
    return randoms_array


get_seven_ordered_domino_array = partial(get_ordered_domino_array, seven_size_domino_array,
                                       additional_data=
                                            list(generate_honest_stapped_rows(size=7)) + 
                                            list(generate_pair_balanced_rows(size=7)) +
                                            list(generate_bidirectional_balanced_rows(size=7)) + 
                                            list(generate_hulf_balanced_rows(size=7)))
get_nine_ordered_domino_array = partial(get_ordered_domino_array, nine_size_domino_array,
                                       additional_data=
                                            list(generate_honest_stapped_rows(size=9)) + 
                                            list(generate_pair_balanced_rows(size=9)) +
                                            list(generate_bidirectional_balanced_rows(size=9)) + 
                                            list(generate_hulf_balanced_rows(size=9)))
get_ten_ordered_domino_array = partial(get_ordered_domino_array, ten_size_domino_array,
                                       additional_data=
                                            list(generate_honest_stapped_rows(size=10)) + 
                                            list(generate_pair_balanced_rows(size=10)) +
                                            list(generate_bidirectional_balanced_rows(size=10)) + 
                                            list(generate_hulf_balanced_rows(size=10)))
get_eleven_ordered_domino_array = partial(get_ordered_domino_array, eleven_size_domino_array,
                                       additional_data=
                                            list(generate_honest_stapped_rows(size=11)) + 
                                            list(generate_pair_balanced_rows(size=11)) +
                                            list(generate_bidirectional_balanced_rows(size=11)) + 
                                            list(generate_hulf_balanced_rows(size=11)))
get_twelve_ordered_domino_array = partial(get_ordered_domino_array, twelve_size_domino_array,
                                       additional_data=
                                            list(generate_honest_stapped_rows(size=12)) + 
                                            list(generate_pair_balanced_rows(size=12)) +
                                            list(generate_bidirectional_balanced_rows(size=12)) + 
                                            list(generate_hulf_balanced_rows(size=12)))
get_fifteen_ordered_domino_array = partial(get_ordered_domino_array, fifteen_size_domino_array,
                                       additional_data=
                                            list(generate_honest_stapped_rows(size=15)) + 
                                            list(generate_pair_balanced_rows(size=15)) +
                                            list(generate_bidirectional_balanced_rows(size=15)) + 
                                            list(generate_hulf_balanced_rows(size=15)))
get_eighteen_ordered_domino_array = partial(get_ordered_domino_array, eighteen_size_domino_array,
                                       additional_data=
                                            list(generate_honest_stapped_rows(size=18)) + 
                                            list(generate_pair_balanced_rows(size=18)) +
                                            list(generate_bidirectional_balanced_rows(size=18)) + 
                                            list(generate_hulf_balanced_rows(size=18)))
get_thirteen_size_domino_array = partial(get_ordered_domino_array, thirteen_size_domino_array,
                                       additional_data=
                                            list(generate_honest_stapped_rows(size=13)) + 
                                            list(generate_pair_balanced_rows(size=13)) +
                                            list(generate_bidirectional_balanced_rows(size=13)) + 
                                            list(generate_hulf_balanced_rows(size=13)))
get_eight_size_domino_array = partial(get_ordered_domino_array, eight_size_domino_array,
                                       additional_data=
                                            list(generate_honest_stapped_rows(size=8)) + 
                                            list(generate_pair_balanced_rows(size=8)) +
                                            list(generate_bidirectional_balanced_rows(size=8)) + 
                                            list(generate_hulf_balanced_rows(size=8)))
get_fourteen_size_domino_array = partial(get_ordered_domino_array, fourteen_size_domino_array,
                                       additional_data=
                                            list(generate_honest_stapped_rows(size=14)) + 
                                            list(generate_pair_balanced_rows(size=14)) +
                                            list(generate_bidirectional_balanced_rows(size=14)) + 
                                            list(generate_hulf_balanced_rows(size=14)))
get_sixteen_size_domino_array = partial(get_ordered_domino_array, sixteen_size_domino_array,
                                       additional_data=
                                            list(generate_honest_stapped_rows(size=16)) + 
                                            list(generate_pair_balanced_rows(size=16)) +
                                            list(generate_bidirectional_balanced_rows(size=16)) + 
                                            list(generate_hulf_balanced_rows(size=16)))
get_seventeen_size_domino_array = partial(get_ordered_domino_array, seventeen_size_domino_array,
                                       additional_data=
                                            list(generate_honest_stapped_rows(size=17)) + 
                                            list(generate_pair_balanced_rows(size=17)) +
                                            list(generate_bidirectional_balanced_rows(size=17)) + 
                                            list(generate_hulf_balanced_rows(size=17)))
get_six_ordered_domino_array = partial(get_ordered_domino_array, domino_array_small,
                                       additional_data=
                                            list(generate_honest_stapped_rows()) + 
                                            list(generate_pair_balanced_rows()) +
                                            list(generate_bidirectional_balanced_rows()) + 
                                            list(generate_hulf_balanced_rows()))

all_samples = {
    6: get_six_ordered_domino_array,
    7: get_seven_ordered_domino_array,
    8: get_eight_size_domino_array,
    9: get_nine_ordered_domino_array,
    10: get_ten_ordered_domino_array,
    11: get_eleven_ordered_domino_array,
    12: get_twelve_ordered_domino_array,
    13: get_thirteen_size_domino_array,
    14: get_fourteen_size_domino_array,
    15: get_fifteen_ordered_domino_array,
    16: get_sixteen_size_domino_array,
    17: get_seventeen_size_domino_array,
    18: get_eighteen_ordered_domino_array
}

all_samples_generators = {
    6: get_six_ordered_domino_array,
    7: get_seven_ordered_domino_array,
    8: get_eight_size_domino_array,
    9: get_nine_ordered_domino_array,
    10: get_ten_ordered_domino_array,
    11: get_eleven_ordered_domino_array,
    12: get_twelve_ordered_domino_array,
    13: get_thirteen_size_domino_array,
    14: get_fourteen_size_domino_array,
    15: get_fifteen_ordered_domino_array,
    16: get_sixteen_size_domino_array,
    17: get_seventeen_size_domino_array,
    18: get_eighteen_ordered_domino_array
}