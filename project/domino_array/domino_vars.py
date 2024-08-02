
from domino_obj import OrderedArray, OrderedDominoCreater, \
    RandomArray


'''
Файл хранит в себе константные наборы Домино
для обучения ML моделей
'''

ordered_domino_array = OrderedArray(
    OrderedDominoCreater(lambda x: x),
    OrderedDominoCreater(lambda x: x + 1),
    OrderedDominoCreater(lambda x: 0),
    OrderedDominoCreater(lambda x: 1),
    OrderedDominoCreater(lambda x: 2),
    OrderedDominoCreater(lambda x: 3),
    OrderedDominoCreater(lambda x: 4),
    OrderedDominoCreater(lambda x: 5),
    OrderedDominoCreater(lambda x: 6),
    OrderedDominoCreater(lambda x: 6 - x),
    OrderedDominoCreater(lambda x: 5 - x),
    OrderedDominoCreater(lambda x: x % 2),
    OrderedDominoCreater(lambda x: int(x % 2 == 0)),
    OrderedDominoCreater(lambda x: x % 2 + 1),
    OrderedDominoCreater(lambda x: x % 2 + 2),
    OrderedDominoCreater(lambda x: x % 2 + 3),
    OrderedDominoCreater(lambda x: x % 2 + 4),
    OrderedDominoCreater(lambda x: x % 2 + 5),

    OrderedDominoCreater(lambda x: x if x % 2 else 0),
    OrderedDominoCreater(lambda x: x if x % 2 else 6),
    OrderedDominoCreater(lambda x: x if x % 2 else 5),
    OrderedDominoCreater(lambda x: x if x % 2 else 4),
    OrderedDominoCreater(lambda x: x if x % 2 else 3),
    OrderedDominoCreater(lambda x: x if x % 2 else 2),
    OrderedDominoCreater(lambda x: x if x % 2 else 1),

    OrderedDominoCreater(lambda x: x if not x % 2 else 0),
    OrderedDominoCreater(lambda x: x if not x % 2 else 6),
    OrderedDominoCreater(lambda x: x if not x % 2 else 5),
    OrderedDominoCreater(lambda x: x if not x % 2 else 4),
    OrderedDominoCreater(lambda x: x if not x % 2 else 3),
    OrderedDominoCreater(lambda x: x if not x % 2 else 1),

    OrderedDominoCreater(lambda x: (x % 4) + 1),
    OrderedDominoCreater(lambda x: (x % 3) + 1),
    OrderedDominoCreater(lambda x: (x % 4)),
    OrderedDominoCreater(lambda x: (x % 3)),

    OrderedDominoCreater(lambda x: 2 if x % 2 else 0),
    OrderedDominoCreater(lambda x: 3 if x % 2 else 0),
    OrderedDominoCreater(lambda x: 4 if x % 2 else 0),
    OrderedDominoCreater(lambda x: 5 if x % 2 else 0),
    OrderedDominoCreater(lambda x: 6 if x % 2 else 0),

    OrderedDominoCreater(lambda x: 2 if x % 2 == 0 else 0),
    OrderedDominoCreater(lambda x: 3 if x % 2 == 0 else 0),
    OrderedDominoCreater(lambda x: 4 if x % 2 == 0 else 0),
    OrderedDominoCreater(lambda x: 5 if x % 2 == 0 else 0),
    OrderedDominoCreater(lambda x: 6 if x % 2 == 0 else 0),

    OrderedDominoCreater(lambda x: 3 if x % 2 else 1),
    OrderedDominoCreater(lambda x: 4 if x % 2 else 1),
    OrderedDominoCreater(lambda x: 5 if x % 2 else 1),
    OrderedDominoCreater(lambda x: 6 if x % 2 else 1),

    OrderedDominoCreater(lambda x: 2 if x % 2 == 0 else 1),
    OrderedDominoCreater(lambda x: 3 if x % 2 == 0 else 1),
    OrderedDominoCreater(lambda x: 4 if x % 2 == 0 else 1),
    OrderedDominoCreater(lambda x: 5 if x % 2 == 0 else 1),
    OrderedDominoCreater(lambda x: 6 if x % 2 == 0 else 1),

    OrderedDominoCreater(lambda x: 4 if x % 2 else 2),
    OrderedDominoCreater(lambda x: 5 if x % 2 else 2),
    OrderedDominoCreater(lambda x: 6 if x % 2 else 2),

    OrderedDominoCreater(lambda x: 3 if x % 2 == 0 else 2),
    OrderedDominoCreater(lambda x: 4 if x % 2 == 0 else 2),
    OrderedDominoCreater(lambda x: 5 if x % 2 == 0 else 2),
    OrderedDominoCreater(lambda x: 6 if x % 2 == 0 else 2),

    OrderedDominoCreater(lambda x: 5 if x % 2 else 3),
    OrderedDominoCreater(lambda x: 6 if x % 2 else 3),

    OrderedDominoCreater(lambda x: 4 if x % 2 == 0 else 3),
    OrderedDominoCreater(lambda x: 5 if x % 2 == 0 else 3),
    OrderedDominoCreater(lambda x: 6 if x % 2 == 0 else 3),

    OrderedDominoCreater(lambda x: 6 if x % 2 else 4),
    OrderedDominoCreater(lambda x: 6 if x % 2 == 0 else 4),

    OrderedDominoCreater(lambda x: x // 2),
    OrderedDominoCreater(lambda x: x // 3),

    OrderedDominoCreater(lambda x: 1 if x < 3 else 0),
    OrderedDominoCreater(lambda x: 1 if x < 3 else 2),
    OrderedDominoCreater(lambda x: 1 if x < 3 else 3),
    OrderedDominoCreater(lambda x: 1 if x < 3 else 4),
    OrderedDominoCreater(lambda x: 1 if x < 3 else 5),
    OrderedDominoCreater(lambda x: 1 if x < 3 else 6),

    OrderedDominoCreater(lambda x: 2 if x < 3 else 0),
    OrderedDominoCreater(lambda x: 2 if x < 3 else 1),
    OrderedDominoCreater(lambda x: 2 if x < 3 else 3),
    OrderedDominoCreater(lambda x: 2 if x < 3 else 4),
    OrderedDominoCreater(lambda x: 2 if x < 3 else 5),
    OrderedDominoCreater(lambda x: 2 if x < 3 else 6),

    OrderedDominoCreater(lambda x: 3 if x < 3 else 0),
    OrderedDominoCreater(lambda x: 3 if x < 3 else 2),
    OrderedDominoCreater(lambda x: 3 if x < 3 else 1),
    OrderedDominoCreater(lambda x: 3 if x < 3 else 4),
    OrderedDominoCreater(lambda x: 3 if x < 3 else 5),
    OrderedDominoCreater(lambda x: 3 if x < 3 else 6),

    OrderedDominoCreater(lambda x: 4 if x < 3 else 0),
    OrderedDominoCreater(lambda x: 4 if x < 3 else 2),
    OrderedDominoCreater(lambda x: 4 if x < 3 else 3),
    OrderedDominoCreater(lambda x: 4 if x < 3 else 1),
    OrderedDominoCreater(lambda x: 4 if x < 3 else 5),
    OrderedDominoCreater(lambda x: 4 if x < 3 else 6),

    OrderedDominoCreater(lambda x: 5 if x < 3 else 0),
    OrderedDominoCreater(lambda x: 5 if x < 3 else 2),
    OrderedDominoCreater(lambda x: 5 if x < 3 else 3),
    OrderedDominoCreater(lambda x: 5 if x < 3 else 1),
    OrderedDominoCreater(lambda x: 5 if x < 3 else 4),
    OrderedDominoCreater(lambda x: 5 if x < 3 else 6),

    OrderedDominoCreater(lambda x: 6 if x < 3 else 0),
    OrderedDominoCreater(lambda x: 6 if x < 3 else 2),
    OrderedDominoCreater(lambda x: 6 if x < 3 else 3),
    OrderedDominoCreater(lambda x: 6 if x < 3 else 5),
    OrderedDominoCreater(lambda x: 6 if x < 3 else 4),
    OrderedDominoCreater(lambda x: 6 if x < 3 else 1),

    OrderedDominoCreater(lambda x: 0 if x < 3 else 6),
    OrderedDominoCreater(lambda x: 0 if x < 3 else 2),
    OrderedDominoCreater(lambda x: 0 if x < 3 else 3),
    OrderedDominoCreater(lambda x: 0 if x < 3 else 5),
    OrderedDominoCreater(lambda x: 0 if x < 3 else 4),

    OrderedDominoCreater(lambda x: 1 if x < 2 else 2 if x < 4 else 3),
    OrderedDominoCreater(lambda x: 2 if x < 2 else 3 if x < 4 else 4),
    OrderedDominoCreater(lambda x: 3 if x < 2 else 4 if x < 4 else 5),
    OrderedDominoCreater(lambda x: 4 if x < 2 else 5 if x < 4 else 6),
    OrderedDominoCreater(lambda x: 2 if x < 2 else 4 if x < 4 else 6),

    OrderedDominoCreater(lambda x: 1 if x < 2 else 2 if x < 4 else 1),
    OrderedDominoCreater(lambda x: 2 if x < 2 else 3 if x < 4 else 2),
    OrderedDominoCreater(lambda x: 3 if x < 2 else 4 if x < 4 else 3),
    OrderedDominoCreater(lambda x: 4 if x < 2 else 5 if x < 4 else 4),
    OrderedDominoCreater(lambda x: 2 if x < 2 else 4 if x < 4 else 5),

    OrderedDominoCreater(lambda x: 2 * x % 3),
    OrderedDominoCreater(lambda x: 2 * x % 5),
    OrderedDominoCreater(lambda x: 2 * x % 6),
    OrderedDominoCreater(lambda x: 3 * (x % 3)),

    OrderedDominoCreater(lambda x: 3 + x if x < 3 else x - 3),
    OrderedDominoCreater(lambda x: (3 + x if x < 3 else x - 3) + 1),

    OrderedDominoCreater(lambda x: 6 - x % 2),
    OrderedDominoCreater(lambda x: 5 - x % 2),

    OrderedDominoCreater(lambda x: 6 - x % 3),
    OrderedDominoCreater(lambda x: 5 - x % 3),
    OrderedDominoCreater(lambda x: 4 - x % 3),
    OrderedDominoCreater(lambda x: 3 - x % 3),
    OrderedDominoCreater(lambda x: 2 - x % 3),

    OrderedDominoCreater(lambda x: 6 - (x % 3) * 2),
    OrderedDominoCreater(lambda x: 5 - (x % 3) * 2),

    OrderedDominoCreater(lambda x: 2 - x if x < 3 else x - 3),
    OrderedDominoCreater(lambda x: 3 - x if x < 3 else x - 2),
    OrderedDominoCreater(lambda x: 4 - x if x < 3 else x - 1),
    OrderedDominoCreater(lambda x: 5 - x if x < 3 else x),
    OrderedDominoCreater(lambda x: 6 - x if x < 3 else x + 1),

    OrderedDominoCreater(lambda x: 5 - x * 2 if x < 3 else x - (5 - x)),
    OrderedDominoCreater(lambda x: 6 - x * 2 if x < 3 else x - (4 - x)),
    OrderedDominoCreater(lambda x: 4 - x * 2 if x < 3 else x - (6 - x)),

    OrderedDominoCreater(lambda x: 6 - 3 * x if x < 3 else (x - 3) * 3),

    OrderedDominoCreater(lambda x: x - x % 2),
    OrderedDominoCreater(lambda x: (6 - x) + x % 2),

    OrderedDominoCreater(lambda x: x - x % 2 if x < 2 else x - x % 2 - 1),
    OrderedDominoCreater(lambda x: (6 - x) + x % 2 if x < 2 else (6 - x) + x % 2 - 1 if x < 4 else 0),

    OrderedDominoCreater(lambda x: x if x < 3 else 5 - x),
    OrderedDominoCreater(lambda x: x + 1 if x < 3 else 5 - (x - 1)),
    OrderedDominoCreater(lambda x: x + 2 if x < 3 else 6 - (x - 1)),
    OrderedDominoCreater(lambda x: x + 3 if x < 3 else 7 - (x - 1)),
    OrderedDominoCreater(lambda x: x + 4 if x < 3 else 8 - (x - 1)),

    OrderedDominoCreater(lambda x: x * 2 if x < 3 else (5 - x) * 2),
    OrderedDominoCreater(lambda x: x * 3 if x < 3 else (5 - x) * 3),
    OrderedDominoCreater(lambda x: (x + 1) * 2 if x < 3 else (5 - x) * 2 + 2),

    OrderedDominoCreater(lambda x: x % 2 if x < 3 else int(not (x % 2))),
    OrderedDominoCreater(lambda x: x % 2 + 1 if x < 3 else int(not (x % 2)) + 1),
    OrderedDominoCreater(lambda x: x % 2 + 2 if x < 3 else int(not (x % 2)) + 2),
    OrderedDominoCreater(lambda x: x % 2 + 4 if x < 3 else int(not (x % 2)) + 4),
    OrderedDominoCreater(lambda x: x % 2 + 5 if x < 3 else int(not (x % 2)) + 5),

    OrderedDominoCreater(lambda x: (x % 2 + 1 if x % 2 else 0) if x < 3 else (int(not (x % 2)) + 1) if not (x % 2) else 0),
    OrderedDominoCreater(lambda x: (x % 2 + 2 if x % 2 else 0) if x < 3 else (int(not (x % 2)) + 2) if not (x % 2) else 0),
    OrderedDominoCreater(lambda x: (x % 2 + 3 if x % 2 else 0) if x < 3 else (int(not (x % 2)) + 3) if not (x % 2) else 0),
    OrderedDominoCreater(lambda x: (x % 2 + 4 if x % 2 else 0) if x < 3 else (int(not (x % 2)) + 4) if not (x % 2) else 0),
    OrderedDominoCreater(lambda x: (x % 2 + 5 if x % 2 else 0) if x < 3 else (int(not (x % 2)) + 5) if not (x % 2) else 0),

    OrderedDominoCreater(lambda x: (x % 2 + 1 if not x % 2 else 0) if x < 3 else (int(not (x % 2)) + 1) if (x % 2) else 0),
    OrderedDominoCreater(lambda x: (x % 2 + 2 if not x % 2 else 0) if x < 3 else (int(not (x % 2)) + 2) if (x % 2) else 0),
    OrderedDominoCreater(lambda x: (x % 2 + 3 if not x % 2 else 0) if x < 3 else (int(not (x % 2)) + 3) if (x % 2) else 0),
    OrderedDominoCreater(lambda x: (x % 2 + 4 if not x % 2 else 0) if x < 3 else (int(not (x % 2)) + 4) if (x % 2) else 0),
    OrderedDominoCreater(lambda x: (x % 2 + 5 if not x % 2 else 0) if x < 3 else (int(not (x % 2)) + 5) if (x % 2) else 0),
    OrderedDominoCreater(lambda x: (x % 2 + 6 if not x % 2 else 0) if x < 3 else (int(not (x % 2)) + 6) if (x % 2) else 0),

    OrderedDominoCreater(lambda x: (x % 2 + 2 if x % 2 else 1) if x < 3 else (int(not (x % 2)) + 2) if not (x % 2) else 1),
    OrderedDominoCreater(lambda x: (x % 2 + 3 if x % 2 else 1) if x < 3 else (int(not (x % 2)) + 3) if not (x % 2) else 1),
    OrderedDominoCreater(lambda x: (x % 2 + 4 if x % 2 else 1) if x < 3 else (int(not (x % 2)) + 4) if not (x % 2) else 1),
    OrderedDominoCreater(lambda x: (x % 2 + 5 if x % 2 else 1) if x < 3 else (int(not (x % 2)) + 5) if not (x % 2) else 1),

    OrderedDominoCreater(lambda x: (x % 2 + 2 if not x % 2 else 1) if x < 3 else (int(not (x % 2)) + 2) if (x % 2) else 1),
    OrderedDominoCreater(lambda x: (x % 2 + 3 if not x % 2 else 1) if x < 3 else (int(not (x % 2)) + 3) if (x % 2) else 1),
    OrderedDominoCreater(lambda x: (x % 2 + 4 if not x % 2 else 1) if x < 3 else (int(not (x % 2)) + 4) if (x % 2) else 1),
    OrderedDominoCreater(lambda x: (x % 2 + 5 if not x % 2 else 1) if x < 3 else (int(not (x % 2)) + 5) if (x % 2) else 1),
    OrderedDominoCreater(lambda x: (x % 2 + 6 if not x % 2 else 1) if x < 3 else (int(not (x % 2)) + 6) if (x % 2) else 1),

    OrderedDominoCreater(lambda x: (x % 2 + 3 if x % 2 else 2) if x < 3 else (int(not (x % 2)) + 3) if not (x % 2) else 2),
    OrderedDominoCreater(lambda x: (x % 2 + 4 if x % 2 else 2) if x < 3 else (int(not (x % 2)) + 4) if not (x % 2) else 2),
    OrderedDominoCreater(lambda x: (x % 2 + 5 if x % 2 else 2) if x < 3 else (int(not (x % 2)) + 5) if not (x % 2) else 2),

    OrderedDominoCreater(lambda x: (x % 2 + 3 if not x % 2 else 2) if x < 3 else (int(not (x % 2)) + 3) if (x % 2) else 2),
    OrderedDominoCreater(lambda x: (x % 2 + 4 if not x % 2 else 2) if x < 3 else (int(not (x % 2)) + 4) if (x % 2) else 2),
    OrderedDominoCreater(lambda x: (x % 2 + 5 if not x % 2 else 2) if x < 3 else (int(not (x % 2)) + 5) if (x % 2) else 2),
    OrderedDominoCreater(lambda x: (x % 2 + 6 if not x % 2 else 2) if x < 3 else (int(not (x % 2)) + 6) if (x % 2) else 2),

    OrderedDominoCreater(lambda x: (x % 2 + 4 if x % 2 else 3) if x < 3 else (int(not (x % 2)) + 4) if not (x % 2) else 3),
    OrderedDominoCreater(lambda x: (x % 2 + 5 if x % 2 else 3) if x < 3 else (int(not (x % 2)) + 5) if not (x % 2) else 3),

    OrderedDominoCreater(lambda x: (x % 2 + 4 if not x % 2 else 3) if x < 3 else (int(not (x % 2)) + 4) if (x % 2) else 3),
    OrderedDominoCreater(lambda x: (x % 2 + 5 if not x % 2 else 3) if x < 3 else (int(not (x % 2)) + 5) if (x % 2) else 3),
    OrderedDominoCreater(lambda x: (x % 2 + 6 if not x % 2 else 3) if x < 3 else (int(not (x % 2)) + 6) if (x % 2) else 3),

    OrderedDominoCreater(lambda x: (x % 2 + 6 if not x % 2 else 4) if x < 3 else (int(not (x % 2)) + 6) if (x % 2) else 4),
    OrderedDominoCreater(lambda x: (x % 2 + 6 if not x % 2 else 5) if x < 3 else (int(not (x % 2)) + 6) if (x % 2) else 5),

    OrderedDominoCreater(lambda x: (x + 1) % 3),
    OrderedDominoCreater(lambda x: (x + 1) % 3 + 1),
    OrderedDominoCreater(lambda x: (x + 1) % 3 + 3),

    OrderedDominoCreater(lambda x: (x + 2) % 3),
    OrderedDominoCreater(lambda x: (x + 2) % 3 + 1),
    OrderedDominoCreater(lambda x: (x + 2) % 3 + 3),

    OrderedDominoCreater(lambda x: (x + 3) % 3 + 3),
    OrderedDominoCreater(lambda x: (x + 3) % 3 + 2),

    OrderedDominoCreater(lambda x: x + 1 if x < 3 else x - 1),
    OrderedDominoCreater(lambda x: x if x < 3 else x - 1),
    OrderedDominoCreater(lambda x: x + 2 if x < 3 else x),

    OrderedDominoCreater(lambda x: (x + 4) % 3 + 2),

    OrderedDominoCreater(lambda x: 1 + x - (x + 1) // 3),
    OrderedDominoCreater(lambda x: 2 + x - (x + 2) // 3),
    OrderedDominoCreater(lambda x: 1 + x - (x + 1) // 4),
    OrderedDominoCreater(lambda x: 2 + x - (x + 2) // 5),

)

randoms_array = RandomArray(416)