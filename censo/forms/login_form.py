# coding: utf-8

from django import forms
from censo.models import Commune
from django.forms.extras.widgets import SelectDateWidget

class LoginForm(forms.Form):
    username = forms.CharField(label = 'Nombre de usuario', max_length=255)
    password = forms.CharField(label = 'Contraseña', max_length=255, widget = forms.PasswordInput)
