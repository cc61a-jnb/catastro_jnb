from django import forms
from censo.models import Commune
from django.forms.extras.widgets import SelectDateWidget

# CHOICES = tuple((c.number, c.name) for c in Commune.objects.all())

class SpikeForm(forms.Form):
    address = forms.CharField(max_length=255)
    commune = forms.ChoiceField(choices=Commune.objects.all())
    phone = forms.CharField(max_length=100)
    foundation_date = forms.DateField(required=False, widget=SelectDateWidget())

class CompanyCadastreForm(forms.Form):
    pass
    # SPECIALTY_CHOICES = (
    #     'Agua',
    #     'Escala',
    #     'Salvamento',
    #     'Rescate Urbano',
    #     'Rescate Vehicular',
    #     'Incendios Forestales',
    #     'Haz Mat',
    #     'Gersa',
    #     'Rescate Minero',
    #     'Incendios Industriales',
    #     'Otro',
    #     'Agua',
    #     'Agua',
    #     'Agua',

    # )

    # company_name
    # active_volunteer_men_number
    # active_volunteer_women_number
    # paid_volunteer_women_number
    # paid_volunteer_men_number
    # required_antiquity_for_being_paid_in_years
    # company_specialty



