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

    def clean(self):
        self.custom_errors = []
    
        self.validate_field_range('jackets_quantity', 'fireman_shoes_volunteer_quantity', 'Por favor corrija los errores en Uniformes Normados')
        
        self.validate_field_range('scott_after_2004_quantity', 'mSA_quantity', 'Por favor corrija los errores en Equipamiento ERA')
        
        self.validate_field_range('hosepipe_38mm_quantity', 'hosepipe_forest_quantity', 'Por favor corrija los errores en Equipamiento Menor - Mangueras')
        
        self.validate_field_range('python_50adjustable_quantity', 'python_70tube_quantity', 'Por favor corrija los errores en Equipamiento Menor - Pitones')
        
        self.validate_field_range('tripok_quantity', 'motorpump_quantity', 'Por favor corrija los errores en Equipamiento Menor - Otro equipamiento')
        
        self.validate_field_range('aircompressor_fixed_quantity', 'aircompressor_bycar_quantity', 'Por favor corrija los errores en Compresores de aire')
        
        self.validate_field_range('cascade_cylinder_quantity', 'cascade_bycar_quantity', 'Por favor corrija los errores en Cascadas')
        
        self.validate_field_range('electricgenerator_fixed_in_car_quantity', 'fk_electricgenerator_fixed_in_barracks_potency', 'Por favor corrija los errores en Generadores Eléctricos')
        
        self.validate_field_range('airmattresses_quantity', 'hazmat_seal_kits_quantity', 'Por favor corrija los errores en Otros')
        
        # If any validation fails, raise error
        if self.custom_errors:
            raise forms.ValidationError(self.custom_errors)
        
        return self.cleaned_data

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
        
    # Display python minor equipment questions as a table
    def render_python_minor_equipment_to_table(self):
        fields = self._field_range('python_50adjustable_quantity', 'python_70tube_quantity')
        table_fields = [fields]

        column_labels = [field.label for field in fields]
        row_labels = ['Nº']

        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')

    # Display other minor equipment questions as a list
    def render_other_minor_equipment_to_list(self):
        fields = self._field_range('tripok_quantity', 'motorpump_quantity')

        return render_fields_as_list(fields, 'list_quantities')
      
	#Display radio equipment
    def render_portable_radio_equipment_to_table(self):
    
        fields = self._field_range('portable_radio_equipment_quantity', 'portable_radio_equipment_model')
        table_fields = [fields]
 
        column_labels = [field.label for field in fields]
        row_labels = ['']

        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities_3')
		
	#Display radio equipment
    def render_antennas_to_table(self):
    
        fields = self._field_range('antenna_equipment_quantity', 'antenna_equipment_power')
        table_fields = [fields]
 
        column_labels = [field.label for field in fields]
        row_labels = ['']

        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities_3')
		
    

    # Display air compressor questions as a list
    def render_air_compressor_to_list(self):
        fields = self._field_range('aircompressor_fixed_quantity', 'aircompressor_bycar_quantity')

        return render_fields_as_list(fields, 'list_quantities')

    # Display cascade questions as a list
    def render_cascade_to_list(self):
        fields = self._field_range('cascade_cylinder_quantity', 'cascade_bycar_quantity')

        return render_fields_as_list(fields, 'list_quantities')

    # Display electric generator questions as a table
    def render_electric_generator_questions_to_table(self):
        fields = self._field_range('electricgenerator_fixed_in_car_quantity', 'fk_electricgenerator_fixed_in_barracks_potency')
        table_fields = split_list(fields, 3)
        column_labels = ['N°', 'Potencia']
        row_labels = ['Fijos en Carros', 'Portátiles', 'Fijos en Cuartel']

        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')
 
    #Display base radio equipment as table
    def render_base_radio_equipment_to_table(self):
        fields = self._field_range('base_radio_equipment_quantity', 'base_radio_equipment_power')
        table_fields = [fields]

        column_labels = [field.label for field in fields]
        row_labels = ['']

        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities_2')
        
    # Display base radio equipment questions as a list
    def render_base_radio_equipment_quantity(self):
        fields = [self['base_radio_equipment_quantity']]
        
        return render_fields_as_list(fields, 'list_quantities')
        
    def render_base_radio_equipment_make_to_list(self):
        fields = self._field_range('base_radio_equipment_manufacturer', 'base_radio_equipment_model')

        return render_fields_as_list(fields)
    
    def render_base_radio_equipment_power(self):
        fields = [self['base_radio_equipment_power']]
        
        return render_fields_as_list(fields, 'list_quantities')

    # Display other equipment questions as a list
    def render_other_equipment_questions_to_list(self):
        fields = self._field_range('airmattresses_quantity', 'hazmat_seal_kits_quantity')

        return render_fields_as_list(fields, 'list_quantities')

    # Display portable radio equipment as a list
    def render_portable_radio_equipment_quantity(self):
        fields = [self['portable_radio_equipment_quantity']]
        
        return render_fields_as_list(fields, 'list_quantities')
        
    def render_portable_radio_equipment_make_to_list(self):
        fields = self._field_range('portable_radio_equipment_quantity', 'portable_radio_equipment_model')

        return render_fields_as_list(fields)

    # Display antenna equipment as a list
    def render_antenna_equipment_quantity(self):
        fields = [self['antenna_equipment_quantity']]
        
        return render_fields_as_list(fields, 'list_quantities')
        
    def render_antenna_equipment_make_to_list(self):
        fields = self._field_range('antenna_equipment_manufacturer', 'antenna_equipment_model')

        return render_fields_as_list(fields)
    
    def render_antenna_equipment_power(self):
        fields = [self['antenna_equipment_power']]
        
        return render_fields_as_list(fields, 'list_quantities')

    # Display observations area
    def render_observations_to_list(self):
        fields = [self['observations']]

        return render_fields_as_list(fields)
        
    # Display staff-only fields
    def render_staff_only_form_to_list(self):
        fields = [self['is_complete'], self['is_correct']]
        
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
        model = MinorMaterialCompanyData
        exclude = ('company',)
