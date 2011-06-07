import logging

from censo.utils import get_menu_data

from django.db import models
from django.db import connections
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from . import Occupation, Company, Administrator

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

    def highest_role(self):
        return self.role_id

    def is_administrator(self):
        return self.user.is_superuser

    def is_regional_operations_manager(self):
        if "Jefe Operaciones" in self.role_name:
            return True
        
        return False
        
    def is_cuerpo_manager(self):
        if self.role_id in [1, 2]:
            return True
        
        return False

    def is_company_manager(self):
        if self.role_id in [5,8]:
            return True
        
        return False

    def has_company_permission(self, cursor, company):
        # check if user is administrator
        if self.is_administrator():
            return True

        # check first if user is company's cuerpo administrator
        if self.is_cuerpo_manager() and self.company.cuerpo == company.cuerpo:
            return True
        
        # last case, company
        if self.is_company_manager() and self.company == company:
            return True

        return False

    def has_cuerpo_permission(self, cursor, cuerpo):
        # check if user is administrator
        if self.is_administrator():
            return True

        # check first if user is in cuerpo
        if self.is_cuerpo_manager() and self.company.cuerpo == cuerpo:
            return True
        
        # now check if is user is regional operations manager
        if self.is_regional_operations_manager():
            cuerpo_region = cuerpo.commune.province.region
            self_region_id = None

            try:
               self_region_id = settings.CARGO_ID_REGION_ID_DICT[self.role_id]
            except KeyError:
                logging.error("Cargo:%s is not defined at the settings CARGO_ID_REGION_ID_DICT dictionary", old_id)
                return False
            return cuerpo_region.old_id == self_region_id

        return False
        
    def get_menu(self):
        if self.is_administrator():
            return get_menu_data(Administrator())
        if self.is_regional_operations_manager():
            return get_menu_data(self.company.cuerpo.region)
        if self.is_cuerpo_manager():
            return get_menu_data(self.company.cuerpo)
        return get_menu_data(None)

    class Meta:
        ordering = ['user']
        app_label = 'censo'


def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user = instance)

post_save.connect(create_user_profile, sender = User)
