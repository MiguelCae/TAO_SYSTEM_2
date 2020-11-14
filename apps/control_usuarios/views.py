from django.shortcuts import render, redirect

#django
from django.contrib.auth import authenticate, login

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, passsword=password)
        if user:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login/login.html', {'error':'Usurio o contraseña inválida'})
            
    return render(request, 'login/login.html')