from controller import PizzeriaController

def main():
    app = PizzeriaController()
    app.run()

if __name__ == '__main__':
    main()

# Выбор между режимом клиента и разработчика
    # 1. Клиент
    # Выбор пиццы или свой рецепт
        # Цена у каждой пиццы
        # Выбор размера пиццы
            # Цена у каждого размера

    # Если свой рецепт, то начинатся выбор ингредиентов
        # Цена у каждого ингредиента

    # Выбор способа оплаты
        # Или отказ от пиццы

    # На каждом шагу нужна кнопка "Назад"

    # В конце выдает информацию о пицце и стоимости
        # Информация о заказе помещается в файл


    # 2. Разработчик
    # Возможность просмотра истории заказов

    # Изменение цен на пиццы и ингредиентов
        # Название, цена

    # Добавление пицц и ингредиентов
        # Название, состав

    # Редактирование пицц
        # Название и состав


    # Кнопка выхода для нового выбора между режимами

# Все должно быть по принципам SOLID и с применением паттернов

'''
Выберите пиццу:
1. Пицца1 - 150р-600р
2. Пицца2 - 600р-1200р
3. Свая пицца - None
4. Выход
...

Размер:
1. Маленький - Xp
2. Средний - Xp
3. Большой - Xp
4. Назад
...

Составьте пиццу:
1. Сыр - р
2. Томаты - р
3. Огурцы - р
4. Ананасы - р
5. Отмена - р
6. Назад
...

Ингридиенты:
1. Холопеньо - р
2. Оливки - р
3. Отмена - р
4. Назад
...

Способ оплаты:
# Итоговая цена
1. Карта
2. Наличные

Информация о пицце:
#Пицца
#Состав


Разработчик:
1. Просмотр истории
2. Изменение
3. Добавление
4. Удаление
5. Выход

История стр1:
1. ...
2. ...
3. ...
4. След страница
5. Прошлая страница
6. Назад

Изменение:
Добавление:
Удаление:
#Пицца + информация
.. Назад
'''