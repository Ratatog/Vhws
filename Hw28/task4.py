from threading import Thread
from os import walk, mkdir
from os.path import isdir
from shutil import copy
from re import sub

# file = input('Введите путь директории: ')
# word = input('Введите слово для поиска: ')
file = './File'
word = 'the_worudo'

to = './to.txt'

def wcopy(file, word:str, to=to):
    with open(to, 'w'): pass
    word = word.lower()
    for a, b, c in walk(file):
        for i in c:
            with open(f'{a}/{i}', 'r') as f:
                strs = ''.join(f.readlines())
                if word in strs:
                    with open(to, 'a+') as f2:
                        f2.write(strs + '\n')
        pass

# wcopy(file, word)

ban_words = ['123', 'the_worudo']

def wfind(bans:list = ban_words, file=to):
    with open(file, 'r') as f:
        strs = ''.join(f.readlines())
    strs = sub('|'.join(bans), '*', strs)
    with open(file, 'w') as f:
        f.write(strs)

# wfind()

thr1 = Thread(target=wcopy, args=(file, word))
thr2 = Thread(target=wfind)

thr1.start()
thr1.join()

thr2.start()
