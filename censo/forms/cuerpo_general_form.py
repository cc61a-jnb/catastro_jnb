# coding: utf-8
from django import forms
from django.forms import ModelForm
from censo.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import date
from django.template import Context, loader
from censo.utils import render_fields_as_table, render_fields_as_list, split_list, combine_fields_errors
from . import BaseForm

class CuerpoGeneralForm(BaseForm):

    def __init__(self, *args, **kwargs):
        super(CuerpoGeneralForm, self).__init__(*args, **kwargs)
        # Define empty label for ISP question
        self.fields['fk_internet_provider'].empty_label = 'No posee'
    
    # Display hardware questions as a table    
    def render_hardware_to_table(self):
        fields = self._field_range('computers_quantity', 'printers_quantity')
        table_fields = [fields]
        
        column_labels = [field.label for field in fields]
        row_labels = ['Cantidad']
        
        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')
        
    # Display ISP question    
    def render_isp_to_list(self):
        fields = [self['fk_internet_provider']]
        
        return render_fields_as_list(fields)

    # Display website/social pages questions as a list    
    def render_web_to_list(self):
        fields = self._field_range('website', 'social_other_account_name')
        
        return render_fields_as_list(fields)
        
    # Display accounting system questions as a list
    def render_accounting_system_to_list(self):
        fields = self._field_range('fk_accounting_system', 'accounting_system_other_name')
        
        return render_fields_as_list(fields)
        
    # Display personnel questions as a table    
    def render_personnel_to_table(self):
        fields = self._field_range('personnel_guard', 'personnel_junior')
        table_fields = split_list(fields, 9)
        
        row_labels = [
            'Cuarteleros cuidadores', 
            'Cuarteleros conductores', 
            'Secretarios', 
            'Contadores', 
            'Operadores Central de Alarmas', 
            'Administrativos', 
            'Mecánicos de planta', 
            'Personal de Aseo', 
            'Servicios generales/Junior'
        ]
        column_labels = ['N°']
        # for loop_fields in table_fields
        #     row_labels = [loop_fields[0].label]
        
        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')

    # Display observations area    
    def render_observations_to_list(self):
        fields = [self['observations']]
        
        return render_fields_as_list(fields)

    class Meta:
        model = CuerpoGeneralData
        exclude = ('cuerpo',)
