# coding: utf-8
from django import forms
from django.forms import ModelForm
from censo.models import *
from django.template import Context, loader
from censo.utils import render_service_acts, render_fields_as_list, split_list, combine_fields_errors
from . import BaseForm

class CuerpoServiceActsForm(BaseForm):

    def clean(self):
        data = self.cleaned_data
        
        self.custom_errors = []

        # If any validation fails, raise error
        if self.custom_errors:
            raise forms.ValidationError(self.custom_errors)

        return self.cleaned_data

    # Display service acts questions as a table
    def render_acts_to_table(self):
        fields = self._field_range('structural_fire_quantity', 'support_other_cuerpos_quantity')
        table_fields = split_list(fields, 12)

        #field_codes = self._field_range('structural_fire_code', 'support_other_cuerpos_code')
        row_labels = [fields.label for fields in fields]
        column_labels = ['Cantidad']

        return render_service_acts(table_fields, column_labels, row_labels, 'table_service_acts')

    def render_acts_to_list(self):

        fields = self._field_range('structural_fire_quantity', 'support_other_cuerpos_quantity')
        return render_fields_as_list(fields)

    # Display staff-only control fields    
    def render_staff_only_form_to_list(self):
        fields = [self['is_complete'], self['is_correct']]
        
        return render_fields_as_list(fields)

    class Meta:
        model = CuerpoServiceActsData
        exclude = ('cuerpo',)
