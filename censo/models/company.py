# coding: utf-8

import logging

from django.db import models
from django.db import connections

class Company(models.Model):

    data_indexes = {
        'phone': 1,
    }

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
    
    cuerpo = models.ForeignKey('Cuerpo', related_name='cuerpo_company')
   # phone = models.CharField(max_length=255, default = '', verbose_name='teléfono')
    mail = models.EmailField(max_length=255, default = '')
    address = models.CharField(max_length=255, default = '', verbose_name='dirección')
    commune = models.ForeignKey('Commune', related_name='+', blank=True, null=True)
    fax = models.CharField(max_length=255, default = '')
    postal_box = models.CharField(max_length=255, default = '')
    website = models.CharField(max_length=255, default = '')
    alarm_central = models.CharField(max_length=255, default = '')
    lemma = models.CharField(max_length=255, default = '')
    foundation_date = models.DateField(blank = True, null = True, verbose_name='fecha fundación')
    
    @property
    def phone(self):
        logging.info("querying %s company phone", self.old_id)
        return self.__get_columns()[self.data_indexes['phone']]

    def __get_columns(self):
        if hasattr(self, 'column_data'): # query caching
            return self.column_data
        else:
            cursor = connections['principal'].cursor()
            user_profile = self.
            query = """SELECT comp_id, comp_telefono
                       FROM companias
                       WHERE comp_id = %s
                    """
            params = (self.old_id,)
            
            cursor.execute(query, params)
            temp_data = cursor.fetchone()
            if temp_data:
                self.column_data = temp_data
            cursor.close()
            return self.column_data

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
        ordering = ['old_id']
        app_label = 'censo'
