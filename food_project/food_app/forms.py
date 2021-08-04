from django import forms
from django.db import models
from django.contrib.auth.models import User
from .models import *

class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter User Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    
    class Meta():
        model = User
        fields = ['username', 'email', 'password']


class OrderForm(forms.ModelForm):
    class Meta():
        model = FoodOrderModel
        fields = '__all__'

