from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Book
from django import forms

class Signup(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','genre','availability','num_available']
        