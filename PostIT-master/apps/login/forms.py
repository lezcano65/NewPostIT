from django import forms
from django.db import models
from django.contrib.auth.forms import User


class changeEmailForm(forms.Form):

    email = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={
        "class": "input-field", "placeholder": "old email"
    }))
    email2 = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={
        "class": "input-field", "placeholder": "new email"
    }))
    email3 = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={
        "class": "input-field", "placeholder": "repeat new email"
    }))

    class Meta():
        model = User
        filter = ["email"]


class changeUsernameForm(forms.Form):
    username = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"class": "input-field", "placeholder": "old username"}))
    username2 = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"class": "input-field", "placeholder": "new username"}))
    username3 = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={"class": "input-field", "placeholder": "repeat new username"}))

    class Meta():
        model = User
        filter = ['username']
