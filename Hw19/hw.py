import re

# 1. Начало с гласной, конец на согласной
answer = r'^[аеёиоуыэюя].*[бвгджзйклмнпрстфхцчшщъь]$'
texts = ['А', 'Адронный коллайдер' ,'Машина', 'Беляш', 'Ералаш', 'Б']

for word in texts:
    res = re.search(answer, word.lower())
    if res:
        print(word)

# 2. Соответсвие всем url-адресам.
answer = r'https?:/(?:/[^/]+)+/?'
text = 'https://ya.ru/search/'

print( re.findall(answer, text) )

# 3. Хотя бы одно слово с заглавной буквы
answer = r'\s[А-ЯA-Z]'
text = 'один Два три четыре Пять'

print( re.search(answer, text) )

# 4. Строки с повторяющейся буквой
answer = r'(\S)\1'
text = 'Поезда Светофоры Картонные'

print( re.search(answer, text) )
