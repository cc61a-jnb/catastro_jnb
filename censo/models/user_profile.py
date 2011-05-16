import logging

from django.db import models
from django.db import connections
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from . import Occupation, Company

class UserProfile(models.Model):
    company = models.ForeignKey(Company, null=True)
    old_id = models.IntegerField(default = 0)
    region = models.ForeignKey('Region', blank = True, null = True)
    user = models.OneToOneField(User)
    role_id = models.IntegerField(default = 0)
    role_name = models.CharField(max_length = 255)

    def __unicode__(self):
        return "Perfil de %s" % self.user
        
    def determine_role(self, cursor):
        query = """SELECT C.cargo_id, C.cargo_nombre
                   FROM cargo AS C INNER JOIN usu_cargo AS UC on C.cargo_id = UC.carg_nombre
                   WHERE UC.id_usu = %s ORDER BY UC.carg_nombre ASC
                """
        params = (self.old_id,)
        cursor.execute(query, params)
        
        self.role_id = 0
        
        for idx, row in enumerate(cursor.fetchall()):
            if self.role_id == 0:
                self.role_id = row[0]
            if 'Jefe Operaciones' in row[1]:
                self.role_name = row[1]
                self.role_id = row[0]
            

    def all_roles(self):
        if hasattr(self, 'roles'): # query caching
            return self.roles
        # roles = self.roles.order_by('old_id')
        cursor = connections['principal'].cursor()
        logging.info("querying %s user roles", self.user.username)
        # we need to get the highest role available for the user, meaning the lowest car_nombre
        query = """SELECT C.cargo_id, C.cargo_nombre
                   FROM cargo AS C INNER JOIN usu_cargo AS UC on C.cargo_id = UC.carg_nombre
                   WHERE UC.id_usu = %s ORDER BY C.cargo_nombre ASC
                """
        params = (self.old_id,)

        cursor.execute(query, params)
        roles = cursor.fetchall()
        if roles:
            self.roles = roles
            return roles
        else:
            return None

    def highest_role(self):
        return self.role_id
        '''
        if self.all_roles():
            return self.all_roles()[0]
        else:
            return None
        '''

    def is_regional_operations_manager(self):
        if "Jefe Operaciones" in self.role_name:
            return True
        else:
            return False
        '''
        for role in self.all_roles():
            if "Jefe Operaciones" in role[1]: # searching in cargo_id
                return True
        return False
        '''

    def is_cuerpo_manager(self):
        if self.role_id in [1, 2]:
            return True
        else:
            return False
            
        '''
        for role in self.all_roles():
            if role[0] in [1, 2]: # searching in cargo_id
                return True
        return False
        '''

    def is_company_manager(self):
        if self.role_id in [5,8]:
            return True
        else:
            return False
        '''
        for role in self.all_roles():
            if role[0] in [4]: # searching in cargo_nombre
                return True
        return False
        '''

    class Meta:
        ordering = ['user']
        app_label = 'censo'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user = instance)

post_save.connect(create_user_profile, sender = User)
