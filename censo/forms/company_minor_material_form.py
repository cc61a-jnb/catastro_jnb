# encoding: utf-8
from django import forms
from django.forms import ModelForm
from censo.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import date
from django.template import Context, loader
from censo.utils import render_fields_as_table, render_fields_as_list, split_list
from . import BaseForm

class CompanyMinorMaterialForm(BaseForm):

    # Display uniforms regulated questions as a table    
    def render_uniforms_regulated_to_table(self):
        fields = self._field_range('jackets_quantity', 'fireman_shoes_volunteer_quantity')
        table_fields = [fields]
        
        column_labels = [field.label for field in fields]
        row_labels = ['Nº']
        
        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')

   # Display ERA equipment questions as a table    
    def render_era_equipment_to_table(self):
        fields = self._field_range('scott_after_2004_quantity', 'mSA_quantity')
        table_fields = [fields]
        
        column_labels = [field.label for field in fields]
        row_labels = ['Nº']
        
        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')

   # Display hosepipe minor equipment questions as a table    
    def render_hosepipe_minor_equipment_to_table(self):
        fields = self._field_range('hosepipe_38mm_quantity', 'hosepipe_forest_quantity')
        table_fields = [fields]
        
        column_labels = [field.label for field in fields]
        row_labels = ['Nº']
        
        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')



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
        model = MinorMaterialCompanyData
        exclude = ('company',)
