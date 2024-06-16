import json


# class Pizza:
#     def __init__(self):
#         pass
    
#     def __str__(self):
#         return f''


class PizzerialeModel:
    def __init__(self):
        self.pizza = None
        self.ings = None
    
    def add_to_pizza(self, pizza_ing):
        self.pizza = pizza_ing
    
    def add_ing(self, ing):
        self.ings = ing
    
    def get_pizza(self):
        return self.pizza, self.ings
    