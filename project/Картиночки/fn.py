
lst = [

    lambda n: n % 3 if n % 3 else 3,
    lambda n: n % 3 if n % 3 else 4,
    lambda n: n % 3 if n % 3 else 5,
    lambda n: n % 3 if n % 3 else 6,

    lambda n: 0 if not n % 3 else 6,
    lambda n: 5 if not n % 3 else 6,
    lambda n: 4 if not n % 3 else 6,
    lambda n: 3 if not n % 3 else 6,
    lambda n: 2 if not n % 3 else 6,
    lambda n: 1 if not n % 3 else 6,

    lambda n: 6 if not n % 3 else 0,
    lambda n: 5 if not n % 3 else 0,
    lambda n: 4 if not n % 3 else 0,
    lambda n: 3 if not n % 3 else 0,
    lambda n: 2 if not n % 3 else 0,
    lambda n: 1 if not n % 3 else 0,

    lambda n: 6 if not n % 3 else 1,
    lambda n: 5 if not n % 3 else 1,
    lambda n: 4 if not n % 3 else 1,
    lambda n: 3 if not n % 3 else 1,
    lambda n: 2 if not n % 3 else 1,
    lambda n: 0 if not n % 3 else 1,

    lambda n: 6 if not n % 3 else 2,
    lambda n: 5 if not n % 3 else 2,
    lambda n: 4 if not n % 3 else 2,
    lambda n: 3 if not n % 3 else 2,
    lambda n: 0 if not n % 3 else 2,
    lambda n: 1 if not n % 3 else 2,

    lambda n: 6 if not n % 3 else 3,
    lambda n: 5 if not n % 3 else 3,
    lambda n: 4 if not n % 3 else 3,
    lambda n: 0 if not n % 3 else 3,
    lambda n: 2 if not n % 3 else 3,
    lambda n: 1 if not n % 3 else 3,

    lambda n: 6 if not n % 3 else 4,
    lambda n: 5 if not n % 3 else 4,
    lambda n: 0 if not n % 3 else 4,
    lambda n: 3 if not n % 3 else 4,
    lambda n: 2 if not n % 3 else 4,
    lambda n: 1 if not n % 3 else 4,

    lambda n: 6 if not n % 3 else 5,
    lambda n: 0 if not n % 3 else 5,
    lambda n: 4 if not n % 3 else 5,
    lambda n: 3 if not n % 3 else 5,
    lambda n: 2 if not n % 3 else 5,
    lambda n: 1 if not n % 3 else 5,
]

for f in lst:
    print([f(n) for n in range(6)])