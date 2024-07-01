from model import ModelController
from view import ViewController

class PizzeriaController:
    def __init__(self):
        self.model = ModelController()
        self.view = ViewController()
        self.b = self.model.back_button
    
    def run(self):
        self.modeChoice()

    def modeChoice(self):
        while True:
            query = self.view.modeChoice()

            if query == '1':
                self.clientChoice()
            elif query == '2':
                self.devChoice()
            elif query == self.b:
                break

            query = None
    
    def clientChoice(self):
        pizzas = list(self.model.pizzas.keys())
        while True:
            query = self.view.clientChoiceP(pizzas)
            if query == self.b:
                return
            if query.isdigit() and 1 <= int(query) <= len(pizzas):
                query = int(query)
                pizza = self.model.pizzas[pizzas[query-1]]
                pizza_name = pizza.name

                price = pizza.price
                if pizza.build_mode:
                    if (res := self.buildChoice()) == None:
                        continue
                    else:
                        pizza_name, price = res

                size = self.sizeChoice(price)
                if size == None:
                    continue
                price *= size.multiplier
                
                pay = self.payChoice(pizza_name, price)
                if pay != None:
                    self.model.logWrite(pizza_name, price, pay)
                    input('Покупка совершена успешно!\nНажмите Enter чтобы выйти...')
    
    def sizeChoice(self, price):
        sizes = list(self.model.sizes.keys())
        while True:
            query = self.view.sizeChoice(self.model.sizes, price)
            if query == self.b:
                return
            if query.isdigit() and 1 <= int(query) <= len(sizes):
                query = int(query)
                return self.model.sizes[sizes[query-1]]

    def buildChoice(self):
        ings = list(self.model.ings.ings.keys())
        count = self.model.ings.max_size
        price = self.model.ings.base_price
        pizza_name = []
        while count > 0:
            query = self.view.buildChoice(self.model.ings.ings, count)
            if query == self.b:
                return
            if query.isdigit() and 1 <= int(query) <= len(ings):
                count -= 1
                query = int(query)
                price += self.model.ings.ings[ings[query-1]]
                pizza_name.append(ings[query-1])
        pizza_name = f'Свой рецепт {sorted(pizza_name)}'
        return pizza_name, price

    def payChoice(self, name, price):
        self.view.payInfo(name, price)
        pays = list(self.model.pays.keys())
        while True:
            query = self.view.payChoice(pays)
            if query == self.b:
                return
            if query.isdigit() and 1 <= int(query) <= len(pays):
                query = int(query)
                return pays[query-1]

    def devChoice(self):
        query = self.view.devChoice()
