from django.shortcuts import render, HttpResponse
from blog_app.dataset import dataset

# class Data:
#     def __init__(self, name) -> None:
#         self.name = name
    
#     def method(self):
#         return f'Вызов метода класса Date'

# Create your views here.
def index(request) -> HttpResponse:
    # return HttpResponse("Привет из Django!")
    # context = {'some_str': 'Какая-то строка',
    #            'some_int': 88,
    #            'some_list': ['Один', 1],
    #            'some_dict': {'fruit': 'apple'},
    #            'data': Data('Ratatog')}
    context = {'posts': dataset}
    
    return render(request, 'blog_app/index.html', context=context)

def post_by_slug(request, post_slug):
    # return HttpResponse(f'Пост с названием {post_slug}')
    post = [post for post in dataset if post['slug'] == post_slug]
    if not post:
        return HttpResponse('404 - Пост не найден', status=404)
    else:
        return render(request, 'blog_app/post_detail.html', context=post[0], status=200)