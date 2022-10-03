from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import User, UserRant
from .forms import userForm, rantForm

#usuarios


class UserCreateView(CreateView):
    model = User
    form_class = userForm
    success_url = '/accounts/login/?next=/'

class UserRantCreateView(CreateView):
    model = UserRant
    form_class = rantForm
    success_url = '/accounts/login/?next=/'