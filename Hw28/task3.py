from threading import Thread
from os import walk, mkdir
from os.path import isdir
from shutil import copy


# file = input('Введите путь к директории: ')
# to = input('Введите путь для копирования директории: ')
file = './File'
to = './To'

def dcopy(file, to:str):
    if to.endswith('/'): to = to[:-1]
    if not isdir(to):
        mkdir(to)

    for a, b, c in walk(file):
        folder = f'{to}{a[1:]}'
        if not isdir(folder):
            mkdir(folder)
            print(f'Создана директория {a}')
        for i in c:
            copy(f'{a}/{i}', folder)
            print(f'Создан файл {i}')

# dcopy(file, to)

thr = Thread(target=dcopy, args=(file, to))
thr.start()
