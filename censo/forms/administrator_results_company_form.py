# encoding: utf-8
from django import forms
from censo.models import Region

class AdministratorResultsCompanyForm(forms.Form):
    region = forms.ChoiceField(choices=Region.get_old_id_name_tuples())

    def __init__(self, *args, **kwargs):
        super(AdministratorResultsCompanyForm, self).__init__(*args, **kwargs)
        # here we can assign our custom css classes to form fields
        self.fields['region'].widget.attrs['id'] = 'region'
        self.fields['region'].widget.attrs['class'] = 'menu_choice_field'