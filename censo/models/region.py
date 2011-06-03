# coding: utf-8

from django.db import models

class Region(models.Model):
    name = models.CharField(max_length = 100)
    old_id = models.IntegerField()
    has_form = False
    
    @classmethod
    def fetch_all(self, cursor):
        query = "SELECT regi_id, regi_nombre FROM regiones"
        cursor.execute(query)
        
        for row in cursor.fetchall():
            region, created = Region.objects.get_or_create(old_id=row[0])
            if created:
                region.name = row[1]
                region.save()
    
    @classmethod
    def menu_pack(self):
        return ['Regiones', self.__name__, False]
    
    @classmethod
    def hierarchical_child(self):
        from . import Cuerpo
        return Cuerpo
        
    def fetch_all_related(self, cursor):
        query = '''SELECT c_cm_p.cuer_id, c_cm_p.cuer_nombre 
                   FROM ((cuerpos as c 
                   INNER JOIN comuna as cm ON c.cuer_comuna = cm.comu_nombre) as c_cm
                   INNER JOIN provincias as p ON c_cm.prov_id = p.prov_id) as c_cm_p
                   WHERE c_cm_p.prov_fk_region = %s'''
        params = (self.old_id,)
        cursor.execute(query, params)
        cuerpo_data_set = cursor.fetchall()
        cuerpo_list = []
        for row in cuerpo_data_set:
            cuerpo_list.append({"id": row[0], "name": row[1]})
        return cuerpo_list
        
    def referring_children(self):
        return Cuerpo.objects.filter(region=self)
    
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
