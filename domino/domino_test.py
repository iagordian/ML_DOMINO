
from schemas import Domino
from ML import DominoLinearClassificator

from random import randint

ordered_f = [1, 2, 3, 4, 5, 6]
ordered_s = [6, 5, 4, 3, 2, 1]

random_f = [randint(0, 6) for _ in range(6)]
random_s = [randint(0, 6) for _ in range(6)]

domino_ordered = Domino(first=ordered_f, second=ordered_s)
domino_random = Domino(first=random_f, second=random_s)

print('Ordered:', domino_ordered, sep='\n', end='\n\n')
print('Random:', domino_random, sep='\n', end='\n\n')

linear_classificator = DominoLinearClassificator.open()

print('Ordered is ordered:', linear_classificator.order_check(domino_ordered))
print('Random is ordered:', linear_classificator.order_check(domino_random))