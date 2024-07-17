from threading import Thread
from random import randint
from math import factorial

def is_prime(a):
    for i in range(2, a//2):
        if a % i == 0:
            return False
    return True

file = input('Введите путь к файлу: ')

def create_list():
    lst = [str(randint(1, 10)) for i in range(25)]
    with open(file, 'w') as f:
        s = ' '.join(lst)
        f.write(s)

def find_prime():
    with open(file, 'r') as f:
        lst = f.readline().split()
        lst = [int(i) for i in lst if is_prime(int(i))]
    print(lst)


def find_fact():
    with open(file, 'r') as f:
        lst = f.readline().split()
        lst = [factorial(int(i)) for i in lst]
    print(lst)



thr_create = Thread(target=create_list)
thr_sum = Thread(target=find_prime)
thr_arith = Thread(target=find_fact)


thr_create.start()
thr_create.join()

thr_sum.start()
thr_arith.start()