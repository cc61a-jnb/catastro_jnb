# coding: utf-8

from django import forms
from django.forms import ModelForm
from censo.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import date
from censo.utils import combine_fields_errors

class BaseForm(ModelForm):

    def picture_fields(self):
        return []
    
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

    def reset_field_errors(self, fields):
        '''
        Method that clears the errors for a given list of boundfields
        This is used to display only one error per form table
        '''
        for field in fields:
            self._errors[field.name] = []
            
    def validate_field_range(self, start_field_name, end_field_name, global_error_message, local_error_message=None):
        '''
        Method that gets a range of fields of a form that are associated graphically (for example in a table)
        and condenses the validation to a single message to avoid cluttering with many identical messages
        if, for example, a user forgets to fill a table in which all attributes are required.
        
        It also adds a error to a global array because the forms are huge
        '''
        fields = self._field_range(start_field_name, end_field_name)
        local_errors = combine_fields_errors(fields)
        if local_errors:
            self.reset_field_errors(fields)
            if not local_error_message:
                local_error_message = local_errors[0]
            self._errors[fields[0].name] = self.error_class([local_error_message])
            self.custom_errors.append(global_error_message)
        return local_errors
        

