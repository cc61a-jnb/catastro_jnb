# coding: utf-8

from django.db import models

class CuerpoANBData(models.Model):
    cuerpo = models.OneToOneField('censo.Cuerpo', blank=True)

    def __unicode__(self):
        return self.cuerpo.name

    class Meta:
        ordering = ['cuerpo']
        app_label = 'censo'

    # Dotación de instructores

    cuerpo_procedure_instructors = models.IntegerField(null=True, blank=True, verbose_name='Instructores área procedimientos')
    cuerpo_health_instructors = models.IntegerField(null=True, blank=True, verbose_name='Instructores área salud')
    cuerpo_specialty_instructors = models.IntegerField(null=True, blank=True, verbose_name='Instructores área de especialidad')
    anb_procedure_instructors = models.IntegerField(null=True, blank=True, verbose_name='Instructores área procedimientos')
    anb_health_instructors = models.IntegerField(null=True, blank=True, verbose_name='Instructores área salud')
    anb_specialty_instructors = models.IntegerField(null=True, blank=True, verbose_name='Instructores área de especialidad')

    # Infrastructura capacitación

    cuerpo_courses_infrastructure_rooms = models.IntegerField(null=True, blank=True, verbose_name='Salas')
    cuerpo_courses_infrastructure_transparencies = models.IntegerField(null=True, blank=True, verbose_name='Máquinas transparencias')
    cuerpo_courses_infrastructure_diapositives = models.IntegerField(null=True, blank=True, verbose_name='Máquinas diapositivas')
    cuerpo_courses_infrastructure_datashow = models.IntegerField(null=True, blank=True, verbose_name='Equipos Data Show')
    cuerpo_courses_infrastructure_telon = models.IntegerField(null=True, blank=True, verbose_name='Telones')
    cuerpo_courses_infrastructure_boards = models.IntegerField(null=True, blank=True, verbose_name='Pizarras')
    cuerpo_courses_infrastructure_tvs = models.IntegerField(null=True, blank=True, verbose_name='TVs')
    cuerpo_courses_infrastructure_video = models.IntegerField(null=True, blank=True, verbose_name='Reproductores de video')
    cuerpo_courses_infrastructure_amplifiers = models.IntegerField(null=True, blank=True, verbose_name='Equipos de amplificación')
    cuerpo_courses_infrastructure_rcp = models.IntegerField(null=True, blank=True, verbose_name='Muñecos RCP')

    # Brigada Juvenil

    cuerpo_brigada_juvenil_antiquity = models.IntegerField(null=True, blank=True, verbose_name='Antigüedad (En años)')
    cuerpo_brigada_juvenil_members_quantity = models.IntegerField(null=True, blank=True, verbose_name='N° brigadieres')
    cuerpo_brigada_juvenil_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nombre de la brigada')
    # TODO: check if this is correct
    cuerpo_brigada_juvenil_responsible_role = models.CharField(max_length=255, null=True, blank=True, verbose_name='Cargo responsable brigada')
    cuerpo_brigada_juvenil_responsible_nombre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nombre responsable brigada')
    cuerpo_brigada_juvenil_responsible_email = models.EmailField(max_length=255, null=True, blank=True, verbose_name='E-mail')

    # Observaciones

    observations = models.TextField(null=True, blank=True, verbose_name='')
