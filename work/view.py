def add_title(title):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(title.center(50, '='))
            result = func(*args, **kwargs)
            print('=' * 50)
            return result
        return wrapper
    return decorator


class PizzeriaView:
    def __init__(self):
        pass
    
    @add_title('Выбор пиццы')
    def wait_user_answer(self):
        print('Выбор пиццы: '
              '\n1. Капри'
              '\n2. Мексиканская'
              '\n3. Кальцоне'
              '\n4. Гавайская'
              '\n5. Чили'
              '\n6. Свой рецепт'
              '\n"quit" - Выход')
        user_query = input('Выберите вариант действия: ')
        return user_query
    
    @add_title('Выбор рецепта')
    def wait_user_recipe(self, curr_ings):
        print(f'Выберите до {curr_ings} ингридиентов для пиццы'
              '\n1. Тесто'
              '\n2. Сыр'
              '\n3. Колбаса'
              '\n4. Огурцы'
              '\n5. Ананасы'
              '\n6. Оливки'
              '\n"end" - Конец')
        user_query = input('Выберите вариант действия: ')
        return user_query
    
    @add_title('Выбор добавок')
    def wait_user_ings(self, curr_ings):
        print(f'Выберите до {curr_ings} добавок: '
              '\n1. Кетчуп'
              '\n2. Майонез'
              '\n3. Острый перец'
              '\n4. Сладкий перец'
              '\n"end" - Конец')
        user_query = input('Выберите вариант действия: ')
        return user_query
    
    @add_title('Итоговая пицца')
    def show_pizza(self, pizza, ings):
        print(f'Пицца: {pizza}'
              f'\nИнгридиенты: {ings}')