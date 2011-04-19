# encoding: utf-8

from django import forms
from django.forms import ModelForm

from censo.models import *
from django.forms.extras.widgets import SelectDateWidget
from datetime import date

class CompanyVolunteerPartialForm(ModelForm):

    class Meta:
        model = VolunteerData
        exclude = ('company',)

class CompanyVolunteerForm(forms.Form):
    
    # primera parte: equipamiento mínimo

    computers_quantity = forms.IntegerField(required=False, label='n° computadores') 
    notebooks_quantity = forms.IntegerField(required=False, label='n° notebooks')
    projectors_quantity = forms.IntegerField(required=False, label='n° proyectores')
    printers_quantity = forms.IntegerField(required=False, label='n° impresoras') 
    has_internet = forms.BooleanField(required=False, label='tiene internet') 
    internet_provider = forms.CharField(max_length=50, required=False, label='proveedor internet')
    
    # segunda parte: redes sociales

    website = forms.URLField(required=False, label='sitio web')
    social_facebook_account_name = forms.CharField(required=False, label='cuenta facebook')
    social_twitter_account_name = forms.CharField(required=False, label='cuenta twitter')
    social_other_account_name = forms.CharField(required=False, label='otro')

    # tercera parte: cantidad voluntarios

    volunteer_total_women_quantity = forms.IntegerField(required=False, label='n° voluntarios totales mujeres')
    volunteer_total_men_quantity = forms.IntegerField(required=False, label='n° voluntarios totales hombres')
    volunteer_paid_women_quantity = forms.IntegerField(required=False, label='n° voluntarios a honorarios mujeres')
    volunteer_paid_men_quantity = forms.IntegerField(required=False, label='n° voluntarios a honorarios hombres')
    volunteer_antiquity_required_to_be_paid = forms.IntegerField(required=False, label='antigüedad requerida para honorarios')
    volunteer_active_women_quantity = forms.IntegerField(required=False, label='n° voluntarios activos mujeres')
    volunteer_active_men_quantity = forms.IntegerField(required=False, label='n° voluntarios totales hombres')
    volunteer_age_between_18_25_quantity = forms.IntegerField(required=False, label='n° voluntarios entre 18 y 25 años')
    volunteer_age_between_26_30_quantity = forms.IntegerField(required=False, label='n° voluntarios entre 26 y 30 años')
    volunteer_age_between_31_35_quantity = forms.IntegerField(required=False, label='n° voluntarios entre 31 y 35 años')
    volunteer_age_between_36_40_quantity = forms.IntegerField(required=False, label='n° voluntarios entre 36 y 40 años')
    volunteer_age_between_41_45_quantity = forms.IntegerField(required=False, label='n° voluntarios entre 41 y 45 años')
    volunteer_age_between_46_50_quantity = forms.IntegerField(required=False, label='n° voluntarios entre 46 y 50 años')
    volunteer_age_between_51_55_quantity = forms.IntegerField(required=False, label='n° voluntarios entre 51 y 55 años')
    volunteer_age_between_56_60_quantity = forms.IntegerField(required=False, label='n° voluntarios entre 56 y 60 años')
    volunteer_age_60_or_more_quantity = forms.IntegerField(required=False, label='n° voluntarios con mas de 60 años')

    # cuarta parte: educación y trabajo

    volunteer_education_basica_complete_quantity = forms.IntegerField(required=False, label='n° voluntarios con enseñanza básica completa')
    volunteer_education_media_complete_quantity = forms.IntegerField(required=False, label='n° voluntarios con enseñanza media completa')
    volunteer_education_universitaria_complete_quantity = forms.IntegerField(required=False, label='n° voluntarios universitarios (4 o 5 años)')
    volunteer_education_tecnica_complete_quantity = forms.IntegerField(required=False, label='n° voluntarios técnicos (3 o 4 años)')
    volunteer_with_work_quantity = forms.IntegerField(required=False, label='n° voluntarios con oficios')

    # quinta parte: formación bomberil

    volunteer_lt_than_3_years_cuerpo_course_quantity = forms.IntegerField(required=False, label='n° voluntarios con menos de 3 años de experiencia en cursos del cuerpo')
    volunteer_gt_than_3_years_cuerpo_course_quantity = forms.IntegerField(required=False, label='n° voluntarios con más de 3 años de experiencia en cursos del cuerpo')
    volunteer_lt_than_3_years_academia_course_quantity = forms.IntegerField(required=False, label='n° voluntarios con menos de 3 años de experiencia en cursos de la academia')
    volunteer_gt_than_3_years_academia_course_quantity = forms.IntegerField(required=False, label='n° voluntarios con más de 3 años de experiencia cursos de la academia')

    # sexta parte: conductores clase F

    volunteer_class_f_bomberos_driver_quantity = forms.IntegerField(required=False, label='n° bomberos con licencia clase F')
    volunteer_class_f_cuarteleros_driver_quantity = forms.IntegerField(required=False, label='n° cuarteleros/conductores con licencia clase F')

    # 7ma parte: Hoja de Vida

    volunteer_hoja_de_vida_cargo = forms.CharField(required=False, label='cargo')
    volunteer_hoja_de_vida_name = forms.CharField(required=False, label='nombre')
    volunteer_hoja_de_vida_email = forms.CharField(required=False, label='correo electrónico')
    volunteer_hoja_de_vida_phone = forms.CharField(required=False, label='teléfono')

    # 8va parte: brigada juvenil

    volunteer_brigada_juvenil_antiquity = forms.IntegerField(required=False, label='Antigüedad')
    volunteer_brigada_juvenil_members_quantity = forms.IntegerField(required=False, label='n° brigadieres')
    volunteer_brigada_juvenil_name = forms.CharField(required=False, label='nombre brigada')
    volunteer_brigada_juvenil_responsible_instructor = forms.CharField(required=False, label='instructor responsable')
    volunteer_brigada_juvenil_responsible_email = forms.CharField(required=False, label='correo electrónico responsable')

    # observaciones
    
    observations = forms.CharField(required=False, widget=forms.Textarea, label='observaciones')

