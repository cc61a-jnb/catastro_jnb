# coding: utf-8
import logging
from django.db import models
from django.db import connections
from . import Commune, Cuerpo

class Company(models.Model):

    data_indexes = {
        'phone': 1,
    }

    old_id = models.IntegerField()
    number = models.IntegerField()
    address = models.CharField(max_length=255, verbose_name='dirección')
    phone = models.CharField(max_length=255, verbose_name='teléfono')
    foundation_date = models.CharField(max_length=255, verbose_name='fecha fundación')
    
    commune = models.ForeignKey('Commune', null=True, related_name='+')
    cuerpo = models.ForeignKey('Cuerpo', null=True, related_name='cuerpo_company')    
    
    @classmethod
    def fetch_from_db(self, cursor, old_id):
        query = "SELECT comp_id, comp_nro, comp_direccion, comp_comuna, comp_telefono, comp_ffundacion, comp_fk_cuerpo FROM companias WHERE comp_id = %s"
        params = (old_id,)
        cursor.execute(query, params)
        
        company_data = cursor.fetchone()
        if not company_data:
            return None
            
        commune = Commune.fetch_from_db(cursor, company_data[3])
        
        if not commune:
            return None
        
        cuerpo = Cuerpo.fetch_from_db(cursor, company_data[6])
        
        if not cuerpo:
            return None
            
        try:
            company = Company.objects.get(old_id = old_id)
        except Company.DoesNotExist:
            company = Company()
            company.old_id = old_id
        
        company.number = company_data[1]
        company.address = company_data[2]
        company.commune = commune
        company.phone = company_data[4]
        company.foundation_date = company_data[5]
        company.cuerpo = cuerpo
        
        company.save()
        
        return company
        

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
