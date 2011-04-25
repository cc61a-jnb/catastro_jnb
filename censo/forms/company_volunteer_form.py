# encoding: utf-8

from django import forms
from django.forms import ModelForm

from censo.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import date

from uni_form.helpers import FormHelper, Submit, Reset
from uni_form.helpers import Layout, Fieldset, Row, HTML

class CompanyVolunteerPartialForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CompanyVolunteerPartialForm, self).__init__(*args, **kwargs)
        self.fields['fk_internet_provider'].empty_label = 'No posee'

    # Attach a formHelper to your forms class.
    helper = FormHelper()
    # create the layout object
    layout = Layout(
                    # first fieldset shows the company
                    Fieldset('', 'computers_quantity'),
                    )

    helper.add_layout(layout)

    submit = Submit('Enviar', 'Enviar')
    helper.add_input(submit)

    class Meta:
        model = VolunteerData
        exclude = ('company',)
        
        
