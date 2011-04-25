# coding: utf-8

from django import forms
from django.forms import ModelForm
from censo.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import date

class CompanyPortadaPartialForm(ModelForm):
    # Redefine foundation_date to use a different widget and year range
    foundation_date = forms.DateField(widget=SelectDateWidget(years = xrange(1800, date.today().year + 1)), label='Fecha fundación')

    class Meta:
        model = Company
        fields = (
        	'address',
        	'phone',
        	'foundation_date',
        )

