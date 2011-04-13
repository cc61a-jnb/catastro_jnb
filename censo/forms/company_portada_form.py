from django import forms
from django import forms
from censo.models import *
from django.forms.extras.widgets import SelectDateWidget

# CHOICES = tuple((c.number, c.name) for c in Commune.objects.all())

class CompanyPortadaForm(forms.Form):
    number = forms.IntegerField()
    address = forms.CharField(max_length=255)
    commune = forms.ChoiceField(choices=Commune.objects.all())
    province = forms.ChoiceField(choices=Province.objects.all())
    region = forms.ChoiceField(choices=Region.objects.all())
    phone = forms.CharField(max_length=100)
    foundation_date = forms.DateField(required=False, widget=SelectDateWidget(list(xrange(1800,2011))))