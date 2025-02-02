from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class EditProfileForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter your username'}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Enter your email'}),
    )
    first_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter your first name'}),
    )
    last_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter your last name'}),
    )
    address = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter your address'}),
    )

    class Meta:
        model = Profile
        fields = ('address',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Passé depuis la vue
        super().__init__(*args, **kwargs)

        # Pré-remplir les champs User
        self.fields['username'].initial = user.username
        self.fields['email'].initial = user.email
        self.fields['first_name'].initial = user.first_name
        self.fields['last_name'].initial = user.last_name

    def save(self, commit=True):
        # Sauvegarder les données User
        user = self.instance.user
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()

        # Sauvegarder les données Profile
        return super().save(commit=commit)


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control",
                                      "placeholder": "Enter your username"}),
        max_length=150,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control",
                                       "placeholder": "Enter your email"})
    )
    first_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control",
                                      "placeholder": "Enter your first name"})
    )
    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control",
                                      "placeholder": "Enter your last name"})
    )
    address = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control",
                                      "placeholder": "Enter your address"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control",
                                          "placeholder": "Your password"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control",
                                          "placeholder": "Confirm password"})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=commit)
        # Vérifier si un profil existe déjà
        profile, created = Profile.objects.get_or_create(user=user)
        profile.address = self.cleaned_data['address']  # Met à jour l'adresse
        if commit:
            profile.save()
        return user