# 1. Реализация паттерна Builder
# 2. Приложение для приготовление пасты
# 3. Реализация паттерна Prototype

from abc import ABC, abstractmethod

class Pasta:
    def __init__(self):
        self.type = None
        self.sauce = None
        self.filling = None
        self.additives = []
    
    def __str__(self):
        string = ''

        string += f'{self.type} ' if self.type else f'Любая паста '
        string += f'с соусом: {self.sauce}, ' if self.sauce else f'с любым соусом, '
        string += f'с начинкой: {self.filling}' if self.filling else f'с любой начинкой'
        if self.additives:
            string += ', с добавками: '
            string += ', '.join(self.additives)
        
        return string


class PastaBuilder(ABC):
    @abstractmethod
    def create_pasta(self):
        pass

class FirstPasta(PastaBuilder):
    def __init__(self):
        self.pasta = Pasta()
    
    def create_pasta(self):
        self.pasta.type = 'Спагетти'
        self.pasta.sauce = 'Сырный'
        self.pasta.filling = 'Какая-то'
        self.pasta.additives.append('Мясные шарики')

class SecondPasta(PastaBuilder):
    def __init__(self):
        self.pasta = Pasta()
    
    def create_pasta(self):
        self.pasta.type = 'Каннеллони'
        self.pasta.sauce = 'Томатный'
        self.pasta.additives.append('Чесночный соус')
        self.pasta.additives.append('Томатный соус')

class ThirdPasta(PastaBuilder):
    def __init__(self):
        self.pasta = Pasta()
    
    def create_pasta(self):
        self.pasta.sauce = 'Базилик'
        self.pasta.filling = 'Какая-то №2'


class Director:

    def make_dish(self, dishCreator):
        dishCreator.create_pasta()
        return str(dishCreator.pasta)
    
if __name__ == "__main__":
    dish = Director().make_dish(FirstPasta())
    print(dish, '\n')
    
    dish = Director().make_dish(SecondPasta())
    print(dish, '\n')

    dish = Director().make_dish(ThirdPasta())
    print(dish)
    
