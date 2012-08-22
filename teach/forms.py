from django import forms #cuz it is a package
import datetime
from django.contrib.auth.models import User

# lolling about the difference between ModelForm and Form
class UserProfileForm(forms.Form):
    favorite_animal = forms.CharField()
