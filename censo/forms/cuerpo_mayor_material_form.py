# coding: utf-8
from django import forms
from django.forms import ModelForm
from censo.models import *
from django.template import Context, loader
from censo.utils import render_fields_as_table, render_fields_as_list, split_list, combine_fields_errors
from . import BaseForm

class CuerpoMayorMaterialForm(BaseForm):

    # Display vehicle info questions as a list
    def render_vehicle_info_questions_to_list(self):
        fields = self._field_range('fk_vehicle_type', 'fk_procedence')
        
        return render_fields_as_list(fields)

    # Display legal status questions as a list
    def render_legal_status_questions_to_list(self):
        fields = self._field_range('registered', 'fk_vehicle_checkup')
        
        return render_fields_as_list(fields)
        
     # Display kilometraje horometraje as a list
    def render_kilometraje_horometraje_to_list(self):
        fields = self._field_range('kilometraje', 'horometraje')
        
        return render_fields_as_list(fields)
        
    # Display caracteristics as a list
    def render_caracteristics_to_list(self):
        fields = self._field_range('fk_fire_engine_camiva_model', 'oil_change_kilometraje')
        
        return render_fields_as_list(fields)
        
    # Display motor change as a list
    def render_motor_change_to_list(self):
        fields = self._field_range('motor_change_new_manufacturer', 'motor_change_new_number')
        
        return render_fields_as_list(fields)
    
    # Display gearbox change as a list
    def render_gearbox_change_to_list(self):
        fields = self._field_range('gearbox_change_new_manufacturer', 'gearbox_change_new_model')
        
        return render_fields_as_list(fields)
 
    class Meta:
        model = CuerpoMayorMaterialData
        exclude = ('cuerpo',)
