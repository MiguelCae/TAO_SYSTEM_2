from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

from .models import Profile


class Registro_Form(UserCreationForm):

    class Meta:
        model = User
        fields = [

            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username':'Usuario',
            'first_name':'Nombres',
            'last_name':'Apellidos',
            'email':'Correo electrónico',
        }
    