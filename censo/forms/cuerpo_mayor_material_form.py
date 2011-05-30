# coding: utf-8
from django import forms
from django.forms import ModelForm
from censo.models import *
from django.template import Context, loader
from django.forms.extras.widgets import SelectDateWidget
from censo.utils import render_fields_as_table, render_fields_as_list, split_list, combine_fields_errors
from . import BaseForm

class CuerpoMayorMaterialForm(BaseForm):

    def clean(self):
        data = self.cleaned_data
        
        self.custom_errors = []
        
        #Denomination is a required field
        if data['denomination'] == u'':
            error_message = 'Este campo es requerido'
            self._errors['denomination'] = self.error_class([error_message])
        
        #The kilometers during the oil change cannot be higher that the current quantity    
        if data['oil_change_kilometraje'] > data ['kilometraje']:
            error_message = 'El kilometraje del último cambio de aceite no puede ser mayor al kilometraje actual'
            self._errors['kilometraje'] = self.error_class([error_message])
            self._errors['oil_change_kilometraje'] = self.error_class([error_message])
            self.custom_errors.append(error_message)
        
        # If any validation fails, raise error
        if self.custom_errors:
            raise forms.ValidationError(self.custom_errors)
        
        return self.cleaned_data
    
    vehicle_year = forms.DateField(label='Año del Vehículo', widget=SelectDateWidget(years=range(1900, 2020)), required=False)
    service_incorporation_date = forms.DateField(label='Fecha de incorporación', widget=SelectDateWidget(years=range(1900, 2020)), required=False)
    last_oil_change_date = forms.DateField(label='Fecha último cambio de aceite', widget=SelectDateWidget(years=range(1900, 2020)), required=False)
        
    
    # Display company selector
    def render_company_question_to_list(self):
        fields = self._field_range('company', 'company')
        
        return render_fields_as_list(fields)

    # Display vehicle info questions as a list
    def render_vehicle_info_questions_to_list(self):
        fields = self._field_range('fk_vehicle_type', 'fk_procedence')
        
        return render_fields_as_list(fields)

    # Display legal status questions as a list
    def render_legal_status_questions_to_list(self):
        fields = self._field_range('registered', 'vehicle_checkup')
        
        return render_fields_as_list(fields)
        
     # Display kilometraje horometraje as a list
    def render_kilometraje_horometraje_to_list(self):
        fields = self._field_range('kilometraje', 'horometraje')
        
        return render_fields_as_list(fields, css_class_name='list_quantities')
        
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
        
    # Display motor/gearbox repairs as a list
    def render_repairs_to_list(self):
        fields = self._field_range('motor_repairs', 'gearbox_repairs')
        
        return render_fields_as_list(fields)

    # The list of all the picture fields in this form    
    def picture_fields(self):
        fields = self._field_range('picture_front_view', 'picture_back_view')
        return [(field, getattr(self.instance, field.name)) for field in fields]
 
    class Meta:
        model = CuerpoMayorMaterialData
        exclude = ('cuerpo',)
