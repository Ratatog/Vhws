from abc import ABC, abstractmethod
from random import randint
from re import findall
from os.path import isfile
from datetime import datetime as dt
from pickle import dump, load
from typing import Union, Iterable

# 1. Реализация паттерна Command
class Icommand(ABC):
    def __init__(self, phone):
        self.phone = phone

    @abstractmethod
    def on(self):
        pass
    @abstractmethod
    def off(self):
        pass

class OnOffButton(Icommand):
    def on(self):
        self.phone.turn_on()
    def off(self):
        self.phone.turn_off()

class Phone():
    def turn_on(self):
        print('Телефон включен')
    ...

class Button:
    def __init__(self, btn):
        self.btn = btn
    
    def press(self):
        self.btn.on()

btn = OnOffButton(Phone())
cmd = Button(btn)
cmd.press()


# 2. Меняющийся набор чисел и логгирование с помощью Proxy
class RNums():
    def __init__(self, quantity, minN, maxN):
        self.nums = [0] * quantity
        self.minN = minN
        self.maxN = maxN
        self.update()

    def update(self):
        for i in range(len(self.nums)):
            self.nums[i] = randint(self.minN, self.maxN)
        with open('nums.txt', 'w') as f:
            f.write(str(self.nums))

    def get_list(self, str):
        return [int(i) for i in findall(r'\d+', str)]
    
    def findmax(self):
        with open('nums.txt', 'r') as f:
            return max(self.get_list(f.readline()))
    def findmin(self):
        with open('nums.txt', 'r') as f:
            return min(self.get_list(f.readline()))
    def findsum(self):
        with open('nums.txt', 'r') as f:
            return sum(self.get_list(f.readline()))

class RNumsProxy(RNums):
    def __init__(self, obj, logN):
        self.obj = obj
        self.loglst = {}
        self.logN = logN
        if not isfile(logN):
            with open(logN, 'w'): ...
    
    def log_write(self, fname, res):
        if fname in self.loglst:
            return self.loglst[fname]
        
        with open(self.logN, 'a') as f:
            f.write(f'{str(dt.now().time())[:8]}, {fname}, {res}\n')
        self.loglst[fname] = res
    
    def update(self):
        self.obj.update()
        self.loglst = {}

    def findmax(self):
        res = self.obj.findmax()
        return self.log_write('findmax', res)
    def findmin(self):
        res = self.obj.findmin()
        return self.log_write('findmim', res)
    def findsum(self):
        res = self.obj.findsum()
        return self.log_write('findsum', res)

a = RNumsProxy(RNums(10, 25, 100), 'log.txt')

a.findmax()
a.findmax()
a.update()
a.findmax()


# 3. Приложение для работы в библиотеке используя все возможные паттерны
class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author
    
    def get_title(self):
        return self.title

#Adapter
class AdapterBook(Book):
    def get_name(self):
        return super().get_title()

class Librarian:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def get_name(self):
        return self.name


class Reader:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def get_name(self):
        return self.name

class Library:
    def __init__(self):
        self.workers = {}
        self.readers = {}
        self.books = {}
    
    def add(self, obj: Union[Librarian, Reader, AdapterBook]):
        name = obj.get_name()
        if isinstance(obj, Librarian):
            self.workers[name] = obj
        elif isinstance(obj, Reader):
            self.readers[name] = obj
        else:
            self.books[name] = obj
        return name
    
    def remove(self, obj: Union[Librarian, Reader, AdapterBook]):
        name = obj.get_name()
        if name in self.workers:
            del self.workers[name]
        elif name in self.readers:
            del self.readers[name]
        elif name in self.books:
            del self.books[name]
        else:
            print('Неудача удаления')
        return name
    
    #Iterator
    def get(self, name, to_file=None, to_iter=False):
        if name in self.workers:
            res = self.workers.get(name)
            it = self.workers
        elif name in self.readers:
            res = self.readers.get(name)
            it = self.readers
        elif name in self.books:
            res = self.books.get(name)
            it = self.books
        else:
            print(f'Неудача поиска {name}')
            return

        if to_iter:
            return (i for i in it)
        
        if not to_file:
            return res
        else:
            try:
                with open(to_file, 'r'): ...
            except Exception:
                with open(to_file, 'w'): ...
            with open(to_file, 'a') as f:
                f.write(res)
        return res

   
    def save_to_file(self, file):
        with open(file, 'wb') as f:
            obj = {'workers': self.workers, 'readers': self.readers, 'books': self.books}
            dump(obj, f)
    
    def read_from_file(self, file):
        try:
            with open(file, 'rb') as f:
                obj = load(f)
                print('Файл найден')
                self.workers = obj['workers']
                self.readers = obj['readers']
                self.books = obj['books']
                return obj
        except Exception as e:
            print(f'Файл не найден или данные записаны неверно {file} {e}')

#Proxy
class ProxyLibrary(Library):
    def __init__(self):
        self.library = Library()
        with open('log.txt', 'w'): ...
        self.curfile = None
        self.hash = {}

    def logging(self, action, res=None):
        with open('log.txt', 'a') as f:
            f.write(f'{str(dt.now().time())[:8]}, {action} - {res}\n')

    def add(self, *args, **kwargs):
        res = self.library.add(*args, **kwargs)
        self.logging('add', res)

    def remove(self, *args, **kwargs):
        res = self.library.remove(*args, **kwargs)
        self.logging('remove', res)

    def get(self, name, to_file=None, to_iter=False):
        if name in self.hash:
            return name
        res = self.library.get(name, to_file=None, to_iter=False)
        self.logging('get', res)
        if not to_file:
            self.hash[name] = name

    def save_to_file(self, *args, **kwargs):
        self.library.save_to_file(*args, **kwargs)
        self.logging('save')
        self.curfile = None

    def read_from_file(self, *args, **kwargs):
        if not self.curfile:
            self.curfile = self.library.read_from_file(*args, **kwargs)
            self.logging('read')

#Command
class Invoker:
    def __init__(self, obj: ProxyLibrary):
        self.lib = obj
    
    def load_n_save(self, file):
        self.lib.read_from_file(file)
        self.lib.save_to_file(file)
    
    def remove_all(self, to_delete='all'):
        if to_delete == 'all':
            self.remove_all('workers')
            self.remove_all('readers')
            self.remove_all('books')
        elif to_delete == 'workers':
            lst = [i for i in self.lib.library.workers]
            for i in lst:
                del self.lib.library.workers[i]
        elif to_delete == 'readers':
            lst = [i for i in self.lib.library.readers]
            for i in lst:
                del self.lib.library.readers[i]
        elif to_delete == 'books':
            lst = [i for i in self.lib.library.books]
            for i in lst:
                del self.lib.library.books[i]
    
    def many_add(self, lst: Iterable[Union[Librarian, Reader, AdapterBook]]):
        for i in lst:
            self.lib.add(i)

librarian = Librarian('Alex', 48, 'female')
reader = Reader('Max', 21, 'male')
book1 = AdapterBook('one', 1988, 'someone')
book2 = AdapterBook('two', 2015, 'nowsomeone')

library = ProxyLibrary()
command = Invoker(library)

library.add(librarian)
library.add(reader)
library.add(book1)
library.add(book2)
library.get('one')
library.save_to_file('text.txt')
print()
command.remove_all()
command.many_add([reader, book2])
command.load_n_save('text.txt')
print()
library.remove(librarian)
library.remove(book1)
library.get('two')