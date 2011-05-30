# coding: utf-8
from django import forms
from django.forms import ModelForm
from censo.models import *
from django.template import Context, loader
from django.forms.extras.widgets import SelectDateWidget
from censo.utils import render_fields_as_table, render_fields_as_list, split_list, combine_fields_errors
from . import BaseForm

class CuerpoMayorMaterialForm(BaseForm):

    #def clean(self):
    #    data = self.cleaned_data
    #    
    #    if data['denomination'] is None:
    #        error_message = 'Este campo es requerido'
    #        self._errors['denomination'] = self.error_class([error_message])
    #YEAR_CHOICE = [(year, year) for year in xrange(2012, 1950, -1)]
    #vehicle_year = forms.IntegerField(label='Año del Vehículo', choices=YEAR_CHOICE)
    service_incorporation_date = forms.DateField(label='Fecha de incorporación', widget=SelectDateWidget(years=range(1900, 2020)))
    last_oil_change_date = forms.DateField(label='Fecha último cambio de aceite', widget=SelectDateWidget(years=range(1900, 2020)))
        
    
    # Display company/central selector
    def render_company_question_to_list(self):
        fields = self._field_range('company', 'cuerpo_vehicle_own')
        
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
        
    # Display motor/gearbox repairs as a list
    def render_repairs_to_list(self):
        fields = self._field_range('motor_repairs', 'gearbox_repairs')
        
        return render_fields_as_list(fields)

    # Display electric generator questions as a table
    def render_electric_generator_questions_to_table(self):
        fields = self._field_range('electricgenerator_fixed_in_car_quantity', 'fk_electricgenerator_fixed_in_barracks_potency')
        table_fields = split_list(fields, 3)
        column_labels = ['N°', 'Potencia']
        row_labels = ['Fijos en Carros', 'Portátiles', 'Fijos en Cuartel']

        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')

    # The list of all the picture fields in this form    
    def picture_fields(self):
        fields = self._field_range('picture_front_view', 'picture_back_view')
        return [(field, getattr(self.instance, field.name)) for field in fields]

    # Display observations area
    def render_observations_to_list(self):
        fields = [self['observations']]

        return render_fields_as_list(fields)
 
    class Meta:
        model = CuerpoMayorMaterialData
        exclude = ('cuerpo',)
