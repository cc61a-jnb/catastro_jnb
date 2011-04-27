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

    class Meta:
        model = InfrastructureCompanyData
        exclude = ('company',)
