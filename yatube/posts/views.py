from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')




# view-функция принимает параметр slug из path()
def group_posts(request, slug):
    return HttpResponse(f'Мороженое номер {slug}')