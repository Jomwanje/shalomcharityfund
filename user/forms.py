from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import NGO, Donation


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class NGOForm(forms.ModelForm):
    class Meta:
        model = NGO
        fields = '__all__'


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'
