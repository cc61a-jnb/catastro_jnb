# encoding: utf-8

from django import forms
from django.forms import ModelForm

from censo.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import date

class CompanyVolunteerPartialForm(ModelForm):

    class Meta:
        model = VolunteerData
        exclude = ('company',)
