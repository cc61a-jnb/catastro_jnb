# coding: utf-8

import logging

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from . import Occupation, Company, Role

class UserProfile(models.Model):
    company = models.ForeignKey(Company, null=True)
    old_id = models.IntegerField(default = 0)
    region = models.ForeignKey('Region', blank = True, null = True)
    user = models.OneToOneField(User)
    role_id = models.IntegerField(default = 0)
    role_name = models.CharField(max_length = 255)

    def __unicode__(self):
        return u"Perfil de %s" % self.user
        
    def update_role(self, cursor):
        role = self.highest_role(cursor)
        if role:
            self.role_id = role[0]
            self.role_name = role[1]
            self.save()

    def all_roles(self, cursor):
        if hasattr(self, 'roles'): # query caching
            return self.roles

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

    def highest_role(self, cursor):
        roles = self.all_roles(cursor)
        if roles:
            return roles[0]
        else:
            return None

    def is_regional_operations_manager(self, cursor):
        for role in self.all_roles(cursor):
            if "Jefe Operaciones" in role[1]: # searching in cargo_id
                return True
        return False

    def is_cuerpo_manager(self, cursor):
        for role in self.all_roles(cursor):
            if role[0] in [1, 2]: # searching in cargo_id
                return True
        return False

    def is_company_manager(self, cursor):
        for role in self.all_roles(cursor):
            if role[0] in [4]: # searching in cargo_nombre
                return True
        return False

    class Meta:
        ordering = ['user']
        app_label = 'censo'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user = instance)

post_save.connect(create_user_profile, sender = User)
