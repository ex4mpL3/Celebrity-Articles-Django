from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.views import generic

from women import forms
from women.models import Women, Category
from women.utils import DataMixin


class WomenHome(DataMixin, generic.ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # get existing context and update him
        c_def = self.get_user_context(title='Главная страница')
        context.update(c_def)
        return context

    def get_queryset(self):  # What data will the class generate
        return Women.objects.filter(is_published=True)


def about(request):
    context = {
        'title': 'о сайте'
    }
    return render(request, 'women/about.html', context)


class AddPage(LoginRequiredMixin, DataMixin, generic.CreateView):
    form_class = forms.AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')  # if there is no get_absolute_url in the model,
    # we specify where to redirect when adding a new record

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        context.update(c_def)
        return context


class ContactFormView(DataMixin, generic.FormView):
    form_class = forms.ContactForm
    template_name = 'women/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        context.update(c_def)
        return context

    def form_valid(self, form):
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = forms.LoginUserForm
    template_name = 'women/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        context.update(c_def)
        return context

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(DataMixin, generic.CreateView):
    form_class = forms.RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        context.update(c_def)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class ShowPost(DataMixin, generic.DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        context.update(c_def)
        return context


class WomenCategory(DataMixin, generic.ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False  # if don`t have records - will throw exception 404

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title=f'Категория - {category.name}',
                                      cat_selected=category.pk)

        context.update(c_def)
        return context


def logout_user(request):
    logout(request)
    return redirect('login')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Your page not found</h1>")