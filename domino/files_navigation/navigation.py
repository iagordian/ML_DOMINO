
import os
from itertools import takewhile

def get_full_path() -> str:
    '''Возвращает полный путь до директории, в которой была вызвана функция'''
    swd = os.getcwd()
    swd = os.path.split(swd)
    swd = list(takewhile(lambda p: p != 'domino', swd))
    swd = os.path.join(*swd, 'domino')
    return swd

def join_file_path(dir, filename) -> str:
    '''Возвращает путь, созданный из имени файла и пути до директории'''
    return os.path.join(dir, filename)

def join_absolute_path(filename) -> str:
    '''Возвращает абсолютный путь до указанного файла на основании папки, в которой вызванная функция'''
    return os.path.join(get_full_path(), filename)