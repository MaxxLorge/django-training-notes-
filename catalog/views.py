from django.shortcuts import render, redirect, get_list_or_404
from rest_framework.response import Response

from .models import Note
from .forms import NoteForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .serializers import UserSerializer,UserDetailedSerializer, NoteSerializer
from rest_framework import generics
# Create your views here.


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailed(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailedSerializer

class NotesList(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

@login_required
def index(request):
    notes = Note.objects.filter(author=request.user)
    if request.method == 'POST':
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            new_note = note_form.save(commit=False)
            new_note.author = request.user
            new_note.save()
    else:
        note_form = NoteForm()
    return render(
        request,
        'index.html',
        context={'notes': notes, 'note_form': note_form, 'user': request.user}
    )

def reg(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        reg_form = UserRegisterForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            user = authenticate(request, username = request.POST['username'], password = request.POST['password1'])
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Не удалось зарегистироваться')
    else:
        reg_form = UserRegisterForm()
    return render(
        request,
        'reg.html',
        context={'reg_form': reg_form}
    )

def auth(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        auth_form = AuthenticationForm(data=request.POST)
        if auth_form.is_valid():
            user = auth_form.get_user()
            login(request, user)
            return redirect('index')
    else:
        auth_form = AuthenticationForm()

    return render(
        request,
        'auth.html',
        context={'auth_form': auth_form}
    )

def user_logout(request):
    logout(request)
    return redirect('auth')