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
    
    def clean(self):
        data = self.cleaned_data
        
        self.custom_errors = []
        # If property type is rented or commodatum, specify end year
        if data['fk_property_title_type']:
            if data['fk_property_title_type'].name != 'Propio':
                if not data['property_rental_commodatum_end_year']:
                    error_message = 'Debe ingresar un año de término de comodato/arriendo'
                    self._errors['property_rental_commodatum_end_year'] = self.error_class([error_message])
                    self.custom_errors.append(error_message)
        
        # If any validation fails, raise error
        if self.custom_errors:
            raise forms.ValidationError(self.custom_errors)
        return self.cleaned_data
    
    # Display built area questions as a table    
    def render_built_area_to_table(self):
        fields = self._field_range('built_area_surface_m2', 'built_area_total_m2')
        table_fields = [fields]
        
        column_labels = [field.label for field in fields]
        row_labels = ['Metros']
        
        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')
    
    # Display land questions as a list
    def render_land_questions_to_list(self):
        fields = self._field_range('main_street_name', 'fk_property_title_type')
        
        return render_fields_as_list(fields)
        
    # Display rental/commodatum year end
    def render_rental_commodatum_end_year_to_list(self):
        fields = [self['property_rental_commodatum_end_year']]
        
        return render_fields_as_list(fields, 'list_quantities')
    
    # The list of all the picture fields in this form    
    def picture_fields(self):
        fields = self._field_range('picture_general_view', 'picture_internal_distribution_view')
        return [(field, getattr(self.instance, field.name)) for field in fields]
        
    def clean(self):
        data = self.cleaned_data
    
        # Pictures must be valid 
        self.custom_errors = []
        
        self.validate_field_range('built_area_surface_m2', 'built_area_total_m2', 'Por favor corrija los errores en Terreno')
        
        self.validate_field_range('building_initial_construction_year', 'building_extension_construction_legal', u'Por favor corrija los errores en Construcción') 
        
        self.validate_field_range('night_guard_office_men_beds', 'night_guard_office_men_bathroom_urinary', u'Por favor corrija los errores en Guardia Nocturna - Hombres')
        
        self.validate_field_range('night_guard_office_women_beds', 'night_guard_office_women_bathroom_wc', u'Por favor corrija los errores en Guardia Nocturna - Mujeres')
        
        self.validate_field_range('picture_general_view', 'picture_internal_distribution_view', u'Por favor ingrese fotografías válidas')
        
        # If any validation fails, raise error
        if self.custom_errors:
            raise forms.ValidationError(self.custom_errors)
            
        if 'fk_property_title_type' in self.cleaned_data:
            if 'property_rental_commodatum_end_year' in self.cleaned_data:
                if not self.cleaned_data['property_rental_commodatum_end_year'] and self.cleaned_data['fk_property_title_type'].requires_end_year:
                    self._errors['property_rental_commodatum_end_year'] = self.error_class(['Por favor defina el año de término del arriendo o comodato'])
                elif self.cleaned_data['property_rental_commodatum_end_year'] and not self.cleaned_data['fk_property_title_type'].requires_end_year:
                    self._errors['property_rental_commodatum_end_year'] = self.error_class(['Sólo defina si la propiedad es un arriendo o comodato'])
        
        return self.cleaned_data
    
    # Display rol sii
    def render_rol_sii_to_list(self):
        fields = [self['rol_sii']]
        
        return render_fields_as_list(fields)
        
    # Display inscription data questions as a list    
    def render_inscription_data_questions_to_list(self):
        fields = self._field_range('inscription_fojas', 'inscription_owner_name')
        
        return render_fields_as_list(fields)
    
    # Display building material type as a list  
    def render_building_material_type_to_list(self):
        fields = [self['building_material_type']]
        
        return render_fields_as_list(fields, 'multiple_choice_field')
        
    # Display building construction questions as a table
    def render_building_construction_to_table(self):
        fields = self._field_range('building_initial_construction_year', 'building_extension_construction_legal')
        table_fields = split_list(fields, 2)
        col_labels = ['Año construcción', 'Regularizado']
        row_labels = ['Inicial', 'Ampliación (si hay)']
        
        return render_fields_as_table(table_fields, col_labels, row_labels, 'table_quantities')
    
    # Display distribution rooms questions as a list    
    def render_distribution_rooms_to_list(self):
        fields = self._field_range('terrain_machine_room_m2', 'terrain_session_room_m2')
        
        return render_fields_as_list(fields, 'list_quantities')
    
    # Display distribution offices questions as a list    
    def render_distribution_offices_to_list(self):
        fields = self._field_range('director_office', 'common_offices')
        
        return render_fields_as_list(fields)    
    
    # Display night guard office men questions as a table
    def render_night_guard_office_men_to_table(self):
        fields = self._field_range('night_guard_office_men_beds', 'night_guard_office_men_bathroom_urinary')
        table_fields = [fields]
        col_names = ['Camas', 'Baños', 'Duchas', 'WC', 'Urinarios']
        row_names = ['N°']
        
        return render_fields_as_table(table_fields, col_names, row_names, 'table_quantities')
    
    # Display night guard office women questions as a table
    def render_night_guard_office_women_to_table(self):
        fields = self._field_range('night_guard_office_women_beds', 'night_guard_office_women_bathroom_wc')
        table_fields = [fields]
        col_names = ['Camas', 'Baños', 'Duchas', 'WC']
        row_names = ['N°']
        
        return render_fields_as_table(table_fields, col_names, row_names, 'table_quantities')
    
    # Display night_guard_office kitchen as a list    
    def render_night_guard_office_kitchen_to_list(self):
        # fields = self._field_range('night_guard_office_men_beds', 'night_guard_office_kitchen')
        fields = [self['night_guard_office_kitchen']]
        
        return render_fields_as_list(fields)
    
    #Display rooms as a list
    def render_rooms_to_list(self):
        fields = self._field_range('cafeteria', 'living_room')
        return render_fields_as_list(fields)

    #Display barrack house rooms as a list
    def render_barrack_house_to_list(self):
        fields = self._field_range('barrack_house_bedroom', 'barrack_house_bathroom')
        return render_fields_as_list(fields)

    #Display bathrooms as a table
    def render_bathrooms_to_table(self):
        fields = self._field_range('common_bathrooms', 'women_bathroom')
        table_fields = [fields]
        col_names = ['Comunes', 'Hombres', 'Mujeres']
        row_names = ['Baños']
        
        return render_fields_as_table(table_fields, col_names, row_names, 'table_quantities')

    #Display other areas as a list
    def render_other_areas_to_list(self):
        fields = self._field_range('storage', 'others')
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
        model = InfrastructureCompanyData
        exclude = ('company',)
