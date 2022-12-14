from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import UserProfileForm, ExtendedUserCreationForm
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'not logged in'
    
    context = {'username': username}
    return render(request, 'prueba/index.html', context)

@login_required
def profile(request):
    return render(request, 'prueba/profile.html')

def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)

            return redirect('index')
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()
    
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'prueba/register.html', context)

def Home(request):
    return render(request, 'home.html')