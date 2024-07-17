from threading import Thread
from random import randint

lst = []

def create_list():
    for i in range(1_000_000):
        lst.append(randint(-100, 100))

def find_sum():
    print('Сумма:', sum(lst))

def find_arith():
    print('Ср. Арифметическое:', sum(lst)/len(lst))


thr_create = Thread(target=create_list)
thr_sum = Thread(target=find_sum)
thr_arith = Thread(target=find_arith)


thr_create.start()
thr_create.join()

thr_sum.start()
thr_arith.start()