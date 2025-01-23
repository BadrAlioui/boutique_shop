from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address',)  # Inclure seulement les champs que vous voulez modifier
        widgets = {
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your address'
            }),
        }




class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your username"}),
        max_length=150,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email"})
    )
    first_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your first name"})
    )
    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your last name"})
    )

    address = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your address"})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter your password"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm your password"})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'password1', 'password2',)

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if len(address) < 5:
            raise forms.ValidationError("The address must be at least 5 characters long.")
        return address

