from django import forms
from django import forms
from censo.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import date

# CHOICES = tuple((c.number, c.name) for c in Commune.objects.all())

class CompanyPortadaForm(forms.Form):
    address = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=100)
    foundation_date = forms.DateField(widget=SelectDateWidget(years = xrange(1800, date.today().year + 1)))

