from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Добро пожаловать!')

def group_posts(request, slug):
    return HttpResponse('Пользователь еще не добавил посты')

