from model import ModelController

def choiceProcess(func):
    def wrapper(*args, **kwargs):
        print('='*50)
        res = func(*args, **kwargs)
        print(f'  "{ModelController.b_b}" - Назад')

        query = input('--> ')
        return query
    
    return wrapper

class ViewController:
    @choiceProcess
    def modeChoice(self):
        print('Выберите режим:')
        print('  1. Режим клиента')
        print('  2. Режим разработчика')
    
    @choiceProcess
    def clientChoiceP(self, pizzas):
        print('Выберите пиццу:')
        for i in range(len(pizzas)):
            print(f'  {i+1}. {pizzas[i]}')
    
    @choiceProcess
    def sizeChoice(self, size, price):
        size_list = list(size.keys())
        print('Выберите размер пиццы:')
        for i in range(len(size_list)):
            p = (size[size_list[i]].multiplier * price) // 1
            print(f'  {i+1}. {size_list[i]} - {p}р.')
    
    @choiceProcess
    def buildChoice(self, ings, count):
        ing_list = list(ings.keys())
        print(f'Выберите ингридиенты(осталось {count}):')
        for i in range(len(ings)):
            p = ings[ing_list[i]]
            print(f'{i+1}. {ing_list[i]} - {p}р.')

    def payInfo(self, name, price):
        print('='*50)
        print('Ваша пицца:\n'
            f'  Название: {name}\n'
            f'  Цена: {price}')
        input('Нажмите Enter чтобы продолжить...')
        print('='*50)

    @choiceProcess
    def payChoice(self, pays):
        print('Выберите способ оплаты:')
        for i in range(len(pays)):
            print(f'  {i+1}. {pays[i]}')
    
    @choiceProcess
    def devChoice(self):
        pass