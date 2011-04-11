from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from . import Occupation, Company, Role

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_last_name = models.CharField(max_length = 40, default = '')
    second_last_lane = models.CharField(max_length = 40, default = '')
    rut = models.CharField(max_length = 10, default = '')
    address = models.CharField(max_length = 255, default = '')
    phone = models.CharField(max_length = 40, default = '')
    cell_phone = models.CharField(max_length = 40, default = '')
    work_phone = models.CharField(max_length = 40, default = '')
    occupation = models.ForeignKey(Occupation)
    work_address = models.CharField(max_length = 255, default = '')
    company = models.ForeignKey(Company)
    roles = models.ManyToManyField(Role, through = 'UserHasRole')

    def __str__(self):
        return "Perfil de %s" % self.user

    class Meta:
        ordering = ['user']
        app_label = 'censo'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user = instance)

post_save.connect(create_user_profile, sender = User)
