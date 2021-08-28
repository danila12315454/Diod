from cProfile import label

from django import forms
from .models import *
class login_form(forms.Form):
    email = forms.EmailField(max_length=40, label="", widget=forms.TextInput(attrs={'placeholder': 'Login or Email'}))
    password = forms.CharField(max_length=30, label="", widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    repit_password = forms.CharField(max_length=30, label="", widget=forms.TextInput(attrs={'placeholder': 'Repeat password'}))


class change_data_form(forms.Form):
    email = forms.CharField(max_length=40, label="email", required=False)
    password = forms.CharField(max_length=40, label="Пароль", required=False)
    description = forms.CharField(max_length=30, label="Описание аккаунта", required=False, widget=forms.Textarea())
    profile_photo = forms.FileField(widget=forms.FileInput(), required=False, label="Фото профиля")
    name = forms.CharField(max_length=40, label="Имя", required=False)
    login = forms.CharField(max_length=30, label="Логин", required=False)

