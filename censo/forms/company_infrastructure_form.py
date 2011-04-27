# encoding: utf-8
from django import forms
from django.forms import ModelForm
from censo.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import date
from django.template import Context, loader
from censo.utils import render_fields_as_table, render_fields_as_list, split_list
from . import BaseForm

class CompanyInfrastructureForm(BaseForm):
    building_material_type = forms.ModelMultipleChoiceField(queryset=BuildingMaterialType.objects.all(), label='Tipo de Material', widget=forms.CheckboxSelectMultiple(), required=False)
    
    # Display built area questions as a table    
    def render_built_area_to_table(self):
        fields = self._field_range('built_area_front_m2', 'built_area_total_m2')
        table_fields = [fields]
        
        column_labels = [field.label for field in fields]
        row_labels = ['Superficie (m2)']
        
        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')
        
    # Display street questions as a list    
    def render_street_questions_to_list(self):
        fields = self._field_range('main_street_name', 'narrow_street_name')
        
        return render_fields_as_list(fields)
        
    # Display Property Title Type question    
    def render_property_title_type_to_list(self):
        fields = [self['fk_property_title_type']]
        #fields = self._field_range('fk_property_title_type', 'property_title_type_other')
        
        return render_fields_as_list(fields)
        
    # Get a range of fields (ordered) between the given field names   
    def _field_range(self, start_field_name, end_field_name):
        fields = self.fields.items()
        return_fields = []
        
        indexing = False;
        
        for idx, field in enumerate(fields):
            if field[0] == start_field_name:
                indexing = True
                
            if indexing:
                return_fields.append(field[0])
                
            if field[0] == end_field_name:
                indexing = False
                
        return [self[field] for field in return_fields]

    class Meta:
        model = InfrastructureCompanyData
        exclude = ('company',)
