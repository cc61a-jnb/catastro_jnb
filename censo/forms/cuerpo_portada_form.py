# coding: utf-8

from django import forms
from django.forms import ModelForm
from censo.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import date
from . import BaseForm
from censo.utils import render_fields_as_table, render_fields_as_list, split_list, combine_fields_errors

class CuerpoPortadaForm(BaseForm):

    def base_position_fields(self):
        fields = self._field_range('superintendent_name', 'intendent_name')
        return fields

    class Meta:
       model = PortadaCuerpoData
       fields = ('superintendent_name', 'vice_superintendent_name', 'commander_name', 'second_commander_name', 'third_commander_name', 'forth_commander_name', 'secretary_name', 'treasury_name', 'intendent_name', 'observations')
