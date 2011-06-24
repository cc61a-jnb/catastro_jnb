# encoding: utf-8
from django import forms
from django.forms import ModelForm
from censo.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import date
from django.template import Context, loader
from censo.utils import render_fields_as_table, render_fields_as_list, split_list
from django.forms.extras.widgets import SelectDateWidget
from . import BaseForm

class CuerpoAlarmCentralForm(BaseForm):
    decree_date = forms.DateField(widget=SelectDateWidget(years=list(xrange(1920, date.today().year+1))),required=False, label="Fecha (otorgada)")

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
        fields = self._field_range('telephone_number132_available', 'cell_equipment_quantity')

        return render_fields_as_list(fields)

    # Display frequencies as a list
    def render_frequencies_to_list(self):
        fields = self._field_range('frequency_one', 'national_emergency_frequency')

        return render_fields_as_list(fields)

    # Display fixed antennas questions as a table
    def render_fixed_antennas_to_table(self):
        fields = self._field_range('fixed_antenna_quantity1', 'fixed_antenna_height2')
        table_fields = split_list(fields, 2)

        first_row_fields = table_fields[0]

        column_labels = [field.label for field in first_row_fields]
        row_labels = ['Antena 1', 'Antena 2']

        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')

    # Display tone_generator as a list
    def render_tone_generator_to_list(self):
        fields = self._field_range('tone_generator_mark', 'tone_generator_capacity')

        return render_fields_as_list(fields)

    # Display portable radio questions as a table
    def render_portable_radio_to_table(self):
        fields = self._field_range('portable_quantity1', 'portable_power3')
        table_fields = split_list(fields, 3)

        first_row_fields = table_fields[0]

        column_labels = [field.label for field in first_row_fields]
        row_labels = ['Portátil 1', 'Portátil 2', 'Portátil 3']

        return render_fields_as_table(table_fields, column_labels, row_labels, 'table_quantities')

    #Display hardware technological support

    def render_hardware_technological_support_to_list(self):
        fields = [self['pc_quantity'], self['fk_os']]

        return render_fields_as_list(fields, 'list_quantities')

    #Display software technological support as a list
    def render_software_technological_support_to_list(self):
        fields = self._field_range('digital_maps', 'origin_software_other')

        return render_fields_as_list(fields)

    #Display Procedimientos (Ex administration - documentation) technological support as a list
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

  # Define custom form validation
    def clean(self):
        data = self.cleaned_data

        # List of all the global errors found in the form so we can display them all at once at the end
        self.custom_errors = []

        normalizado = data.get('normalized_frequency', None)
        #caso en que es Normalizada es Si
        if normalizado == 2:
            # verificamos que estén decreto y fecha otorgada
            decree = data.get('decree', None)

            if not decree:
                self._errors['decree'] = self.error_class([u'Debe especificar el N° de decreto'])
           
            date  = data.get('decree_date', None)
            if not date:
                self._errors['decree_date'] = self.error_class([u'Debe especificar la fecha de entrega de decreto'])

        #caso en que es Normalizada es No
        if normalizado == 1:
            # dejamos pasar el decreto y fecha en blanco.
            decree = data.get('decree', None)

        return self.cleaned_data

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
        model = CuerpoAlarmCentralData
        exclude = ('cuerpo',)
