import re

# 1. Начало с гласной, конец на согласной
answer = r'^[аеёиоуыэюя].*[бвгджзйклмнпрстфхцчшщъь]$'
texts = ['А', 'Адронный коллайдер' ,'Машина', 'Беляш', 'Ералаш', 'Б']

for word in texts:
    res = re.search(answer, word.lower())
    if res:
        print(word)