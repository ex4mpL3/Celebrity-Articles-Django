from django.urls import path


from .views import (
    WomenHome,
    WomenCategory,
    ShowPost,
    AddPage,
    about,
    contact,
    login,
    logout_user,
    register,
)

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),

    path('about/', about, name='about'),

    path('addpage/', AddPage.as_view(), name='add_page'),

    path('login/', login, name='login'),

    path('register/', register, name='register'),

    path('logout/', logout_user, name='logout'),

    path('contact/', contact, name='contact'),

    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),

    path('cats/<int:cat_id>/', WomenCategory.as_view(), name='category'),
]
