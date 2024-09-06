from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def pages(request, num):
    return HttpResponse(f'Страница {num}')