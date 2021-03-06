# coding: utf-8

import logging

from django.db import models

class Region(models.Model):
    name = models.CharField(max_length = 100)
    old_id = models.IntegerField()
    has_form = False

    @classmethod
    def get_old_id_name_tuples(self):
        """
        Returns a generator of tuples (old_id, name) for regions,
        Useful to construct ChoiceFields
        """
        return ((r.old_id, r.name) for r in self.objects.all())
    
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
    
    @classmethod
    def fetch_all_related(self, cursor, region_id):
        query = '''SELECT c_cm_p.cuer_id, c_cm_p.cuer_nombre 
                   FROM ((cuerpos as c 
                   INNER JOIN comuna as cm ON c.cuer_comuna = cm.comu_nombre) as c_cm
                   INNER JOIN provincias as p ON c_cm.prov_id = p.prov_id) as c_cm_p
                   WHERE c_cm_p.prov_fk_region = %s
                   ORDER BY c_cm_p.cuer_nombre'''
        params = (region_id,)
        cursor.execute(query, params)
        cuerpo_data_set = cursor.fetchall()
        cuerpo_list = []
        for row in cuerpo_data_set:
            cuerpo_list.append({"id": row[0], "name": row[1]})
        return cuerpo_list
        
    def referring_children(self):
        from . import Cuerpo
        return Cuerpo.objects.filter(commune__province__region=self)
    
    @classmethod
    def fetch_from_db(self, cursor, old_id):
        query = "SELECT regi_nombre FROM regiones WHERE regi_id = %s"
        params = (old_id,)
        cursor.execute(query, params)
        
        region_data = cursor.fetchone()
        if not region_data:
            logging.error("Could not fetch region:%s", old_id)
            return None
            
        try:
            region = Region.objects.get(old_id = old_id)
            logging.info("Successfully fetched existing region:%s", old_id)
        except Region.DoesNotExist:
            logging.info("Successfully fetched region:%s for the first time", old_id)
            region = Region()
            region.old_id = old_id
            
        region.name = region_data[0]
        region.save()
        
        return region
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['old_id']
        app_label = 'censo'
