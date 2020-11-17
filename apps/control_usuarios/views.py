from django.shortcuts import render, redirect

#django
from django.contrib.auth import authenticate, login

# Create your views here.


def login_view(request):
    return redirect('list')