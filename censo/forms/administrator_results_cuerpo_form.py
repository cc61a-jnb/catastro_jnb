# encoding: utf-8
from django import forms
from censo.models import *

class AdministratorResultsCuerpoForm(forms.Form):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(AdministratorResultsCuerpoForm, self).__init__(*args, **kwargs)
        # here we can assign our custom css classes to form fields
        self.fields['region'].widget.attrs['class'] = 'menu_choice_field'