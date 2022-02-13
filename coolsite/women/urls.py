from django.urls import path


from .views import (
    index,
    show_category,
    about,
    addpage,
    contact,
    login,
    show_post,
    logout_user,
)

urlpatterns = [
    path('', index, name='home'),

    path('about/', about, name='about'),

    path('addpage/', addpage, name='add_page'),

    path('login/', login, name='login'),

    path('logout/', logout_user, name='logout'),

    path('contact/', contact, name='contact'),

    path('post/<slug:post_slug>', show_post, name='post'),

    path('cats/<int:cat_id>/', show_category, name='category'),
]
