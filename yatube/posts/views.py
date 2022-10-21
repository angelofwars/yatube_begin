from django.http import HttpResponse
from django.shortcuts import render
# Главная страница
def index(request):
    title = 'Yatube - соцсеть для разработчиков'
    context = {
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Главная страница',
    }
    return render(request, 'posts/index.html', context)




# view-функция принимает параметр slug из path()
def group_posts(request, slug):
    return render(request, 'posts/group_list.html')