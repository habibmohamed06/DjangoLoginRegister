from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

def newsignup(request):
    if request.method == "GET":
        form = CreateUserForm()
        return render(request, 'signup.html', {"form": form})
    else:
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                saveuser = User.objects.create_user(request.POST.get('username'), email=request.POST.get('email'), password = request.POST.get('password1'))
                saveuser.save()
                return render(request, 'index.html', {"form": UserCreationForm,"user": request.POST.get('username')})
            except:
                return render(request, 'signup.html', {"form": UserCreationForm,"error": request.POST.get('username') + " already exists !"})
        else:
            return render(request, 'signup.html', {"form": UserCreationForm,"error": "The passwords didn't Match!"})

def signin(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        emails = User.objects.filter(is_active=True).values_list('email', flat=True)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/accueil')
        else:
            return render(request, 'index.html', {"form": UserCreationForm,"error": "The username or the password is incorrect!"})
    context = {}
    return render(request, 'index.html', context)


    

def accueil(request):
    return render(request, 'accueil.html')
