# coding: utf-8
from django import forms
from django.forms import ModelForm
from censo.models import *
from django.template import Context, loader
from censo.utils import render_fields_as_table, render_fields_as_list, split_list, combine_fields_errors
from . import BaseForm

class CuerpoANBForm(BaseForm):
    
    # Display instructor questions as a table    
    def render_instructors_to_table(self):
        fields = self._field_range('cuerpo_procedure_instructors', 'anb_specialty_instructors')
        table_fields = split_list(fields, 2)
        
        column_labels = ['Área procedimientos', 'Área salud', 'Área de especialidad']
        row_labels = ['Cursos del Cuerpo', 'Cursos de la Academia']
        
        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')
        
    # Display course infrastructure questions as a list    
    def render_infrastructure_to_list(self):
        fields = self._field_range('cuerpo_courses_infrastructure_rooms', 'cuerpo_courses_infrastructure_rcp')
        
        return render_fields_as_list(fields, 'list_quantities')

    # Display brigade questions as a list    
    def render_brigade_number_to_list(self):
        fields = self._field_range('volunteer_brigada_juvenil_antiquity', 'volunteer_brigada_juvenil_members_quantity')
        
        return render_fields_as_list(fields, 'list_quantities')
    
    def render_brigade_data_to_list(self):
        fields = self._field_range('volunteer_brigada_juvenil_name', 'volunteer_brigada_juvenil_responsible_email')
        
        return render_fields_as_list(fields)

    # Display observations area    
    def render_observations_to_list(self):
        fields = [self['observations']]
        
        return render_fields_as_list(fields)

    class Meta:
        model = CuerpoANBData
        exclude = ('cuerpo',)
