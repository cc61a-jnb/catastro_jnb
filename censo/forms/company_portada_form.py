# coding: utf-8

from django import forms
from django.forms import ModelForm
from censo.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import date
from . import BaseForm
from censo.utils import render_fields_as_table, render_fields_as_list, split_list, combine_fields_errors

class CompanyPortadaForm(BaseForm):


    def base_position_fields(self):
        fields = self._field_range('director_name', 'assistant_name')
        return fields

    # Display staff-only control fields
    def render_staff_only_form_to_list(self):
        fields = [self['is_complete'], self['is_correct']]
        
        return render_fields_as_list(fields)

    class Meta:
       model = PortadaCompanyData
       fields = ('director_name', 'captain_name', 'secretary_name',
            'tesorero_name', 'lieutenant_1_name', 'lieutenant_2_name', 'lieutenant_3_name', 'lieutenant_4_name', 'assistant_name', 'observations', 'is_complete', 'is_correct')
