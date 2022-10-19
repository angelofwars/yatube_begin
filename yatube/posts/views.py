from django.http import HttpResponse
from django.shortcuts import render
# Главная страница
def index(request):
    return render(request, 'posts/index.html')




# view-функция принимает параметр slug из path()
def group_posts(request, slug):
    return HttpResponse(f'Мороженое номер {slug}')