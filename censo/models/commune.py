# coding: utf-8

import logging

from django.db import models

class Commune(models.Model):
    old_id = models.IntegerField()
    name = models.CharField(max_length = 100)
    province = models.ForeignKey('Province')
    
    @classmethod
    def fetch_from_db(self, cursor, old_id):
        from . import Province
    
        query = "SELECT comu_ide, prov_id FROM comuna WHERE comu_nombre = %s"
        params = (old_id,)
        cursor.execute(query, params)
        
        commune_data = cursor.fetchone()
        if not commune_data
            logging.error("Could not fetch commune:%s", old_id)
            return None
            
        province = Province.fetch_from_db(cursor, commune_data[1])
        
        if not province:
            logging.error("Could not fetch commune:%s's province", old_id)
            return None
            
        try:
            commune = Commune.objects.get(old_id = commune_data[0])
            logging.info("Successfully fetched existing commune:%s", old_id)
        except Commune.DoesNotExist:
            logging.info("Successfully fetched commune:%s for the first time", old_id)
            commune = Commune()
            commune.old_id = commune_data[0]
            
        commune.name = old_id
        commune.province = province
        commune.save()
        
        return commune
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'censo'
