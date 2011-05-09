# coding: utf-8

from django.db import models

class Region(models.Model):
    name = models.CharField(max_length = 100)
    old_id = models.IntegerField()
    
    @classmethod
    def fetch_from_db(self, cursor, old_id):
        query = "SELECT regi_nombre FROM regiones WHERE regi_id = %s"
        params = (old_id,)
        cursor.execute(query, params)
        
        region_data = cursor.fetchone()
        if not region_data:
            logging.info("Cannot find region with id (%d)", old_id)
            return None
            
        try:
            region = Region.objects.get(old_id = old_id)
        except Region.DoesNotExist:
            region = Region()
            region.old_id = old_id
            
        region.name = region_data[0]
        region.save()
        
        return region
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'censo'
