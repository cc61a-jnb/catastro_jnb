# coding: utf-8
from django import forms
from django.forms import ModelForm
from censo.models import *
from django.template import Context, loader
from django.forms.extras.widgets import SelectDateWidget
from censo.utils import render_fields_as_table, render_fields_as_list, split_list, combine_fields_errors
from . import BaseForm
import pdb

class CuerpoMayorMaterialForm(BaseForm):

    def clean(self):
        data = self.cleaned_data
        
        self.custom_errors = []
        #self.validate_field_range('fk_vehicle_type', 'fk_procedence','Corrija los campos')
        #self.validate_field_range('registered', 'vehicle_checkup','Corrija los campos2 ')
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

        # This must be affiliated either with a company or with central
        if not data['company'] and data['cuerpo_vehicle_own'] == 0:
            error_message = 'Debe especificar una compañia o nivel central'
            self._errors['company'] = self.error_class([error_message])

        if data['company'] and data['cuerpo_vehicle_own'] != 0:
            error_message = 'Debe especificar sólo una compañia o nivel central, no ambas'
            self._errors['company'] = self.error_class([error_message])
            
        # case when there's no chassis brand selected and the other field has no data
        if  data['fk_chassis_or_truck_manufacturer']:
            if data['fk_chassis_or_truck_manufacturer'].name== "Otra marca" and not data['chassis_or_truck_manufacturer_other']:
                error_message ='Debe especificar otra marca de chasis'
                self._errors['chassis_or_truck_manufacturer_other'] = self.error_class([error_message])
                self.custom_errors.append(error_message)
                
         # case when there's other carrosado brand selected and the other field has no data
        if  data['fk_carrosado_manufacturer']:
            if data['fk_carrosado_manufacturer'].name== "Otra marca"  and not data['carrosado_manufacturer_other']:
                error_message ='Debe especificar otra marca del carrosado'
                self._errors['carrosado_manufacturer_other'] = self.error_class([error_message])  
                self.custom_errors.append(error_message)
                
        #case when there's other bomb brand/model selected and the other fields have no data
        if  data['fk_fire_engine_camiva_model']:
            if data['fk_fire_engine_camiva_model'].name== "Otra marca/modelo"  and not data['fire_engine_other_manufacturer']:
                error_message ='Debe especificar otra marca de la bomba'
                self._errors['fire_engine_other_manufacturer'] = self.error_class([error_message])
                self.custom_errors.append(error_message)

        # If any validation fails, raise error
        if self.custom_errors:
            raise forms.ValidationError(self.custom_errors)

        return self.cleaned_data

    service_incorporation_date = forms.DateField(label='Fecha de incorporación', widget=SelectDateWidget(years=xrange(2011, 1899, -1)), required=False)
    last_oil_change_date = forms.DateField(label='Fecha último cambio de aceite', widget=SelectDateWidget(years=xrange(2011, 1899, -1)), required=False)
    legal_registered_date = forms.DateField(label='Fecha de inscripción', widget=SelectDateWidget(years=xrange(2011, 1899, -1)), required=False)


    # Display company/central selector
    def render_company_question_to_list(self):
        fields = self._field_range('company', 'cuerpo_vehicle_own')

        return render_fields_as_list(fields)

    # Display vehicle info questions as a list
    def render_vehicle_info_questions_to_list(self):
        fields = self._field_range('fk_vehicle_type', 'fk_procedence')

        return render_fields_as_list(fields)
        
    # Display vehicle staff-only questions as list
    def render_vehicle_staff_only_questions_to_list(self):
        fields = self._field_range('folio', 'approval_number')
        
        return render_fields_as_list(fields)

    # Display legal registry questions as list
    def render_legal_registry_questions_to_list(self):
        fields = self._field_range('registered', 'licence_plate')
        
        return render_fields_as_list(fields)

    # Display legal staff-only questions as a list
    def render_legal_staff_only_questions_to_list(self):
        fields = [self['legal_registered_name'], self['legal_registered_date'], self['legal_repertorio_escritura'], self['legal_notary']]
        
        return render_fields_as_list(fields)

    # Display legal status questions as a list
    def render_legal_status_questions_to_list(self):
        fields = [self['vehicle_registration'], self['vehicle_checkup']]

        return render_fields_as_list(fields)

     # Display kilometraje horometraje as a list
    def render_kilometraje_horometraje_to_list(self):
        fields = self._field_range('kilometraje', 'horometraje')

        return render_fields_as_list(fields, css_class_name='list_quantities')

    # Display caracteristics as a list
    def render_caracteristics_to_list(self):
        fields = self._field_range('fk_fire_engine_camiva_model', 'fire_engine_other_model')

        return render_fields_as_list(fields)

	# Display maintenance as a list
    def render_maintenance_to_list(self):
        fields = self._field_range('last_oil_change_date', 'oil_change_kilometraje')

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
        
    # Display staff-only control fields    
    def render_staff_only_form_to_list(self):
        fields = [self['is_complete'], self['is_correct']]
        
        return render_fields_as_list(fields)

    class Meta:
        model = CuerpoMayorMaterialData
        exclude = ('cuerpo',)
