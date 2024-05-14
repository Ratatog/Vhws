import re
from string import punctuation


# 1. Напишите регулярное выражение для разбора строк логов определенного формата. 
# Например, для строки лога "2024-05-12 12:34:56 [INFO] Сообщение лога" нужно 
# извлечь дату, время, уровень логирования и само сообщение.
text = '2024-05-12 12:34:56 [INFO] Сообщение лога'
answer = r'(\S*)\s(\S*)\s(\S*)\s(.*)'

print( re.findall(answer, text)[0] )

# 2. Напишите регулярное выражение, которое проверит, является ли строка допустимым паролем. 
# Пароль считается допустимым, если он содержит как минимум 8 символов, включая 
# хотя бы одну строчную букву, одну заглавную букву, одну цифру и один специальный символ.
answer = [r'.{8,}', r'[a-z]', r'[A-Z]', r'[0-9]', f'[{punctuation}]']
text = 'Ab-45678'

for i in answer:
    if not re.search(i, text):
        print('Пароль недопустим')
        break
else:
    print('Пароль допустим')

# 3.Напишите регулярное выражение, которое извлечет данные из HTML-таблицы, включая теги 
# <table>, <tr>, <td>, и содержимое ячеек. Например, из строки HTML-таблицы:
text = '<div class="test">Блок блок<p data_id="abc">Абзац</p>Блок</div>'
answer = r'<[^/][^>]*>'

print(re.findall(answer, text))

# 4. Напишите регулярное выражение, которое найдет все ссылки в тексте, включая ссылки 
# на веб-сайты (http/https), электронные адреса и ссылки на файлы. Затем оберните его 
# в функцию, которая возвращает данные в виде словаря:
# {"Ссылки": [...], "Почты": [...], "Файлы": [...]}
answer = r'(?P<srcs>https?:/(/[^\s/]+)+/?)|(?P<mails>[\S]+@[\S]+.(ru|com))|(?P<files>[\S]:(\\[^\s\\]+)+\\?)'
text = 'someText https://ya.ru/search http://vk.com/ ratatog@mail.ru C:\GeForce\Video someText'
res = {'srcs': [], 'mails': [], 'files': []}

def use(reg: re.Match, dct: dict):
    result = re.finditer(reg, text)
    for i in result:
        for k, v in i.groupdict().items():
            if v:
                dct[k].append(v)
use(answer, res)

print(res)
