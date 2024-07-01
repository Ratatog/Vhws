from pickle import dump, load
from os.path import isfile
from datetime import datetime

class Pizza:
    def __init__(self, name, base_price, add_mode=True, build_mode=False):
        self.name = name
        self.price = base_price
        self.build_mode = build_mode

class Size:
    def __init__(self, name, multiplier):
        self.name = name
        self.multiplier = multiplier

class Build:
    def __init__(self, ings, max_size=6, base_price=50):
        self.ings = ings
        self.max_size = max_size
        self.base_price = base_price

class Pay:
    def __init__(self, name):
        self.name = name
    

class ModelController:
    b_b = 'b'
    def __init__(self):
        self.log_name = 'log.txt'
        self.menu_name = 'menu.pickle'
        self.back_button = self.b_b
        self.menu = self.get_menu()

        #--pizzas
        self.pizzas = {'Классика': Pizza('Классика', 500),
                       'Пепперони': Pizza('Пепперони', 600),
                       'Гавайская': Pizza('Гавайская', 400),
                       'Свой рецепт': Pizza('Свой рецепт', 0, build_mode=True)}
        self.pizzas = self.menu.get('pizzas', self.pizzas)
        #--sizes
        self.sizes = {'Маленький': Size('Маленький', 0.7),
                      'Средний': Size('Средний', 1.0),
                      'Большой': Size('Большой', 1.3)}
        self.sizes = self.menu.get('sizes', self.sizes)
        #--ings
        self.ings = Build({'Помидор': 70,'Сыр': 80, 'Колбаса': 100,
                           'Огурец': 60, 'Ананас': 65, 'Оливки': 85})
        self.ings = self.menu.get('ings', self.ings)
        #--pays
        self.pays = {'Наличные': Pay('Наличные'), 'Карта': Pay('Карта'),
                     'Криптовалюта': Pay('Криптовалюта')}
        self.pays = self.menu.get('pays', self.pays)
        #-----

    def get_menu(self):
        if not isfile(self.menu_name):
            with open(self.menu_name, 'wb') as f: dump({}, f)
            
        with open(self.menu_name, 'rb') as f:
            try:
                menu = load(f)
            except Exception:
                menu = {}
                dump(menu, f)
        return menu
        
    def logWrite(self, pizza_name, price, pay):
        if not isfile(self.log_name):
            with open(self.log_name, 'w'): ...
        with open(self.log_name, 'a', encoding='utf-8') as f:
            time = str(datetime.now())[:-7]
            f.write(f'{time} - {pizza_name} - {price} - {pay}\n')
        
