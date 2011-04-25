# encoding: utf-8

from django import forms
from django.forms import ModelForm

from censo.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import date

class CompanyVolunteerPartialForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CompanyVolunteerPartialForm, self).__init__(*args, **kwargs)
        # Define empty label for ISP question
        self.fields['fk_internet_provider'].empty_label = 'No posee'


    class Meta:
        model = VolunteerData
        exclude = ('company',)
        
        
