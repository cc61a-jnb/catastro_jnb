# coding: utf-8

from django.db import models

class VolunteerData(models.Model):
    company = models.OneToOneField('censo.Company', blank=True)

    def __unicode__(self):
        return self.company.name

    class Meta:
        ordering = ['company']
        app_label = 'censo'
        
    # parte 0: especialidades
    
    specialities = models.ManyToManyField('Speciality', blank = True, null = True)
    specialities_other = models.CharField(max_length=255, null=True, blank=True, verbose_name='Otros')

    # primera parte: equipamiento mínimo

    computers_quantity = models.IntegerField(null=True, blank=True, verbose_name='Computadores') 
    notebooks_quantity = models.IntegerField(null=True, blank=True, verbose_name='Notebooks')
    projectors_quantity = models.IntegerField(null=True, blank=True, verbose_name='Proyectores')
    printers_quantity = models.IntegerField(null=True, blank=True, verbose_name='Impresoras') 
    fk_internet_provider = models.ForeignKey('InternetProvider', verbose_name='Proveedor de Internet', blank=True, null=True)
    
    # segunda parte: redes sociales

    website = models.URLField(null=True, blank=True, verbose_name='Sitio web')
    social_facebook_account_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Cuenta Facebook')
    social_twitter_account_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Cuenta Twitter')
    social_other_account_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='otro')

    # tercera parte: cantidad voluntarios

    volunteer_total_men_quantity = models.IntegerField(default=0, verbose_name='Hombres')
    volunteer_total_women_quantity = models.IntegerField(default=0, verbose_name='Mujeres')
    
    volunteer_active_men_quantity = models.IntegerField(default=0, verbose_name='Hombres')
    volunteer_active_women_quantity = models.IntegerField(default=0, verbose_name='Mujeres')
    volunteer_honorary_men_quantity = models.IntegerField(default=0)
    volunteer_honorary_women_quantity = models.IntegerField(default=0)
    volunteer_antiquity_required_to_honorary = models.IntegerField(null=True, blank=True, verbose_name='antigüedad requerida para ser honorario')
    
    
    volunteer_age_between_18_25_men_quantity = models.IntegerField(default=0, verbose_name='18 - 25')
    volunteer_age_between_18_25_women_quantity = models.IntegerField(default=0, verbose_name='18 - 25')
    volunteer_age_between_26_30_men_quantity = models.IntegerField(default=0, verbose_name='26 - 30')
    volunteer_age_between_26_30_women_quantity = models.IntegerField(default=0, verbose_name='26 - 30')
    volunteer_age_between_31_35_men_quantity = models.IntegerField(default=0, verbose_name='31 - 35')
    volunteer_age_between_31_35_women_quantity = models.IntegerField(default=0, verbose_name='31 - 35')
    volunteer_age_between_36_40_men_quantity = models.IntegerField(default=0, verbose_name='36 - 40')
    volunteer_age_between_36_40_women_quantity = models.IntegerField(default=0, verbose_name='36 - 40')
    volunteer_age_between_41_45_men_quantity = models.IntegerField(default=0, verbose_name='41 - 45')
    volunteer_age_between_41_45_women_quantity = models.IntegerField(default=0, verbose_name='41 - 45')
    volunteer_age_between_46_50_men_quantity = models.IntegerField(default=0, verbose_name='46 - 50')
    volunteer_age_between_46_50_women_quantity = models.IntegerField(default=0, verbose_name='46 - 50')
    volunteer_age_between_51_55_men_quantity = models.IntegerField(default=0, verbose_name='51 - 55')
    volunteer_age_between_51_55_women_quantity = models.IntegerField(default=0, verbose_name='51 - 55')
    volunteer_age_between_56_60_men_quantity = models.IntegerField(default=0, verbose_name='56 - 60')
    volunteer_age_between_56_60_women_quantity = models.IntegerField(default=0, verbose_name='56 - 60')
    volunteer_age_60_or_more_men_quantity = models.IntegerField(default=0, verbose_name='61+')
    volunteer_age_60_or_more_women_quantity = models.IntegerField(default=0, verbose_name='61+')

    # cuarta parte: educación y trabajo

    volunteer_education_basica_complete_quantity = models.IntegerField(default=0, verbose_name='n° voluntarios con enseñanza básica completa')
    volunteer_education_media_complete_quantity = models.IntegerField(default=0, verbose_name='n° voluntarios con enseñanza media completa')
    volunteer_education_universitaria_complete_quantity = models.IntegerField(default=0, verbose_name='n° voluntarios universitarios (4 o 5 años)')
    volunteer_education_tecnica_complete_quantity = models.IntegerField(default=0, verbose_name='n° voluntarios técnicos (3 o 4 años)')
    volunteer_with_work_quantity = models.IntegerField(default=0, verbose_name='n° voluntarios con oficios')

    # quinta parte: formación bomberil

    volunteer_lt_than_3_years_cuerpo_course_quantity = models.IntegerField(null=True, blank=True, verbose_name='Menos de 3 años')
    volunteer_gt_than_3_years_cuerpo_course_quantity = models.IntegerField(null=True, blank=True, verbose_name='Más de 3 años')
    volunteer_lt_than_3_years_academia_course_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios con menos de 3 años de experiencia')
    volunteer_gt_than_3_years_academia_course_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° voluntarios con más de 3 años de experiencia')

    # sexta parte: conductores clase F

    volunteer_class_f_bomberos_driver_quantity = models.IntegerField(null=True, blank=True, verbose_name='N° bomberos con licencia clase F')
    volunteer_class_f_cuarteleros_driver_quantity = models.IntegerField(null=True, blank=True, verbose_name='N° cuarteleros/conductores con licencia clase F')

    # 7ma parte: Hoja de Vida

    volunteer_hoja_de_vida_cargo = models.CharField(max_length=255, null=True, blank=True, verbose_name='Cargo')
    #fk_volunteer_hoja_de_vida_cargo = models.ForeignKey('Role', null=True, blank=True, verbose_name='Cargo')
    volunteer_hoja_de_vida_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nombre')
    volunteer_hoja_de_vida_email = models.CharField(max_length=255, null=True, blank=True, verbose_name='Correo electrónico')
    volunteer_hoja_de_vida_phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='Teléfono')

    # 8va parte: brigada juvenil

    volunteer_brigada_juvenil_antiquity = models.IntegerField(null=True, blank=True, verbose_name='Antigüedad')
    volunteer_brigada_juvenil_members_quantity = models.IntegerField(null=True, blank=True, verbose_name='n° brigadieres')
    volunteer_brigada_juvenil_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='nombre brigada')
    volunteer_brigada_juvenil_responsible_instructor = models.CharField(max_length=255, null=True, blank=True, verbose_name='instructor responsable')
    volunteer_brigada_juvenil_responsible_email = models.EmailField(max_length=255, null=True, blank=True, verbose_name='correo electrónico responsable')

    # observaciones
    
    observations = models.TextField(null=True, blank=True, verbose_name='')
