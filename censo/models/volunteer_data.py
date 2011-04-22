# coding: utf-8

from django.db import models

class VolunteerData(models.Model):
    
    company = models.OneToOneField('censo.Company', blank=True)
    # primera parte: equipamiento mínimo

    def __unicode__(self):
        return self.company.name

    class Meta:
        ordering = ['company']
        app_label = 'censo'

    # primera parte: equipamiento mínimo

    computers_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° computadores') 
    notebooks_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° notebooks')
    projectors_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° proyectores')
    printers_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° impresoras') 
    fk_internet_provider = models.ForeignKey('InternetProvider', verbose_name='Proveedor de Internet', blank=True, null=True)
    
    # segunda parte: redes sociales

    website = models.URLField(null=True, blank=True, verbose_name='sitio web')
    social_facebook_account_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='cuenta facebook')
    social_twitter_account_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='cuenta twitter')
    social_other_account_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='otro')

    # tercera parte: cantidad voluntarios

    volunteer_total_women_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios totales mujeres')
    volunteer_total_men_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios totales hombres')
    volunteer_honorary_women_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios honorarios mujeres')
    volunteer_honorary_men_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios honorarios hombres')
    volunteer_antiquity_required_to_honorary = models.IntegerField(null=True, blank=True, verbose_name='antigüedad requerida para ser honorario')
    volunteer_active_women_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios activos mujeres')
    volunteer_active_men_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios activos hombres')
    volunteer_age_between_18_25_men_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios hombres entre 18 y 25 años')
    volunteer_age_between_18_25_women_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios mujeres entre 18 y 25 años')
    volunteer_age_between_26_30_men_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios hombres entre 26 y 30 años')
    volunteer_age_between_26_30_women_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios mujeres entre 26 y 30 años')
    volunteer_age_between_31_35_men_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios hombres entre 31 y 35 años')
    volunteer_age_between_31_35_women_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios mujeres entre 31 y 35 años')
    volunteer_age_between_36_40_men_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios hombres entre 36 y 40 años')
    volunteer_age_between_36_40_women_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios mujeres entre 36 y 40 años')
    volunteer_age_between_41_45_men_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios hombres entre 41 y 45 años')
    volunteer_age_between_41_45_women_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios mujeres entre 41 y 45 años')
    volunteer_age_between_46_50_men_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios hombres entre 46 y 50 años')
    volunteer_age_between_46_50_women_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios mujeres entre 46 y 50 años')
    volunteer_age_between_51_55_men_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios hombres entre 51 y 55 años')
    volunteer_age_between_51_55_women_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios mujeres entre 51 y 55 años')
    volunteer_age_between_56_60_men_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios hombres entre 56 y 60 años')
    volunteer_age_between_56_60_women_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios mujeres entre 56 y 60 años')
    volunteer_age_60_or_more_men_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios hombres con mas de 60 años')
    volunteer_age_60_or_more_women_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios mujeres con mas de 60 años')

    # cuarta parte: educación y trabajo

    volunteer_education_basica_complete_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios con enseñanza básica completa')
    volunteer_education_media_complete_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios con enseñanza media completa')
    volunteer_education_universitaria_complete_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios universitarios (4 o 5 años)')
    volunteer_education_tecnica_complete_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios técnicos (3 o 4 años)')
    volunteer_with_work_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios con oficios')

    # quinta parte: formación bomberil

    volunteer_lt_than_3_years_cuerpo_course_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios con menos de 3 años de experiencia')
    volunteer_gt_than_3_years_cuerpo_course_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios con más de 3 años de experiencia')
    volunteer_lt_than_3_years_academia_course_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios con menos de 3 años de experiencia')
    volunteer_gt_than_3_years_academia_course_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios con más de 3 años de experiencia')

    # sexta parte: conductores clase F

    volunteer_class_f_bomberos_driver_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° bomberos con licencia clase F')
    volunteer_class_f_cuarteleros_driver_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° cuarteleros/conductores con licencia clase F')

    # 7ma parte: Hoja de Vida

    volunteer_hoja_de_vida_cargo = models.CharField(max_length=255, null=True, blank=True, verbose_name='cargo')
    volunteer_hoja_de_vida_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='nombre')
    volunteer_hoja_de_vida_email = models.CharField(max_length=255, null=True, blank=True, verbose_name='correo electrónico')
    volunteer_hoja_de_vida_phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='teléfono')

    # 8va parte: brigada juvenil

    volunteer_brigada_juvenil_antiquity = models.IntegerField(null=True, blank=True, verbose_name='Antigüedad')
    volunteer_brigada_juvenil_members_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° brigadieres')
    volunteer_brigada_juvenil_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='nombre brigada')
    volunteer_brigada_juvenil_responsible_instructor = models.CharField(max_length=255, null=True, blank=True, verbose_name='instructor responsable')
    volunteer_brigada_juvenil_responsible_email = models.CharField(max_length=255, null=True, blank=True, verbose_name='correo electrónico responsable')

    # observaciones
    
    observations = models.TextField(max_length=255, null=True, blank=True, verbose_name='observaciones')
