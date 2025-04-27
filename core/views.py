from django.shortcuts import render, redirect, get_object_or_404
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from .models import Routine
from .forms import RoutineForm

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

def fortnite(request):
    return render(request, 'core/fortnite.html')

@login_required
def profile(request):
    routines = Routine.objects.filter(user=request.user)
    return render(request, 'core/profile.html', {'routines': routines})

@login_required
def create_routine(request, game):
    if request.method == 'POST':
        form = RoutineForm(request.POST)
        if form.is_valid():
            routine = form.save(commit=False)
            routine.user = request.user
            routine.game = game.upper()
            routine.save()
            return redirect('profile')
    else:
        form = RoutineForm(initial={'game': game.upper()})
    return render(request, 'core/routine_form.html', {'form': form})

@login_required
def edit_routine(request, pk):
    routine = get_object_or_404(Routine, pk=pk, user=request.user)
    if request.method == 'POST':
        form = RoutineForm(request.POST, instance=routine)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = RoutineForm(instance=routine)
    return render(request, 'core/routine_form.html', {'form': form})

@login_required
def delete_routine(request, pk):
    routine = get_object_or_404(Routine, pk=pk, user=request.user)
    if request.method == 'POST':
        routine.delete()
        return redirect('profile')
    return render(request, 'core/confirm_delete.html', {'routine': routine})