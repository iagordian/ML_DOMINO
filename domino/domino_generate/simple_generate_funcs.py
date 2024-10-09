
import numpy as np
from typing import Optional
from functools import partial

def generate_simple_rows(*generate_rows_fucs, size: Optional[int] = 6):

  for i in range(7):
    for j in range(7):
      if i != j:
        for k in range(7):
          if k not in [i, j]:
            for f in generate_rows_fucs:
              yield f(size, i, j, k)

def get_honest_steped_row(size, i, j, k):

  indexes = np.arange(size)

  row = np.zeros(size)
  row[indexes % 2 == 0] = i
  row[indexes % 4 == 3] = j
  row[indexes % 4 == 1] = k

  nxt = j + (j - k)

  if all([
      nxt >= 0,
      nxt <= 6,
      nxt != i
  ]):
    row[indexes % 6 == 5] = nxt

  return row

def get_non_honest_steped_row(size, i, j, k):

  indexes = np.arange(size)

  row = np.zeros(size)
  row[indexes % 2 == 1] = i
  row[indexes % 4 == 2] = j
  row[indexes % 4 == 0] = k

  nxt = j + (j - k)

  if all([
      nxt >= 0,
      nxt <= 6,
      nxt != i
  ]):
    row[indexes % 6 == 4] = nxt

  return row

def get_pair_balanced_row(size, i, j, k):

  row = np.zeros(size)
  indexes = np.arange(size)
  row[indexes % 6 < 2] = i
  row[(indexes % 6 > 1) & (indexes % 6 < 4)] = j
  row[indexes % 6 > 3] = k

  return row

def get_bidirectional_balanced_row(size, i, j, k):

  row = np.zeros(size)
  indexes = np.arange(size)
  row[indexes % 6 == 0] = i
  row[indexes % 6 == 5] = i
  row[indexes % 6 == 1] = j
  row[indexes % 6 == 4] = j
  row[indexes % 6 == 2] = k
  row[indexes % 6 == 3] = k

  return row

def get_hulf_balanced_row(size, i, j, k):

  row = np.zeros(size)
  indexes = np.arange(size)
  row[indexes % 3 == 2] = i
  row[indexes % 2 == 1] = j
  row[indexes % 1 == 0] = k

  return row

generate_honest_stapped_rows = partial(generate_simple_rows, get_honest_steped_row, get_non_honest_steped_row)
generate_pair_balanced_rows = partial(generate_simple_rows, get_pair_balanced_row)
generate_bidirectional_balanced_rows = partial(generate_simple_rows, get_bidirectional_balanced_row)
generate_hulf_balanced_rows = partial(generate_simple_rows, get_hulf_balanced_row)