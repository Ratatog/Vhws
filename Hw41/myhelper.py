'''
# Установка джанго
pip install django

# Создание зависимостей в проекте
pip freeze > requirements.txt

# Создание джанго проекта
django-admin startproject mysite [. - Чтобы не было главной папки]

# Команда для запуска сервера
py manage.py runserver

# Создание приложения в проекте
py manage.py startapp blog_app

# Добавление приложения в проект settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    ...
    'blog_app',
]

# Прописывание маршрута в файле urls.py
urlpatterns = [
    ...
    path('', index),
]

# Статика
STATICFILES_DIRS = [
    BASE_DIR / 'static'
] # "Для необычных путей"

# Шаблоны
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
    },
]
'''
