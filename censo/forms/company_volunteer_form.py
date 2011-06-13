# encoding: utf-8
from django import forms
from django.forms import ModelForm
from censo.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import date
from django.template import Context, loader
from censo.utils import render_fields_as_table, render_fields_as_list, split_list, combine_fields_errors
from . import BaseForm

class CompanyVolunteerForm(BaseForm):
    specialities = forms.ModelMultipleChoiceField(queryset=Speciality.objects.all(), label='Especialidades Compañía', widget=forms.CheckboxSelectMultiple(), required=False)

    def __init__(self, *args, **kwargs):
        super(CompanyVolunteerForm, self).__init__(*args, **kwargs)
        # Define empty label for ISP question
        self.fields['fk_internet_provider'].empty_label = 'No posee'
    
    # Define custom form validation    
    def clean(self):
        data = self.cleaned_data
        
        # List of all the global errors found in the form so we can display them all at once at the end
        self.custom_errors = []
        
        # Zero validation: Tech infraestructure
        local_errors = self.validate_field_range('computers_quantity', 'printers_quantity', 'Por favor corrija los errores en Soporte Tecnológico')
        
        # First validation: We need the total men and women
        local_errors = self.validate_field_range('volunteer_total_men_quantity', 'volunteer_total_women_quantity', 'Por favor corrija los errores en el total de hombres y mujeres de la compañía')
        
        self.validate_field_range('volunteer_antiquity_required_to_honorary', 'volunteer_antiquity_required_to_honorary', 'Por favor corrija la antiguëdad requerida para ser honorario')
        
        if local_errors:
            # The required numbers were not supplied, so we invalidate the possible error messages of the 
            # numeric fields because the logic that controls the number of messages per table will not be
            # executed (because we can't check the sums)
            fields = self._field_range('volunteer_active_men_quantity', 'volunteer_with_work_quantity')
            self.reset_field_errors(fields)            
        else:
            # We run the rest of the numeric validations ONLY if the user specified the total
            # number of men and women, otherwise we wouldn't be able to check the sums
            total_men = data['volunteer_total_men_quantity']
            total_women = data['volunteer_total_women_quantity']
        
            # Active + Honorary must equal total
            local_errors = self.validate_field_range('volunteer_active_men_quantity', 'volunteer_honorary_women_quantity', 'Por favor corrija los errores en el número de voluntarios activos y honorarios')


            if not local_errors:
                error_messages = []
                # Active + Honorary must equal total (men)
                if data['volunteer_active_men_quantity'] + data['volunteer_honorary_men_quantity'] != total_men:
                    error_message = 'Suma de voluntarios activos y honorarios hombres no calza con el total'
                    #self._errors['volunteer_active_men_quantity'] = self.error_class([error_message])
                    error_messages.append(error_message)
                    self.custom_errors.append(error_message)
            
                # Active + Honorary must equal total (women)
                if data['volunteer_active_women_quantity'] + data['volunteer_honorary_women_quantity'] != total_women:
                    error_message = 'Suma de voluntarios activos y honorarios mujeres no calza con el total'
                    #self._errors['volunteer_active_men_quantity'] = self.error_class([error_message])
                    error_messages.append(error_message)
                    self.custom_errors.append(error_message)
            
                if error_messages:
                    self._errors['volunteer_active_men_quantity'] = self.error_class(error_messages)
            # Sum of age-range volunteers must equal total        
            local_errors = self.validate_field_range('volunteer_age_between_18_25_men_quantity', 'volunteer_age_60_or_more_women_quantity', 'Por favor corrija los errores en el número de voluntarios por rango de edad')

            if not local_errors:
                error_messages = []
                
                age_fields = self._field_range('volunteer_age_between_18_25_men_quantity', 'volunteer_age_60_or_more_women_quantity')
                men_age_fields = age_fields[::2]
                women_age_fields = age_fields[1::2]
                
                # Sum of age-range volunteers must equal total (men)
                sum_men_age_fields = 0
                for field in men_age_fields:
                    sum_men_age_fields += self.cleaned_data[field.name]
                    
                if sum_men_age_fields != total_men:
                    error_message = 'Suma de voluntarios hombres por edad no calza con el total'
                    #self._errors['volunteer_age_between_18_25_men_quantity'] = self.error_class([error_message])
                    error_messages.append(error_message)
                    self.custom_errors.append(error_message)
                
                # Sum of age-range volunteers must equal total (women)    
                sum_women_age_fields = 0
                for field in women_age_fields:
                    sum_women_age_fields += self.cleaned_data[field.name]
                    
                if sum_women_age_fields != total_women:
                    error_message = 'Suma de voluntarios mujeres por edad no calza con el total'
                    #self._errors['volunteer_age_between_18_25_men_quantity'] = self.error_class([error_message])
                    error_messages.append(error_message)
                    self.custom_errors.append(error_message)
                    
                if error_messages:
                    self._errors['volunteer_age_between_18_25_men_quantity'] = self.error_class(error_messages)
            
            # Sum of volunteer education must equal total    
            local_errors = self.validate_field_range('volunteer_education_basica_complete_quantity', 'volunteer_with_work_quantity', 'Por favor corrija los errores en el número de voluntarios por educación / oficio')
            
            if not local_errors:
                education_fields = self._field_range('volunteer_education_basica_complete_quantity', 'volunteer_with_work_quantity')
                sum_education_fields = 0
                for field in education_fields:
                    sum_education_fields += self.cleaned_data[field.name]
                    
                if sum_education_fields != total_men + total_women:
                    error_message = 'Suma de voluntarios por educación no calza con el total'
                    self._errors['volunteer_education_basica_complete_quantity'] = self.error_class([error_message])
                    self.custom_errors.append(error_message)

        # Company must have at least 1 specialty    
        if not data['specialities'] and not data['specialities_other']:
            self._errors['specialities'] = self.error_class(['Debe especificar por lo menos una especialidad'])
        
        # Other validations....
        self.validate_field_range('volunteer_lt_than_3_years_cuerpo_course_quantity', 'volunteer_gt_than_3_years_academia_course_quantity', 'Por favor corrija los errores en Formación Bomberil - ANB')
        
        self.validate_field_range('volunteer_class_f_bomberos_driver_quantity', 'volunteer_class_f_cuarteleros_driver_quantity', 'Por favor corrija los errores en Conductores clase F')
        
        self.validate_field_range('volunteer_brigada_juvenil_antiquity', 'volunteer_brigada_juvenil_members_quantity', 'Por favor corrija los errores en Brigada Juvenil de Compañía')
            
        
        # If any validation fails, raise error
        if self.custom_errors:
            raise forms.ValidationError(self.custom_errors)
            
        return self.cleaned_data
    
    # Display hardware questions as a table    
    def render_hardware_to_table(self):
        fields = self._field_range('computers_quantity', 'printers_quantity')
        table_fields = [fields]
        
        column_labels = [field.label for field in fields]
        row_labels = ['Cantidad']
        
        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')
    
    # Display total volunteers questions as a table    
    def render_total_volunteers_to_table(self):
        fields = self._field_range('volunteer_total_men_quantity', 'volunteer_total_women_quantity')
        table_fields = [fields]
        
        column_labels = [field.label for field in fields]
        row_labels = ['Cantidad']
        
        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')        
    
    # Display active + honorary volunteers questions as a table    
    def render_detailed_volunteers_to_table(self):
        fields = self._field_range('volunteer_active_men_quantity', 'volunteer_honorary_women_quantity')
        table_fields = split_list(fields, 2)
        
        first_row_fields = table_fields[0]
        
        column_labels = [field.label for field in first_row_fields]
        row_labels = ['Activos', 'Honorarios']
        
        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')
    
    # Display ANB volunteer formation questions as a table    
    def render_formation_to_table(self):
        fields = self._field_range('volunteer_lt_than_3_years_cuerpo_course_quantity', 'volunteer_gt_than_3_years_academia_course_quantity')
        table_fields = split_list(fields, 2)
        
        first_row_fields = table_fields[0]
        
        column_labels = [field.label for field in first_row_fields]
        row_labels = ['Cursos del Cuerpo', 'Cursos de la academia']
        
        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')
    
    # Display volunteer age range questions as a table    
    def render_volunteers_age_range_to_table(self):
        fields = self._field_range('volunteer_age_between_18_25_men_quantity', 'volunteer_age_60_or_more_women_quantity')
        table_fields = split_list(fields, 9)
        
        row_labels = [row_field[0].label for row_field in table_fields]
        col_labels = ['Hombres', 'Mujeres']
        
        return render_fields_as_table(table_fields, col_labels, row_labels, 'table_quantities')    
    
    # Display ISP question    
    def render_isp_to_list(self):
        fields = [self['fk_internet_provider']]
        
        return render_fields_as_list(fields)
    
    # Display honorary antiquity question  
    def render_antiquity_to_list(self):
        fields = [self['volunteer_antiquity_required_to_honorary']]
        
        return render_fields_as_list(fields, 'list_quantities')
    
    # Display website/social pages questions as a list    
    def render_social_technologies_to_list(self):
        fields = self._field_range('website', 'social_other_account_name')
        
        return render_fields_as_list(fields)
    
    # Display drivers questions as a list    
    def render_drivers_to_list(self):
        fields = self._field_range('volunteer_class_f_bomberos_driver_quantity', 'volunteer_class_f_cuarteleros_driver_quantity')
        
        return render_fields_as_list(fields, 'list_quantities')
    
    # Display life sheet manager questions as a list    
    def render_life_sheet_to_list(self):
        fields = self._field_range('volunteer_hoja_de_vida_cargo', 'volunteer_hoja_de_vida_phone')
        
        return render_fields_as_list(fields)
    
    # Display brigade questions as a list    
    def render_brigade_number_to_list(self):
        fields = self._field_range('volunteer_brigada_juvenil_antiquity', 'volunteer_brigada_juvenil_members_quantity')
        
        return render_fields_as_list(fields, 'list_quantities')
    
    def render_brigade_data_to_list(self):
        fields = self._field_range('volunteer_brigada_juvenil_name', 'volunteer_brigada_juvenil_responsible_email')
        
        return render_fields_as_list(fields)
    
    # Display observations area    
    def render_observations_to_list(self):
        fields = [self['observations']]
        
        return render_fields_as_list(fields)
        
    # Display staff-only fields
    def render_staff_only_form_to_list(self):
        fields = [self['is_complete'], self['is_correct']]
        
        return render_fields_as_list(fields)
    
    # Display volunteer education level questions as a list    
    def render_volunteer_education_to_list(self):
        fields = self._field_range('volunteer_education_basica_complete_quantity', 'volunteer_with_work_quantity')
        
        return render_fields_as_list(fields, 'list_quantities')
        
    def render_internet_technology_use_section(self):
        return CompanyVolunteerForm.render_fields_as_table()
    
    def render_technology_support_form(self):
        fields = self.fields.items()
        table_data = ['Cantidad', [self[fields[i][0]] for i in xrange(0, 4)]]
        template = loader.get_template('tags/single_row_table_form.html')
        c = Context({
            'table_data': table_data,
        })
        return template.render(c)

    class Meta:
        model = VolunteerData
        exclude = ('company',)
