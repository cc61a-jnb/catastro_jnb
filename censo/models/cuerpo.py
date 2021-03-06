# coding: utf-8

import logging

from django.db import models
from django.db import connections
from . import Commune

class Cuerpo(models.Model):
    old_id = models.IntegerField()
    name = models.CharField(max_length=100)
    commune = models.ForeignKey('Commune', related_name='+')
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    foundation_date = models.CharField(max_length=255)
    npers_juri = models.CharField(max_length=255)
    decree_date = models.CharField(max_length=255)
    has_form = True
    
    @classmethod
    def menu_pack(self):
        return ['Cuerpos', self.__name__, True]
    
    @classmethod
    def hierarchical_child(self):
        from . import Company
        return Company
        
    def referring_children(self):
        from . import Company
        return Company.objects.filter(cuerpo=self)

    @classmethod
    def fetch_from_db(self, cursor, old_id):
        from . import Province
    
        query = "SELECT cuer_nombre, cuer_comuna, cuer_telefono, cuer_direccion, cuer_fecha_fund, cuer_npers_juri, cuer_fech_decre FROM cuerpos WHERE cuer_id = %s"
        params = (old_id,)
        cursor.execute(query, params)
        
        cuerpo_data = cursor.fetchone()
        if not cuerpo_data:
            logging.error("Could not fetch cuerpo:%s", old_id)
            return None
            
        commune = Commune.fetch_from_db(cursor, cuerpo_data[1])
        
        if not commune:
            logging.error("Could not fetch cuerpo:%s's commune", old_id)
            return None
            
        try:
            cuerpo = Cuerpo.objects.get(old_id = old_id)
            logging.info("Successfully fetched existing cuerpo:%s", old_id)
        except Cuerpo.DoesNotExist:
            logging.info("Successfully fetched cuerpo:%s for the first time", old_id)
            cuerpo = Cuerpo()
            cuerpo.old_id = old_id
            
        cuerpo.name = cuerpo_data[0]
        cuerpo.commune = commune
        cuerpo.phone = cuerpo_data[2]
        cuerpo.address = cuerpo_data[3]
        cuerpo.foundation_date = cuerpo_data[4]
        cuerpo.npers_juri = cuerpo_data[5]
        cuerpo.decree_date = cuerpo_data[6]
        cuerpo.save()
        
        cuerpo.fetch_related_company_ids(cursor)
        
        return cuerpo

    def fetch_related_company_ids(self, cursor):
        from . import Company
        
        logging.info("Fetching cuerpo:%s's companies", self.old_id)
        query = "SELECT comp_id FROM companias WHERE comp_fk_cuerpo = %s"
        params = (self.old_id,)
        cursor.execute(query, params)
        rows = cursor.fetchall()
        
        for row in rows:
            Company.fetch_from_db(cursor, row[0], cuerpo=self)

    def __unicode__(self):
        return u'Cuerpo de Bomberos de %s' % self.name

    class Meta:
        ordering = ['name']
        app_label = 'censo'
