
from domino.domino_generate import get_six_ordered_domino_array, \
    get_seven_ordered_domino_array, get_nine_ordered_domino_array, \
    get_ten_ordered_domino_array, get_eleven_ordered_domino_array, \
    get_twelve_ordered_domino_array, get_fifteen_ordered_domino_array, \
    get_eighteen_ordered_domino_array, all_samples

get_six_ordered_domino_array()
get_seven_ordered_domino_array()
get_nine_ordered_domino_array()
get_ten_ordered_domino_array()
get_eleven_ordered_domino_array()
get_twelve_ordered_domino_array()
get_fifteen_ordered_domino_array()
get_eighteen_ordered_domino_array()

for size, arr in all_samples.items():
    print(f'Размер выборки из рядов домино размера {size} - {len(arr)}')