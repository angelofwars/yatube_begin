from django.shortcuts import render
# Импортируем модель, чтобы обратиться к ней
from .models import Post


# Главная страница
def index(request):
    title = 'Yatube - соцсеть для разработчиков'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)



# view-функция принимает параметр slug из path()
def group_posts(request, slug):
    return render(request, 'posts/group_list.html')