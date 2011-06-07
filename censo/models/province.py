# coding: utf-8

import logging

from django.db import models

class Province(models.Model):
    name = models.CharField(max_length = 100)
    region = models.ForeignKey('Region')
    old_id = models.IntegerField()
    
    @classmethod
    def fetch_from_db(self, cursor, old_id):
        from . import Region
    
        query = "SELECT prov_nombre, prov_fk_region FROM provincias WHERE prov_id = %s"
        params = (old_id,)
        cursor.execute(query, params)
        
        province_data = cursor.fetchone()
        if not province_data:
            logging.info("Cannot find province with id (%s)", old_id)
            return None
            
        region = Region.fetch_from_db(cursor, province_data[1])
        
        if not region:
            return None
            
        try:
            province = Province.objects.get(old_id = old_id)
        except Province.DoesNotExist:
            province = Province()
            province.old_id = old_id
            
        province.name = province_data[0]
        province.region = region
        province.save()
        
        return province
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'censo'
