
import os
from itertools import takewhile

def get_full_path():
    swd = os.getcwd()
    swd = os.path.split(swd)
    swd = list(takewhile(lambda p: p != 'domino', swd))
    swd = os.path.join(*swd, 'domino')
    return swd

def join_file_path(dir, filename):
    return os.path.join(dir, filename)

def join_absolute_path(filename):
    return os.path.join(get_full_path(), filename)