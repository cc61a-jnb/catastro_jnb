# coding: utf-8
from django import forms
from django.forms import ModelForm
from censo.models import *
from django.template import Context, loader
from censo.utils import render_fields_as_table, render_fields_as_list, split_list, combine_fields_errors
from . import BaseForm

class CuerpoMayorMaterialForm(BaseForm):

    class Meta:
        model = CuerpoANBData
        fields = ()
