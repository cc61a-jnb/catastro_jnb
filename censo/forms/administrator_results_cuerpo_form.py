# encoding: utf-8
from django import forms
from censo.models import *

class AdministratorResultsCuerpoForm(forms.Form):
    region = forms.ModelChoiceField(queryset=Region.objects.all())
