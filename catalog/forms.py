from django import forms
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password1','password2']

class NoteForm(forms.ModelForm):
    title = forms.CharField(label='Название', widget=forms.TextInput)
    content = forms.CharField(label='Текст', widget=forms.Textarea)
    class Meta:
        model = Note
        fields = ['title', 'content']
