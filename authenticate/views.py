from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import User
from .forms import SignUpForm

# Page d'authentification de base
def auth_view(request):
    return render(request, 'authenticate/authenticate.html', {})

# Connexion utilisateur
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('login')  
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')  
    else:
        return render(request, 'authenticate/login.html', {})

# Déconnexion utilisateur
def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home') 

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save() 
            username = form.cleaned_data['username']  
            raw_password = form.cleaned_data['password1']  
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request, "Your account has been created successfully!")
                return redirect('home')
        else:
            messages.error(request, "There was an error in your registration. Please try again.")
    else:
        form = SignUpForm()
    return render(request, 'authenticate/register.html', {'form': form})