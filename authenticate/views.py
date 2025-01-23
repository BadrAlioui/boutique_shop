from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm, EditProfileForm
from .models import Profile


# Page d'authentification de base
def auth_view(request):
    return render(request, 'authenticate/authenticate.html')

# Connexion utilisateur
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'authenticate/login.html') 
    return render(request, 'authenticate/login.html')


# Déconnexion utilisateur
def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')

# Inscription utilisateur
def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            address = form.cleaned_data['address']
            Profile.objects.filter(user=user).update(address=address)
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request, "Your account has been created successfully!")
                print("Redirection effectuée vers 'home'")
                return redirect('home')
        else:
            print("Formulaire invalide :", form.errors)
            messages.error(request, "There was an error in your registration. Please try again.")
    else:
        form = SignUpForm()
    return render(request, 'authenticate/register.html', {'form': form})

  


# Modification du profil utilisateur
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            print("Redirection effectuée vers 'home'")
            return redirect('home')
        else:
            print("Formulaire invalide :", form.errors)
            messages.error(request, "There was an error updating your profile. Please try again.")
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'authenticate/edit_profile.html', {'edit_form': form})



def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Your password has been updated successfully!")
            return redirect('home')
        else:
            messages.error(request, "There was an error updating your password. Please try again.")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'authenticate/change_password.html', {'edit_form': form})

