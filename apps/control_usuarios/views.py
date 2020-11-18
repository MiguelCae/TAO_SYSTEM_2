from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from django.views.generic import CreateView

#django
from django.contrib.auth import authenticate, login

from .forms import Registro_Form

# Create your views here.


def login_view(request):
    return redirect('list')


class Registro_view(CreateView):
    model = User
    template_name = 'registration/registro.html'
    form_class = Registro_Form
    def get_success_url(self):
        return reverse('Home')

