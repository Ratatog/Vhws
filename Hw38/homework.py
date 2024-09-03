"""ДОМАШКА"""

import sqlite3 as sq


with sq.connect('bd1.sqlite3') as con:
    cur = con.cursor()

    # 1. Создать таблицу "Студенты"
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        first_name TEXT,
        last_name TEXT,
        age INTEGER,
        group_name TEXT
    )
    ''')
    # Наполнить таблицу "Студенты"
    cur.execute('''
    INSERT INTO Students (first_name, last_name, age, group_name) VALUES 
    ('Иван', 'Иванов', 20, 'Группа A'),
    ('Мария', 'Петрова', 22, 'Группа B')
    ''')

    # 2. Создать таблицу "Продукты"
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        name TEXT,
        price REAL,
        quantity INTEGER
    )
    ''')
    # Наполнить таблицу "Продукты"
    cur.execute('''
    INSERT INTO Products (name, price, quantity) VALUES 
    ('Яблоко', 1.50, 100),
    ('Банан', 2.00, 50)
    ''')

    # 3. Создать таблицу "Заказы"
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
        order_number INTEGER,
        order_date DATE,
        total_amount REAL
    )
    ''')
    # Наполнить таблицу "Заказы"
    cur.execute('''
    INSERT INTO Orders (order_number, order_date, total_amount) VALUES 
    (101, '2024-09-01', 150.00),
    (102, '2024-09-02', 200.00)
    ''')

    # 4. Создать таблицу "Книги"
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        title TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT
    )
    ''')
    # Наполнить таблицу "Книги"
    cur.execute('''
    INSERT INTO Books (title, author, publication_year, genre) VALUES 
    ('Война и мир', 'Лев Толстой', 1869, 'Роман'),
    ('Преступление и наказание', 'Фёдор Достоевский', 1866, 'Роман')
    ''')

    # 5. Создать таблицу "Клиенты"
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Clients (
        first_name TEXT,
        last_name TEXT,
        address TEXT,
        phone TEXT
    )
    ''')
    # Наполнить таблицу "Клиенты"
    cur.execute('''
    INSERT INTO Clients (first_name, last_name, address, phone) VALUES 
    ('Анна', 'Сидорова', 'ул. Ленина, 10', '123-456-7890'),
    ('Олег', 'Кузнецов', 'ул. Пушкина, 20', '098-765-4321')
    ''')

    # 6. Создать таблицу "Сотрудники"
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        first_name TEXT,
        last_name TEXT,
        position TEXT,
        salary REAL
    )
    ''')
    # Наполнить таблицу "Сотрудники"
    cur.execute('''
    INSERT INTO Employees (first_name, last_name, position, salary) VALUES 
    ('Екатерина', 'Смирнова', 'Менеджер', 50000.00),
    ('Дмитрий', 'Волков', 'Разработчик', 60000.00)
    ''')

    # 7. Создать таблицу "Задачи"
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Tasks (
        title TEXT,
        description TEXT,
        status TEXT
    )
    ''')
    # Наполнить таблицу "Задачи"
    cur.execute('''
    INSERT INTO Tasks (title, description, status) VALUES 
    ('Задача 1', 'Описание задачи 1', 'выполнена'),
    ('Задача 2', 'Описание задачи 2', 'не выполнена')
    ''')

    # 8. Создать таблицу "Фильмы"
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Movies (
        title TEXT,
        director TEXT,
        release_year INTEGER,
        genre TEXT
    )
    ''')
    # Наполнить таблицу "Фильмы"
    cur.execute('''
    INSERT INTO Movies (title, director, release_year, genre) VALUES 
    ('Интерстеллар', 'Кристофер Нолан', 2014, 'Научная фантастика'),
    ('Паразиты', 'Пон Джун-хо', 2019, 'Триллер')
    ''')

    # 9. Создать таблицу "Компьютеры"
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Computers (
        model TEXT,
        processor TEXT,
        ram INTEGER,
        price REAL
    )
    ''')
    # Наполнить таблицу "Компьютеры"
    cur.execute('''
    INSERT INTO Computers (model, processor, ram, price) VALUES 
    ('Dell XPS 13', 'Intel i7', 16, 1200.00),
    ('MacBook Pro', 'Apple M1', 16, 1500.00)
    ''')

    # 10. Создать таблицу "События"
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Events (
        title TEXT,
        date DATE,
        description TEXT
    )
    ''')
    # Наполнить таблицу "События"
    cur.execute('''
    INSERT INTO Events (title, date, description) VALUES 
    ('Конференция', '2024-10-10', 'Ежегодная конференция по технологиям'),
    ('Концерт', '2024-11-15', 'Концерт классической музыки')
    ''')
