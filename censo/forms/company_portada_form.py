# coding: utf-8

from django import forms
from django.forms import ModelForm
from censo.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import date
from . import BaseForm
from censo.utils import render_fields_as_table, render_fields_as_list, split_list, combine_fields_errors

class CompanyPortadaForm(BaseForm):

    # Display company number question
    #def render_company_number(self):
    #    fields = [self['number']]
        
    #    return render_fields_as_list(fields, 'list_quantities')
    
    # Display company address questions    
    #def render_company_address(self):
    #    fields = [self['address'], self['commune']]
        
    #    return render_fields_as_list(fields)
    
    # Display company other data questions    
    #def render_company_data(self):
    #    fields = [self['phone'], self['foundation_date']]
        
    #    return render_fields_as_list(fields)
        
    def base_position_fields(self):
        fields = self._field_range('director_name', 'assistant_name')
        return fields

    class Meta:
       model = PortadaCompanyData
       fields = ('director_name', 'captain_name', 'secretary_name',
            'tesorero_name', 'lieutenant_1_name', 'lieutenant_2_name', 'lieutenant_3_name', 'lieutenant_4_name', 'assistant_name', 'observations')
