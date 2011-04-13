from django import forms
from django import forms
from censo.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import date

# CHOICES = tuple((c.number, c.name) for c in Commune.objects.all())

class CompanyPortadaForm(forms.Form):
    number = forms.IntegerField()
    address = forms.CharField(max_length=255)
    commune = forms.ModelChoiceField(queryset=Commune.objects.all())
    province = forms.ModelChoiceField(queryset=Province.objects.all())
    region = forms.ModelChoiceField(queryset=Region.objects.all())
    phone = forms.CharField(max_length=100)
    foundation_date = forms.DateField(widget=SelectDateWidget(years = xrange(1800, date.today().year + 1)))

