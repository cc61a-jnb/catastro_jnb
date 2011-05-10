# coding: utf-8

from django.db import models

class Company(models.Model):
    old_id = models.IntegerField()
    number = models.IntegerField()
    
    director_name = models.CharField(max_length=255, default = '', verbose_name='Director', blank=True, null=True)
    captain_name = models.CharField(max_length=255, default = '', verbose_name='Capitán', blank=True, null=True)
    secretary_name = models.CharField(max_length=255, default = '', verbose_name='Secretario', blank=True, null=True)
    tesorero_name = models.CharField(max_length=255, default = '', verbose_name='Tesorero', blank=True, null=True)
    lieutenant_1_name = models.CharField(max_length=255, default = '', verbose_name='Teniente 1°', blank=True, null=True)
    lieutenant_2_name = models.CharField(max_length=255, default = '', verbose_name='Teniente 2°', blank=True, null=True)
    lieutenant_3_name = models.CharField(max_length=255, default = '', verbose_name='Teniente 3°', blank=True, null=True)
    lieutenant_4_name = models.CharField(max_length=255, default = '', verbose_name='Teniente 4°', blank=True, null=True)
    assistant_name = models.CharField(max_length=255, default = '', verbose_name='Ayudante', blank=True, null=True)
    
    name = models.CharField(max_length = 255, default = '')
    cuerpo = models.ForeignKey('Cuerpo', related_name='cuerpo_company')
    phone = models.CharField(max_length=255, default = '', verbose_name='teléfono')
    mail = models.EmailField(max_length=255, default = '')
    address = models.CharField(max_length=255, default = '', verbose_name='dirección')
    commune = models.ForeignKey('Commune', related_name='+', blank=True, null=True)
    fax = models.CharField(max_length=255, default = '')
    postal_box = models.CharField(max_length=255, default = '')
    website = models.CharField(max_length=255, default = '')
    alarm_central = models.CharField(max_length=255, default = '')
    lemma = models.CharField(max_length=255, default = '')
    communes = models.ManyToManyField('Commune', blank=True, null=True)
    foundation_date = models.DateField(blank = True, null = True, verbose_name='fecha fundación')
    
    # observaciones
    observations = models.TextField(null=True, blank=True, verbose_name='')
    
    def __unicode__(self):
        return self.name
        
    def string_number(self):
        '''
        Converts the company number to corresponding string (e.g. 1 => "Primera")
        '''
        conversion_table = ['',
            'Primera',
            'Segunda',
            'Tercera',
            'Cuarta',
            'Quinta',
            'Sexta',
            'Séptima',
            'Octava',
            'Novena',
            'Décima',
            'Undécima',
            'Duodécima',
            'Décimotercera',
            'Décimocuarta',
            'Décimoquinta',
            'Décimosexta',
            'Decimoséptima',
            'Decimooctava',
            'Decimonovena',
            'Vigésima',
            'Vigésimoprimera',
            'Vigésimosegunda',
        ]
        try:
            return conversion_table[self.number] + ' Compañía'
        except IndexError:
            return ''
            

    class Meta:
        ordering = ['name']
        app_label = 'censo'
