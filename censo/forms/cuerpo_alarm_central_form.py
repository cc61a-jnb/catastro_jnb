# encoding: utf-8
from django import forms
from django.forms import ModelForm
from censo.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import date
from django.template import Context, loader
from censo.utils import render_fields_as_table, render_fields_as_list, split_list
from . import BaseForm

class CuerpoAlarmCentralForm(BaseForm):


    # Display contacts details as a list
    def render_contacts_details_to_list(self):
        fields = self._field_range('adress_alarm_central', 'email_alarm_central')
        
        return render_fields_as_list(fields)

    # Display role shift questions as a table    
    def render_role_shift_to_table(self):
        fields = self._field_range('tomorrow_roleshift_quantity', 'night_roleshift_quantity')
        table_fields = [fields]
        
        column_labels = [field.label for field in fields]
        row_labels = ['Rol de turnos']
        
        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')

    # Display operators 24/7/365
    def render_operators_availableatalltimes_to_list(self):
        fields = [self['operators_availableatalltimes_quantity']]
        
        return render_fields_as_list(fields, 'list_quantities')

    # Display telephone exchange as a list
    def render_telephone_exchange_to_list(self):
        fields = self._field_range('telephoneexchange_electricalsupport', 'telephoneexchange_satellitesupport_mark')
        
        return render_fields_as_list(fields)

    # Display telephone lines questions as a table    
    def render_telephone_lines_to_table(self):
        fields = self._field_range('telephonelines_enable_quantity', 'telephonelines_input_quantity')
        table_fields = [fields]
        
        column_labels = [field.label for field in fields]
        row_labels = ['Nº']
        
        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')

    # Display phone calls as a list
    def render_phone_calls_to_list(self):
        fields = self._field_range('call_log', 'call_recording')
        
        return render_fields_as_list(fields)
    
    # Display cell equipment
    def render_cell_equipment_to_list(self):
        fields = [self['cell_equipment_quantity']]
        
        return render_fields_as_list(fields, 'list_quantities')    

    # Display frequencies as a list
    def render_frequencies_to_list(self):
        fields = self._field_range('frequency_one', 'national_emergency_frequency')
        
        return render_fields_as_list(fields)
    

    # Display tone_generator as a list
    def render_tone_generator_to_list(self):
        fields = self._field_range('tone_generator_mark', 'tone_generator_capacity')
        
        return render_fields_as_list(fields)

    #Display hardware technological support

    def render_hardware_technological_support_to_list(self):
        fields = [self['pc_quantity']]
        
        return render_fields_as_list(fields, 'list_quantities')
   
    #Display software technological support as a list
    def render_software_technological_support_to_list(self):
        fields = self._field_range('fk_os', 'origin_software_other')
        
        return render_fields_as_list(fields)

    #Display administration - documentation technological support as a list
    def render_administration_documentation_technological_support_to_list(self):
        fields = self._field_range('alarm_classification', 'fk_coded_keys')
        
        return render_fields_as_list(fields)
   
    #Display internet technological support
    def render_internet_technological_support_to_list(self):
        fields = [self['fk_internet_provider']]
        
        return render_fields_as_list(fields)


    # Display phone calls as a list
    def render_backup_power_to_list(self):
        fields = self._field_range('type_backup_power', 'energizing_backup_power')
        
        return render_fields_as_list(fields)

    # Display observations area    
    def render_observations_to_list(self):
        fields = [self['observations']]
        
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
        model = CuerpoAlarmCentralData
        exclude = ('cuerpo',)
