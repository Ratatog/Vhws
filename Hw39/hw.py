"""
1.	Создать  БД “онлайн-магазина,”с таблицами users, orders, products(таблицы можно создать через СУБД и наполнить их можно там же) и требования:
    a.	Пользователи могут регистрироваться, входить в систему и изменять свои данные.
    b.	Пользователи могут просматривать каталог товаров, добавлять их в корзину и оформлять заказы.
"""

import click
import sqlite3 as sq

@click.group
def task1(): pass

# Регистрация (добавление в базу данных)
@click.command(name='reg')
@click.option('--name', prompt='Введите имя пользователя')
@click.option('--email', prompt='Введите почту')
def register(name, email):
    with sq.connect('bd1.sqlite3') as con:
        cur = con.cursor()
        cur.execute(f"""
        INSERT INTO users (name, email) VALUES
        ("{name}", "{email}")
        """)

# Просмотр каталога
@click.command(name='catalog')
def read_products():
    with sq.connect('bd1.sqlite3') as con:
        cur = con.cursor()
        res = cur.execute("""
        SELECT name, price
        FROM products
        """).fetchall()
        for i in range(len(res)):
            print(f'{i}. {res[i][0]} - {res[i][1]}р.')

# Добавление в корзину (Без "аккаунта")
@click.command(name='add')
@click.option('--user', prompt='Введите имя пользователя')
@click.option('--prod', prompt='Введите id товара или Имя товара')
def add_to_cart(user, prod: str):
    with sq.connect('bd1.sqlite3') as con:
        cur = con.cursor()
        cart = cur.execute(f"""
        SELECT cart
        FROM users
        WHERE name = "{user}"
        """).fetchone()
        if cart is None:
            print('Пользователь не найден')
            return
        
        col = 'id' if prod.isdigit() else 'name'
        product = cur.execute(f"""
        SELECT name, price
        FROM products
        WHERE {col} = "{prod}"
        """).fetchone()
        if product is None:
            print('Продукт не найден')
            return
        
        prod_list = [] if not cart[0] else cart[0].split(';')
        prod_list.append(f'{product[0]}${product[1]}')
        prod_str = ';'.join(prod_list)
        cur.execute(f"""
        UPDATE users
        SET cart = "{prod_str}"
        WHERE name = "{user}"
        """)
        
# Покупка и очиска корзины
@click.command(name='buy')
@click.option('--user', prompt='Введите имя пользователя')
def buy_cart(user):
    with sq.connect('bd1.sqlite3') as con:
        cur = con.cursor()
        cart = cur.execute(f"""
        SELECT cart
        FROM users
        WHERE name = "{user}"
        """).fetchone()
        if cart is None:
            print('Пользователь не найден')
            return

        cart_list = cart[0].split(';')
        print('Покупка совершена успешно')
        print(f'Цена: {sum([float(i.split('$')[1]) for i in cart_list])}')
        input()
        print('Товары:')
        for i in range(len(cart_list)):
            p = cart_list[i].split('$')
            print(f'{i+1}. {p[0]} - {p[1]}')
            
        cur.execute(f"""
        UPDATE users
        SET cart = ''
        WHERE name = "{user}"
        """)
        
        
# Просмотр и изменение корзины
# ...
# (В задании не было)
        


task1.add_command(register)
task1.add_command(read_products)
task1.add_command(add_to_cart)
task1.add_command(buy_cart)

if __name__ == '__main__':
    task1()