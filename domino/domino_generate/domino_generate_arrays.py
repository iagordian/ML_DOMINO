

from domino.domino_obj import SixOrderedDominoCreater, SevenOrderedDominoCreater, \
    NineOrderedDominoCreater, TenOrderedDominoCreater, ElevenOrderedDominoCreater, \
    TwelveOrderedDominoCreater, FifteenOrderedDominoCreater, EighteenOrderedDominoCreater, \
    ThirteenOrderedDominoCreater, EightOrderedDominoCreater, FourteenOrderedDominoCreater, \
    SixteenOrderedDominoCreater, SeventeenteenOrderedDominoCreater

domino_array_small = [
    SixOrderedDominoCreater(lambda x: x),
    SixOrderedDominoCreater(lambda x: x + 1),
    SixOrderedDominoCreater(lambda x: 0),
    SixOrderedDominoCreater(lambda x: 1),
    SixOrderedDominoCreater(lambda x: 2),
    SixOrderedDominoCreater(lambda x: 3),
    SixOrderedDominoCreater(lambda x: 4),
    SixOrderedDominoCreater(lambda x: 5),
    SixOrderedDominoCreater(lambda x: 6),
    SixOrderedDominoCreater(lambda x: x % 2 + 1),
    SixOrderedDominoCreater(lambda x: x % 2 + 2),
    SixOrderedDominoCreater(lambda x: x % 2 + 3),
    SixOrderedDominoCreater(lambda x: x % 2 + 4),
    SixOrderedDominoCreater(lambda x: x % 2 + 5),
    SixOrderedDominoCreater(lambda x: 6 - x),    
    SixOrderedDominoCreater(lambda x: x % 2),
    SixOrderedDominoCreater(lambda x: int(x % 2 == 0)),     

    SixOrderedDominoCreater(lambda x: x if not x % 2 else 6),
    SixOrderedDominoCreater(lambda x: x if not x % 2 else 5),
    SixOrderedDominoCreater(lambda x: x if not x % 2 else 4),
    SixOrderedDominoCreater(lambda x: x if not x % 2 else 3),
    SixOrderedDominoCreater(lambda x: x if not x % 2 else 1),

    SixOrderedDominoCreater(lambda x: 5 - x),

    SixOrderedDominoCreater(lambda x: (x % 3) + 1),
    SixOrderedDominoCreater(lambda x: (x % 3)),

    SixOrderedDominoCreater(lambda x: x if x % 2 else 0),
    SixOrderedDominoCreater(lambda x: x if x % 2 else 6),
    SixOrderedDominoCreater(lambda x: x if x % 2 else 4),
    SixOrderedDominoCreater(lambda x: x if x % 2 else 2),

    SixOrderedDominoCreater(lambda x: 2 if x % 2 else 0),
    SixOrderedDominoCreater(lambda x: 3 if x % 2 else 0),
    SixOrderedDominoCreater(lambda x: 4 if x % 2 else 0),
    SixOrderedDominoCreater(lambda x: 5 if x % 2 else 0),
    SixOrderedDominoCreater(lambda x: 6 if x % 2 else 0),

    SixOrderedDominoCreater(lambda x: 2 if x % 2 == 0 else 1),
    SixOrderedDominoCreater(lambda x: 3 if x % 2 == 0 else 1),
    SixOrderedDominoCreater(lambda x: 4 if x % 2 == 0 else 1),
    SixOrderedDominoCreater(lambda x: 5 if x % 2 == 0 else 1),
    SixOrderedDominoCreater(lambda x: 6 if x % 2 == 0 else 1),

    SixOrderedDominoCreater(lambda x: 2 if x % 2 == 0 else 0),
    SixOrderedDominoCreater(lambda x: 3 if x % 2 == 0 else 0),
    SixOrderedDominoCreater(lambda x: 4 if x % 2 == 0 else 0),
    SixOrderedDominoCreater(lambda x: 5 if x % 2 == 0 else 0),
    SixOrderedDominoCreater(lambda x: 6 if x % 2 == 0 else 0),

    SixOrderedDominoCreater(lambda x: 3 if x % 2 else 1),
    SixOrderedDominoCreater(lambda x: 4 if x % 2 else 1),
    SixOrderedDominoCreater(lambda x: 5 if x % 2 else 1),
    SixOrderedDominoCreater(lambda x: 6 if x % 2 else 1),

    SixOrderedDominoCreater(lambda x: 4 if x % 2 else 2),
    SixOrderedDominoCreater(lambda x: 5 if x % 2 else 2),
    SixOrderedDominoCreater(lambda x: 6 if x % 2 else 2),

    SixOrderedDominoCreater(lambda x: 3 if x % 2 == 0 else 2),
    SixOrderedDominoCreater(lambda x: 4 if x % 2 == 0 else 2),
    SixOrderedDominoCreater(lambda x: 5 if x % 2 == 0 else 2),
    SixOrderedDominoCreater(lambda x: 6 if x % 2 == 0 else 2),

    SixOrderedDominoCreater(lambda x: 5 if x % 2 else 3),
    SixOrderedDominoCreater(lambda x: 6 if x % 2 else 3),

    SixOrderedDominoCreater(lambda x: 4 if x % 2 == 0 else 3),
    SixOrderedDominoCreater(lambda x: 5 if x % 2 == 0 else 3),
    SixOrderedDominoCreater(lambda x: 6 if x % 2 == 0 else 3),

    SixOrderedDominoCreater(lambda x: 6 if x % 2 else 4),
    SixOrderedDominoCreater(lambda x: 6 if x % 2 == 0 else 4),

    SixOrderedDominoCreater(lambda x: x // 2),
    SixOrderedDominoCreater(lambda x: x // 3),

    SixOrderedDominoCreater(lambda x: 1 if x < 3 else 0),
    SixOrderedDominoCreater(lambda x: 1 if x < 3 else 2),
    SixOrderedDominoCreater(lambda x: 1 if x < 3 else 3),
    SixOrderedDominoCreater(lambda x: 1 if x < 3 else 4),
    SixOrderedDominoCreater(lambda x: 1 if x < 3 else 5),
    SixOrderedDominoCreater(lambda x: 1 if x < 3 else 6),

    SixOrderedDominoCreater(lambda x: 2 if x < 3 else 0),
    SixOrderedDominoCreater(lambda x: 2 if x < 3 else 1),
    SixOrderedDominoCreater(lambda x: 2 if x < 3 else 3),
    SixOrderedDominoCreater(lambda x: 2 if x < 3 else 4),
    SixOrderedDominoCreater(lambda x: 2 if x < 3 else 5),
    SixOrderedDominoCreater(lambda x: 2 if x < 3 else 6),

    SixOrderedDominoCreater(lambda x: 3 if x < 3 else 0),
    SixOrderedDominoCreater(lambda x: 3 if x < 3 else 2),
    SixOrderedDominoCreater(lambda x: 3 if x < 3 else 1),
    SixOrderedDominoCreater(lambda x: 3 if x < 3 else 4),
    SixOrderedDominoCreater(lambda x: 3 if x < 3 else 5),
    SixOrderedDominoCreater(lambda x: 3 if x < 3 else 6),

    SixOrderedDominoCreater(lambda x: 4 if x < 3 else 0),
    SixOrderedDominoCreater(lambda x: 4 if x < 3 else 2),
    SixOrderedDominoCreater(lambda x: 4 if x < 3 else 3),
    SixOrderedDominoCreater(lambda x: 4 if x < 3 else 1),
    SixOrderedDominoCreater(lambda x: 4 if x < 3 else 5),
    SixOrderedDominoCreater(lambda x: 4 if x < 3 else 6),

    SixOrderedDominoCreater(lambda x: 5 if x < 3 else 0),
    SixOrderedDominoCreater(lambda x: 5 if x < 3 else 2),
    SixOrderedDominoCreater(lambda x: 5 if x < 3 else 3),
    SixOrderedDominoCreater(lambda x: 5 if x < 3 else 1),
    SixOrderedDominoCreater(lambda x: 5 if x < 3 else 4),
    SixOrderedDominoCreater(lambda x: 5 if x < 3 else 6),

    SixOrderedDominoCreater(lambda x: 6 if x < 3 else 0),
    SixOrderedDominoCreater(lambda x: 6 if x < 3 else 2),
    SixOrderedDominoCreater(lambda x: 6 if x < 3 else 3),
    SixOrderedDominoCreater(lambda x: 6 if x < 3 else 5),
    SixOrderedDominoCreater(lambda x: 6 if x < 3 else 4),
    SixOrderedDominoCreater(lambda x: 6 if x < 3 else 1),

    SixOrderedDominoCreater(lambda x: 0 if x < 3 else 6),
    SixOrderedDominoCreater(lambda x: 0 if x < 3 else 2),
    SixOrderedDominoCreater(lambda x: 0 if x < 3 else 3),
    SixOrderedDominoCreater(lambda x: 0 if x < 3 else 5),
    SixOrderedDominoCreater(lambda x: 0 if x < 3 else 4),

    SixOrderedDominoCreater(lambda x: 1 if x < 2 else 2 if x < 4 else 3),
    SixOrderedDominoCreater(lambda x: 2 if x < 2 else 3 if x < 4 else 4),
    SixOrderedDominoCreater(lambda x: 3 if x < 2 else 4 if x < 4 else 5),
    SixOrderedDominoCreater(lambda x: 4 if x < 2 else 5 if x < 4 else 6),
    SixOrderedDominoCreater(lambda x: 2 if x < 2 else 4 if x < 4 else 6),

    SixOrderedDominoCreater(lambda x: 1 if x < 2 else 2 if x < 4 else 1),
    SixOrderedDominoCreater(lambda x: 2 if x < 2 else 3 if x < 4 else 2),
    SixOrderedDominoCreater(lambda x: 3 if x < 2 else 4 if x < 4 else 3),
    SixOrderedDominoCreater(lambda x: 4 if x < 2 else 5 if x < 4 else 4),
    SixOrderedDominoCreater(lambda x: 2 if x < 2 else 4 if x < 4 else 5),

    SixOrderedDominoCreater(lambda x: 2 * x % 3),
    SixOrderedDominoCreater(lambda x: 2 * x % 6),
    SixOrderedDominoCreater(lambda x: 3 * (x % 3)),

    SixOrderedDominoCreater(lambda x: 3 + x if x < 3 else x - 3),
    SixOrderedDominoCreater(lambda x: (3 + x if x < 3 else x - 3) + 1),

    SixOrderedDominoCreater(lambda x: 6 - x % 2),
    SixOrderedDominoCreater(lambda x: 5 - x % 2),

    SixOrderedDominoCreater(lambda x: 6 - x % 3),
    SixOrderedDominoCreater(lambda x: 5 - x % 3),
    SixOrderedDominoCreater(lambda x: 4 - x % 3),
    SixOrderedDominoCreater(lambda x: 3 - x % 3),
    SixOrderedDominoCreater(lambda x: 2 - x % 3),

    SixOrderedDominoCreater(lambda x: 6 - (x % 3) * 2),
    SixOrderedDominoCreater(lambda x: 5 - (x % 3) * 2),

    SixOrderedDominoCreater(lambda x: 2 - x if x < 3 else x - 3),
    SixOrderedDominoCreater(lambda x: 3 - x if x < 3 else x - 2),
    SixOrderedDominoCreater(lambda x: 4 - x if x < 3 else x - 1),
    SixOrderedDominoCreater(lambda x: 5 - x if x < 3 else x),
    SixOrderedDominoCreater(lambda x: 6 - x if x < 3 else x + 1),

    SixOrderedDominoCreater(lambda x: 5 - x * 2 if x < 3 else x - (5 - x)),
    SixOrderedDominoCreater(lambda x: 6 - x * 2 if x < 3 else x - (4 - x)),
    SixOrderedDominoCreater(lambda x: 4 - x * 2 if x < 3 else x - (6 - x)),

    SixOrderedDominoCreater(lambda x: 6 - 3 * x if x < 3 else (x - 3) * 3),

    SixOrderedDominoCreater(lambda x: x - x % 2),
    SixOrderedDominoCreater(lambda x: (6 - x) + x % 2),

    SixOrderedDominoCreater(lambda x: x - x % 2 if x < 2 else x - x % 2 - 1),
    SixOrderedDominoCreater(lambda x: (6 - x) + x % 2 if x < 2 else (6 - x) + x % 2 - 1 if x < 4 else 0),

    SixOrderedDominoCreater(lambda x: x if x < 3 else 5 - x),
    SixOrderedDominoCreater(lambda x: x + 1 if x < 3 else 5 - (x - 1)),
    SixOrderedDominoCreater(lambda x: x + 2 if x < 3 else 6 - (x - 1)),
    SixOrderedDominoCreater(lambda x: x + 3 if x < 3 else 7 - (x - 1)),
    SixOrderedDominoCreater(lambda x: x + 4 if x < 3 else 8 - (x - 1)),

    SixOrderedDominoCreater(lambda x: x * 2 if x < 3 else (5 - x) * 2),
    SixOrderedDominoCreater(lambda x: x * 3 if x < 3 else (5 - x) * 3),
    SixOrderedDominoCreater(lambda x: (x + 1) * 2 if x < 3 else (5 - x) * 2 + 2),

    SixOrderedDominoCreater(lambda x: x % 2 if x < 3 else int(not (x % 2))),
    SixOrderedDominoCreater(lambda x: x % 2 + 1 if x < 3 else int(not (x % 2)) + 1),
    SixOrderedDominoCreater(lambda x: x % 2 + 2 if x < 3 else int(not (x % 2)) + 2),
    SixOrderedDominoCreater(lambda x: x % 2 + 4 if x < 3 else int(not (x % 2)) + 4),
    SixOrderedDominoCreater(lambda x: x % 2 + 5 if x < 3 else int(not (x % 2)) + 5),

    SixOrderedDominoCreater(lambda x: (x % 2 + 1 if x % 2 else 0) if x < 3 else (int(not (x % 2)) + 1) if not (x % 2) else 0),
    SixOrderedDominoCreater(lambda x: (x % 2 + 2 if x % 2 else 0) if x < 3 else (int(not (x % 2)) + 2) if not (x % 2) else 0),
    SixOrderedDominoCreater(lambda x: (x % 2 + 3 if x % 2 else 0) if x < 3 else (int(not (x % 2)) + 3) if not (x % 2) else 0),
    SixOrderedDominoCreater(lambda x: (x % 2 + 4 if x % 2 else 0) if x < 3 else (int(not (x % 2)) + 4) if not (x % 2) else 0),
    SixOrderedDominoCreater(lambda x: (x % 2 + 5 if x % 2 else 0) if x < 3 else (int(not (x % 2)) + 5) if not (x % 2) else 0),

    SixOrderedDominoCreater(lambda x: (x % 2 + 1 if not x % 2 else 0) if x < 3 else (int(not (x % 2)) + 1) if (x % 2) else 0),
    SixOrderedDominoCreater(lambda x: (x % 2 + 2 if not x % 2 else 0) if x < 3 else (int(not (x % 2)) + 2) if (x % 2) else 0),
    SixOrderedDominoCreater(lambda x: (x % 2 + 3 if not x % 2 else 0) if x < 3 else (int(not (x % 2)) + 3) if (x % 2) else 0),
    SixOrderedDominoCreater(lambda x: (x % 2 + 4 if not x % 2 else 0) if x < 3 else (int(not (x % 2)) + 4) if (x % 2) else 0),
    SixOrderedDominoCreater(lambda x: (x % 2 + 5 if not x % 2 else 0) if x < 3 else (int(not (x % 2)) + 5) if (x % 2) else 0),
    SixOrderedDominoCreater(lambda x: (x % 2 + 6 if not x % 2 else 0) if x < 3 else (int(not (x % 2)) + 6) if (x % 2) else 0),

    SixOrderedDominoCreater(lambda x: (x % 2 + 2 if x % 2 else 1) if x < 3 else (int(not (x % 2)) + 2) if not (x % 2) else 1),
    SixOrderedDominoCreater(lambda x: (x % 2 + 3 if x % 2 else 1) if x < 3 else (int(not (x % 2)) + 3) if not (x % 2) else 1),
    SixOrderedDominoCreater(lambda x: (x % 2 + 4 if x % 2 else 1) if x < 3 else (int(not (x % 2)) + 4) if not (x % 2) else 1),
    SixOrderedDominoCreater(lambda x: (x % 2 + 5 if x % 2 else 1) if x < 3 else (int(not (x % 2)) + 5) if not (x % 2) else 1),

    SixOrderedDominoCreater(lambda x: (x % 2 + 2 if not x % 2 else 1) if x < 3 else (int(not (x % 2)) + 2) if (x % 2) else 1),
    SixOrderedDominoCreater(lambda x: (x % 2 + 3 if not x % 2 else 1) if x < 3 else (int(not (x % 2)) + 3) if (x % 2) else 1),
    SixOrderedDominoCreater(lambda x: (x % 2 + 4 if not x % 2 else 1) if x < 3 else (int(not (x % 2)) + 4) if (x % 2) else 1),
    SixOrderedDominoCreater(lambda x: (x % 2 + 5 if not x % 2 else 1) if x < 3 else (int(not (x % 2)) + 5) if (x % 2) else 1),
    SixOrderedDominoCreater(lambda x: (x % 2 + 6 if not x % 2 else 1) if x < 3 else (int(not (x % 2)) + 6) if (x % 2) else 1),

    SixOrderedDominoCreater(lambda x: (x % 2 + 3 if x % 2 else 2) if x < 3 else (int(not (x % 2)) + 3) if not (x % 2) else 2),
    SixOrderedDominoCreater(lambda x: (x % 2 + 4 if x % 2 else 2) if x < 3 else (int(not (x % 2)) + 4) if not (x % 2) else 2),
    SixOrderedDominoCreater(lambda x: (x % 2 + 5 if x % 2 else 2) if x < 3 else (int(not (x % 2)) + 5) if not (x % 2) else 2),

    SixOrderedDominoCreater(lambda x: (x % 2 + 3 if not x % 2 else 2) if x < 3 else (int(not (x % 2)) + 3) if (x % 2) else 2),
    SixOrderedDominoCreater(lambda x: (x % 2 + 4 if not x % 2 else 2) if x < 3 else (int(not (x % 2)) + 4) if (x % 2) else 2),
    SixOrderedDominoCreater(lambda x: (x % 2 + 5 if not x % 2 else 2) if x < 3 else (int(not (x % 2)) + 5) if (x % 2) else 2),
    SixOrderedDominoCreater(lambda x: (x % 2 + 6 if not x % 2 else 2) if x < 3 else (int(not (x % 2)) + 6) if (x % 2) else 2),

    SixOrderedDominoCreater(lambda x: (x % 2 + 4 if x % 2 else 3) if x < 3 else (int(not (x % 2)) + 4) if not (x % 2) else 3),
    SixOrderedDominoCreater(lambda x: (x % 2 + 5 if x % 2 else 3) if x < 3 else (int(not (x % 2)) + 5) if not (x % 2) else 3),

    SixOrderedDominoCreater(lambda x: (x % 2 + 4 if not x % 2 else 3) if x < 3 else (int(not (x % 2)) + 4) if (x % 2) else 3),
    SixOrderedDominoCreater(lambda x: (x % 2 + 5 if not x % 2 else 3) if x < 3 else (int(not (x % 2)) + 5) if (x % 2) else 3),
    SixOrderedDominoCreater(lambda x: (x % 2 + 6 if not x % 2 else 3) if x < 3 else (int(not (x % 2)) + 6) if (x % 2) else 3),

    SixOrderedDominoCreater(lambda x: (x % 2 + 6 if not x % 2 else 4) if x < 3 else (int(not (x % 2)) + 6) if (x % 2) else 4),
    SixOrderedDominoCreater(lambda x: (x % 2 + 6 if not x % 2 else 5) if x < 3 else (int(not (x % 2)) + 6) if (x % 2) else 5),

    SixOrderedDominoCreater(lambda x: {1: 5, 3: 4, 5: 3}.get(x) if x % 2 else 6),
    SixOrderedDominoCreater(lambda x: {1: 5, 3: 4, 5: 3}.get(x) if x % 2 else 2),
    SixOrderedDominoCreater(lambda x: {1: 5, 3: 4, 5: 3}.get(x) if x % 2 else 1),

    SixOrderedDominoCreater(lambda x: (x + 1) % 3),
    SixOrderedDominoCreater(lambda x: (x + 1) % 3 + 1),
    SixOrderedDominoCreater(lambda x: (x + 1) % 3 + 3),

    SixOrderedDominoCreater(lambda x: (x + 2) % 3),
    SixOrderedDominoCreater(lambda x: (x + 2) % 3 + 1),
    SixOrderedDominoCreater(lambda x: (x + 2) % 3 + 3),

    SixOrderedDominoCreater(lambda x: (x + 3) % 3 + 3),
    SixOrderedDominoCreater(lambda x: (x + 3) % 3 + 2),

    SixOrderedDominoCreater(lambda x: x + 1 if x < 3 else x - 1),
    SixOrderedDominoCreater(lambda x: x if x < 3 else x - 1),
    SixOrderedDominoCreater(lambda x: x + 2 if x < 3 else x),

    SixOrderedDominoCreater(lambda x: (x + 4) % 3 + 2),

    SixOrderedDominoCreater(lambda x: 1 + x - (x + 1) // 3),
    SixOrderedDominoCreater(lambda x: 2 + x - (x + 2) // 3),
    SixOrderedDominoCreater(lambda x: 1 + x - (x + 1) // 4),
    SixOrderedDominoCreater(lambda x: 2 + x - (x + 2) // 5),

    SixOrderedDominoCreater(lambda n: n % 3 if n % 3 else 4),
    SixOrderedDominoCreater(lambda n: n % 3 if n % 3 else 5),
    SixOrderedDominoCreater(lambda n: n % 3 if n % 3 else 6),

    SixOrderedDominoCreater(lambda n: 0 if not n % 3 else 6),
    SixOrderedDominoCreater(lambda n: 5 if not n % 3 else 6),
    SixOrderedDominoCreater(lambda n: 4 if not n % 3 else 6),
    SixOrderedDominoCreater(lambda n: 3 if not n % 3 else 6),
    SixOrderedDominoCreater(lambda n: 2 if not n % 3 else 6),
    SixOrderedDominoCreater(lambda n: 1 if not n % 3 else 6),

    SixOrderedDominoCreater(lambda n: 6 if not n % 3 else 0),
    SixOrderedDominoCreater(lambda n: 5 if not n % 3 else 0),
    SixOrderedDominoCreater(lambda n: 4 if not n % 3 else 0),
    SixOrderedDominoCreater(lambda n: 3 if not n % 3 else 0),
    SixOrderedDominoCreater(lambda n: 2 if not n % 3 else 0),
    SixOrderedDominoCreater(lambda n: 1 if not n % 3 else 0),

    SixOrderedDominoCreater(lambda n: 6 if not n % 3 else 1),
    SixOrderedDominoCreater(lambda n: 5 if not n % 3 else 1),
    SixOrderedDominoCreater(lambda n: 4 if not n % 3 else 1),
    SixOrderedDominoCreater(lambda n: 3 if not n % 3 else 1),
    SixOrderedDominoCreater(lambda n: 2 if not n % 3 else 1),
    SixOrderedDominoCreater(lambda n: 0 if not n % 3 else 1),

    SixOrderedDominoCreater(lambda n: 6 if not n % 3 else 2),
    SixOrderedDominoCreater(lambda n: 5 if not n % 3 else 2),
    SixOrderedDominoCreater(lambda n: 4 if not n % 3 else 2),
    SixOrderedDominoCreater(lambda n: 3 if not n % 3 else 2),
    SixOrderedDominoCreater(lambda n: 0 if not n % 3 else 2),
    SixOrderedDominoCreater(lambda n: 1 if not n % 3 else 2),

    SixOrderedDominoCreater(lambda n: 6 if not n % 3 else 3),
    SixOrderedDominoCreater(lambda n: 5 if not n % 3 else 3),
    SixOrderedDominoCreater(lambda n: 4 if not n % 3 else 3),
    SixOrderedDominoCreater(lambda n: 0 if not n % 3 else 3),
    SixOrderedDominoCreater(lambda n: 2 if not n % 3 else 3),
    SixOrderedDominoCreater(lambda n: 1 if not n % 3 else 3),

    SixOrderedDominoCreater(lambda n: 6 if not n % 3 else 4),
    SixOrderedDominoCreater(lambda n: 5 if not n % 3 else 4),
    SixOrderedDominoCreater(lambda n: 0 if not n % 3 else 4),
    SixOrderedDominoCreater(lambda n: 3 if not n % 3 else 4),
    SixOrderedDominoCreater(lambda n: 2 if not n % 3 else 4),
    SixOrderedDominoCreater(lambda n: 1 if not n % 3 else 4),

    SixOrderedDominoCreater(lambda n: 6 if not n % 3 else 5),
    SixOrderedDominoCreater(lambda n: 0 if not n % 3 else 5),
    SixOrderedDominoCreater(lambda n: 4 if not n % 3 else 5),
    SixOrderedDominoCreater(lambda n: 3 if not n % 3 else 5),
    SixOrderedDominoCreater(lambda n: 2 if not n % 3 else 5),
    SixOrderedDominoCreater(lambda n: 1 if not n % 3 else 5),
]

is_standart_generate_funcs = [
    lambda n: 1 if n not in [0, 5] else 0,
    lambda n: 0 if n not in [0, 5] else 1,
    lambda n: 0 if n not in [0, 5] else 2,
    lambda n: 0 if n not in [0, 5] else 3,
    lambda n: 0 if n not in [0, 5] else 4,
    lambda n: 0 if n not in [0, 5] else 5,
    lambda n: 0 if n not in [0, 5] else 6,
    lambda n: 1 if n % 2 else 0,
    lambda n: 0 if n % 2 else 1,
    lambda n: 2 if n % 2 else 0,
    lambda n: 3 if n % 2 else 0,
    lambda n: 4 if n % 2 else 0,
    lambda n: 5 if n % 2 else 0,
    lambda n: 6 if n % 2 else 0,
    lambda n: 1 if n in [2, 5] else 0,
    lambda n: 0 if n in [2, 5] else 1,
    lambda n: 2 if n in [2, 5] else 0,
    lambda n: 3 if n in [2, 5] else 0,
    lambda n: 4 if n in [2, 5] else 0,
    lambda n: 5 if n in [2, 5] else 0,
    lambda n: 6 if n in [2, 5] else 0,
]

simple_generate_funcs = [

    lambda n: n // 4,
    lambda n: n // 4 + 1,
    lambda n: n // 4 + 2,

    lambda n: n // 2,
    lambda n: n // 2 + 1,
    lambda n: n // 2 + 2,

    lambda n: n // 3,

    lambda n: 6 - n // 2,
    lambda n: 5 - n // 2,
    lambda n: 4 - n // 2,

    lambda n: n % 6 + 1,
    lambda n: n % 7,
    lambda n: n % 5,
    lambda n: n % 4,
    lambda n: n % 3,
    lambda n: n % 2,

    lambda n: n % 2 * 2,
    lambda n: n % 2 * 3,
    lambda n: n % 2 * 4,
    lambda n: n % 2 * 5,
    lambda n: n % 2 * 6,

    lambda n: 1 - n % 2,
    lambda n: (1 - n % 2) * 2,
    lambda n: (1 - n % 2) * 3,
    lambda n: (1 - n % 2) * 4,
    lambda n: (1 - n % 2) * 5,
    lambda n: (1 - n % 2) * 6,

    lambda n: n % 3 * 2,
    lambda n: n % 3 * 3,

    lambda n: (2 - n % 3) * 2,
    lambda n: (2 - n % 3) * 3,

    lambda n: n % 4 * 2,
    lambda n: (3 - n % 4) * 2,

    lambda n: 5 - n % 6,
    lambda n: 4 - n % 5,

    lambda n: 1 if n % 2 else 2,
    lambda n: 3 if n % 2 else 2,
    lambda n: 4 if n % 2 else 2,
    lambda n: 5 if n % 2 else 2,
    lambda n: 6 if n % 2 else 2,

    lambda n: 1 if n % 2 else 3,
    lambda n: 2 if n % 2 else 3,
    lambda n: 4 if n % 2 else 3,
    lambda n: 5 if n % 2 else 3,
    lambda n: 6 if n % 2 else 3,

    lambda n: 1 if n % 2 else 4,
    lambda n: 2 if n % 2 else 4,
    lambda n: 3 if n % 2 else 4,
    lambda n: 5 if n % 2 else 4,
    lambda n: 6 if n % 2 else 4,

    lambda n: 1 if n % 2 else 5,
    lambda n: 2 if n % 2 else 5,
    lambda n: 3 if n % 2 else 5,
    lambda n: 4 if n % 2 else 5,
    lambda n: 6 if n % 2 else 5,

    lambda n: 1 if n % 2 else 6,
    lambda n: 2 if n % 2 else 6,
    lambda n: 3 if n % 2 else 6,
    lambda n: 4 if n % 2 else 6,
    lambda n: 5 if n % 2 else 6,

    lambda n: 1 if not n % 2 else 2,
    lambda n: 1 if not n % 2 else 3,
    lambda n: 1 if not n % 2 else 4,
    lambda n: 1 if not n % 2 else 5,
    lambda n: 1 if not n % 2 else 6,

    lambda n: n + n % 2 if n % 2 else 2,
    lambda n: n + n % 2 if n % 2 else 3,
    lambda n: n + n % 2 if n % 2 else 4,
    lambda n: n + n % 2 if n % 2 else 5,
    
    lambda n: n if n % 6 else 3,

    lambda n: 1 if n % 4 < 2 else n % 4,
    lambda n: 1 if n % 4 < 3 else n % 4,

    lambda n: 0 if n % 4 < 2 else n % 4,
    lambda n: 4 if n % 4 < 2 else n % 4,
    lambda n: 5 if n % 4 < 2 else n % 4,
    lambda n: 6 if n % 4 < 2 else n % 4,

    lambda n: 1 if n % 4 < 2 else n % 4 - 1,
    lambda n: 0 if n % 4 < 2 else n % 4 - 1,

    lambda n: 1 if n % 4 < 2 else n % 4 + 1,
    lambda n: 1 if n % 4 < 2 else n % 4 + 2,
    lambda n: 1 if n % 4 < 2 else n % 4 + 3,

    lambda n: 2 if n % 4 < 2 else n % 4 + 1,
    lambda n: 2 if n % 4 < 2 else n % 4 + 2,
    lambda n: 2 if n % 4 < 2 else n % 4 + 3,

    lambda n: 0 if n % 4 < 3 else n % 4 - 1,

    lambda n: 2 if n % 4 < 3 else n % 4,
    lambda n: 4 if n % 4 < 3 else n % 4,
    lambda n: 5 if n % 4 < 3 else n % 4,

    lambda n: 2 if n % 4 < 3 else n % 4 - 1,
    lambda n: 4 if n % 4 < 3 else n % 4 - 2,
    lambda n: 5 if n % 4 < 3 else n % 4 - 3,

    lambda n: 0 if not n % 4 < 3 else n % 4,
    lambda n: 4 if not n % 4 < 3 else n % 4,
    lambda n: 5 if not n % 4 < 3 else n % 4,
    lambda n: 6 if not n % 4 < 3 else n % 4,


    lambda n: 0 if not n % 4 < 3 else n % 4 + 1,
    lambda n: 4 if not n % 4 < 3 else n % 4 + 1,
    lambda n: 5 if not n % 4 < 3 else n % 4 + 1,
    lambda n: 6 if not n % 4 < 3 else n % 4 + 1,

    lambda n: 0 if not n % 4 < 3 else n % 4 + 2,
    lambda n: 4 if not n % 4 < 3 else n % 4 + 2,
    lambda n: 5 if not n % 4 < 3 else n % 4 + 2,
    lambda n: 6 if not n % 4 < 3 else n % 4 + 2,

    lambda n: n % 4 if not n % 4 < 3 else n % 4 + 2,
    lambda n: n - 1 if n % 3 else 5,
    lambda n: n + 1 if n % 3 else 4,

    lambda n: n if n < 4 else 2 - n % 4,    
    
]

nine_generate_funcs = simple_generate_funcs[:65] + [

    lambda n: n % 6 if not n % 5 else 0,
    lambda n: n % 6 if not n % 5 else 1,
    lambda n: n % 6 if not n % 5 else 2,
    lambda n: n % 6 if not n % 5 else 3,
    lambda n: n % 6 if not n % 5 else 4,
    lambda n: n % 6 if not n % 5 else 6,

    lambda n: n % 6 + 1 if not n % 5 else 0,
    lambda n: n % 6 + 1 if not n % 5 else 2,
    lambda n: n % 6 + 1 if not n % 5 else 3,
    lambda n: n % 6 + 1 if not n % 5 else 4,   

    lambda n: n if n < 7 else 5 - n % 7,
    lambda n: n if n < 6 else 4 - n % 6,
    lambda n: n if n < 5 else 3 - n % 5,

    lambda n: n if n < 5 else 3 - n % 5 + 1,
    lambda n: n if n < 6 else 4 - n % 6 + 1,

    lambda n: n if n < 7 else 3 - n % 5 + 1,
    
    lambda n: n % 4 if not n % 4 < 3 else n % 4 + 2,
    
    lambda n: 0 if not n % 4 < 3 else n % 4 + 1,
    lambda n: 4 if not n % 4 < 3 else n % 4 + 1,
    lambda n: 5 if not n % 4 < 3 else n % 4 + 1,
    lambda n: 6 if not n % 4 < 3 else n % 4 + 1,

    lambda n: 0 if not n % 4 < 3 else n % 4,
    lambda n: 4 if not n % 4 < 3 else n % 4,
    lambda n: 5 if not n % 4 < 3 else n % 4,
    lambda n: 6 if not n % 4 < 3 else n % 4,

    lambda n: 2 if n % 4 < 3 else n % 4 - 1,
    lambda n: 4 if n % 4 < 3 else n % 4 - 2,
    lambda n: 5 if n % 4 < 3 else n % 4 - 3,

    lambda n: 2 if n % 4 < 3 else n % 4,
    lambda n: 4 if n % 4 < 3 else n % 4,
    lambda n: 5 if n % 4 < 3 else n % 4,

    lambda n: 2 if n % 4 < 2 else n % 4 + 1,
    lambda n: 2 if n % 4 < 2 else n % 4 + 2,
    lambda n: 2 if n % 4 < 2 else n % 4 + 3,

    lambda n: 0 if n % 4 < 3 else n % 4 - 1,    
      
]

ten_generate_funcs = nine_generate_funcs[:77] + nine_generate_funcs[-20:] + [
    lambda n: n // 4 * 2,
    lambda n: n // 4 * 3,
    lambda n: n // 4 * 2 + 1,
    lambda n: n // 3 + 1,
]

eleven_generate_funcs = simple_generate_funcs[:5] + simple_generate_funcs[10:65] + \
    ten_generate_funcs[-4:] + [
        lambda n: n // 6,
        lambda n: n // 6 * 2,
        lambda n: n // 6 * 3,
        lambda n: n // 6 * 4,
        lambda n: n // 6 * 5,
        lambda n: n // 6 * 6,

        lambda n: n // 6 if n // 6 else 1,
        lambda n: n // 6 * 2 if n // 6 else 1,
        lambda n: n // 6 * 3 if n // 6 else 1,
        lambda n: n // 6 * 4 if n // 6 else 1,
        lambda n: n // 6 * 5 if n // 6 else 1,
        lambda n: n // 6 * 6 if n // 6 else 1,

        lambda n: 6 - n // 6,
        lambda n: 6 - n // 6 * 2,
        lambda n: 6 - n // 6 * 3,
        lambda n: 6 - n // 6 * 4,
        lambda n: 6 - n // 6 * 5,
        lambda n: 6 - n // 6 * 6,

        lambda n: n % 6 if n < 6 else (6 - n % 6),
        
        
        lambda n: n % 4 if (n // 4) % 2 else (4 - n % 4),
        lambda n: n % 5 if (n // 5) % 2 else (5 - n % 5),

        lambda n: n % 3 if (n // 3) % 2 else (3 - n % 3),
        lambda n: n % 2 if (n // 2) % 2 else (2 - n % 2),
        lambda n: n % 6 if (n // 6) % 2 else (6 - n % 6),

        lambda n: n % 4 if (n // 4) % 3 else (4 - n % 4),

        lambda n: n % 4 if not (n // 4) % 2 else (4 - n % 4),
        lambda n: n % 5 if not (n // 5) % 2 else (5 - n % 5),

        lambda n: n % 3 if not (n // 3) % 2 else (3 - n % 3),
        lambda n: n % 2 if not (n // 2) % 2 else (2 - n % 2),

        lambda n: n % 4 if not (n // 4) % 3 else (4 - n % 4),

        lambda n: n % 4 + 1 if (n // 4) % 2 else (6 - n % 4),

        lambda n: n % 3 + 1 if (n // 3) % 2 else (4 - n % 3),
        lambda n: n % 2 + 1 if (n // 2) % 2 else (3 - n % 2),
        lambda n: n % 6 if (n // 6) % 2 else n % 6,

        lambda n: n % 4 + 1 if not (n // 4) % 2 else (5 - n % 4),
        lambda n: n % 5 + 1 if not (n // 5) % 2 else (6 - n % 5),

        lambda n: n % 3 + 1 if not (n // 3) % 2 else (4 - n % 3),
        lambda n: n % 2 + 1 if not (n // 2) % 2 else (3 - n % 2),

        lambda n: n % 4 + 1 if not (n // 4) % 3 else (5 - n % 4),
    ]


twelve_generate_funcs = eleven_generate_funcs
fifteen_generate_funcs = simple_generate_funcs[:3] + nine_generate_funcs[10:69] + \
    eleven_generate_funcs[-20:] + [
        lambda n: 6 - n % 6,
        lambda n: 6 - n % 5,
        lambda n: 6 - n % 4,
        lambda n: 6 - n % 3,
        lambda n: 5 - n % 3 if (n // 3) % 2 else n % 3 + 2,

        lambda n: 5 - n % 3 if not (n // 3) % 2 else n % 3 + 2,
        
        lambda n: n // 5 * 2,
        lambda n: n // 6 * 2,
        lambda n: n // 7 * 2,
        lambda n: n // 8 * 2,
        lambda n: n // 9 * 2,
        lambda n: n // 8 * 3,
        lambda n: n // 9 * 3,

        lambda n: n // 4 if n // 4 else 4,
        lambda n: n // 4 if n % 4 else 4,
        lambda n: n // 4 + 1 if n % 4 else 4,
        lambda n: n // 3 if n % 3 else 5,
        lambda n: n // 3 if n % 3 else 6,
    ]

eighteen_generate_funcs = fifteen_generate_funcs

eight_generate_funcs = nine_generate_funcs[:75] + fifteen_generate_funcs[-5:] + eleven_generate_funcs[60:80]

seven_size_domino_array = [SevenOrderedDominoCreater(f) for f in simple_generate_funcs]
nine_size_domino_array = [NineOrderedDominoCreater(f) for f in nine_generate_funcs]
ten_size_domino_array = [TenOrderedDominoCreater(f) for f in ten_generate_funcs]
eleven_size_domino_array = [ElevenOrderedDominoCreater(f) for f in eleven_generate_funcs]
twelve_size_domino_array = [TwelveOrderedDominoCreater(f) for f in twelve_generate_funcs]
fifteen_size_domino_array = [FifteenOrderedDominoCreater(f) for f in fifteen_generate_funcs]
eighteen_size_domino_array = [EighteenOrderedDominoCreater(f) for f in eighteen_generate_funcs]
standart_domino_array = [SixOrderedDominoCreater(f) for f in is_standart_generate_funcs]
thirteen_size_domino_array = [ThirteenOrderedDominoCreater(f) for f in eighteen_generate_funcs]
eight_size_domino_array = [EightOrderedDominoCreater(f) for f in eight_generate_funcs]
fourteen_size_domino_array = [FourteenOrderedDominoCreater(f) for f in eighteen_generate_funcs]
sixteen_size_domino_array = [SixteenOrderedDominoCreater(f) for f in eighteen_generate_funcs]
seventeen_size_domino_array = [SeventeenteenOrderedDominoCreater(f) for f in eighteen_generate_funcs]