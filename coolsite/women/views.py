from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponseNotFound

from .forms import AddPostForm
from .models import Women

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'},
]


def index(request):
    context = {
        'title': 'главная страница',
        'menu': menu,
        'posts': Women.objects.all(),
        'cat_selected': 0,  # show all category
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    context = {
        'title': 'о сайте'
    }
    return render(request, 'women/about.html', context)


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    context = {
        'menu': menu,
        'title': "Добавление статьи",
        'form': form,
    }
    return render(request, 'women/addpage.html', context=context)


def contact(request):
    pass


def login(request):
    pass


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'women/post.html', context=context)


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    context = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': posts,
        'cat_selected': cat_id,  # show the desired category
    }
    return render(request, 'women/index.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Your page not found</h1>")