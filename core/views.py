from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 

def index(request):
    return render(request, 'core/index.html')

def games(request):
    return render(request, 'core/games.html')

def routine(request):
    return render(request, 'core/routine.html')

def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
        
    context = {'signupform':form}

    return render(request, 'core/signup.html', context=context)


def login(request):

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                
                auth.login(request, user)

                return redirect("routine")
    context = {'loginform':form}

    return render(request, 'core/login.html', context=context)

def user_logout(request):

    auth.logout(request)

    return redirect('/')

@login_required(login_url="login")
def myscrims(request):
    return render(request, 'core/myscrims.html')


def valorant(request):
    return render(request, 'core/valorant.html')

def cs2(request):
    return render(request, 'core/cs2.html')

def profile(request):
    return render(request, 'core/profile.html')