from model import PizzerialeModel
from view import PizzeriaView


class PizzeriaController:
    def __init__(self):
        self.model = PizzerialeModel()
        self.view = PizzeriaView()

    def run(self):
        query = None
        while query != 'quit':
            query = self.view.wait_user_answer()
            self.check_user_answer(query)
        
            self.view.show_pizza(*self.model.get_pizza())
            input()

        
    def add_ings(self):
        MAX_INGS = 3
        curr_ings = 0
        ings = []
        query = None
        while query != 'end' and curr_ings < MAX_INGS:
            query = self.view.wait_user_ings(MAX_INGS - curr_ings)
            if res := self.check_user_ings(query):
                ings.append(res)
                curr_ings += 1
        return ings

    def new_recipe(self):
        MAX_INGS = 5
        curr_ings = 0
        pizza = []
        query = None
        while query != 'end' and curr_ings < MAX_INGS:
            query = self.view.wait_user_recipe(MAX_INGS - curr_ings)
            if res := self.check_user_recipe(query):
                pizza.append(res)
                curr_ings += 1
        return pizza
        
        
    
    def check_user_answer(self, answer):
        if answer == '6':
            pizza = self.new_recipe()
        elif answer == '1':
            pizza = 'Капри'
        elif answer == '2':
            pizza = 'Мексиканская'
        elif answer == '3':
            pizza = 'Кальцоне'
        elif answer == '4':
            pizza = 'Гавайская'
        elif answer == '5':
            pizza = 'Чили'
        self.model.add_to_pizza(pizza)

        ings = self.add_ings()
        self.model.add_ing(ings)
    
    def check_user_recipe(self, answer):
        if answer == '1':
            return 'Тесто'
        elif answer == '2':
            return 'Сыр'
        elif answer == '3':
            return 'Колбаса'
        elif answer == '4':
            return 'Огурцы'
        elif answer == '5':
            return 'Ананасы'
        elif answer == '6':
            return 'Оливки'

    
    def check_user_ings(self, answer):
        if answer == '1':
            return 'Кетчуп'
        elif answer == '2':
            return 'Майонез'
        elif answer == '3':
            return 'Острый перец'
        elif answer == '4':
            return 'Сладкий перец'