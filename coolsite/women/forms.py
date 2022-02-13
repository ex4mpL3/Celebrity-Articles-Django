from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from captcha.fields import CaptchaField

from .models import *


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class RegisterUserForm(UserCreationForm):
    # These fields are optional, duplicated because in the password field in the
    # meta styles of the widget are not applied
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))

    email = forms.EmailField(label='Эл. почта',
                             widget=forms.EmailInput(attrs={'class': 'form-input'}))

    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    password2 = forms.CharField(label='Повторить пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'  # Replacing text in a list "-----------------"

    class Meta:
        model = Women
        fields = ('title',
                  'slug',
                  'content',
                  'photo',
                  'is_published',
                  'cat',
                  )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    # validator for title field
    def clean__title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title


class AddPostFormIndependent(forms.Form):
    title = forms.CharField(max_length=255,
                            label="Заголовок",
                            widget=forms.TextInput(attrs={'class': 'form-input'}))

    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'color': 60, 'rows': 10}))
    is_published = forms.BooleanField(required=False, initial=True)  # check box
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),
                                 empty_label="Категория не выбрана")


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Эл. почта')
    content = forms.CharField(widget=forms.Textarea(attrs={'color': 60, 'rows': 10}))
    captcha = CaptchaField()