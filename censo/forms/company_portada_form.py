# coding: utf-8

from django import forms
from django.forms import ModelForm
from censo.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import date

class CompanyPortadaPartialForm(ModelForm):

    class Meta:
        model = Company
        exclude = (
        	'old_id',
        	'number',
        	'name',
        	'cuerpo',
        	'phone',
        	'mail',
        	'commune',
        	'fax',
        	'postal_box',
        	'website',
        	'alarm_central',
        	'lemma',
        	'specialities',
        	'communes',
        )
        fields = (
        'address',
        'phone',
        'foundation_date',
        )

class CompanyPortadaForm(forms.Form):
    address = forms.CharField(max_length=255, label='dirección')
    phone = forms.CharField(max_length=100, label='teléfono')
    foundation_date = forms.DateField(widget=SelectDateWidget(years = xrange(1800, date.today().year + 1)), label='fecha fundación')

