from django.urls import path


from .views import (
    WomenHome,
    WomenCategory,
    ShowPost,
    AddPage,
    about,
    ContactFormView,
    LoginUser,
    logout_user,
    RegisterUser,
)

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),

    path('about/', about, name='about'),

    path('addpage/', AddPage.as_view(), name='add_page'),

    path('login/', LoginUser.as_view(), name='login'),

    path('register/', RegisterUser.as_view(), name='register'),

    path('logout/', logout_user, name='logout'),

    path('contact/', ContactFormView.as_view(), name='contact'),

    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),

    path('cats/<int:cat_id>/', WomenCategory.as_view(), name='category'),
]
