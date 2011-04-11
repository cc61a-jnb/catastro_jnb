from django import forms
from censo.models import Commune

# CHOICES = tuple((c.number, c.name) for c in Commune.objects.all())

class SpikeForm(forms.Form):
    address = forms.CharField(max_length=255)
    commune = forms.ChoiceField(choices=Commune.objects.all())
    phone = forms.CharField(max_length=100)
    foundation_date = forms.DateField(required=False)