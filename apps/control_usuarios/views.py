from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver



from django.views.generic import CreateView
from apps.control_usuarios.models import Profile

#django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import Registro_Form

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name='Veterinarios'):
                return redirect('list_vet')
            elif user.groups.filter(name='Colaboradores'):
                return redirect('registro_mascota')
            elif user.groups.filter(name='Director'):
                return redirect('list')
            else:
                return redirect ('Home')
        else:
            return render(request, 'registration/login.html', {'error':'El usuario o la contraseña no coiciden'})
    return render (request, 'registration/login.html' )

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_conf = request.POST['password_confirmation']
        if password != password_conf:
            return render(request,'registration/registro.html', {'error': 'Las contraseñas no coinciden'})
        user = User.objects.create_user(username=username, password=password)
        user.first_name = request.POST['nombre']
        user.last_name = request.POST['Apellidos']
        user.save()
        profile = Profile(user=user)
        profile.save()
        return redirect('login')
    return render(request,'registration/registro.html')

def save_profile(sender, instance, created, **kwargs):
    if created:
        g1 = Group.objects.get(name='Adoptantes')
        instance.groups.add(g1)
post_save.connect(save_profile, sender=User)




class Registro_view(CreateView):
    model = User
    template_name = 'registration/registro.html'
    form_class = Registro_Form
    def get_success_url(self):
        return reverse('Home')


def send_email(mail, asunto, cuerpo):
    print(mail)
    print(asunto)
    print(cuerpo)



def indexmail(request):
    if request.method == 'POST':
        # mail = User.objects.filter(is_active=True).exclude(email='').values_list('email', flat=True)
        receiver = []
        for user in User.objects.all():
            receiver.append(user.email)
        asunto = request.POST.get('asunto')
        cuerpo = request.POST.get('cuerpo')
        send_mail(
            asunto,
            cuerpo,
            settings.EMAIL_HOST_USER,
            receiver,
            fail_silently=False
         )
    return render(request, 'mail.html', {})

